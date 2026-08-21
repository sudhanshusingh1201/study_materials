---
title: "Topic 48 - Linux System Administration & Process Management (ps, top, systemctl, df, free, kill)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# ⚙️ Topic 48: Linux System Administration & Process Management (ps, top, systemctl, df, free, kill)

Bhai, ek system administrator ya penetration tester ke roop me, aapko ye pata hona chahiye ki Linux OS backend me resource management kaise karta hai. System par chalne wale active applications (Processes), background services (daemons), RAM/Disk status aur crashed processes ko terminate karna system administration ka main core part hai.

---

### 🏛️ 1. Process Management (Chal rahi commands ko track karna)

Linux me jab bhi koi program execute hota hai, use ek unique numeric **PID (Process ID)** milti hai.

#### A. Process View commands
* **`ps`** (Process Status): Current terminal me chal rahe active processes dekhne ke liye.
  * **`ps aux`** or **`ps -ef`** (Standard system-wide view): System par chal rahe **saare users** ke background aur active processes ki details (PID, CPU%, Memory%) dikhata hai.
  ```bash
  ps aux | grep apache2
  ```
* **`top`** / **`htop`** (Real-Time Monitor): Task Manager ki tarah real-time processor, RAM usage aur busy processes ki list dikhata hai (Exit karne ke liye `q` dabayein).

#### B. Process Control commands (Terminate/Kill)
* **`kill <PID>`**: Process ko band (terminate) karne ke liye.
* **`kill -9 <PID>`** (Force Kill): Agar koi process hang ho gayi hai aur normal terminate nahi ho rahi, toh system use forcibly shut down karta hai.
* **`killall <process_name>`**: Naam se saare matches ko ek sath kill karna (jaise `killall firefox`).

---

### ⚙️ 2. System Services Management (`systemd` & `systemctl`)
Modern Linux distributions background services ko manage karne ke liye **`systemd`** process manager use karte hain. Iska controller tool **`systemctl`** hai:
* **Service start karna:** `sudo systemctl start ssh`
* **Service stop karna:** `sudo systemctl stop ssh`
* **Service Status check karna:** `systemctl status ssh`
* **Boot time auto-start enable karna:** `sudo systemctl enable ssh` *(Reboot ke baad service automatic start ho jayegi).*
* **Boot time auto-start disable karna:** `sudo systemctl disable ssh`

---

### 📊 3. Storage & Memory Auditing (Disk and RAM check)

* **`df -h`** (Disk Free): Hard drive space configurations check karta hai (Hum `-h` yaani Human-Readable format me print karte hain, jaise GB/MB).
* **`du -sh <folder>`** (Directory Usage): Kisi specific folder ka actual size batata hai.
  ```bash
  du -sh /var/log/
  ```
* **`free -h`** (Free RAM): System ki total RAM, used RAM, aur available swap memory status dynamically display karta hai.
* **`uptime`**: System kab se bina reboot kiye chal raha hai aur kitna average CPU load hai.

---

### 🔑 Real-World Analogy (The Chef's Kitchen Kitchen Management 👨‍🍳🍳)
* **Processes (PID):** Kitchen me ban rahi alag-alag dishes (jaise Soup, Pasta). Har dish ka apna gas stove burner ID (PID) hota hai.
* **`ps aux`:** Chef ki checking list jo monitor karti hai ki kaun-kaun se burners par kaunse recipes pak rahi hain.
* **`kill -9`:** Chef dwara kisi kharab dish (crashed process) ko stove band karke sidhe trash box me dump kar dena.
* **`systemctl` (Kitchen Appliances):** Fridge ya Exhaust fan ko start/stop karna ya use enable karna (taaki subah kitchen khulne par automatic start ho jaye).
* **`df -h` & `free -h`:** Kitchen containers me bacha raw material (Hard drive space) aur helper kitchen slab space (RAM capacity) check karna.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, system administration options check karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** System par chal rahe saare users ke processes ki detail list `ps aux` command se check karein aur use `less` me pipe karein.
2. **Task 2:** Apne system me memory usage check karne ke liye human readable formatting flag ke sath **`free -h`** run karein.
3. **Task 3:** Disk storage memory configurations verify karne ke liye **`df -h`** command execute karke root `/` partition ka available size batayein.
4. **Task 4:** Apache web server or SSH server (jaise `ssh`) ka status verify karne ke liye run karein: `systemctl status ssh` (ya `sudo systemctl status ssh`).
5. **Task 5:** Dynamic tasks updates monitor check karne ke liye live screen terminal command **`top`** execute karein aur `q` press karke exit verify karein.
6. **Task 6:** `/var/log` folder ka total space utilization count check karne ke liye command run karein: `sudo du -sh /var/log`.
7. **Task 7:** Ek dummy process background run setup check karein: `sleep 1000 &` (& lagane se process background me chali jayegi), aur use check karne ke liye `ps aux | grep sleep` run karein.
8. **Task 8:** Background sleep process ka PID identify karke use force kill syntax se terminate karein: `kill -9 <PID>`.
9. **Task 9:** System uptime status check karein aur verify karein ki average CPU loads kya parameters show ho rahe hain.
10. **Task 10:** Hacking backdoors configuration setups me background daemon processes aur persistent boot systemctl services run karne ke main security impacts kya hain? 2 lines me explain karein.

---
