---
title: "Topic 08 - Nmap Scan All Ports (-p-)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 8: Nmap Scan All Ports (-p-)

### 1. Explanation (Hinglish)
Nmap mein **`-p-`** flag ka use **target system ke sabhi 65,535 ports ko scan karne ke liye** kiya jata hai.

Default Nmap scan target ke sirf **top 1,000 most common ports** ko scan karta hai. Lekin custom ports par chalne wali hidden services ko dhoondhne ke liye full range scan zaroori hai.

#### 🚪 Real-world Analogy: Checking Every Single Door
Socho aap ek hotel inspector ho jisme total **65,535 rooms (ports)** hain:
- **Default Scan:** Aap sirf receptionist se top 1,000 standard suites check karte ho.
- **`-p-` Scan:** Aap room number 1 se 65,535 tak ke har ek darwaze par jaakar knock karte ho.

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par saare ports scan karne ke liye commands:

**Task 1: Target ke saare 65,535 ports scan karna:**
```bash
nmap -p- scanme.nmap.org
```

**Task 2: Full port scan ko fast karne ke liye Timing template (-T4) add karna:**
```bash
nmap -p- -T4 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap mein `-p-` command target system ke kis range ke ports ko scan karti hai?
- **A)** Top 1,000 ports.
- **B)** Ports 1 to 1024.
- **C)** Ports 1 to 65,535.

#### 🎯 Assignment
1. Apne Kali Linux terminal par run karein: `nmap -p- localhost`
2. Dekhein ki default scan ke comparison mein isme kitna time lagta hai aur loopback par koi extra port open mila ya nahi.
3. Quiz ka correct answer aur localhost scan time mujhe chat mein batayein!

---