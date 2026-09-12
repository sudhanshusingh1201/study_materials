---
title: "Topic 49 - Linux Process Deep-Dive: Lifecycle, Signals & Job Control"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# ⚡ Topic 49: Linux Process Deep-Dive: Lifecycle, Signals & Job Control (pstree, pgrep, pkill, SIGKILL/SIGTERM, fg, bg, nohup)

Bhai, **Topic 48** me humne basic process commands (`ps`, `top`, `kill`) dekhi thi. Lekin Linux me **Process Management** ko 100% master karne ke liye process lifecycle, parent-child process tree, process signals (SIGKILL, SIGTERM), job control (`fg`, `bg`), aur terminal detachment (`nohup`, `disown`) ko deep me samajhna padta hai.

Cybersecurity me, privilege escalation, persistent payloads setup aur malware analysis me processes ki life cycle samajhna critical hota hai.

---

### 🏛️ 1. Program vs Process (Basic Difference)

* **Program:** Disk par rakhi ek **static file** (executable code, jaise `/usr/bin/nmap` ya `/bin/bash`). Ye jab tak execute na ho, tab tak memory consume nahi karta.
* **Process:** Jab program ko run kiya jata hai, toh RAM me uska ek **active, living instance** banta hai jise **Process** kehte hain. Process ke paas apni RAM memory, PID, Owner (User), aur File Descriptors hote hain.

---

### 🌲 2. Process Tree & Parent-Child Hierarchy (PPID)

Linux me **har process ka ek Parent Process hota hai** (jise `PPID` kehte hain).
* System boot hone par sabse pehla process chalta hai: **PID 1 (`systemd` ya `init`)**.
* Saare baaki processes PID 1 ke bacche (children) ya descendants hote hain.
* **`pstree`**: System ke saare processes ko ek beautiful tree structure me dikhta hai:
  ```bash
  pstree -p
  ```
  *(Isse parent aur unke child process PIDs visual format me samajh aate hain).*

---

### 🔄 3. Process States (Process ki Awastha)

Terminal me `ps aux` chalane par `STAT` column me ye letters dikhte hain:
1. **R (Running / Runnable):** Process active hai ya CPU execution slot ka wait kar raha hai.
2. **S (Interruptible Sleep):** Process kisi event ya user input ka wait kar raha hai (most common).
3. **D (Uninterruptible Sleep):** Process Direct Disk I/O ka wait kar raha hai (is state me process `kill -9` ko bhi ignore kar sakta hai jab tak I/O complete na ho).
4. **Z (Zombie / Defunct):** Process khatam ho chuka hai, lekin uske parent process ne abhi tak uska exit status collect nahi kiya. Ye RAM memory space toh nahi leta par PID table occupy karta hai.
5. **T (Stopped):** Process ko `Ctrl + Z` se pause/stop kar diya gaya hai.

---

### 📡 4. Linux Signals (Processes se Baat Karna)

Kernel ya users processes ko control karne ke liye **Signals** bhejte hain. Important signals:

| Signal Name | Number | Shortcut / Action | Function |
| :--- | :--- | :--- | :--- |
| **SIGHUP** | 1 | Terminal Hangup | Process ko bina kill kiye config reload karna. |
| **SIGINT** | 2 | `Ctrl + C` | Keyboard Interrupt Request (Graceful stop). |
| **SIGKILL** | 9 | `kill -9 <PID>` | **Force Kill Immediately** (Kernel forceful kill, process ignore nahi kar sakta). |
| **SIGTERM** | 15 | `kill <PID>` | **Graceful Termination Request** (Default `kill`, process ko clean exit karne deta hai). |
| **SIGTSTP** | 20 | `Ctrl + Z` | Terminal Stop / Pause process. |

---

### 🎛️ 5. Job Control (Foreground, Background & Detachment)

Terminal par multiple tasks ek sath chalane ke liye Job Control ka use kiya jata hai:

* **Background me run karna (`&`):**
  ```bash
  ping 8.8.8.8 > ping_log.txt &
  ```
* **Active Jobs dekhna (`jobs`):**
  ```bash
  jobs -l
  ```
* **Background job ko Front par laana (`fg`):**
  ```bash
  fg %1    # Job number 1 ko foreground me laao
  ```
* **Paused job ko background me resume karna (`bg`):**
  `Ctrl + Z` se pause karne ke baad, `bg %1` daba kar use background me resume karein.
* **Terminal Band hone par bhi task chalte rakhna (`nohup` & `disown`):**
  Normal process terminal close karte hi `SIGHUP` signal paakar death ho jata hai. Isse bachne ke liye:
  ```bash
  nohup python3 long_script.py &
  ```
  Ya running job par: `disown -h %1`

---

### 🎯 6. Advanced Process Utilities (`pgrep`, `pkill`, `nice`)

* **`pgrep <name>`**: Naam se PID dhoondhna:
  ```bash
  pgrep -l firefox
  ```
* **`pkill <name>`**: Naam se direct kill karna:
  ```bash
  pkill -9 -f "python3 long_script.py"
  ```
* **`nice` & `renice` (Process Priority):**
  Priority scale `-20` (Highest priority) se `19` (Lowest priority) hoti hai:
  ```bash
  nice -n -10 nmap 192.168.1.1    # High priority par run karna
  renice -n 5 -p 1234             # Existing process ki priority change karna
  ```

---

### 🔑 Real-World Analogy (The Restaurant Kitchen & Waiters 🍽️🤖)
* **Program vs Process:** Recipe book me likhi dish ki recipe = **Program**. Kitchen me order aane par pak rahi actual dish = **Process**.
* **Process Tree (Parent-Child):** Head Chef (PID 1 `systemd`) ne Junior Chef ko task diya, Junior Chef ne Helper को task diya. Helper ka parent Junior Chef hai.
* **SIGTERM (Signal 15):** Helper se kehna: *"Apna kaam samet kar 5 min me chutti karo"* (Graceful).
* **SIGKILL (Signal 9):** Security guard dwara helper ko instantly kitchen se baahar phenk dena (Immediate force kill).
* **`nohup`:** Dish ko counter se utha kar automatic heating box me daal dena taaki agar Waiter (Terminal) chutti karke chala bhi jaye, toh dish kharab na ho.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, Process 101 mechanics check karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** System par process tree check karne ke liye **`pstree`** run karein aur dekhein ki PID 1 `systemd` (ya `init`) ke niche saari processes kaise branched hain.
2. **Task 2:** Apne active shell ka PID aur uske parent process ka PID check karne ke liye command run karein: `echo "PID: $$ | PPID: $PPID"`.
3. **Task 3:** Ek long-running background job shuru karein: `sleep 500 &` aur terminal par output integer job number verify karein.
4. **Task 4:** Active terminal jobs ki list dekhne ke liye command **`jobs -l`** execute karein.
5. **Task 5:** `sleep 500` job ka PID search karne ke liye **`pgrep sleep`** chala kar matching PID print karein.
6. **Task 6:** Ek foreground command chalaayein `sleep 200`, phir keyboard shortcut **`Ctrl + Z`** press karke analyze karein (State: Stopped).
7. **Task 7:** `jobs` me stopped `sleep 200` ko background me active resume karne ke liye **`bg %1`** chalaayein.
8. **Task 8:** Background me chal rahe `sleep` processes ko ek hi jhatke me kill karne ke liye pattern command run karein: **`pkill -9 sleep`**.
9. **Task 9:** Terminal close hone par bhi execution active rakhne ka syntax verify karne ke liye test karein: `nohup ping -c 5 8.8.8.8 > nohup_test.out &` aur check karein `nohup.out` ya custom file me output write hua ya nahi.
10. **Task 10:** Hacking tools (jaise Metasploit handlers ya long-running port scans) ko remote VPS par chalaate waqt `nohup` ya `tmux` / `screen` sessions use karne ki kya security & operational importance hai? 2 lines me explain karein.

---
