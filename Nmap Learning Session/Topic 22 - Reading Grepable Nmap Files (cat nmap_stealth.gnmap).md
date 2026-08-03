---
title: "Topic 22 - Reading Grepable Nmap Files (cat nmap_stealth.gnmap)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 22: Reading Grepable Nmap Files (cat nmap_stealth.gnmap)

### 1. Explanation (Hinglish)
Aapne jo command select ki hai: **`cat nmap_stealth.gnmap`**, yeh do concepts ko combine karti hai: **`cat` command** aur **`.gnmap` (Grepable Nmap) file format**.

Chalo iska detailed breakdown karte hain:

1. **`cat` (Concatenate) Command:**
   - Linux mein `cat` ek basic utility command hai jiska use kisi text file ke full content ko direct terminal screen par print (display) karne ke liye kiya jata hai.
   - Example: `cat file.txt` chalaane par file ke andar ka saara text screen par print ho jayega.

2. **`.gnmap` (Grepable Nmap) File Format:**
   - Jab hum Nmap scan run karte waqt `-oG` ya `-oA` flag lagakar results ko save karte hain, toh Nmap ek `.gnmap` extension wali file generate karta hai.
   - Normal Nmap output vertical format mein hota hai jisme bohot saari empty lines aur tables hote hain. Lekin `.gnmap` format mein target **har ek host (IP address) ki complete scanning report ko ek single horizontal line mein store** kiya jata hai.
   - Is single-line layout ke karan hum standard command-line tools (jaise `grep`, `cut`, `awk`) ka use karke hazaaron scanned hosts mein se specific IPs ya ports ko milliseconds mein filter kar sakte hain.

---

#### 📁 `.gnmap` Format Structure Example:
```text
Host: 45.33.32.156 (scanme.nmap.org)	Status: Up
Host: 45.33.32.156 (scanme.nmap.org)	Ports: 22/open/tcp//ssh///, 80/open/tcp//http///, 9929/open/tcp//nping-echo///	Ignored State: closed (997)
```
*Hinglish Note: Aap dekh sakte hain ki isme host IP, status, aur saare open ports comma-separated hokar ek hi line mein hain.*

---

#### 🚪 Real-world Analogy: The Single-Line Registry Book
Socho aap ek security inspector ho:
- **Normal Output (`-oN`):** Aap ek full register copy maintain karte ho jisme har flat ke liye ek alag page hota hai aur details likhi hoti hain. Padhne mein aasan hai, par computer filter ke liye complex hai.
- **Grepable Output (`-oG`):** Aap ek single long horizontal list banate ho jahan har line ek flat ki list store karti hai: *"Flat 101, Status: Occupied, Open Gates: Gate A, Gate B"*. Agar kisi ko check karna ho ki kaun-kaun se flats mein Gate B open hai, toh wo ruler lagakar seedhe check kar sakta hai bina pages change kiye.

---

### 💻 Kali Linux Practice Task
Grepable file create aur check karne ke tasks:

**Task 1: Ek scan run karke grepable format save karein:**
```bash
nmap -oG nmap_stealth.gnmap scanme.nmap.org
```

**Task 2: File content check karein command se:**
```bash
cat nmap_stealth.gnmap
```
*(Observe karein ki standard screen structure ke comparison mein output single lines mein comma-separated formatted hai).*

**Task 3: Grep tool use karke direct open ports filter karna (Standard Pentesting technique):**
```bash
grep -i "open" nmap_stealth.gnmap
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Linux command line interface par kisi text file ke full content ko direct console output screen par print karne ke liye kis command ka use kiya jata hai?
- **A)** `ls`
- **B)** `cat`
- **C)** `grep`

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `nmap -oG test_scan.gnmap localhost`
2. Scan completion ke baad run karein: `cat test_scan.gnmap`
3. Check karein ki is file ke andhar host details horizontal formats mein save hain.
4. Quiz ka answer aur text status mujhe chat mein share karein!

---