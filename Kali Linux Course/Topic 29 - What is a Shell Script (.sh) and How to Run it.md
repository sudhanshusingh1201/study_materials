---
title: "Topic 29 - What is a Shell Script (.sh) and How to Run it"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🐚 Topic 29: What is a Shell Script (.sh) and How to Run it?

Bhai, Linux me jab hume ek se zyada commands ko automatic ek ke baad ek sequential execute karna hota hai, toh hum un commands ko ek normal text file me save kar dete hain jise **Shell Script** kehte hain aur iski file extension **`.sh`** hoti hai. Ye hacking exploits execution aur system automation me sabse core factor hai.

---

### 🐚 Shell Script (.sh) Kya Hai?
* **Shell Script:** Ye ek instruction list (text file) hoti hai jo shell (jaise Bash or Zsh) ko directly sequential execution process batati hai.
* Ise run karte hi system file ke andar likhi har command ko top to bottom automatic execute kar deta hai, bina kisi manual typing delay ke.

---

### 🔑 Real-World Analogy (Doctor's Prescription / Recipe Slip 📝)
Maan lo aapko ek complex **Khana (System automation tasks)** banana hai. 
* Agar aap chef ko har ek step phone karke bataoge (jaise: pehle oil dalo, fir pyaz dalo), toh kafi time waste hoga.
* Iske badle aap chef ko ek **Recipe Slip (Shell script - `.sh`)** pakda dete ho jisme saare steps shuru se aakhir tak likhe hain. Chef use dekhta hai aur bina aapse dobara pooche automatic recipe bana deta hai. Linux me ye recipe sheet **`.sh`** file hai.

---

### ⚙️ Anatomy of a Shell Script:
Ek basic script structure aisa dikhta hai:

```bash
#!/bin/bash
# (Ye comments hain jo run nahi hote)
echo "Starting System Audit..."
uptime
echo "Audit Completed!"
```

#### 💡 The Shebang (`#!/bin/bash` or `#!/bin/zsh`)
Script ki sabse **pehli line** humesha **`#!`** (Shebang) se shuru hoti hai.
* **Purpose:** Ye system compiler ko batati hai ki is file ko execute karne ke liye kis software interpreter (shell program) ka use karna hai. (e.g., `/bin/bash` or `/bin/zsh`).

---

### ⚡ How to Create & Execute a Script (Step-by-Step Guide):

#### Step 1: Create File using Nano
```bash
nano auto_ping.sh
```
*(Open nano, write Shebang and commands, then save and exit).*

#### Step 2: Make it Executable (Most Important 🔑)
By default, standard file format ke pass run permission nahi hoti. Ise run bypass permissions dene ke liye `chmod` lagana padta hai:
```bash
chmod +x auto_ping.sh
```

#### Step 3: Run the Script (Two Ways 🚀)
* **Method A: Direct execution (Relative Path path check):**
  ```bash
  ./auto_ping.sh
  ```
  *(Yahan `./` batata hai ki file current directory me hi hai).*
* **Method B: Running via Shell interpreter directly:**
  ```bash
  bash auto_ping.sh
  ```
  *(Is method me check bypass ho jata hai aur file bina `chmod +x` kiye bhi execute ho sakti hai).*

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, shell script validation check karne ke liye in tasks ko complete karein:

1. **Task 1:** Apne home folder me ek fresh script file banayein (`nano my_first_script.sh`).
2. **Task 2:** Script ke sabse pehli line par **Shebang (`#!/bin/bash`)** specify karein aur uske baad `echo "Bhai Script Chal Rahi Hai!"` line likhein, aur save karke exits karein.
3. **Task 3:** Bina permissions badle, ise directly run karne ki koshish karein: `./my_first_script.sh`. Dekhein kya output error aata hai.
4. **Task 4:** Permission Denied error ko solve karne ke liye, `chmod` command ka use karke script ko execution (`x`) rights grant karein.
5. **Task 5:** Rights active hone ke baad, command `./my_first_script.sh` ko run karke output screen par status check karein.
6. **Task 6:** Ab file se execute permissions wapas chinne ke liye `chmod -x` run karein. Aur bina rights active kiye, **`bash my_first_script.sh`** command chala kar check karein ki kya script run ho gayi.
7. **Task 7:** Script ke andar multiple commands execute check setup karein. `nano` se file open karein, aur default updates checking operations command (e.g., `pwd`, `whoami`, `uptime`) line by line add karke verify save karein.
8. **Task 8:** Dynamic scripts automation parameters me comments ka inclusion check karne ke liye line ke aage **`#`** lagakar kuch remarks enter karein aur check karein ki wo comments bypass hote hain ya nahi.
9. **Task 9:** Absolute path system ka use karke, user home se `/home/kali/my_first_script.sh` script execute karne ki fully qualified command run check karein.
10. **Task 10:** Hacking tools payloads setups me dynamic shell automation (.sh files execution) ke basic significance aur benefits points explain karein.

---