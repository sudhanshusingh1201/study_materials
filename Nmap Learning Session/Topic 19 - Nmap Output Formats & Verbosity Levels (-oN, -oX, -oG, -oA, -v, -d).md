---
title: "Topic 19 - Nmap Output Formats & Verbosity Levels (-oN, -oX, -oG, -oA, -v, -d)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 19: Nmap Output Formats & Verbosity Levels (-oN, -oX, -oG, -oA, -v, -d)

### 1. Explanation (Hinglish)
Nmap scans chalate waqt do zaroori features use hote hain: **Verbosity** (screen par live details print karna) aur **Output Saving** (results ko files mein save karna).

---

### 1. Verbosity (Live Details on Screen)
Default scan jab tak complete nahi hota, screen par koi active update nahi deta. Scan progress ko real-time dekhne ke liye ye flags use hote hain:
- **`-v` (Verbose):** Nmap ko active banata hai. Jaise hi use target par koi open port dikhega, wo instant screen par show karega: *"Discovered open port 80/tcp"*.
- **`-vv` (Very Verbose):** Yeh `-v` se bhi double updates (detailed progress percentages aur internal socket logs) deta hai.
- **`-d` (Debugging):** Troubleshooting ke liye use hota hai. Scanner ke internally kya errors aa rahi hain, use packet-by-packet show karta hai (very noisy).

---

### 2. Output Formats (Results ko Save Karna)
Reports aur documentation ke liye scans ko file mein store karna zaroori hai. Nmap 4 major output formats support karta hai:

1. **`-oN <filename>` (Normal Format):** 
   - Console screen par jo standard human-readable format dikhta hai, bilkul wahi text format file mein save ho jata hai (e.g., `scan.nmap`).
2. **`-oG <filename>` (Grepable Format):** 
   - Isme har host ki detail ek single horizontal line mein store hoti hai. Yeh format Linux utilities (`grep`, `awk`, `cut`) ke zariye specific ports/IP addresses filter out karne ke liye perfect hai.
3. **`-oX <filename>` (XML Format):** 
   - Results ko XML file format mein save karta hai jo Metasploit ya Zenmap jaise tools ke backend import systems ke liye use hota hai.
4. **`-oA <basename>` (All Formats Combo):** 
   - Yeh teeno formats (`.nmap`, `.gnmap`, `.xml`) ek sath ek single command se same prefix name ke sath save kar deta hai (e.g., `nmap -oA my_scan target`).

---

#### 🗃️ Real-world Analogy: The Market Inspector's Reports
- **Without `-v` (No Verbose):** Inspector building checking karne jata hai, 15 minutes chup rehta hai aur aane ke baad direct bolta hai: *"Checking done, ye rahi details."*
- **With `-v` (Verbose):** Inspector gate check karte hi phone par call karke live batata hai: *"Main room 101 par hoon, ye khula hai. Ab kitchen check ho raha hai..."*
- **`-oN` (Hand-written diary):** Inspector general notebook mein details likhta hai readable sheets mein.
- **`-oG` (Excel list style):** Inspector details ko single line cells mein store karta hai taaki direct sorting filter run ho sake.
- **`-oX` (Official portal upload):** Inspector formatted database code (XML) file banata hai.
- **`-oA` (Complete File Case):** Inspector ek folder bracket (Basename) banata hai jisme hand-written sheet, excel list, aur db file teeno save karke file lock kar deta hai.

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par outputs save aur view karne ke tasks:

**Task 1: Real-time updates ke sath scan run karna:**
```bash
nmap -v scanme.nmap.org
```

**Task 2: Teeno formats ek sath `ls_scan` prefix se save karna:**
```bash
nmap -v -oA ls_scan scanme.nmap.org
```
*(Scan complete hone par type karein `ls` aur check karein file systems: `ls_scan.nmap`, `ls_scan.gnmap`, aur `ls_scan.xml` check ho jayenge).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap scan outputs ko Normal, XML, aur Grepable formats mein ek sath ek single command se save karne ke liye kis flag combo ka use kiya jata hai?
- **A)** `-oN`
- **B)** `-oA`
- **C)** `-oG`

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `nmap -v -oG localhost_scan.txt localhost`
2. Scan complete hone par type karein: `cat localhost_scan.txt`
3. Check karein ki kya file ke andar details standard console output ke badle horizontal formatting format mein saved hain?
4. Quiz ka answer aur text status mujhe chat mein batayein!

---