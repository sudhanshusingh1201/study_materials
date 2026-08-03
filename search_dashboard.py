import http.server
import socketserver
import json
import re
import os
import webbrowser

PORT = 8000
NOTES_FILE = "Computer Networking - Study Notes.md"

def parse_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    chunks = content.split('\n## ')
    topics = []
    
    for chunk in chunks[1:]:
        lines = chunk.strip().split('\n')
        if not lines:
            continue
        title = lines[0].strip()
        if "Table of Contents" in title:
            continue
        content_body = '\n'.join(lines[1:]).strip()
        
        num_match = re.search(r'\b(\d+)\b', title)
        topic_id = int(num_match.group(1)) if num_match else len(topics) + 1
        
        topics.append({
            "id": topic_id,
            "title": title,
            "content": content_body
        })
    return sorted(topics, key=lambda x: x['id'])

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌐 Networking Study Notes Search Dashboard</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Marked.js for Markdown Parsing -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    
    <!-- Highlight.js for Code Highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/tokyo-night-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

    <style>
        :root {
            --bg-primary: #080c14;
            --bg-sidebar: rgba(13, 20, 35, 0.85);
            --bg-card: rgba(20, 30, 54, 0.4);
            --accent-gradient: linear-gradient(135deg, #6366f1, #a855f7);
            --accent-solid: #6366f1;
            --accent-glow: rgba(99, 102, 241, 0.2);
            --border-color: rgba(255, 255, 255, 0.08);
            --text-primary: #f3f4f6;
            --text-secondary: #9ca3af;
            --text-muted: #6b7280;
            --sidebar-width: 360px;
            --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif;
        }

        body {
            background-color: var(--bg-primary);
            color: var(--text-primary);
            height: 100vh;
            overflow: hidden;
            display: flex;
        }

        /* Sidebar Styling */
        .sidebar {
            width: var(--sidebar-width);
            background-color: var(--bg-sidebar);
            border-right: 1px solid var(--border-color);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            display: flex;
            flex-direction: column;
            height: 100%;
            z-index: 10;
            transition: var(--transition);
        }

        .sidebar-header {
            padding: 24px;
            border-bottom: 1px solid var(--border-color);
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 1.25rem;
            font-weight: 700;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 18px;
        }

        .logo i {
            -webkit-text-fill-color: initial;
            background: var(--accent-gradient);
            color: #fff;
            padding: 8px 10px;
            border-radius: 10px;
            font-size: 1rem;
        }

        .search-container {
            position: relative;
        }

        .search-container i {
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            font-size: 0.95rem;
        }

        .search-input {
            width: 100%;
            padding: 12px 16px 12px 42px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            color: var(--text-primary);
            font-size: 0.9rem;
            outline: none;
            transition: var(--transition);
        }

        .search-input:focus {
            border-color: var(--accent-solid);
            background: rgba(255, 255, 255, 0.08);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }

        .topic-list-container {
            flex: 1;
            overflow-y: auto;
            padding: 16px;
        }

        .topic-list-container::-webkit-scrollbar {
            width: 5px;
        }

        .topic-list-container::-webkit-scrollbar-thumb {
            background: var(--border-color);
            border-radius: 4px;
        }

        .topic-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 14px 16px;
            border-radius: 12px;
            cursor: pointer;
            margin-bottom: 8px;
            transition: var(--transition);
            border: 1px solid transparent;
        }

        .topic-item:hover {
            background: rgba(255, 255, 255, 0.04);
            border-color: var(--border-color);
        }

        .topic-item.active {
            background: var(--accent-gradient);
            color: #ffffff;
            box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
        }

        .topic-item.active .topic-title {
            color: #ffffff;
            font-weight: 600;
        }

        .topic-item.active .topic-num {
            background: rgba(255, 255, 255, 0.25);
            color: #ffffff;
        }

        .topic-num {
            font-size: 0.75rem;
            font-weight: 700;
            background: rgba(255, 255, 255, 0.08);
            color: var(--text-secondary);
            padding: 4px 8px;
            border-radius: 6px;
            min-width: 32px;
            text-align: center;
        }

        .topic-title {
            font-size: 0.88rem;
            color: var(--text-secondary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            flex: 1;
        }

        /* Main Content Styling */
        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            height: 100%;
            background-color: var(--bg-primary);
            position: relative;
        }

        .content-header {
            padding: 20px 40px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(8, 12, 20, 0.8);
            backdrop-filter: blur(10px);
            z-index: 5;
        }

        .header-left {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .toggle-sidebar-btn {
            background: none;
            border: none;
            color: var(--text-secondary);
            font-size: 1.2rem;
            cursor: pointer;
            padding: 8px;
            border-radius: 8px;
            transition: var(--transition);
        }

        .toggle-sidebar-btn:hover {
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-primary);
        }

        .header-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            padding: 10px 16px;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: 500;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: var(--transition);
        }

        .btn:hover {
            background: rgba(255, 255, 255, 0.1);
            color: var(--text-primary);
            border-color: var(--text-secondary);
        }

        .btn-accent {
            background: var(--accent-gradient);
            color: #fff;
            border: none;
        }

        .btn-accent:hover {
            opacity: 0.9;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.25);
        }

        .viewer-container {
            flex: 1;
            overflow-y: auto;
            padding: 40px;
            scroll-behavior: smooth;
        }

        .viewer-container::-webkit-scrollbar {
            width: 8px;
        }

        .viewer-container::-webkit-scrollbar-thumb {
            background: var(--border-color);
            border-radius: 4px;
        }

        .markdown-body {
            max-width: 880px;
            margin: 0 auto;
            font-size: 1.05rem;
            line-height: 1.75;
            color: #d1d5db;
        }

        /* Markdown Overrides */
        .markdown-body h1, .markdown-body h2, .markdown-body h3 {
            color: #ffffff;
            margin-top: 1.8em;
            margin-bottom: 0.8em;
            font-weight: 700;
        }

        .markdown-body h2 {
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.4em;
            font-size: 1.6rem;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .markdown-body h3 {
            font-size: 1.25rem;
            color: #c084fc;
            margin-top: 1.5em;
        }

        .markdown-body p {
            margin-bottom: 1.2em;
        }

        .markdown-body ul, .markdown-body ol {
            margin-bottom: 1.2em;
            padding-left: 24px;
        }

        .markdown-body li {
            margin-bottom: 0.5em;
        }

        .markdown-body blockquote {
            border-left: 4px solid var(--accent-solid);
            background: rgba(99, 102, 241, 0.08);
            padding: 16px 24px;
            border-radius: 0 12px 12px 0;
            margin: 20px 0;
            color: #e5e7eb;
        }

        .markdown-body code {
            font-family: 'Fira Code', monospace;
            background: rgba(255, 255, 255, 0.08);
            padding: 2px 6px;
            border-radius: 6px;
            font-size: 0.9em;
            color: #f43f5e;
        }

        .markdown-body pre code {
            background: none;
            padding: 0;
            color: inherit;
        }

        .markdown-body pre {
            background: #0d1117;
            border: 1px solid var(--border-color);
            padding: 20px;
            border-radius: 12px;
            overflow-x: auto;
            margin: 24px 0;
        }

        .markdown-body table {
            width: 100%;
            border-collapse: collapse;
            margin: 24px 0;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid var(--border-color);
        }

        .markdown-body th, .markdown-body td {
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }

        .markdown-body th {
            background-color: rgba(255, 255, 255, 0.04);
            color: #ffffff;
            font-weight: 600;
        }

        .bottom-nav {
            display: flex;
            justify-content: space-between;
            max-width: 880px;
            margin: 60px auto 20px auto;
            border-top: 1px solid var(--border-color);
            padding-top: 30px;
        }

        .welcome-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            text-align: center;
            max-width: 500px;
            margin: 0 auto;
        }

        .welcome-icon {
            font-size: 4rem;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 24px;
            animation: float 4s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .welcome-title {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .welcome-desc {
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .toast {
            position: absolute;
            bottom: 30px;
            right: 30px;
            background: #10b981;
            color: #fff;
            padding: 12px 24px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 0.9rem;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
            display: flex;
            align-items: center;
            gap: 8px;
            transform: translateY(100px);
            opacity: 0;
            transition: var(--transition);
            z-index: 100;
        }

        .toast.show {
            transform: translateY(0);
            opacity: 1;
        }
    </style>
</head>
<body>

    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="logo">
                <i class="fa-solid fa-network-wired"></i>
                <span>Study Hub Search</span>
            </div>
            <div class="search-container">
                <i class="fa-solid fa-magnifying-glass"></i>
                <input type="text" class="search-input" id="searchInput" placeholder="Search topics (e.g. DHCP, TCP)...">
            </div>
        </div>
        <div class="topic-list-container" id="topicList">
            <!-- Dynamic Topics -->
        </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <div class="content-header" id="contentHeader" style="display: none;">
            <div class="header-left">
                <button class="toggle-sidebar-btn" id="toggleSidebar">
                    <i class="fa-solid fa-bars"></i>
                </button>
                <div class="header-title" id="currentTopicTitle">Topic Title</div>
            </div>
            <div class="header-actions">
                <button class="btn" id="copyBtn"><i class="fa-solid fa-copy"></i> Copy Markdown</button>
            </div>
        </div>

        <div class="viewer-container" id="viewerContainer">
            <div class="welcome-container" id="welcomeScreen">
                <div class="welcome-icon"><i class="fa-solid fa-compass"></i></div>
                <h2 class="welcome-title">Networking Study Searcher</h2>
                <p class="welcome-desc">Type in the search box to find topics instantly, or select any topic from the list to start reading the parsed study notes.</p>
            </div>
            <div class="markdown-body" id="renderedContent" style="display: none;">
                <!-- Rendered content -->
            </div>
        </div>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast">
        <i class="fa-solid fa-circle-check"></i>
        <span>Copied to Clipboard!</span>
    </div>

    <script>
        let allNotes = [];
        let activeNote = null;

        // Initialize marked with highlight.js
        marked.setOptions({
            highlight: function(code, lang) {
                const language = hljs.getLanguage(lang) ? lang : 'plaintext';
                return hljs.highlight(code, { language }).value;
            }
        });

        // Toggle Sidebar
        const sidebar = document.getElementById('sidebar');
        document.getElementById('toggleSidebar').addEventListener('click', () => {
            if (sidebar.style.width === '0px' || sidebar.style.display === 'none') {
                sidebar.style.width = 'var(--sidebar-width)';
                sidebar.style.display = 'flex';
            } else {
                sidebar.style.width = '0px';
                setTimeout(() => { sidebar.style.display = 'none'; }, 250);
            }
        });

        // Load Notes from API
        async function fetchNotes() {
            try {
                const res = await fetch('/api/notes');
                allNotes = await res.json();
                renderTopicList(allNotes);
            } catch (err) {
                console.error("Error loading notes:", err);
            }
        }

        // Render Sidebar List
        function renderTopicList(notes) {
            const list = document.getElementById('topicList');
            list.innerHTML = '';
            
            notes.forEach(note => {
                const item = document.createElement('div');
                item.className = 'topic-item';
                if (activeNote && activeNote.id === note.id) {
                    item.className += ' active';
                }
                item.addEventListener('click', () => selectTopic(note));
                
                item.innerHTML = `
                    <div class="topic-num">${note.id}</div>
                    <div class="topic-title">${note.title}</div>
                `;
                list.appendChild(item);
            });
        }

        // Search/Filter logic
        document.getElementById('searchInput').addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            const filtered = allNotes.filter(note => 
                note.title.toLowerCase().includes(query) || 
                note.content.toLowerCase().includes(query)
            );
            renderTopicList(filtered);
        });

        // Select Topic
        function selectTopic(note) {
            activeNote = note;
            
            // Show elements
            document.getElementById('welcomeScreen').style.display = 'none';
            document.getElementById('contentHeader').style.display = 'flex';
            document.getElementById('renderedContent').style.display = 'block';
            
            // Set title and content
            document.getElementById('currentTopicTitle').innerText = note.title;
            
            // Render Markdown
            const htmlContent = marked.parse(note.content);
            const contentContainer = document.getElementById('renderedContent');
            
            // Append next/prev navigation links inside reader
            const currentIdx = allNotes.findIndex(n => n.id === note.id);
            let navHtml = '<div class="bottom-nav">';
            if (currentIdx > 0) {
                navHtml += `<button class="btn" onclick="goToTopic(${allNotes[currentIdx-1].id})"><i class="fa-solid fa-arrow-left"></i> Previous Topic</button>`;
            } else {
                navHtml += '<div></div>';
            }
            if (currentIdx < allNotes.length - 1) {
                navHtml += `<button class="btn btn-accent" onclick="goToTopic(${allNotes[currentIdx+1].id})">Next Topic <i class="fa-solid fa-arrow-right"></i></button>`;
            } else {
                navHtml += '<div></div>';
            }
            navHtml += '</div>';

            contentContainer.innerHTML = htmlContent + navHtml;
            
            // Trigger highlight
            document.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightElement(block);
            });

            // Re-render topic list to update active highlight
            renderTopicList(allNotes);

            // Scroll to top
            document.getElementById('viewerContainer').scrollTop = 0;
        }

        function goToTopic(id) {
            const note = allNotes.find(n => n.id === id);
            if (note) selectTopic(note);
        }

        // Copy Button Action
        document.getElementById('copyBtn').addEventListener('click', () => {
            if (!activeNote) return;
            const fullText = `## ${activeNote.title}\n\n${activeNote.content}`;
            navigator.clipboard.writeText(fullText).then(() => {
                const toast = document.getElementById('toast');
                toast.classList.add('show');
                setTimeout(() => { toast.classList.remove('show'); }, 2000);
            });
        });

        // Init load
        fetchNotes();
    </script>
</body>
</html>
"""

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode('utf-8'))
        elif self.path == '/api/notes':
            try:
                topics = parse_notes()
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps(topics).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run():
    print(f"Starting local notes search server on http://localhost:{PORT}...")
    webbrowser.open(f"http://localhost:{PORT}")
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.shutdown()

if __name__ == '__main__':
    run()
