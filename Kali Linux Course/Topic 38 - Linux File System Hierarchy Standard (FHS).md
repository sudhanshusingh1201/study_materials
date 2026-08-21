---
title: "Topic 38 - Linux File System Hierarchy Standard (FHS)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🏢 Topic 38: Linux File System Hierarchy Standard (FHS)

Bhai, Windows me hume alag-alag drive letters (jaise `C:\`, `D:\`, `E:\`) dikhte hain. Lekin Linux me aisa nahi hota! Linux me ek hi single unified directory structure hoti hai jise **File System Hierarchy Standard (FHS)** kehte hain. 

Linux me saari directories, files, devices, ya external hard disks ek single root directory **`/`** (Forward Slash) se start hokar ek bade tree structure ke roop me failti hain. 

---

### 🏢 Major Linux Directories and Their Purposes

Linux ke tree structure ke different folders ka specific kaam hota hai:

#### 1. `/` (Root Directory)
Ye poore system ka main basement (base) hai. Har ek file aur folder is directory ke andar hi exist karta hai.

#### 2. `/bin` (Essential User Binaries)
Isme system ke basic commands ke executables hote hain jo system boot hone aur single-user mode me chalne ke liye zaroori hain (jaise `ls`, `cp`, `mv`, `cat`). Modern OS me ye `/usr/bin` ka link hota hai.

#### 3. `/sbin` (System Binaries)
System administration ke essential tools (jaise `fdisk`, `iptables`, `ifconfig`, `reboot`). Ye commands root (superuser) privilege ke bina direct normal user run nahi kar sakta.

#### 4. `/etc` (Configuration Files) ⚙️
Linux ka brain! Isme system aur applications ke saare configuration (settings) files save hoti hain.
* *Examples:* `/etc/passwd` (user settings), `/etc/resolv.conf` (DNS settings), `/etc/apt/sources.list` (repositories update list).

#### 5. `/home` (User Home Directories) 👤
Regular users ki personal file space (jaise Windows me `C:\Users\Name`). Kali Linux me regular user ka home `/home/kali/` hota hai.

#### 6. `/root` (Superuser/Root Home Directory) 👑
System administrator (Root user) ka personal private home directory hai. Ye `/home` partition se alag rakhi jaati hai taaki agar `/home` fail ho jaye tab bhi Root user log in karke maintain kar sake.

#### 7. `/var` (Variable Files & Logs) 📝
Isme wo files hoti hain jinka size aur data system execution ke sath lagatar badalta rehta hai, jaise database registers aur system log files (`/var/log/`).

#### 8. `/tmp` (Temporary Files) 🗑️
Applications dwara dynamic use ke liye temporary files yahan save hoti hain. System reboot hone par is directory ka data automatic wipe (delete) ho jata hai.

#### 9. `/dev` (Device Files) 🔌
Linux me hardware devices ko file ke roop me dekha jata hai (Everything is a file).
* *Examples:* `/dev/sda` (Pehli hard disk), `/dev/null` (A virtual black hole—jo bhi isme send karoge wo gayab ho jayega!).

#### 10. `/proc` & `/sys` (Virtual RAM Directories) 🧠
Ye directories hard disk par real space nahi letin. Ye virtual file systems hain jo RAM me exist karte hain aur kernel dwara processes (`/proc`) aur hardware details (`/sys`) ko show karne ke liye banaye jaate hain.

---

### 🔑 Real-World Analogy (The Giant Office Building 🏢🗄️)
Maan lo poora Linux system ek **badi Office Building (`/`)** hai:
* **`/etc` (Admin Office):** Jahan company ke saare rules, employee details, settings, aur registration logs rakhe hain.
* **`/home` (Regular Employee Cabins):** Har employee ka apna cabin jahan wo apni files aur personal cheezein rakhta hai.
* **`/root` (CEO's Penthouse Suite):** Building ke top floor par CEO (administrator) ka secure personal office.
* **`/bin` & `/sbin` (Maintenance Toolrooms):** Maintenance tools (screwdrivers, hammers) rakhne ka room jise system chalaye rakhne ke liye workers use karte hain.
* **`/var` (Log Register Room):** Jahan live security logs aur dynamic events continuously note ho rahe hain.
* **`/tmp` (Draft Whiteboards):** Jahan employees temporary notes likhte hain jo shaam ko office band hote waqt saaf ho jaate hain.
* **`/dev` (Wall Outlets):** Physical monitor cables, socket ports, aur connection panels jo hardware devices ko support dete hain.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, Linux file structure ko practical examine karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** Root directory par jaane ke liye `cd /` chala kar `ls -la` run karein aur screen par main system directories layout confirm karein.
2. **Task 2:** Apne system ke users settings check karne ke liye config file `/etc/passwd` ka file type checking utility `file /etc/passwd` run karein.
3. **Task 3:** `/var/log` folder ke andar ja kar `ls` karein aur dekhein ki Kali Linux me system aur authentication logs kis folder me collect hote hain.
4. **Task 4:** `/tmp` directory ke andar `touch temp_test.txt` banayein, phir system reboot karein aur check karein ki kya file reboot ke baad delete hui.
5. **Task 5:** `/root` folder ke andar `cd /root` se jaane ki koshish karein. Check karein ki normal accounts me kya error aata hai (Permission Denied), aur use solve karne ka command structure batayein (`sudo`).
6. **Task 6:** Virtual process directory `/proc` ke andar dynamic folders check karein. `/proc/cpuinfo` file ko read karne ke liye `cat /proc/cpuinfo` chala kar systems CPU specifications verify karein.
7. **Task 7:** `whereis ls` chala kar check karein ki `ls` command ka binary executable `/bin` directory me hi saved hai na.
8. **Task 8:** Virtual devices check karne ke liye `file /dev/null` aur `file /dev/urandom` commands chala kar unke specific system configurations categories dekhein.
9. **Task 9:** Linux system configurations me `/usr` directory ke basic full form (User System Resources) aur iske scope significance ko short point out karein.
10. **Task 10:** Hacking tools custom installations ke dauran manual configurations packages ko `/opt` folder me install karne ki standard system recommendations kyu di jaati hain? 2 lines me explain karein.

---
