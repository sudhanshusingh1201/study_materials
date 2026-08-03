---
title: "Topic 21 - Linux Command cp (Copy Files and Directories)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 📄 Topic 21: Linux Command: cp (Copy Files and Directories)

Bhai, files aur folders ko duplicate (copy) karna operating system ka ek basic core function hai. Linux CLI me is duplicate replication ke liye hum **`cp`** command use karte hain.

---

### 📄 cp Command Kya Hai?
* **cp:** **C**o**p**y.
* Ye command kisi file ya folder ki copy banati hai aur use source directory se utha kar destination path par save karti hai.

---

### 🔑 Real-World Analogy (Photocopy Machine 🖨️)
Maan lo aapke paas ek **important document (Source File)** hai. Aap use lekar ek **photocopy machine** me dalte ho aur ek **duplicate copy (Destination File)** nikalte ho. 
* Original document aapke paas safe rehta hai aur aapko ek extra duplicate page mil jata hai jise aap kahin bhi rakh sakte ho. Terminal me is photocopy process ko **`cp`** kehte hain.

---

### 🗂️ Basic Syntax:
```bash
cp [options] <source_path> <destination_path>
```

---

### ⚡ Critical cp Flags (Flags Guide)

File copy ko control karne ke liye in flags ka use sabse zyada kiya jata hai:

#### 1. Simple Copy (Single File)
```bash
cp file.txt file_backup.txt
```
*(Isse current folder me `file.txt` ki ek duplicate copy `file_backup.txt` ke naam se ban jayegi).*

#### 2. `cp -r` or `cp -R` (Recursive - Copy Folders) 📁
Agar aap bina is flag ke kisi folder (directory) ko copy karne ki koshish karoge: `cp folder1 folder2`, toh Linux error bhejega: `cp: -r not specified; omitting directory 'folder1'`.
* **Rasta:** Folder ko copy karne ke liye `-r` (recursive) lagana zaroori hai taaki folder ke andar ki saari sub-files aur sub-folders bhi copy ho sakein.
  ```bash
  cp -r /home/kali/Projects /tmp/
  ```

#### 3. `cp -i` (Interactive - Ask Before Overwrite ⚠️)
Agar destination path par pehle se hi same name ki file exit karti hai, toh default system use direct delete/overwrite kar dega bina aapse pooche. `-i` lagane par screen par prompt aayega: *"overwrite destination_file? (y/n)"*.
  ```bash
  cp -i important.txt backup/
  ```

#### 4. `cp -v` (Verbose - Show Progress 📝)
Ye command exact print karti hai ki background me kaun-kaunsi file copy ho rahi hai (badi directories copy karte waqt visual validation ke liye best hai).
  ```bash
  cp -rv my_folder/ /tmp/
  ```
  *Output:* `'my_folder/file1.txt' -> '/tmp/my_folder/file1.txt'`

#### 5. `cp -p` (Preserve Attributes 🔒)
Ye file ki meta-information (jaise modification date, time, file owner, permissions) ko destination copy par bilkul original preserve rakhti hai, change nahi hone deti. (System backups me useful hai).

#### 6. `cp -u` (Update Only 🔄)
Ye tabhi copy karega jab source file destination file se **nayi (newer)** ho, ya fir destination par wo file exist na karti ho.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `cp` command par pakad banane ke liye in tasks ko execute karein:

1. **Task 1:** Apne user home directory (`~`) me ek simple blank file banayein (`touch test_copy.txt`). Fir use usi location me `test_copy_backup.txt` ke naam se duplicate copy karein.
2. **Task 2:** Apne home folder me ek naya folder banayein (`mkdir my_lab`). Ab normal file `test_copy.txt` ko is `my_lab` folder ke andar copy karein dynamic relative path se.
3. **Task 3:** Ab simple `cp my_lab my_lab_backup` command chalakar dekhein ki kya error aata hai. Us error ko solve karne ke liye kaunsa flag lagayenge? Command chala kar verify karein.
4. **Task 4:** Kali Linux ke default configuration directory `/etc/apt` ko recursive format me `/tmp` folder ke andar copy karein aur output confirm karein.
5. **Task 5:** `/tmp/apt` folder ke andar files copy hone par, verify karein ki local copy create hui ya nahi `ls` command se.
6. **Task 6:** Ek hi single command line me multiple files (jaise `file1.txt`, `file2.txt`) ko ek sath kisi folder (jaise `my_lab`) me kaise copy karenge? Command run karein.
7. **Task 7:** Destination file pehle se exist karne par warning request check karne ke liye **`-i`** flag ka use karke copy command chalayein aur confirmation prompt me `n` select karein.
8. **Task 8:** Pure copy progress log ko screen par monitor karne ke liye, files copy karte waqt **`-v`** flag lagakar command execute karein.
9. **Task 9:** Absolute paths ka use karke, user `/home/kali/test_copy.txt` file ko system temporary folder `/tmp` me copy karne ki fully qualified command run karein.
10. **Task 10:** Copy kiye gaye files ke actual creation/modification time timestamps ko original metadata ke sath matches preserved rakhne ke liye kaunsa flag lagayenge? Command framework note karein.

---