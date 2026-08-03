---
title: "Topic 33 - Linux Command: file (Determine File Type)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🔍 Topic 33: Linux Command: file (Determine File Type)

Bhai, Windows me system file type pehchanne ke liye **file extension** (jaise `.txt`, `.exe`, `.png`) par completely rely karta hai. Agar aap Windows me `virus.exe` ka naam badal kar `virus.txt` kar doge, toh Windows confuse ho jayega aur use Notepad me kholne ki koshish karega.

Lekin **Linux aisa nahi karta!** Linux file extension ko importance nahi deta. Linux kisi bhi file ke actual structure aur uske header data (jise **Magic Bytes** kehte hain) ko read karke batata hai ki file asal me kya hai. Is kaam ke liye hum **`file`** command ka use karte hain.

---

### 🔍 file Command Kya Hai?
* **file:** Ye ek inbuilt utility command hai jo kisi bhi file ke internal contents aur bytes ko inspect karke uska exact file type (ASCII text, ELF binary, JPEG image, zip archive, etc.) detect karti hai.
* Hacking me iska use bahut zaroori hai. Jab hum target system se koi unknown payload or executable download karte hain jiska extension na ho, toh `file` chalakar hum uska nature pata karte hain.

filew

### 🔑 Real-World Analogy (The Laboratory Test 🏷️🧪)
* Maan lo aapke samne ek cold drink ki bottle rakhi hai, lekin us par kisi ne **"Water 💧"** ka fake label (extension) chipka diya hai.
* Agar aap sirf label dekhoge (Windows way), toh aap use paani samajh loge.
* Lekin agar aap use ek **Chemical Test Lab (file command)** me bhejte ho, toh lab testing se pata chalta hai ki andar carbonated water aur color mix hai, yani wo ek cold drink 🥤 hai!
* `file` command bina label par bharosa kiye, file ke andar ka chemical test (Magic Bytes inspection) karti hai.

---

### ⚡ file Command Operations & Flags (Usage Guide)

#### 1. Basic Usage: `file <filename>`
Ek single file ka real structure check karne ke liye:
```bash
file target_file
```
*Agar `target_file` ek hacking script hai jiska extension `.txt` rakha gaya hai, toh ye output dikhayega: `target_file: Bourne-Again shell script, ASCII text executable`.*

---

#### 2. Scan All Files: `file *`
Current directory me jitni bhi files aur folders hain, un sabhi ka file type ek sath print karne ke liye asterisk (`*`) wildcard use hota hai:
```bash
file *
```
*Output Example:*
```text
auto_ping.sh: Bourne-Again shell script, ASCII text executable
important_ips: ASCII text
my_lab:       directory
payload:      ELF 64-bit LSB executable, x86-64, version 1 (SYSV)
```
*(Yahan aap bina extension ke bhi directory, shell script aur ELF binary ko clear differentiate kar sakte hain).*

---

#### 3. Scan Inside a Specific Directory: `file directory_name/*`
Agar aap current directory me khade hokar kisi doosre folder ke saare items ka type check karna chahte hain, toh relative/absolute path ke sath `*` lagayein:
```bash
file my_lab/*
```
*(Ye `my_lab/` directory ke andar ki har ek file ka test report screen par print kar dega).*

---

#### 4. Read Special/Device Files: `file -s` (Special File Probe) ⚠️
Linux me hardware devices, partitions aur ports ko `/dev/` folder ke andar special files ke roop me represent kiya jata hai. 
* By default, `file` command in special files ko read nahi karti kyunki aisa karne se device interrupt ho sakta hai ya terminal crash ho sakta hai.
* **`-s` (Special)** flag device block levels ko active probe karke batata hai ki us special file/device par kaunsa file system installed hai (Requires Sudo).
```bash
sudo file -s /dev/sda1
```
*Output:* `/dev/sda1: SGI XFS filesystem data, UUID=...` (Ya Ext4, NTFS, FAT etc. filesystem type detect hoga).

---

#### 5. Filter Files with Character Ranges: `file pattern[range]`
Agar aapko ek range me aane wali files ka type check karna hai (jaise sirf `file_1`, `file_2`, `file_3` ya `data_a`, `data_b`), toh shell globbing ranges bracket `[]` ka use karein:
```bash
file file_[1-3].txt
```
*(Ye sirf `file_1.txt`, `file_2.txt`, aur `file_3.txt` ka type bataega).*

```bash
file payload_[a-c]
```
*(Ye `payload_a`, `payload_b`, aur `payload_c` ko check karein).*

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `file` command ki parameters verify karne ke liye in tasks ko execute karein:

1. **Task 1:** Apne home folder me `touch test_magic.txt` banayein. Uske baad `file test_magic.txt` chala kar check karein ki empty file par kya output aata hai.
2. **Task 2:** Us file ke andar `echo "Bhai study material update"` run karke kuch write karein. Phir se `file test_magic.txt` run karein aur dekhein ki kya type change ho kar `ASCII text` ho gaya.
3. **Task 3:** Us file ka name rename (`mv`) karke `test_magic.png` kar dein. Phir `file test_magic.png` run karke verify karein ki kya Linux uske fakeness ko pehchan gaya.
4. **Task 4:** Apne `/etc/` folder ke andar ki top levels files ko check karne ke liye `file /etc/*` command execute karein.
5. **Task 5:** Current directory me `file *` run karein aur identify karein ki screen par directories aur documents me differences kaise dikhte hain.
6. **Task 6:** Hacking setups me use hone wale tool binary ka system type checking syntax (jaise `file /usr/bin/nmap`) run karein aur output details check karein (ELF format system).
7. **Task 7:** Partition details check karne ke liye `file -s` flag ka syntax structure command execute karein (e.g. `sudo file -s /dev/loop0`).
8. **Task 8:** Teen mock files banayein: `host_1.txt`, `host_2.txt`, aur `host_3.txt`. Range feature use karke in teenon ko ek sath test karne ke liye `file host_[1-3].txt` chala kar output dekhein.
9. **Task 9:** Letters range selection check karne ke liye files `host_a.txt`, `host_b.txt` create karke `file host_[a-c].txt` command execute verify karein.
10. **Task 10:** Windows operating system aur Linux operating system me file extension recognition (pechane) ke primary difference ko simple 2 lines me detail me explain karein.

---
