---
title: "Topic 20 - Linux Command pwd (Print Working Directory)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 📍 Topic 20: Linux Command: pwd (Print Working Directory)

Bhai, Linux me jab hum deep and complex structures ke directories me traverse karte hain, toh hum aasaani se apna exact path bhul sakte hain (kyunki shell display prompt humesha full path show nahi karta). Is situation me **`pwd`** command hamare liye compass ka kaam karti hai.

---

### 📍 pwd Command Kya Hai?
* **pwd:** **P**rint **W**orking **D**irectory.
* Ye command dynamic shell ko ye instructions deti hai ki: *"Main abhi system ke kis precise location/folder par khada hoon, uska poora absolute path output print karo."*

---

### 🔑 Real-World Analogy (GPS / Current Location 🗺️)
Maan lo aap ek **bohot badi multi-story shopping mall (Linux directory system)** ke andar ghum rahe ho. Ghumte-ghumte aap ek specific section me pahunche par aap bhul gaye ki aap ground floor par ho, basement me ho ya first floor ke back corner me. 
* Aap mall ke map kiosk par ja kar jo **"You Are Here"** ka red dot check karte ho taaki aapko apni exact position pata chal sake, terminal me wahi red dot check karna **`pwd`** chalana hai.

---

### ⚡ Physical vs. Logical Paths (Advanced pwd Flags)

Linux directories me shortcuts (Symbolic Links) create kiye jate hain. Agar hum symbolic link use karke kisi folder me ghuste hain, toh `pwd` ke pass location print karne ke do optional behaviors hote hain:

#### 1. `pwd -L` (Logical Path - Default)
* Ye command wahi path print karegi jisse aap physically travel karke aaye hain, bhale hi wo path ek symbolic link (shortcut) hi kyu na ho. (Default behavior bina flag ke bhi yahi hota hai).
* *Usage:* `pwd -L`

#### 2. `pwd -P` (Physical Path - Actual Location) 🌟
* Agar aap kisi symbolic link directory ke andar hain, toh ye command shortcut path ko resolve karke **original database location (actual physical hard disk path)** print karegi.

##### 🚀 Symlink Example in Kali:
Kali Linux me `/var/mail` folder ek symbolic link (shortcut) hai jo actual me `/var/spool/mail` folder ko redirect karta hai.
1. `cd /var/mail` chalakar jab aap wahan pahunchenge.
2. Ab run karein `pwd -L` ➡️ Output: `/var/mail` (Logical shortcut path).
3. Ab run karein `pwd -P` ➡️ Output: `/var/spool/mail` (Asli hard disk physical folder location).

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `pwd` concept ko terminal par confirm karne ke liye ye 10 tasks execute karo:

1. **Task 1:** Terminal open karte hi bina koi doosri command chalaye, simple `pwd` run karein aur check karein ki default path kya display hota hai.
2. **Task 2:** System user ke home directory (`~`) ke andhar switch karein aur `pwd` chalakar verify karein ki home indicator `~` ka actual absolute path system root ke reference me kya hai.
3. **Task 3:** Root directory `/` me switch karke `pwd` run karein aur confirm karein ki output kya aata hai.
4. **Task 4:** Path `/usr/share/wordlists` me switch karein aur verify karein ki `pwd` output aapka exact input matching show kar raha hai.
5. **Task 5:** Ek generic script folder path `/var/run` me switch karein (ye folder `/run` ka shortcut/symlink hota hai). Wahan `pwd` (bina flag ke) run karke output note karein.
6. **Task 6:** Task 5 me switch kiye gaye `/var/run` directory ke andar ab physical path check karne ke liye **`pwd -P`** command run karein. Dekhein ki output change hota hai ya nahi.
7. **Task 7:** Ek step back parent folder `/var` me aane ke liye `cd ..` run karein aur fir se `pwd` run karke location check karein.
8. **Task 8:** Linux command line environment properties me `pwd` command ek shell internal parameter environment variable read karti hai jise `$PWD` kehte hain. Terminal me `echo $PWD` command run karke check karein ki output standard `pwd` matching show karta hai ya nahi.
9. **Task 9:** Absolute path `/etc/network` me relative path entry ke baad `pwd` run karein.
10. **Task 10:** Home user ke terminal prompt me aane ke baad `cd Downloads` run karein aur check karein ki `pwd` kya output generate karta hai.

---