---
title: "Topic 43 - Linux User & Group Management (useradd, usermod, passwd, /etc/passwd, /etc/shadow)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 👤 Topic 43: Linux User & Group Management (useradd, usermod, passwd, /etc/passwd, /etc/shadow)

Bhai, Linux ek robust **Multi-User Operating System** hai. Iska matlab hai ki ek hi system par ek sath multiple users login karke alag-alag permissions ke sath kaam kar sakte hain. Cybersecurity me systems ko secure karne ya access gain karne ke liye User accounts, groups, aur unke credentials databases ko analyze karna mandatory hai.

---

### 🏛️ Linux User Categories (UIDs)
Linux me har user ko ek numeric ID di jaati hai jise **UID (User ID)** kehte hain:
1. **Root User (UID 0):** Ultimate superuser, iske paas system par unlimited control hota hai.
2. **System Users (UID 1 - 999):** Ye real humans nahi hote, balki system services aur background processes ko chalane ke liye hote hain (jaise `daemon`, `bin`, `mail`, `ssh`).
3. **Regular Users (UID 1000 onwards):** Normal log jo system par login karte hain (jaise aapka default `kali` account).

---

### 📂 Major Files (User Databases)

#### 1. `/etc/passwd` (User Details database)
Is file me system ke sabhi accounts ki specifications hoti hain. Ye sabhi users ke liye readable hoti hai. Iski har line colon `:` se divided hoti hai aur usme **7 fields** hote hain:
```text
kali:x:1000:1000:Kali User,,,:/home/kali:/usr/bin/zsh
```
* **Field 1 (`kali`):** Username.
* **Field 2 (`x`):** Password placeholder (iska matlab hai real password hash `/etc/shadow` me saved hai).
* **Field 3 (`1000`):** UID (User ID).
* **Field 4 (`1000`):** GID (Group ID).
* **Field 5 (`Kali User,,,`):** User description or comments.
* **Field 6 (`/home/kali`):** User ki Home directory path.
* **Field 7 (`/usr/bin/zsh`):** User ka login Shell path.

#### 2. `/etc/shadow` (Secure Passwords Hash database) 🔐
Is file me users ke actual **Encrypted Password Hashes** saved hote hain. Security reasons ke liye is file ko normal user read nahi kar sakta (sirf `root` ke paas read access hota hai).
* *Fields:* Username, encrypted password string (e.g. SHA-512 hashes start with `$6$`), password change dates.
* *Cybersecurity Info:* Hackers `/etc/shadow` file ko dump karke password crack (brute force) karne ke liye **John the Ripper** ya **Hashcat** tools use karte hain.

#### 3. `/etc/group` (Group configurations)
Linux me permissions groups ke forms me manage ki jaati hain. Is file me saare groups aur unke members ki list hoti hai.

---

### 🛠️ User & Group Management Commands

* **`useradd -m <username>`**: Naya user account create karna (`-m` flag naye user ke liye `/home/` me directory touch karta hai).
* **`passwd <username>`**: Kisi user ka password set ya change karna.
* **`usermod -aG <group> <username>`**: Kisi user ke configurations update karna. Hacking/Admin operations me user ko privileges dene ke liye use `sudo` group me add kiya jata hai:
  ```bash
  sudo usermod -aG sudo target_user
  ```
  *(Yahan `-aG` ka matlab hai: Append to Group).*
* **`userdel -r <username>`**: User account delete karna (`-r` flag use user ki home directory files ke sath complete delete kar deta hai).
* **`groups <username>`**: Check karna ki user kis-kis security groups ka part hai.
* **`id <username>`**: User ki active UID, GID, aur groups information fetch karna.

---

### 🔑 Real-World Analogy (The Apartment Building 🏢🔑)
Maan lo Linux system ek bada **Apartment Complex (Building)** hai:
* **Root User (UID 0):** Building owner or manager jiske paas master-key hai aur wo kisi bhi room me ja sakta hai.
* **Regular Users:** Rooms me rehne wale tenants (kirayedari) jo apne room me jo chahe karein par bina permission doosre ke room me nahi ja sakte.
* **`/etc/passwd` (The Tenant Directory Board):** Entry lobby me laga bada board jo sabhi ko batata hai ki kaun-kaun se flat (rooms) me kaun rehta hai, unki category kya hai aur unka shell (login shell) kya hai.
* **`/etc/shadow` (The Lockbox):** Manager ke secure office me rakha ek locker jisme sabhi rooms ki keys aur code combinations safe hain. Ise aam log haath nahi laga sakte.
* **`usermod`:** Tenant ko gym ya pool club (security groups) ki access membership dilwana.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, user administration verify karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** Apne current user ki UID aur default groups checking ke liye **`id`** aur **`groups`** commands run karke parameters verify karein.
2. **Task 2:** System configurations me naya check user `testuser` create karein home directory ke sath: `sudo useradd -m testuser`.
3. **Task 3:** `testuser` ka default password change/set karne ke liye `sudo passwd testuser` command chala kar new password set karein.
4. **Task 4:** Check karein ki kya `/home` folder ke andar naya user directory setup `ls -la /home` verify ho raha hai.
5. **Task 5:** `/etc/passwd` me se specifically `testuser` ki entries search/inspect karne ke liye grep pipe check karein: `grep "testuser" /etc/passwd`.
6. **Task 6:** Normal user me shadow database `/etc/shadow` read karne ki koshish karein: `cat /etc/shadow` (observe errors). Phir root access se run karke checks confirm karein: `sudo cat /etc/shadow`.
7. **Task 7:** `testuser` ko administrators group `sudo` me add karne ke liye appropriate mod command chala kar verify karein: `sudo usermod -aG sudo testuser`.
8. **Task 8:** Verification ke liye `groups testuser` run karein aur confirm karein ki wo `sudo` group ka member ban gaya hai.
9. **Task 9:** Admin setups verify ho jaane ke baad account delete karne ke liye files remove flag ke sath `sudo userdel -r testuser` execute karein.
10. **Task 10:** Red Team assessment aur local privilege escalation vulnerabilities analysis me UID 0 validation aur shadow hashes extraction ka kya significance hai? 2 lines me explain karein.

---
