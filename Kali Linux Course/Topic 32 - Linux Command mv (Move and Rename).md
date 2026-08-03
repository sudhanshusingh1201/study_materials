---
title: "Topic 32 - Linux Command mv (Move and Rename)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 📦 Topic 32: Linux Command: mv (Move and Rename)

Bhai, files aur directories ko ek folder se doosre folder me transfer karne, ya unka **Name badalne (Rename)** ke liye Linux me ek hi single command use hoti hai: **`mv`**.

---

### 📦 mv Command Kya Hai?
* **mv:** **M**o**v**e.
* Is command ke do main kaam hote hain:
  1. Files aur Folders ko cut-paste (move) karna.
  2. Files aur Folders ka naam badalna (Rename). (Linux me rename ke liye koi alag command nahi hoti).

---

### 🔑 Real-World Analogy (Cardboard Box & Label Sticker 📦🏷️)
* **Move Operation:** Jaise aap apne room se ek **Kitab (File)** uthate ho, use ek **Gatte ke dibbe (mv command)** me daalte ho, aur doosre room (Destination folder) me le ja kar rakh dete ho. Ab wo kitab purane room me nahi milegi.
* **Rename Operation:** Kitab wahi rack par rakhi hui hai. Aap ek **Label Sticker (Rename parameter)** uthate ho aur purane naam ke upar naya naam chipka dete ho. Kitab ki location change nahi hui, sirf uski identity/name change ho gaya.

---

### 🗂️ Basic Command Syntax:
```bash
mv [options] <source_path> <destination_path>
```

---

### ⚡ Critical mv Operations & Flags (Usage Guide)

#### 1. File Rename Karna (Same Directory)
Agar source aur destination dono path same folder me hain, toh ye file ka naam badal dega:
```bash
mv old_file.txt new_file.txt
```

#### 2. File Move (Cut-Paste) Karna
File ko doosre folder me shift karne ke liye:
```bash
mv file.txt /tmp/
```
*(Isse `file.txt` user directory se cut hokar `/tmp` directory me chali jayegi).*

#### 3. `mv -i` (Interactive Mode ⚠️ - Safety Prompt)
Agar destination folder me pehle se hi same name ki file exit karti hai, toh default `mv` bina pooche use overwrite/replace kar dega. `-i` lagane par screen par confirmation prompt aayega: *"overwrite destination_file? (y/n)"*.
  ```bash
  mv -i data.txt backup/
  ```

#### 4. `mv -n` (No Clobber - Prevent Overwrite 🚫)
Agar destination par file pehle se exist karti hai, toh ye move process ko silently cancel (skip) kar dega, overwrite bilkul nahi karega.
  ```bash
  mv -n script.sh production/
  ```

#### 5. `mv -v` (Verbose 📝)
Ek folder se doosre folder me files shift hote waqt console par live transfers confirmation reports track karne ke liye:
  ```bash
  mv -v file.txt /tmp/
  ```
  *Output:* `renamed 'file.txt' -> '/tmp/file.txt'`

---

### 🔍 Difference between cp and mv:
* **`cp` (Copy):** Original file wahi rehti hai, aur uski ek extra photocopy destination par chali jaati hai. (Do files ban jaati hain).
* **`mv` (Move):** Original file apni location se completely cut ho kar destination par paste ho jaati hai. (Single file rehti hai).

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `mv` operations control verify karne ke liye in tasks ko terminal par test karein:

1. **Task 1:** Apne home folder me ek test file banayein (`touch old_identity.txt`). Ab use `mv` command se rename karke `new_identity.txt` set karein.
2. **Task 2:** `ls` run karke verify karein ki kya `old_identity.txt` list se remove hokar sirf `new_identity.txt` bacha hai.
3. **Task 3:** `new_identity.txt` file ko dynamic relative path se apne pehle banaye gaye directory `my_lab/` ke andar move (cut-paste) karein.
4. **Task 4:** Check karein ki kya file `my_lab/new_identity.txt` folder me pahunch chuki hai aur home directory se gayab ho gayi hai.
5. **Task 5:** `/tmp` folder ke andar ek naya folder banayein `temp_lab` (`mkdir /tmp/temp_lab`). Apne home folder ke `my_lab` directory ko pure contents ke sath `/tmp/temp_lab` ke andar shift karne ki command chala kar check karein.
6. **Task 6:** Ek hi command line me multiple files (jaise `file.txt`, `iplist.txt`) ko ek sath `/tmp/` folder me move karne ki execution verify karein.
7. **Task 7:** Overwrite safety alert verify karne ke liye **`-i`** flag lagakar same name files overwrite moves check karke prompt confirm karein.
8. **Task 8:** Safe copy/move operations check karne ke liye **`-n`** (no overwrite) flag execution run check karein.
9. **Task 9:** Transferred logs check karne ke liye verbose flag **`-v`** ke through move command execute karein aur screen layout confirm karein.
10. **Task 10:** Hacking directory organizations aur scripts structures rearrangement me `mv` command ke benefits aur usage highlights points analyze karein.

---