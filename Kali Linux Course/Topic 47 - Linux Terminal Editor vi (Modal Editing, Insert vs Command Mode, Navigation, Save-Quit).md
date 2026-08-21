---
title: "Topic 47 - Linux Terminal Editor: vi (Modal Editing, Command/Insert Modes, Save & Quit)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 📝 Topic 47: Linux Terminal Editor: vi (Modal Editing, Command/Insert Modes, Save & Quit)

Bhai, humne **Topic 23** me standard text editor **`nano`** seekha tha jo bohot user-friendly hai. Lekin Linux administration aur cybersecurity me sabse important text editor **`vi`** (ya uski advanced version **`vim`**) hai. 

Duniya ke lagatar 99.9% Linux servers aur embedded devices par `vi` pre-installed hota hai (bina GUI ke). Agar aap kisi secure system me shell access paate ho aur wahan settings edit karni hain, toh aapko `vi` chalana aana hi chahiye. Isko seekhna shuruat me thoda tricky hota hai kyunki ye **Modes** par chalta hai.

---

### 🏛️ The Three Modes of `vi` (Working Style)

`vi` normal notepad ki tarah nahi chalta. Iske andar **3 main modes** hote hain:

```
                  +-----------------------+
                  |  COMMAND MODE (Default) | <---+
                  +-----------------------+     |
                     /                 \        | (Press Esc)
      (Press i, a, o)                  (Press :) |
                   v                     v      |
         +-------------+         +---------------+
         | INSERT MODE |         | EX COMMANDS   |
         +-------------+         +---------------+
```

1. **Command Mode (Default Mode):**
   Jab aap `vi` open karte ho, toh aap isi mode me hote ho. Isme aap jo bhi key press karoge, wo **text nahi likhegi** balki **shortcuts/commands** run karegi (jaise delete, copy, paste).
2. **Insert Mode (Typing Mode):**
   Text likhne ke liye. Command mode se **`i`** key press karne par aap Insert mode me jaate hain. Ab aap normal notepad ki tarah type kar sakte hain. Wapas Command mode me aane ke liye **`Esc`** key dabayein.
3. **Last-Line / Ex Command Mode (Colon `:` Mode):**
   Save aur exit karne ke liye. Command mode me **`:`** (colon) type karne par cursor screen ke sabse bottom me chala jata hai. Yahan aap saving aur quitting ke rules likhte ho.

---

### 🎛️ Essential vi Commands Cheat Sheet

#### 1. Entering Typing Mode (From Command Mode)
* **`i`**: Insert (Cursor ki position par type karna shuru karein).
* **`a`**: Append (Cursor ke ek character baad se typing start).
* **`o`**: Open line (Cursor ke niche ek naye khali line banakar typing start).

#### 2. Saving and Quitting (From Command Mode type `:` first)
* **`:w`**: Write (File save karna).
* **`:q`**: Quit (Exit karna, agar file modified na ho).
* **`:wq`**: Save and Quit (Save karke exit - Sabse zyada use hota hai).
* **`:q!`**: Force Quit (Bina save kiye exit karna—bohot useful!).

#### 3. Command Mode Navigation & Editing (Autopilot shortcuts)
* **`x`**: Cursor jis character par hai, use delete (erase) karna.
* **`dd`**: Poori ki poori line ko cut/delete karna.
* **`yy`**: Poori line ko copy (yank) karna.
* **`p`**: Copy ya cut ki gayi line ko cursor ke niche paste karna.
* **`u`**: Undo (Pichla action revert karna).
* **`Ctrl + R`**: Redo (Undo kiye action ko wapas laana).
* **`/keyword`**: Search (File me word dhoondhna. Next match ke liye `n` dabayein).

---

### 🔑 Real-World Analogy (The Fighter Jet Cockpit 🎛️🕹️)
Think of `vi` as a **Fighter Jet dashboard**:
* **Command Mode (Autopilot/Weapon Control):** Har button dabane par complex functions trigger hote hain (e.g. `d` for destroy line, `y` for yield copy). Agar aap autopilot mode me text likhne ki koshish karoge toh flight crash ho jayegi!
* **Insert Mode (Manual Flight Steering):** Aapne red button **`i`** daba kar cockpit steering apne haath me le li. Ab aap windshield par text type kar sakte hain. Autopilot control wapas lene ke liye aap dashboard reset button **`Esc`** dabate hain.
* **Colon `:` Mode (Base control tower):** Base station ko message bhejna: `w` (file save karke register karo) aur `q` (engine shutdown quit).

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `vi` editor ke mechanics check karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** `vi` editor me ek naye file open karein: `vi vi_test.txt`. Check karein default roop se kaunsa mode khula hai (Command Mode).
2. **Task 2:** Typing mode me jaane ke liye **`i`** press karein aur niche status bar par check karein kya `--- INSERT ---` likha hua aa raha hai.
3. **Task 3:** Insert mode me ye lines type karein:
   ```text
   Line 1: Linux is fun
   Line 2: Cyber Security notes
   Line 3: Vi editor testing
   ```
4. **Task 4:** Typing band karke command mode me wapas jaane ke liye **`Esc`** key dabayein (check karein niche se `--- INSERT ---` text gayab hua ya nahi).
5. **Task 5:** Cursor ko Line 2 par le jaakar keyboard par double **`d`** (`dd`) press karein aur check karein kya poori line delete ho gayi (line cut action).
6. **Task 6:** Delete ki gayi line ko cursor ke niche wapas paste karne ke liye command mode me **`p`** press karke verify karein.
7. **Task 7:** Revert check karne ke liye **`u`** key (Undo) press karein aur check karein line back update hui ya nahi.
8. **Task 8:** File ko save aur close karne ke liye Command mode me **`:`** type karein aur bottom console me **`wq`** likh kar enter press karein.
9. **Task 9:** `vi_test.txt` ko bina save kiye discard exit karne ka method test karne ke liye file kholkar badlaav karein aur command mode me **`:q!`** chala kar exit check karein.
10. **Task 10:** Minimal Linux servers (jaise recovery consoles ya embedded routers) me standard administration configurations setups ke dauran `vi` editor ka use karna kyu indispensable hai? 2 lines me explain karein.

---
