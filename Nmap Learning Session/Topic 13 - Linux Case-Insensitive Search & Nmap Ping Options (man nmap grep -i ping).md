---
title: "Topic 13 - Linux Case-Insensitive Search & Nmap Ping Options (man nmap grep -i ping)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 13: Linux Case-Insensitive Search & Nmap Ping Options (man nmap | grep -i "ping")

### 1. Explanation (Hinglish)
- **`grep -i` (Ignore Case):** Search ko case-insensitive banata hai, jisse word ka capital/small variation ignore hokar saare matches show hote hain.
- **`"ping"` options:** Nmap mein ping/discovery se related options check karna.

---

### 💻 Kali Linux Practice Task
Terminal checks:

**Task 1: Default vs case-insensitive check:**
```bash
nmap --help | grep "ping"
nmap --help | grep -i "ping"
```

**Task 2: Multiple terms filter check karna:**
```bash
nmap --help | grep -i -E "ping|discovery"
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Linux `grep` command mein case-insensitive search (capital aur small variations dono include karna) karne ke liye kis flag ka use kiya jata hai?
- **A)** `-c`
- **B)** `-v`
- **C)** `-i`

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `nmap --help | grep -i "scan"`
2. Quiz ka answer aur assignment search summary mujhe chat mein batayein!

---