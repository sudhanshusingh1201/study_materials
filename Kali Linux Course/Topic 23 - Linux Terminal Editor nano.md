---
title: "Topic 23 - Linux Terminal Editor nano"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 📝 Topic 23: Linux Terminal Editor: nano

Bhai, text documents read karne ke liye `cat` toh badhiya hai, par jab hume configuration files (jaise proxychains configs) ko modify karna ho ya scripting payloads (.py, .sh) likhne hon, toh hume terminal ke andar ek **Text Editor** ki zaroorat hoti hai. Linux me beginners ke liye sabse simple aur friendly editor hai **`nano`**.

---

### 📝 nano Editor Kya Hai?
* **nano:** Ek lightweight command-line text editor hai jo bina GUI open kiye terminal ke andar hi files direct text-mode write aur edit karne ki user interface facility deta hai.
* Iski sabse achhi baat ye hai ki iske saare control shortcuts screen ke niche humesha likhe rehte hain, isliye beginners ko variables yaad nahi rakhne padte.

---

### 🔑 Real-World Analogy (Notepad 📝)
Maan lo aapke paas Windows ka **Notepad** application hai jisme aap plain notes likhte ho. Terminal ke andar wahi Notepad application **`nano`** editor hai. Ye clean paper display deta hai jisme formatting (bold/italic) ke bina direct dynamic texts and script blocks manage kiye ja sakte hain.

---

### 🗂️ Basic Command Syntax:
```bash
nano filename.txt
```
* **Note:** Agar `filename.txt` folder me pehle se exist karti hai, toh ye use editing screen me open kar dega. Agar file exist nahi karti, toh ye ek khali display open karega, aur jab aap use save karoge toh system automatic naye name se file generate kar dega.

---

### ⚡ Critical nano Shortcuts (Ctrl is represented by `^`)

Nano editor screen ke bottom line shortcuts list me check karein, jahan caret **`^`** symbol ka matlab hota hai keyboard **`Ctrl`** key:

1. **`Ctrl + O` (WriteOut / Save):**
   * Key press karne par system aakhir me file name confirmation poochega, `Enter` press karte hi file hard disk me save ho jayegi.
2. **`Ctrl + X` (Exit / Close):**
   * Editor screen close karne ke liye. Agar files me changes kiye hain toh system confirmation option dega: *"Save modified buffer? (y/n)"*. Yes ke liye `y` aur No ke liye `n` type karein.
3. **`Ctrl + W` (Where Is / Search):**
   * File content me specific words (jaise proxy settings dynamic lines) search karne ke liye use hota hai. Word type karke search click karein, cursor exact destination matches par switch kar dega.
4. **`Ctrl + K` (Cut Line / Delete Line):**
   * Cursor jis line par khada hoga, ye poori line cut (delete) kar dega buffer clipboard cache me.
5. **`Ctrl + U` (Uncut Text / Paste Line):**
   * Cut ki gayi lines ko cursor point par paste karne ke liye trigger.
6. **`Ctrl + R` (Read File / Insert File):**
   * Apni current file ke andar, kisi doosri local file ka poora content cursor position par insert (embed) karne ki speed technique.
7. **`Ctrl + _` (Go to Line / Switch Counter):**
   * Badi script files me direct line number (e.g., Line 50) switch jumps ke liye.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `nano` commands control practice karne ke liye in tasks ko complete karein:

1. **Task 1:** Terminal me run karein `nano my_editor.txt`. Apne baare me 3-4 lines type karein, aur bina exit kiye use **`Ctrl+O`** se save karein.
2. **Task 2:** File save karne ke baad, exit karne ke liye **`Ctrl+X`** run karein aur verify karein ki local list me file ban chuki hai.
3. **Task 3:** Ab dubara `nano my_editor.txt` open karein. 3rd line ke target text ko cut (delete) karne ke liye **`Ctrl+K`** chala kar checks verify karein.
4. **Task 4:** Cut kiye gaye text ko aakhir me paste karne ke liye, document end space par cursor le ja kar **`Ctrl+U`** run karein.
5. **Task 5:** Document ke andar specific word search test karne ke liye **`Ctrl+W`** use karke check karein ki wo correct location show karta hai ya nahi.
6. **Task 6:** Ab document me external file content insert validation check karein. Cursor bottom par rakh kar **`Ctrl+R`** shortcut use karein aur source file `user_info.txt` specify karke verify karein.
7. **Task 7:** Document edit completion par, exits command `Ctrl+X` use karke save prompt verify karein aur changes safe save karke desktop verify karein.
8. **Task 8:** Kali configuration file `/etc/resolv.conf` ko `nano` ke through read-only mode me check validation ke liye run karne ki syntax parameters note karein. (Hint: read-only ke liye `nano -v filename` use hota hai).
9. **Task 9:** Ek file me 20-30 random dummy lines generate karein. Ab direct command shell interface me specific line numbers jumps ke liye **`Ctrl+_`** parameters test karein.
10. **Task 10:** Hacking labs configuration setups me config lines details verify karne ke liye nano terminal configuration file setups parameters check karein.

---