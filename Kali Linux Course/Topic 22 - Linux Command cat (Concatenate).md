---
title: "Topic 22 - Linux Command cat (Concatenate)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 📣 Topic 22: Linux Command: cat (Concatenate)

Bhai, files banane, unhe merge karne, aur unke contents ko screen par direct read karne ke liye Linux ka sabse versatile aur commonly used command hai **`cat`**.

---

### 📣 cat Command Kya Hai?
* **cat:** **Cat**enate (ya **Con**catenate - jiska matlab hota hai cheezon ko aapas me jodna).
* Is command ka main use text files ke contents ko check karne aur multiple files ko aapas me combine (merge) karne ke liye hota hai.

---

### 🔑 Real-World Analogy (Megaphone / Speaker 📣)
Maan lo aapke paas ek **Dairy (File)** hai jiske andar kuch secrets likhe hain. Aap ek **Megaphone/Mike (cat command)** uthate ho aur us dairy me likhe saare pages ko zor-zor se sabko bol kar sunane lagte ho. 
* Aap ek dairy ke baad doosri dairy bhi sequence me padh sakte ho. Terminal me isi files ko "bol kar screen par display karna" **`cat`** kehlata hai.

---

### ⚡ Main Functions of cat (Uses of cat)

`cat` command se terminal me teen main functions execute kiye ja sakte hain:

#### 1. Display File Contents (File Padhnan 📖)
```bash
cat iplist.txt
```
*(Isse `iplist.txt` ke andar jitni bhi IP lines hain, wo sab screen par display ho jayengi).*

#### 2. Combine Multiple Files (Merge display 🔗)
```bash
cat file1.txt file2.txt
```
*(Ye pehle `file1.txt` ka data print karega aur uske immediate baad `file2.txt` ka content print karega).*

#### 3. Create Files and Write Text (Nayi File Likhna ✍️)
Bina kisi editor (nano/vi) ko open kiye, direct terminal se file likhne ke liye redirection `>` operator ka use kiya jata hai:
```bash
cat > my_notes.txt
```
* **How it works:** Is command ko chalate hi cursor fresh line par chala jayega. Ab aap jo bhi text likhna chahte hain, type karein. When writing is done, keyboard par **`Ctrl+D`** press kijiye. System use save kar dega.

---

### ⚡ Critical cat Flags (Options Cheat Sheet)

#### 1. `cat -n` (Display Line Numbers 🔢)
Ye file ke content ko list karte waqt har line ke shuru me automatic index counters (line numbers) show karega. (Code ya target tables scan karte waqt best hai).
  ```bash
  cat -n iplist.txt
  ```

#### 2. `cat -s` (Squeeze Blank Lines 🗜️)
Agar file me bohot saari consecutive khali (blank) lines hain, toh `-s` flag un sabhi multiple blank spaces ko compress karke single empty line space me convert kar deta hai, jisse layout readable ho jata hai.
  ```bash
  cat -s textfile.txt
  ```

#### 3. `cat -T` (Show Tabs 🛑)
Ye code files debugging me bohot useful hai. Ye code me spaces aur tab parameters ko distinguish karne ke liye har **Tab** input ko character **`^I`** me convert karke display karta hai.

#### 4. `cat -E` (Show Line Ends 💲)
Har line ke end point par **`$`** symbol print karega taaki aap check kar sakein ki line ke end me koi extra hidden space (trailing space) toh chhupha nahi hai.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, in tasks ko terminal par test karke `cat` features ko master karein:

1. **Task 1:** Apne user home directory (`~`) me `cat` command ka use karke ek naye file banayein (`cat > user_info.txt`), usme apna name aur state type karein, aur `Ctrl+D` se save karein.
2. **Task 2:** Task 1 me banayi gayi `user_info.txt` file ka content screen par read karne ke liye command run karein.
3. **Task 3:** Home folder me installed files me se `/etc/passwd` file ke contents ko read karein system details verify karne ke liye command path note karein.
4. **Task 4:** `/etc/resolv.conf` dns configuration file ke contents ko line numbers (index count) ke sath display karne ke liye kaunsi flag command best hai? Run karein.
5. **Task 5:** Ek file banayein `words.txt` jisme 3-4 consecutive empty lines space ho. Ab **`-s`** flag lagakar verify karein ki multiple empty lines single line me compress hoti hain ya nahi.
6. **Task 6:** Do different text files (jaise `file.txt` aur `iplist.txt`) ke contents ko ek hi single display flow index me sequential merge print karne ki command run karein.
7. **Task 7:** Overwrite operator **`>`** ka use karke, do files (`file.txt` aur `iplist.txt`) ke contents ko combine karke ek teesri nayi file `master_list.txt` me save karein.
8. **Task 8:** Append redirection **`>>`** ka use karke, `user_info.txt` file ke aakhir me ek extra text line "Cyber Security Student" add karein, aur `cat` se check karein ki data insert hua ya overwrite.
9. **Task 9:** File path content read karte waqt, tabs spacing verify karne ke liye **`-T`** flag lagakar command execute karein.
10. **Task 10:** Standard file `master_list.txt` ke lines endpoint whitespace traces validation ke liye check indicators show karne wali **`-E`** flag execution verify karein.

---