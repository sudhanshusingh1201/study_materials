---
title: "Topic 27 - Linux Command chown (Change Owner)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 👑 Topic 27: Linux Command: chown (Change Owner)

Bhai, Linux ek multi-user operating system hai jahan security maintain rakhne ke liye har file/folder ka ek dedicated **Owner (Malik)** aur ek specific **Group** hota hai. Agar aapko kisi file ka malik badalna ho (jaise root se hatakar normal user kali ko dena ho), toh hum **`chown`** command ka use karte hain.

---

### 👑 chown Command Kya Hai?
* **chown:** **Ch**ange **Own**er.
* Is command ka primary function kisi file ya directory ke ownership (malikana haq) aur group settings ko system level par modify karna hota hai.

---

### 🔑 Real-World Analogy (Property Registry / Registry Office 🏠)
Maan lo ek **Makaan (File)** hai jo abhi **Ramesh (User: Root)** ke naam par registered hai. 
* Ramesh wo makaan **Suresh (User: Kali)** ko bech deta hai. 
* Ab Suresh ko registry office jaakar sarkari papers par makaan ka ownership Suresh ke naam karwana hoga.
* Linux me files ke case me ye registry update karne ka kaam **`chown`** command karti hai.

---

### 🗂️ Basic Command Syntax:
```bash
sudo chown <new_owner> <filename>
```
* **IMPORTANT:** Kyunki file ka owner badalna ek sensitive aur high-privilege administrative action hai, isliye is command ke aage humesha **`sudo`** (SuperUser Do) lagana mandatory hota hai.

#### ⚡ Owner and Group dono ek sath badalna:
Aap ek hi command se owner aur group dono change kar sakte hain owner aur group ke beech me `:` symbol lagakar:
```bash
sudo chown kali:kali report.txt
```
*(Yahan file ka owner `kali` ho jayega aur group bhi `kali` set ho jayega).*

---

### ⚡ Critical chown Flags & Options (Cheat Sheet)

#### 1. `chown -R` (Recursive Ownership Change 📁)
Agar aapke paas ek folder hai jiske andar hazaron files aur sub-folders hain, aur aap sabhi ka owner ek baar me change karna chahte hain, toh **`-R` (Capital R)** flag lagayein:
  ```bash
  sudo chown -R kali:kali /home/kali/my_lab/
  ```

#### 2. `chown -v` (Verbose Mode 📝)
Ye command exact print karti hai ki screen par kis-kis file ki ownership change hui hai (visual validation ke liye useful hai).
  ```bash
  sudo chown -v kali file.txt
  ```
  *Output:* `changed ownership of 'file.txt' from root to kali`

#### 3. `chown --reference=ref_file target_file`
Agar aap chahte ho ki `target_file` ka owner aur group wahi ho jaye jo pehle se `ref_file` ka hai, toh reference attribute use karein.

---

### ⚠️ Common Troubleshooting (Permission Denied)
Agar aap normal user `kali` ho aur bina `sudo` ke kisi file ka owner change karne ki koshish karoge:
```bash
chown root file.txt
```
➡️ Output: `chown: changing ownership of 'file.txt': Operation not permitted`
* **Reason:** Security policy ke according sirf `root` user (admin) hi ownership transfer kar sakta hai. Isliye humesha aage `sudo` lagana na bhulein!

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `chown` commands control verify karne ke liye in tasks ko terminal par test karein:

1. **Task 1:** Apne home directory me ek test file banayein (`touch ownership_test.txt`) aur `ls -l` chalakar iska current owner aur group name check karein.
2. **Task 2:** `chown` chalakar file ka owner `root` set karne ki koshish karein bina `sudo` lagaye. Check karein ki kya error message screen par show hota hai.
3. **Task 3:** Ab **`sudo chown root ownership_test.txt`** command chala kar password enter karein. Uske baad `ls -l` chalakar verify karein ki kya owner change hokar `root` hua.
4. **Task 4:** Owner change hone ke baad, normal user se use edit karne ki koshish karein (`nano ownership_test.txt`). Dekhein ki kya niche read-only warning ya permission error dikhta hai.
5. **Task 5:** Ek single command run karein jisse file ka owner aur group dono wapas **`kali:kali`** ho jayein (use: `sudo chown kali:kali ownership_test.txt`).
6. **Task 6:** Task 5 complete hone ke baad `ls -l` chalakar verify karein ki owner aur group wapas standard state me aa chuke hain.
7. **Task 7:** Folder levels par recursive verification ke liye `sudo chown -R root:root my_lab/` command chalayein aur check karein ki `my_lab` folder aur uske andar ki files ka status kya ho gaya hai.
8. **Task 8:** Verbose report checking ke liye **`-v`** flag lagakar command chala kar check karein ki ownership transfer alerts kaise print hote hain.
9. **Task 9:** Wapas apne `my_lab` folder aur files ki ownership ko **`kali:kali`** me revert back karein taaki aap use standard bina sudo privileges ke edit kar sakein.
10. **Task 10:** Linux systems me secure configurations aur multi-user permission systems me `chown` ki relevance aur administrative use-cases explain karein.

---