---
title: "Topic 20 - How to navigate Nmap Manual Pages (man nmap)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 20: How to navigate Nmap Manual Pages (man nmap)

### 1. Explanation (Hinglish)
**`man nmap`** command Kali Linux (aur baaki Linux systems) mein Nmap utility ke user manual documentation ko kholti hai. Is manual page mein Nmap ke saare scanning configurations, definitions, flags, aur usage details detailed manual ke roop mein save rehte hain.

Lekin, manual page open hone ke baad navigate kaise karein aur flags ko dhoondhein kaise, iske liye keyboard shortcuts pata hona zaroori hai:

#### ⌨️ Manual Page Shortcuts:

1. **Scrolling (Niche-Upar jana):**
   - **`Arrow keys (Up/Down)`** या **`Enter`**: Ek-ek line niche/upar scroll karne ke liye.
   - **`Spacebar`** ya **`f` (Forward)**: Ek-ek full page direct scroll niche karne ke liye.
   - **`b` (Backward)**: Ek-ek full page back/upar jaane ke liye.

2. **Searching (Manual ke andar text dhoondhna):**
   - **`/` (Forward Slash):** Keyboard par `/` press karein, isse bottom par search box aayega. Uske aage apna keyword likhein (e.g., `/Timing`) aur Enter press karein.
   - **`n` (Next Match):** Agle matching word par jump karne ke liye.
   - **`N` (Previous Match):** Pichle matching word par jump karne ke liye.

3. **Quitting (Manual se bahar aana):**
   - **`q` (Quit):** Manual page close karke normal terminal screen par wapas aane ke liye.

#### 📖 Real-world Analogy: Reading a Huge Encyclopedia
Socho aap library mein **1000 pages ki encyclopedia** kholte ho:
- `man nmap` chalana matlab book ko open karke table par rakhna.
- **Spacebar** dabana matlab fast-forward pages flip karna.
- **`/` (Slash)** use karna matlab direct page index index search check karna taaki specific word highlight ho sake.
- **`q`** key press karna matlab book band karke wapas normal class screen par aana.

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par in navigation keys ko live run karke test karein:

**Task 1: Manual page open aur check-up karna:**
1. Type command in terminal:
   ```bash
   man nmap
   ```
2. Screen load hote hi **`Spacebar`** 3-4 baar press karke page skips check karein.
3. Type karein: `/stealth` aur Enter dabayein.
4. Keyword highlight hone par next matches ke liye **`n`** key 2-3 baar press karke jump karein.
5. Search se free hokar manual se exit hone ke liye **`q`** key press karein.

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Linux manual pages (man pages) ke andar query reading check complete karne ke baad, exit hokar normal command line screen par aane ke liye kis keyboard key shortcut ka use kiya jata hai?
- **A)** `Esc`
- **B)** `q`
- **C)** `Ctrl + C`

#### 🎯 Assignment
1. Terminal par `man nmap` open karein.
2. Search shortcut (`/`) use karke dhoondhein: `Timing Templates`.
3. Check karein ki timing templates (`-T0` to `-T5`) ki exact details manual mein kis section page par saved hain.
4. Quiz ka correct answer aur timings options search confirmation mujhe chat mein share karein!

---