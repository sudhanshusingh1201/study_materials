---
title: "Topic 12 - Linux Piping & Grepping (man nmap grep sn)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 12: Linux Piping & Grepping (man nmap | grep sn)

### 1. Explanation (Hinglish)
- **`man`:** Command manual details kholna.
- **`|` (Pipe):** Ek command ke output ko doosri command ke input mein transfer karna.
- **`grep`:** Specific word/pattern ko search karna.

---

### 💻 Kali Linux Practice Task
Terminal check tasks:

**Task 1: Normal grep search run karna:**
```bash
man nmap | grep sn
```

**Task 2: Exact `-Pn` flag search check karna:**
```bash
nmap --help | grep -i "\-Pn"
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Linux system mein ek command ke text output ko direct doosri command ke input buffer mein transfer karne ke liye kaunsa pipe symbol use kiya jata hai?
- **A)** `>`
- **B)** `|`
- **C)** `&`

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `nmap --help | grep -i "\-sT"`
2. Quiz ka answer aur assignment output mujhe chat mein share karein!

---