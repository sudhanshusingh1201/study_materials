---
title: "Topic 26 - Linux Command echo (Print Text)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🗣️ Topic 26: Linux Command: echo (Print Text)

Bhai, terminal me text lines ko display karne, environment variables ke values ko check karne, ya scripting me screen par status updates print karne ke liye jo command use ki jaati hai, use **`echo`** kehte hain.

---

### 🗣️ echo Command Kya Hai?
* **echo:** Repeat/Goonj.
* Is command ka primary function kisi text line ya parameters ko direct terminal output screen par print (echo) karna hota hai.

---

### 🔑 Real-World Analogy (Parrot / Tota 🦜)
Maan lo aapke paas ek **bolne wala tota (parrot)** hai. 
* Aap uske saamne jo bhi bologe (jaise: "Hacking is fun"), tota wahi exact words repeat kar dega.
* Agar aap uske paas koi stored variable reference puchoge, toh wo us variable ke andar ka data check karke boldega. Terminal me isi dynamic repeat-system ko **`echo`** kehte hain.

---

### 🗂️ Basic Command Syntax:
```bash
echo "Hello Sudhanshu"
```
*(Isse terminal screen par `Hello Sudhanshu` output print ho jayega).*

---

### ⚡ Critical echo Flags & Features (Cheat Sheet)

Aap `echo` command ka behavior change karne ke liye in flags ka use kar sakte hain:

#### 1. Print Environment Variables (Variables Check 📊)
Linux ke internal path aur active configurations variables (jo CAPITAL letters me hote hain) ko print karne ke liye variable ke aage **`$`** symbol lagakar `echo` chalaaya jaata hai:
  ```bash
  echo $USER  # Output: kali (Current logged-in user)
  echo $HOME  # Output: /home/kali (User's home directory path)
  echo $PATH  # Output: System execution directories search paths
  ```

#### 2. `echo -e` (Enable Backslash Escapes ⚡)
Ye flag sabse powerful hai scripting me. Ye backslash characters code symbols ko print layout formats me convert karta hai:
* **`\n` (Newline):** Text ko agli line (next row) me bhej deta hai.
* **`\t` (Tab space):** Beech me tab space add karta hai.

##### 🚀 Newline Example:
```bash
echo -e "Line One\nLine Two"
```
*Output:*
```text
Line One
Line Two
```

#### 3. `echo -n` (No Newline 🚫)
Standard `echo` line print karne ke baad cursor ko automatic new line par switch kar deta hai. `-n` lagane par **trailing newline remove** ho jaati hai aur cursor usi line ke end me chipka rehta hai.
  ```bash
  echo -n "Kali Linux"
  ```

#### 4. File Redirections (Create & Append 📝)
`echo` ko pipe redirection operators ke sath combine karke fast write operation kiya jata hai:
* **Overwrite (`>`):** Nayi text file banane ya purani file ko overwrite karne ke liye:
  ```bash
  echo "My IP: 192.168.1.1" > ip.txt
  ```
* **Append (`>>`):** File ke aakhir me bina purane data ko delete kiye naya line add karne ke liye:
  ```bash
  echo "My Subnet: 255.255.255.0" >> ip.txt
  ```

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `echo` functionalities confirm karne ke liye in tasks ko terminal par test karein:

1. **Task 1:** Terminal open karein aur `echo` command ka use karke ek line screen par print karein: "Kali Linux is my favorite OS".
2. **Task 2:** Apne terminal par dynamic variable **`$USER`** ko print karke confirm karein ki aapka current active logging name kya show ho raha hai.
3. **Task 3:** Aap system home directory kis path par config hai, use check karne ke liye **`$HOME`** variable check command execute karein.
4. **Task 4:** Terminal me **`-e`** flag ka use karke ek single `echo` command se teen lines sequence me print karein: "Red Team", "Blue Team", "Purple Team" (Hint: use `\n` line breaks).
5. **Task 5:** Double horizontal columns structure represent karne ke liye **`\t`** escape parameter ka use karke output print karein: "Name" aur "Roll No" (Hint: `echo -e "Name\tRoll No"`).
6. **Task 6:** Normal `echo` aur **`-n`** flag lagakar run kiye gaye outputs ke beech cursor positions checks verify karein.
7. **Task 7:** Overwrite redirection operator **`>`** ka use karke dynamic string "Target IP: 10.10.10.5" ko `target.txt` file ke andar write karein.
8. **Task 8:** Target.txt file ko read karne ke liye `cat target.txt` run karein aur verify karein ki content enter ho gaya hai.
9. **Task 9:** Append redirection operator **`>>`** ka use karke `target.txt` file ke aakhir me "Target Port: 80" add karein aur verify karein ki first line safe hai ya delete ho gayi.
10. **Task 10:** Hacking terminals me color displays configurations trigger karne ke liye color coding parameter echo test setups run check verify karein (e.g., `echo -e "\e[1;31mThis is Red Text\e[0m"`).

---