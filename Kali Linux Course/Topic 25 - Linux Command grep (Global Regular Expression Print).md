---
title: "Topic 25 - Linux Command grep (Global Regular Expression Print)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🔍 Topic 25: Linux Command: grep (Global Regular Expression Print)

Bhai, terminal me jab hume kisi bohot badi text file (jaise logs ya config files) me se **kisi khaas word ya pattern (jaise "src", IP, or error)** ko dhoondhna hota hai, toh hum **`grep`** command ka use karte hain. Ye CLI ka **Ctrl + F** (Find) option hai!

---

### 🔍 grep Command Kya Hai?
* **grep:** **G**lobal **R**egular **E**xpression **P**rint.
* Ye files ke andar contents ko line-by-line scan karta hai aur sirf wahi lines print karta hai jo aapke search keyword (pattern) se match karti hain.

---

### 🔑 Real-World Analogy (Tea Strainer / Chhanni 🧪)
Maan lo aapke paas **Chai aur Patti (purn file content)** ka mixture hai. 
* Agar aap use direct cup me daloge, toh patti bhi aa jayegi. 
* Lekin agar aap **Chhanni (grep command)** ka use karoge, toh sirf patti cup me nahi jayegi aur aapko clean chai milegi. 
* Linux me pure content me se sirf match hone wale words ko chhan kar bahar nikalna **`grep`** ka kaam hai.

---

### 🗂️ Basic Command Syntax:
```bash
grep "search_word" filename.txt
```

---

### ⚡ Critical grep Flags (Search Options Guide)

Aap in flags ka use karke search filtration ko modify kar sakte ho:

#### 1. `grep -i "word"` (Ignore Case 🔠)
Linux case-sensitive hai, yaani `src` aur `SRC` alag hain. Agar aap chahte ho ki matches me capitalization ka farq padhe bina saare matches dikhein, toh **`-i`** lagayein:
  ```bash
  grep -i "src" /etc/apt/sources.list
  ```
  *(Ye "src", "SRC", "Src" sabhi patterns ko match karega).*

#### 2. `grep -v "word"` (Invert Match / Remove Word 🚫)
Agar aap chahte ho ki display par wo saari lines aayein jinme **wo word na ho**, toh `-v` flag use karein. (Noise filter karne ke liye best hai).
  ```bash
  grep -v "root" /etc/passwd
  ```

#### 3. `grep -n "word"` (Show Line Numbers 🔢)
Ye batayega ki match hone wali line file ke andar kis particular line number par exist karti hai.
  ```bash
  grep -n "kali" /etc/passwd
  ```

#### 4. `grep -r "word"` or `grep -R` (Recursive Search 📁)
Agar aapko single file ke badle **pure folder aur sub-folders** ke andar ki sabhi files me koi word dhoondhna ho (jaise kisi configuration folder me system configuration key search karni ho):
  ```bash
  grep -r "192.168" /etc/
  ```

#### 5. `grep -w "word"` (Whole Word Matches Only 🔤)
Ye command exact full word matches search karegi. Agar aap `src` search kar rahe hain, toh ye `sources` ya `srccode` ko match nahi karega, sirf exact `src` word ko match karega.
  ```bash
  grep -w "src" filename.txt
  ```

#### 6. `grep -c "word"` (Count Matches 🔢)
Ye match hone wali lines ko screen par print nahi karega, balki batayega ki total kitni lines me wo word exist karta hai (count total matches).

---

### 🤝 The Power of Pipe operator (`|`) + grep 🔗
Linux me `grep` ko normal command output filter karne ke liye sabse zyada **Pipe (`|`)** ke sath use kiya jata hai. Pipe pehli command ke output ko `grep` me inject kar deta hai:

* **Example 1:** System processes check karte waqt sirf `apache2` server find karna:
  ```bash
  ps aux | grep "apache2"
  ```
* **Example 2:** Terminal execution command history me se sirf `ssh` commands filter karna:
  ```bash
  history | grep "ssh"
  ```

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `grep` search capabilities verify karne ke liye in tasks ko execute karein:

1. **Task 1:** File `/etc/apt/sources.list.d/kali.sources` ke andar search filter lagakar word **`src`** dhoondhein.
2. **Task 2:** Task 1 me `src` dhoondhte waqt **`-i` (Ignore Case)** flag use karein aur check karein ki kya capital `SRC` ya normal combinations bhi print ho rahe hain.
3. **Task 3:** File `/etc/passwd` ke andar default line numbers verify karne ke liye user **`kali`** ko matching line number **`-n`** flag ke sath dhoondhein.
4. **Task 4:** `/etc/passwd` file ke andar user `root` ki entry ko **exclude (remove)** karke baaki users list dekhne ke liye **`-v`** filter command run karein.
5. **Task 5:** Ek generic recursive command chala kar check karein ki user configuration path `/etc/pam.d/` ke kis-kis folder file ke andar configuration word **`pam`** use kiya gaya hai. (Hint: use `-r`).
6. **Task 6:** Kali system configuration `/etc/resolv.conf` dns details me word **`nameserver`** kitni lines me likha hua hai, uski numeric total count nikalne ke liye **`-c`** flag run karein.
7. **Task 7:** Pipe line structure ka use karein: Apne active running network processes check karein ya active connections me `ss -tulpn | grep "53"` chalakar verify karein ki port 53 (DNS) run ho raha hai ya nahi.
8. **Task 8:** Kali system history memory me check karein ki aapne pichli commands me **`nano`** ka use kab-kab kiya tha. (Command: `history | grep "nano"`).
9. **Task 9:** Whole word matching verify karne ke liye directory path check command: `/etc/passwd` me exact username word **`da`** search karein `-w` ke sath aur verify karein ki ye `daemon` user ko bypass (omit) kar deta hai ya nahi.
10. **Task 10:** Ek sath ignore case, line numbers aur whole word matches verify karne ke liye teen flags combine karke `/etc/apt/sources.list.d/kali.sources` me check command execute karein.

---