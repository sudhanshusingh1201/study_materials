# Topic 03 - Preparation of Metasploit Lab

Bhai, cyber security aur vulnerability exploitation practice karne ke liye ek secure aur isolated **Lab Environment** set up karna sabse important step hai. Hacking payloads aur exploits ko real-world networks se door rakhne ke liye is setup ka use kiya jata hai.

---

## 1. Core Architecture of the Lab

Is lab environment me do main components (Virtual Machines) hote hain jo aapas me connect hote hain par outside local network se insulated rehte hain:

```mermaid
graph LR
    subgraph Isolated Lab Network
    A[Kali Linux VM<br>Attacker Machine<br>IP: 192.168.56.X] <--> B[Metasploitable 2 VM<br>Victim Machine<br>IP: 192.168.56.Y]
    end
    C[Host Machine / Router] -.->|BLOCKED!| Isolated Network
```

1. **The Attacker VM (Kali Linux):** 
   * Hamari main machine jahan se exploits execute kiye jayenge. Isme Metasploit, Nmap aur auxiliary scripts pre-loaded hote hain.
2. **The Victim VM (Metasploitable 2):**
   * Rapid7 dwara banayi gayi ek deliberately vulnerable Linux-based operating system. Isme open ports, custom vulnerabilities aur outdated services active rehti hain taaki hum testing kar sakein.

---

## 2. Step-by-Step Installation

### Step A: Hypervisor Setup
* **Software:** **VirtualBox** ya **VMware Workstation Player** download aur install karein. (VirtualBox is highly recommended).

### Step B: Attacker Machine Setup
* Download the pre-built VirtualBox image of **Kali Linux** from the official website.
* VirtualBox me import karein (`File > Import Appliance`).

### Step C: Victim Machine Setup
* Download the **Metasploitable 2** zip file from SourceForge.
* Unzip the folder.
* VirtualBox me `New Machine` create karein, OS type `Linux (Ubuntu 64-bit)` select karein, aur custom virtual hard disk select karte waqt unzipped `Metasploitable.vmdk` file ko choose karein.

---

## 3. Network Configuration (The Isolation Shield 🛡️)

Target systems ko hack karte waqt exploits hamare real home network par na jayein aur target secure rahe, iske liye VirtualBox me network settings modify karte hain:

### Recommended: Host-Only Network
* **VirtualBox Configuration:**
  1. VirtualBox ke main menu me `File > Tools > Network Manager` par jayein aur ek Host-only Network interface create karein (e.g., `vboxnet0`).
  2. Dono VMs (Kali & Metasploitable) ki network settings me jayein.
  3. **Attached to:** select karein **Host-only Adapter**.
  4. Name block me select karein matching interface (e.g., `vboxnet0`).
* **Advantage:** Dono machines local machine browser aur aapas me dynamic connections bana payengi par internet blocked rahega.

---

## 4. Initializing Metasploit Database Services

Kali Linux start hone ke baad database integrations verify karne ke liye terminal commands run karein:

### 1. Start PostgreSQL Service
```bash
sudo systemctl start postgresql
```

### 2. Initialize Metasploit DB schema (Required once)
```bash
sudo msfdb init
```

### 3. Open Msfconsole
```bash
msfconsole -q
```

### 4. Verify Database Status
```text
msf6 > db_status
```
*Expected Output:* `[*] Connected to msf. Connection type: postgresql.`

---

## 5. Lab Verification Checks

Dono machines properly connect ho chuki hain, isko check karne ke liye:

1. **Victim VM login parameters:** Default username `msfadmin` aur password `msfadmin` use karein.
2. **Check IP of target:** Metasploitable me run karein `ifconfig` (Let's assume IP is `192.168.56.102`).
3. **Ping Check from Kali:** Kali terminal se verify karein:
   ```bash
   ping -c 3 192.168.56.102
   ```
4. **Fast scan verification in MSF:**
   ```text
   msf6 > db_nmap -F 192.168.56.102
   msf6 > hosts
   ```
