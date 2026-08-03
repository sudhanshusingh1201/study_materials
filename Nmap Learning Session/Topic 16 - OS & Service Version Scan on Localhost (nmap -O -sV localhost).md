---
title: "Topic 16 - OS & Service Version Scan on Localhost (nmap -O -sV localhost)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 16: OS & Service Version Scan on Localhost (nmap -O -sV localhost)

### 1. Explanation (Hinglish)
Aapne jo command select ki hai: **`nmap -O -sV localhost`**, yeh target machine (is case mein aapki local machine `localhost` / `127.0.0.1`) par ek sath do scans execute karti hai:
1. **`-O` (OS Detection):** Target operating system (Windows/Linux/macOS) identify karne ke liye.
2. **`-sV` (Service Version Detection):** Local ports par chalne wali services ke exact versions grab karne ke liye.

---

### ⚠️ Zaroori Rule: Privilege Restriction
Agar aap normal user account se ye command chalate hain:
```bash
nmap -O -sV localhost
```
Toh Nmap error dega: **`TCP/IP fingerprinting (OS scan) requires root privileges.`**

**Aisa kyun hota hai?**
OS Detection (`-O`) karne ke liye Nmap ko low-level custom raw TCP/UDP packets design karke bhejne hote hain. Normal user account ko OS raw sockets generate karne ki permission nahi deta. Isliye is scan ko hamesha **`sudo`** (superuser) ke sath run karna padta hai:

```bash
sudo nmap -O -sV localhost
```

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par in tasks ko check karein:

**Task 1: Normal privilege execution error check karna:**
```bash
nmap -O -sV localhost
```
*(Notice karein root warning error message).*

**Task 2: Proper scanning with Root Privileges:**
```bash
sudo nmap -O -sV localhost
```
*(Local scan hone ke karan scan super-fast complete ho jayega. Check karein OS guessing status).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
OS Detection (`-O`) jaise raw packets scans chalane ke liye Nmap ko root/administrator access dene ke liye Linux mein kis keyword prefix ka use kiya jata hai?
- **A)** `run`
- **B)** `sudo`
- **C)** `admin`

#### 🎯 Assignment
1. Kali Linux terminal par run karein: `sudo nmap -O -sV localhost`
2. Dekhein ki kya aapke localhost par koi port open mila.
3. Operating System guessing report mein system ne aapki Kali machine ka kernel OS version kya match kiya.
4. Quiz ka correct answer aur output updates mujhe share karein!

---