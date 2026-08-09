# Topic 02 - Installation and Setup of Metasploit

Metasploit chalane se pehle iska environment setup aur database connection samajhna bohot zaroori hai. Is note mein hum Kali Linux par iske dynamic integration aur doosre platforms par installation ke practical steps ko deep dive karenge.

---

## 1. Real-World Analogy: Lab Setup Kyun Zaroori Hai?

Maan lijiye aap ek fire-fighter hain aur aapko aag lagane/bujhane ki practice karni hai:
* **Miscalibrated Practice:** Agar aap seedhe kisi public jungle ya building mein aag lagakar testing karenge, toh tabahi mach jayegi aur police aapko jail mein daal degi.
* **Controlled Practice:** Aap ek proper test laboratory (fire training center) banate hain jahan har cheez controlled hoti hai aur nuksaan hone ka koi khatra nahi hota.
* **Hacking Lab Setup:** Kali Linux (Attacker VM) aur database configure karna wahi controlled laboratory setup hai, taaki aap jo bhi exploits run karo, woh target range se bahar na jayein.

---

## 2. Installation on Different Platforms

Metasploit ko run karne ke teen tareeqe hain:

### A. Kali Linux & Parrot OS (Pre-installed)
Kali Linux penetration testing ke liye banaya gaya hai. Isme Metasploit **pehle se installed** aata hai. Aapko sirf ise up-to-date rakhna padta hai:
```bash
sudo apt update && sudo apt install metasploit-framework -y
```

### B. Linux (Ubuntu / Debian / CentOS) par Manual Install
Agar aap ek plain Ubuntu system ko hacking rig banana chahte ho, toh Rapid7 ka official script use kar sakte ho:
```bash
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
chmod 755 msfinstall && \
./msfinstall
```

### C. Windows / macOS Installation
Windows par Metasploit installer available hai, lekin iska use **highly discouraged** hai.
* **Kyun?** Windows Defender aur antivirus Metasploit ke core payloads (Meterpreter dlls, executables) ko turant delete/quarantine kar dete hain. Isse tool bar-bar crash hoti hai.

---

## 3. Practical: Database Integration (`msfdb` setup)

Metasploit PostgreSQL database engine use karta hai. Iska connection setup karne ka sahi tarika:

### Step 1: Start database service
PostgreSQL ko target reports store karne ke liye background mein chalna padta hai:
```bash
sudo systemctl start postgresql
```
*(Verify karne ke liye: `sudo systemctl status postgresql`)*

### Step 2: Set autostart (Optional)
Agar aap chahte hain ki Kali system open hote hi database khud chal jaye:
```bash
sudo systemctl enable postgresql
```

### Step 3: Initialize Database schema
Pehli baar database chalate waqt credentials aur users configure karne ke liye:
```bash
sudo msfdb init
```
*(Yeh check karega ki database ready hai ya nahi, aur new configuration parameters set karega).*

### Step 4: Starting msfconsole with database
`msfconsole` likhne ke bajaye direct terminal se database integrated launch karein:
```bash
sudo msfdb run
```

---

## 4. Advanced Troubleshooting: Database resets

Kahi baar database crash ho jata hai ya sync loose kar deta hai. Aise mein database ko reset aur restart karne ka command:

* **Database Re-initialization:**
  ```bash
  sudo msfdb reinit
  ```
  *(Yeh command purane database data ko drop karke fresh schema deploy karegi).*
  
* **Check database connection type (inside msfconsole):**
  ```text
  msf6 > db_status
  ```

---

## 5. Practice Exercises for Setup Mastery

1. **Exercise 1 (Autostart Status):**
   Kali Linux terminal par `systemctl is-active postgresql` run karke check karein ki kya service active hai ya inactive?

2. **Exercise 2 (Troubleshooting):**
   Maan lijiye aapne `msfconsole` chalaya aur `db_status` mein `no connection` aa raha hai. Is situation ko resolve karne ke liye step-by-step kaun si commands run karenge?
