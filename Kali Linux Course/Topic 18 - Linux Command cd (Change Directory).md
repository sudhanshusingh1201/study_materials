---
title: "Topic 18 - Linux Command cd (Change Directory)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 📁 Topic 18: Linux Command: cd (Change Directory)

Bhai, Linux terminal par kaam karte time navigation seekhna sabse pehla step hai. **`cd`** command hi wo tool hai jo hume terminal me ek directory (folder) se doosri directory me aane-jaane ki absolute control deta hai.

---

### 📁 cd Command Kya Hai?
* **cd:** **C**hange **D**irectory.
* Linux filesystem ek tree-like structure hota hai jahan root (`/`) directory se saare folders (like `/etc`, `/home`, `/var`) nikalte hain. `cd` ka use karke hum is network path tree me move karte hain.

---

### 🔑 Real-World Analogy (Ghar Ke Kamre 🚪)
Maan lo aapka computer ek **bada ghar** hai aur alag-alag folders us ghar ke **kamre (rooms)** hain:
* Abhi aap **Living Room** me ho, aur aapko **Kitchen** me jana hai. Aap jo chal kar ek kamre se doosre kamre me jaate ho, terminal me wahi chalna **`cd`** command hai.

---

### 📂 Path Types (cd chalane ke do tarike)

Linux me kisi folder tak pahunchne ke do types ke paths hote hain:

#### 1. Absolute Path (Pura Address ✉️):
* Ye path humesha system root `/` (starting point) se shuru hota hai. Aap chahe system ke kisi bhi folder me ho, absolute path se aap direct exact location par pahunch jaoge.
* *Real-world Analogy:* Kisi ko pin-code aur city name ke sath full postal home address dena.
* *Example:*
  ```bash
  cd /var/www/html
  ```

#### 2. Relative Path (Dostana Address 📍):
* Ye path aapke **current folder location** ke reference me kaam karta hai. Agar aap pehle se `/var` folder me hain, toh `/var/www/html` tak jane ke liye poora address type karne ki zaroorat nahi hai.
* *Real-world Analogy:* Ghar ke andar khade hokar kisi ko bolna: *"Side wale kamre me chale jao."*
* *Example (If already in `/var`):*
  ```bash
  cd www/html
  ```

---

### ⚡ Crucial cd Shortcuts (Booster Cheat Sheet)

Linux terminal me `cd` ke sath kuch special characters ka use karke fast navigation kiya jata hai:

| Command | Short Description | Real-world Analogy |
| :--- | :--- | :--- |
| **`cd`** or **`cd ~`** | User ke **Home Directory** (`/home/username`) me le jayega. | Apne khud ke personal bedroom me chale jana. |
| **`cd ..`** | Ek level **piche (parent folder)** me wapas le jayega. | Kamre se nikal kar piche corridor/hallway me aana. |
| **`cd ../..`** | Do levels piche (parent of parent) le jayega. | Do baar piche chalna. |
| **`cd -`** | User ko uske **pichle (previous) folder** me wapas bhej dega (Undo button). | Browser me "Back" arrow press karna. |
| **`cd /`** | Pure system ki ultimate starting base **Root Directory** me le jayega. | Ghar ke main entry gate par khade ho jana. |
| **`cd .`** | Current directory (koi change nahi hoga). | Usi jagah par khade rehna. |

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, ab in 10 tasks ko apne local Kali Linux terminal par practice karo taaki `cd` command par command pakki ho jaye:

1. **Task 1:** Terminal open karein aur check karein ki aap default kis directory me hain. Fir simple `cd /` type karke enter karein aur verify karein ki path kya ho gaya hai.
2. **Task 2:** Apne user home directory me direct jump karne ke liye kaunsi shortcut command use karenge? Run karke confirm karein.
3. **Task 3:** Absolute path ka use karke directory `/usr/share/wordlists` ke andar switch karein.
4. **Task 4:** Task 3 complete hone ke baad, bin path type kiye, ek step back parent directory `/usr/share` me aane ke liye kaunsi command chalayenge?
5. **Task 5:** `/etc/network` folder ke andar relative path ka use karke switch karein agar aap abhi `/etc` ke andar khade hain.
6. **Task 6:** Ek single command line execute karke teen step piche (three levels back in hierarchy) kaise move karenge? Command likhein.
7. **Task 7:** Maan lo aap pehle `/var/log` me the, aur fir aap switch karke `/etc/apt` me chale gaye. Ab bina folder name type kiye wapas `/var/log` me switch karne ki fast custom command kya hai?
8. **Task 8:** Root directory `/` aur user home directory `~` me basic visual difference kya hai shell prompt path indicators me? Check karke likhein.
9. **Task 9:** Command terminal me `cd .` (single dot) run karne par directory location change kyu nahi hoti? Apne words me explain karein.
10. **Task 10:** `/home` directory ke andar switch karein aur `ls` command run karke check karein ki wahan aapke system user ka folder name kya hai. Fir dynamic absolute path se seedhe us user folder ke `/Downloads` subdirectory me enter karein.

---