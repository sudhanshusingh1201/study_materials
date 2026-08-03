---
title: "Topic 23 - Nmap Normal Output Format (-oN)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 23: Nmap Normal Output Format (-oN)

### 1. Explanation (Hinglish)
Aapne jo command option select kiya hai: **`-oN nmap_connect`**, yeh Nmap mein output saving ka sabse standard aur basic mechanism hai.

Chalo is command components ko aasan shabdon mein break-down karte hain:

1. **`-oN` (Output Normal):**
   - **`-o`**: Output flag.
   - **`N`**: Normal.
   - Yeh Nmap ko instruct karta hai ki jo scan output aapko screen terminal par default roop se display hota hai, use bilkul usi format mein ek standard human-readable text file mein write (save) kare.

2. **`nmap_connect` (File Name):**
   - Yeh humari file ka custom name hai. Nmap isme by-default koi text extension connect nahi karta. Lekin identification ke liye security auditors ise `.nmap` ya `.txt` extension ke sath save karte hain (e.g., `nmap_connect.nmap`).

#### ❓ Hume iski zarurat kyun hoti hai?
- **Human Readability:** Yeh format logs ko aasan padhne ke roop mein maintain karta hai. Agar kisi client, manager ya non-technical team member ko scan summary bhejni ho, toh ye format best hai.
- **Copy-Paste Documentation:** Apne research notes ya reports (jaise Obsidian vault files) mein results directly copy-paste karne ke liye.

---

#### 🚪 Real-world Analogy: The Inspector's Official Report Sheet
Socho aap ek security checker ho aur aapne building inspect ki hai:
- **`-oN` (Normal Diary entry):** Checking complete karne ke baad, aap details ko apni formal diary page par standard, clean format mein likhte ho (jaise: *"Room 80: Open, Active service: Apache"*). Ise koi bhi insaan asani se padh sakta hai.
- **`-oG` (Database listing):** Aap raw details ko ek single horizontal excel row line mein commas ke sath fill karte ho (computer read karne ke liye, jo human eyes ke liye messy ho sakti hai).
`-oN` humari wahi clean hand-written diary report sheet hai.

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par standard output save aur monitor karne ke tasks:

**Task 1: Standard format file save command run karna:**
```bash
nmap -oN nmap_connect.nmap scanme.nmap.org
```

**Task 2: Saved file details read karna console par:**
```bash
cat nmap_connect.nmap
```
*(Observe karein ki screen par saved file ka content default terminal console screen output ki tarah clean tabular layout mein saved hai).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap results ko human-readable normal text formatting formats (standard console representation style) mein save karne ke liye kis flag code option ka use kiya jata hai?
- **A)** `-oX`
- **B)** `-oN`
- **C)** `-oG`

#### 🎯 Assignment
1. Kali Linux terminal par run karein: `nmap -oN localhost_normal.txt localhost`
2. Scan complete hone par test print karein: `cat localhost_normal.txt`
3. Verify karein ki file details console screen format ke identical hain.
4. Quiz ka answer aur tasks completion updates mujhe chat mein share karein!

---