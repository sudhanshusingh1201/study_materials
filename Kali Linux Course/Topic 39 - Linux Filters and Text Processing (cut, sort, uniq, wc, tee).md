---
title: "Topic 39 - Linux Filters & Text Processing (cut, sort, uniq, wc, tee)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# ⚙️ Topic 39: Linux Filters & Text Processing (cut, sort, uniq, wc, tee)

Bhai, Linux CLI ka sabse bada power feature hai **Pipes (`|`)** ka use karke commands ko aapas me connect karna. Jab hum ek command ka output doosri command me bhejte hain, toh beech me data ko clean aur process karne ke liye **Filters** ka use kiya jata hai.

Cybersecurity assessments (jaise Nmap scan output, active IPs, ya wordlists data extraction) me data ko clean karne ke liye ye text processing filters aapke sabse bade weapons hain.

---

### ⚙️ Core Text-Processing Filters

#### 1. `cut` (Sections aur Columns ko cut karna)
Ye file ki har line se selected fields ya character columns ko cut karke nikalta hai.
* **`-d` (Delimiter):** Wo symbol jo columns ko separate karta hai (jaise comma `,`, colon `:` ya space).
* **`-f` (Field):** Kaunsa column number nikalna hai.
* *Example (Extracting usernames from `/etc/passwd`):*
  ```bash
  cut -d':' -f1 /etc/passwd
  ```
  *(Ye `/etc/passwd` file me colon `:` ko boundary maan kar pehla column (usernames) print karega).*

---

#### 2. `sort` (Data ko lines me sort karna)
Ye lines ko alphabetically ya numerically sort (arrange) karta hai.
* **Basic usage:** `sort list.txt` (Alphabetical order).
* **`-n` (Numerical sort):** Numbers ke basis par sort karne ke liye.
* **`-r` (Reverse sort):** Z to A ya descending order me sort karne ke liye.
* *Example:*
  ```bash
  sort -n -r ip_list.txt
  ```

---

#### 3. `uniq` (Duplicate entries remove karna) 🚫
Ye lagatar aane wali duplicate lines ko remove karke sirf single unique line print karta hai.
* **⚠️ WARNING:** `uniq` command sirf **apne just niche aane wali line** se compare karti hai. Isiliye `uniq` lagane se pehle **`sort`** karna zaroori hai!
* **`-c` (Count):** Har unique line kitni baar repeat hui hai, uska count batata hai.
* *Example (Sorting and counting unique IPs):*
  ```bash
  sort ip_list.txt | uniq -c
  ```

---

#### 4. `wc` (Word, Line, & Character Count) 📊
Ye file ke andar ka statistics count batata hai.
* **`-l` (Line count):** Sabse zyada use hone wala flag jo file me total lines batata hai.
* **`-w` (Word count):** Total words.
* **`-c` (Byte/Character count):** Total characters.
* *Example (Counting total entries in a wordlist):*
  ```bash
  wc -l rockyou.txt
  ```

---

#### 5. `tee` (Screen print + File write simultaneously) 🔀
Normal redirection (`>`) output ko file me bhejta hai par screen par kuch nahi dikhata. **`tee`** command ek T-splitter ki tarah kaam karti hai—ye output ko terminal screen par bhi dikhati hai aur sath hi sath file me bhi save karti hai.
* *Example:*
  ```bash
  ls -la | tee directory_backup.txt
  ```
  *(Output screen par bhi dikhega aur `directory_backup.txt` me save bhi ho jayega).*

---

### 🔑 Real-World Analogy (The Juice Factory 🍹⚙️)
Maan lo terminal pipeline (`|`) ke andar se behne wala data **Ganne (Sugarcane)** ki tarah hai:
* **`cut` (Peeler):** Ganne ke upar ka chhilka utaar kar sirf kaam ka hissa rakhta hai (faltu columns ko uda deta hai).
* **`sort` (Organizer):** Ganne ke pieces ko unki lambai (numerical/alphabetical order) ke hisab se line me laga deta hai.
* **`uniq` (Quality Checker):** Bilkul same dikhne wale duplicate pieces ko fenk deta hai taaki unique taste bana rahe.
* **`wc` (Scale):** Processed ganno ko gin (count) leta hai.
* **`tee` (Splitter Tap):** Tayyaar ganne ke juice ko customer ke glass (screen) me bhi dalta hai aur side me ek backup storage container (file) me bhi fill karta jata hai.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, data filters verify karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** Ek sample file banayein `raw_data.txt` aur usme ye details likhein (name:role format):
   ```text
   admin:administrator
   kali:tester
   kali:tester
   sudhanshu:admin
   guest:read-only
   ```
2. **Task 2:** Delimiter `:` ka use karke sirf names (column 1) ko nikalne ke liye `cut -d':' -f1 raw_data.txt` chala kar verify karein.
3. **Task 3:** `raw_data.txt` ke role column (column 2) ko extract karne ke liye appropriate `cut` command likhein.
4. **Task 4:** Names column ko extract karke alphabetically sort karne ke liye `cut -d':' -f1 raw_data.txt | sort` pipe verify karein.
5. **Task 5:** Bina sort kiye direct `uniq raw_data.txt` chalayein aur check karein kya duplicates clean hue. Phir `sort raw_data.txt | uniq` chala kar difference dekhein.
6. **Task 6:** Duplicate entries kitni baar repeat ho rahi hain, count ke sath check karne ke liye `sort raw_data.txt | uniq -c` chala kar verify karein.
7. **Task 7:** `raw_data.txt` file me total kitni lines hain, use dynamic count karne ke liye `wc -l raw_data.txt` ka count check karein.
8. **Task 8:** Kali Linux authentication logs list me check karein ki aakhri 10 events me se kitne unique messages generate hue: `tail /var/log/alternatives.log | sort | uniq`.
9. **Task 9:** Ek command chala kar output ko screen par bhi dekhein aur file `tee_test.txt` me save bhi karein: `whoami | tee tee_test.txt`.
10. **Task 10:** Cybersecurity scanning outputs filters (jaise IP logs segregation) me `cut`, `sort` aur `uniq` ke dynamic integration workflows ka kya role hai? 2 lines me explain karein.

---
