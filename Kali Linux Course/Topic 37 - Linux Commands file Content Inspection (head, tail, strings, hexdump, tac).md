---
title: "Topic 37 - Linux Commands: File Content Inspection (head, tail, strings, hexdump, tac)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 📖 Topic 37: Linux Commands: File Content Inspection (head, tail, strings, hexdump, tac)

Bhai, humne pichli topics me file read karne ke liye **`cat`** (Topic 22) aur **`less`** (Topic 24) commands seekhi thi. Lekin Linux me different situations (jaise bade log files check karna, binaries investigate karna, ya live updates track karna) ke liye alag-alag commands hoti hain.

Cybersecurity aur system analysis me, pure 10GB ke log file ko `cat` karna terminal ko hang kar sakta hai. Isliye hume parts me file content inspect karna aana chahiye.

---

### ⚡ Core File Content Inspection Commands

#### 1. `head` (Start / Top level lines read karna)
Ye file ki shuruat ki lines (default top 10 lines) dikhata hai.
* **Basic usage:**
  ```bash
  head wordlist.txt
  ```
* **Custom lines specify karna (`-n`):**
  Agar aapko sirf starting ki **5 lines** dekhni hain:
  ```bash
  head -n 5 wordlist.txt
  ```

---

#### 2. `tail` (End / Bottom level lines read karna) 🏷️
Ye file ke aakhri ka hissa (default last 10 lines) dikhata hai.
* **Basic usage:**
  ```bash
  tail auth.log
  ```
* **Live Log Monitoring (`tail -f` - A Hacker's Favorite):**
  Hacking aur system monitoring me, jab active connections logs generate ho rahe hote hain, toh hum chahte hain ki monitor par screen live update ho. **`-f` (follow)** flag lagane se jaise hi file me nayi line judegi, wo screen par live scroll hone lagegi.
  ```bash
  tail -f /var/log/auth.log
  ```
  *(Press `Ctrl + C` to stop monitoring).*

---

#### 3. `tac` (Reverse Line Order 🔄 - cat ka ulta)
`cat` file ko line 1 se aakhri line tak padhta hai. **`tac`** bilkul iska opposite (ulta) kaam karta hai—ye file ki last line ko sabse pehle aur line 1 ko sabse aakhri me print karta hai.
```bash
tac my_steps.txt
```

---

#### 4. `strings` (Extract Printable Text from Binaries 🕵️‍♂️)
Compiled binaries (jaise `.exe`, `.elf` executables, or images) readable text me nahi hoti. Unhe `cat` karne par kachra output aata hai.
* **`strings`** command kisi bhi file (chahe compiled malware hi kyun na ho) ke andar se saare **printable ASCII characters** (English words, URLs, hardcoded passwords, IP addresses) ko extract karke print kar deti hai.
  ```bash
  strings malware_payload
  ```
  *(Cybersecurity analysis me iska use static malware analysis ke pehle step me kiya jata hai).*

---

#### 5. `hexdump` & `xxd` (Raw Bytes in Hexadecimal 🧮)
Kuch files corrupt ho jaati hain ya unka header verification fail ho jata hai. Unke actual raw structure (Hex codes aur characters) ko side-by-side inspect karne ke liye hum in tools ka use karte hain:
* **`hexdump -C <file>`** (Canonical hex+ASCII display):
  ```bash
  hexdump -C image.png
  ```
* **`xxd <file>`** (Equivalent and highly formatted hexadecimal dump tool):
  ```bash
  xxd target.bin
  ```

---

### 🔑 Real-World Analogy (The Book Inspector 📚🔍)
Maan lo aapko ek 500 pages ki moti book inspect karni hai:
* **`head`:** Jaise book ke shuru ke **5 lines or index** padhna.
* **`tail`:** Jaise book ki **aakhri summary lines** ya conclusion padhna.
* **`tail -f`:** Jaise live news ticker ko padhna (jahan har naya event aate hi niche judta jata hai).
* **`strings`:** Jaise kisi Japanese book me se sirf **English me likhe words** ko chun kar nikal lena.
* **`hexdump`:** Jaise book ke har page ke paper structure, binding fibers, aur ink molecules ko micro-level par analyze karna.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, file inspection parameters check karne ke liye in tasks ko execute karein:

1. **Task 1:** Ek test file banayein `words_master.txt` jisme 15 lines likhein (jaise 1 se 15 tak counting). Ab standard `head words_master.txt` chala kar check karein ki kitni lines print hoti hain.
2. **Task 2:** Apne local network scan lists or passwords wordlist ke top **3 entries** dekhne ke liye `head -n 3 words_master.txt` ka syntax run karein.
3. **Task 3:** `words_master.txt` ke sabse bottom ki last 5 entries monitor karne ke liye `tail -n 5 words_master.txt` run karein.
4. **Task 4:** Kali Linux ke default authentication system log files (jaise `/var/log/alternatives.log`) ke bottom parts ko read karne ke liye `tail` chala kar check karein.
5. **Task 5:** `tac words_master.txt` chalayein aur verify karein ki kya 15th line top par aur 1st line bottom par show ho rahi hai (reverse list).
6. **Task 6:** Hacking binary tool utility path `/usr/bin/whoami` par simple `cat` chalakar screen garbage check karein, aur phir **`strings /usr/bin/whoami`** chala kar output readable text check karein.
7. **Task 7:** Check karein ki kya dynamic binary (e.g. `/usr/bin/ls`) ke strings logs ko grep kiya ja sakta hai: `strings /usr/bin/ls | grep -i "author"`.
8. **Task 8:** Image file structure magic headers check karne ke liye `xxd test_magic.png` (ya koi png file) ka hexa-decimal dump analyze karein.
9. **Task 9:** Hexadecimal verification database check ke liye Canonical format flag **`-C`** lagakar run karein: `hexdump -C words_master.txt`.
10. **Task 10:** Hacking investigations aur digital forensics payloads monitoring me `tail -f` aur `strings` command ke unique use-cases ko details me compare karein.

---
