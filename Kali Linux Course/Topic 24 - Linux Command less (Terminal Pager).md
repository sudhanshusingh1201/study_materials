---
title: "Topic 24 - Linux Command less (Terminal Pager)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 📖 Topic 24: Linux Command: less (Terminal Pager)

Bhai, agar file choti ho toh `cat` se use display par read karna aasan hai. Par agar file bohot badi ho (jaise `/var/log/dpkg.log` jisme hazaron lines hain, ya hacking wordlist `rockyou.txt`), toh `cat` chalane par pura terminal screen bhar jata hai aur terminal crash/lag ho sakta hai. Badi files ko smoothly aur parts me read karne ke liye hum **`less`** command ka use karte hain.

---

### 📖 less Command Kya Hai?
* **less:** Ye ek terminal pager program hai. 
* Ye file ke content ko screen par ek sath dump nahi karta, balki use **page-by-page (screen size ke according)** open karta hai. 
* *Fact:* Linux world me ek purani line kaafi famous hai: *"less is more, but more is less."* (Ye purane `more` command ka upgraded version hai).

---

### 🔑 Real-World Analogy (E-Reader / Kindle 📖)
Maan lo aapko 500 pages ki ek novel padhni hai:
* **cat command:** Jaise novel ke saare pages ko ek sath chipka kar ek bohot lambi scroll sheet bana di jaye aur use chhat se niche gira diya jaye. (Aap scroll up-down karte thak jaoge).
* **less command:** Jaise aapko ek **Kindle / E-Reader** de diya jaye. Aap screen par ek baar me sirf 1 page hi dekh sakte ho. Aap switch dabakar agla page laate ho (`Space`), back key daba kar piche jaate ho (`b`), aur text search karte ho.

---

### 🗂️ Basic Command Syntax:
```bash
less /var/log/dpkg.log
```
*(Isse log file ek clean paginated interface me open ho jayegi. Is screen se exit karne ke liye keyboard par **`q`** dabana hota hai).*

---

### ⚡ Keyboard Shortcuts inside less (Master Controls 🎮)

Jab file `less` me open ho, toh keyboard par in buttons ka use karke fast navigate karein:

#### 1. Page & Line Navigation:
* **`Spacebar`** or **`Page Down`**: Go down 1 full page (agla page).
* **`b`** or **`Page Up`**: Go up (backward) 1 full page (pichla page).
* **`Down Arrow`** or **`Enter`**: Move down 1 single line.
* **`Up Arrow`**: Move up 1 single line.
* **`G` (Capital G):** Directly jump to the **end (bottom)** of the file.
* **`g` (small g):** Directly jump to the **beginning (top)** of the file.

#### 2. Search Commands:
* **`/keyword`**: Forward search. `/` lagane ke baad jo word search karna hai type karein aur `Enter` dabayein:
  * **`n` (next):** Agle match par jump karne ke liye.
  * **`N` (previous):** Pichle match par wapas aane ke liye.
* **`?keyword`**: Backward search (piche ki taraf search karne ke liye).

#### 3. Exit:
* **`q` (Quit):** Interface close karke terminal prompt me wapas aane ke liye.

---

### ⚡ Useful Flags:
* **`less -N`**: File open karte waqt left side me line numbers bhi print karega.
  ```bash
  less -N /var/log/dpkg.log
  ```

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `less` commands controls practice karne ke liye in tasks ko complete karein:

1. **Task 1:** System password metadata file `/etc/passwd` ko `less` command ke zariye open karein.
2. **Task 2:** Interface open hone ke baad, keyboard par **`Spacebar`** aur **`b`** press karke scroll forward aur backward verify karein.
3. **Task 3:** File ke sabse aakhri line par direct jump karne ke liye kaunsa keyboard shortcut use karenge? Run karke check karein.
4. **Task 4:** Task 3 complete hone ke baad, direct file ke starting index (Line 1) par jump karne ke liye shortcut use karein.
5. **Task 5:** `/etc/passwd` file ke andar user `kali` search karne ke liye forward search syntax run karein.
6. **Task 6:** Search results active hone par, key **`n`** aur **`N`** daba kar matches toggle verify karein.
7. **Task 7:** System logs file `/var/log/dpkg.log` ko side indices numbers ke sath open karne ke liye command run karein. (Hint: use `-N` flag).
8. **Task 8:** Open `less` screen ke andar, single-line down move karne ke liye keyboard ke kaunse do controls trigger kiye ja sakte hain?
9. **Task 9:** Target file read check complete hone ke baad, terminal interface me clean back return switch button execute karein.
10. **Task 10:** Command lines pipeline checks me: `ls -la /etc | less` command run karein aur batayein ki is execution framework ka kya purpose hai. (Hint: piping concept stack).

---