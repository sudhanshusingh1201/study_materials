---
title: "Topic 28 - Linux Command chmod (Change Permissions)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🔑 Topic 28: Linux Command: chmod (Change Permissions)

Bhai, Linux security model files aur directories ke access rules par depend karta hai. Jab bhi aap koi exploit payload ya tool GitHub se download karte hain, toh security constraints ke kaaran use run karne ki direct execution permission nahi hoti (`Permission Denied` error aata hai). File ke permissions ko update/modify karne ke liye hum **`chmod`** command ka use karte hain.

---

### 🔑 chmod Command Kya Hai?
* **chmod:** **Ch**ange **Mod**e.
* Is command ka primary use file aur directory permissions (Read, Write, Execute) ko change karne ke liye kiya jata hai.

---

### 🔑 Real-World Analogy (Restricted Area Entry Passes 🎫)
Maan lo ek server room (File) hai jisme entry ke liye security checks hain. Security office aapko teen tarah ke access passes de sakta hai:
1. **Read (`r`) Pass:** Aap room ke andar ja kar files ko sirf **dekh (read)** sakte ho, chhu nahi sakte.
2. **Write (`w`) Pass:** Aap data me **badlaav (modify/delete)** kar sakte ho.
3. **Execute (`x`) Pass:** Aap computer systems ko **start/run** kar sakte ho.

Ab, ye passes teen groups ko diye ja sakte hain: **Owner (Aap)**, **Group (Aapki team)**, aur **Others (Bahar ke log)**. **`chmod`** wahi system administrator hai jo ye passes control karta hai.

---

### ⚙️ Permissions Structure in Linux:
`ls -l` chalane par permissions string aisi dikhti hai:
`-rwxrwxr-x`
* **r (Read):** Value = **`4`** (File dekhne ki permission).
* **w (Write):** Value = **`2`** (File edit/delete karne ki permission).
* **x (Execute):** Value = **`1`** (Script/Tool run karne ki permission).

---

### ⚡ Two Methods to Change Permissions:

#### Method A: Symbolic Mode (Using Characters 🔤)
Simple symbols ka use karke permissions add ya remove karna:
* **Who (Kiske liye):** `u` (User/Owner), `g` (Group), `o` (Others), `a` (All/Everyone).
* **Action (Operation):** `+` (Add permission), `-` (Remove permission), `=` (Set exact permission).

##### 🚀 Examples:
* **Exploit/Payload ko run permission dena (Most Common in Hacking 🛡️):**
  ```bash
  chmod +x payload.sh
  ```
  *(Isse system ke sabhi users ke liye execution `x` bypass active ho jayega).*
* **Sirf Owner ko execution permission dena:**
  ```bash
  chmod u+x exploit.py
  ```
* **Group se write delete karna:**
  ```bash
  chmod g-w target.txt
  ```

---

#### Method B: Octal / Numeric Mode (Using Numbers 🔢)
Ye professional standard hai. Isme hum base numbers (r=4, w=2, x=1) ko add karke teen digit ka code dete hain: **`[User][Group][Others]`**.

##### 🔒 Numeric Math Formula:
* **`7`** = `4+2+1` (rwx - Read, Write, Execute sub-access).
* **`6`** = `4+2+0` (rw- - Read aur Write only).
* **`5`** = `4+0+1` (r-x - Read aur Execute only).
* **`4`** = `4+0+0` (r-- - Read Only).
* **`0`** = `0+0+0` (--- - No permissions).

##### 🚀 Common Hacking Examples:
* **`chmod 777 exploit.sh`** ➡️ Sabhi users ko full permissions (`rwxrwxrwx`). (Kafi insecure hai, testing me use hota hai).
* **`chmod 755 script.py`** ➡️ Owner ko Full access (`7`), baaki group aur public ko sirf read aur execute (`5`) access. (Standard executable scripts standard).
* **`chmod 600 id_rsa`** ➡️ Sirf owner ko read/write (`6`) access, group aur public ko zero access (`00`). (Mandatory for SSH Private keys, warna ssh allow nahi karta security errors ke karan).

---

### ⚡ Critical chmod Flags:
* **`chmod -R` (Recursive 📁):** Pure folder aur uske andar ki files ke permissions ek sath change karne ke liye.
* **`chmod -v` (Verbose):** Kon-konse permissions change hue, screen par live monitor karne ke liye.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, `chmod` features verify karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** Apne home folder me ek file banayein (`touch test_permission.sh`). Iske default permissions check karne ke liye `ls -l` chalayein aur permissions string notebook me likhein.
2. **Task 2:** Symbol operator **`+x`** ka use karke script ko execution status active karein aur dekhein ki kya file ka text color terminal list me green ho jata hai.
3. **Task 3:** Execution active hone ke baad, symbolic remove operator **`-x`** ka use karke file se execution permission wapas le lein.
4. **Task 4:** Numeric mode ka use karke test file ke permissions ko **`chmod 777 test_permission.sh`** set karein. `ls -l` chalakar verify karein ki kya pure permission block me `rwxrwxrwx` show ho raha hai.
5. **Task 5:** Security standards ke according, user ke private SSH keys ko leak hone se bachane ke liye use **`600`** set karna padta hai. `chmod 600 test_permission.sh` run karein aur `ls -l` se check karein ki kya group aur public permission string blank (`---`) ho gayi.
6. **Task 6:** Normal scripts default numeric permission **`755`** set karein aur check karein ki prompt string output kya dikhata hai.
7. **Task 7:** Ek naya directory banayein `sec_folder` (`mkdir sec_folder`). Is directory ko full permission set **`777`** apply karke ls layout check karein.
8. **Task 8:** Verbose checking ke liye **`-v`** flag ka use karke permissions change run karein aur screen status messages verify karein (e.g., `chmod -v 755 test_permission.sh`).
9. **Task 9:** `/home/kali/my_lab` directory aur uske andar ki sabhi sub-files ko recursive mode **`-R`** ke through owner read-only mode (`chmod -R 755`) me update karne ki command framework execute check verify karein.
10. **Task 10:** Hacking tools exploit execution me `chmod` ka basic usage check logic explain karein.

---