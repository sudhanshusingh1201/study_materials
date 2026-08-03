---
title: "Topic 35 - Linux Command: rename (Bulk Rename Files using Patterns)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🔄 Topic 35: Linux Command: rename (Bulk Rename Files using Patterns)

Bhai, agar aapko terminal par ek single file rename karni ho, toh aap simple **`mv old.txt new.txt`** chala lete hain (jaise humne Topic 32 me seekha tha). 

Lekin imagine karo ki aapke paas ek folder me **100 ya 1000 files** hain (jaise log files, payloads ya target scan results), aur aapko un sabhi ka extension `.txt` se badal kar `.html` karna hai, ya unke naam ke aage se `temp_` word hatana hai. Agar aap ek-ek karke `mv` chalaoge, toh pura din nikal jayega. 

Is kaam ke liye Linux me ek super powerful command hoti hai: **`rename`**.

---

### 🔄 rename Command Kya Hai?
* **rename:** Ye command Perl programming language ke **Regular Expressions (Regex)** rules ka use karke multiple files ko ek sath bulk me rename (search and replace) karti hai.
* Kali Linux me ye tool by default installed hota hai (Perl-based variant).

---

### 🗂️ Regular Expression Syntax (The `s/find/replace/` Rule)
Is command me rename karne ka syntax is tarah likha jata hai:
```bash
rename [options] 's/purana_pattern/naya_pattern/' target_files
```
* **`s` (Substitute):** Iska matlab hai "badlo".
* **`/purana_pattern/`:** Wo word ya pattern jise dhoondhna (find) hai.
* **`/naya_pattern/`:** Wo naya word jo purane word ki jagah fit (replace) hoga.

---

### 🔑 Real-World Analogy (Excel Find & Replace 🔍🔄)
Maan lo aapke paas ek sheet me 50 students ke roll numbers likhe hain aur har number ke aage "STUDENT_" likha hai. 
* Agar aap ek-ek karke change karoge, toh boring ho jayega.
* Aap Microsoft Excel me **Ctrl + H** dabate ho aur **"Find: STUDENT_"** aur **"Replace with: KALI_"** karke **"Replace All"** kar dete ho. Ek second me sab badal jata hai.
* Linux me `rename` command wahi **"Replace All"** tool hai jo files ke naam par chalta hai.

---

### ⚡ rename Command Flags (Safety & Usage Guide)

#### 1. Dry Run Mode: `rename -n` (🛡️ Save Yourself From Disasters)
Regex me aapse galti ho sakti hai aur ho sakta hai ki aapki important files ke naam kharab ho jayein. 
* **`-n` (No action)** flag chalane se system file ko rename nahi karta, balki screen par **sirf preview dikhata hai** ki agar hum ise run karenge toh kya badlaav hoga. Ye safe test hai.
```bash
rename -n 's/\.txt/\.html/' *.txt
```
*Output preview:* `rename(file1.txt, file1.html)` (Lekin file actual me rename nahi hui hai).

---

#### 2. Verbose Mode: `rename -v`
Jab aap double-check kar lein ki pattern sahi hai, toh verbose flag lagakar command execute karein taaki screen par live log dikhe ki kaunsi file badal chuki hai:
```bash
rename -v 's/\.txt/\.html/' *.txt
```
*Output:* `file1.txt renamed as file1.html`

---

#### 3. Specific Operations:
* **Prefix Hatana (Delete a Word):**
  Agar files ka naam `temp_log1.txt`, `temp_log2.txt` hai aur `temp_` hatana hai:
  ```bash
  rename 's/temp_//' temp_*
  ```
  *(Yahan replace pattern empty `/` chhod diya, jisse `temp_` word remove ho jayega).*

* **Extension Badalna (Bulk Extension Change):**
  Sabh files ka `.txt` hatakar `.csv` karne ke liye (yahan `\.` dot ko treat karne ke liye escape `\` lagaya jata hai):
  ```bash
  rename 's/\.txt/\.csv/' *.txt
  ```

* **Uppercase to Lowercase (Aksharon ko chota karna):**
  Agar file names capital me hain (`FILE.TXT`) aur unhe chota karna hai (`file.txt`), toh Perl translation syntax `y/A-Z/a-z/` use hota hai:
  ```bash
  rename 'y/A-Z/a-z/' *
  ```

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `rename` command patterns check karne ke liye in tasks ko execute karein:

1. **Task 1:** Apne folder me 3 temporary files banayein: `test_1.log`, `test_2.log`, aur `test_3.log`.
2. **Task 2:** Dry run command `rename -n 's/test_/file_/' test_*` chalayein aur check karein ki preview kya dikhata hai (verify karein ki kya files actually rename nahi huin).
3. **Task 3:** Verbose flag `-v` lagakar actual execution run karein: `rename -v 's/test_/file_/' test_*`. Check karein ki files ke names `file_1.log`, `file_2.log` ho gaye hain.
4. **Task 4:** Ab `file_` prefix wali files me se completely prefix hatane ke liye `rename 's/file_//' file_*` run karein aur files ke names simple `1.log`, `2.log` karke verify karein.
5. **Task 5:** In files ke log extension ko badal kar text karne ke liye `rename -v 's/\.log/\.txt/' *.log` chala kar output log check karein.
6. **Task 6:** Ek file banayein `SECRET_DATA.txt`. Ise lowercase me convert karne ke liye translation rule `rename -v 'y/A-Z/a-z/' SECRET_DATA.txt` chala kar check karein.
7. **Task 7:** Multiple dots handling: `file.test.txt` file ka type checking karke pattern test setup chala kar extension badle: `rename -n 's/\.txt/\.bak/' *.txt` run karke preview dekhein.
8. **Task 8:** Dry-run options `-n` ke basic importance ko security automation me kyu mandatory mana jata hai? Apne wordings me short explanation dein.
9. **Task 9:** Ek file `old_backup.zip` banayein, aur regular expression search substitute dynamic operation replace verify karein.
10. **Task 10:** Hacking tools ke log outputs aur target database ranges structures cleanings me regex based `rename` command ke use cases detail me short analyze karein.

---
