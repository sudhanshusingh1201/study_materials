# Topic 03 - Kali Linux & Metasploit VMware Setup Guide

Hacking aur penetration testing ko safe environment mein seekhne ke liye VMware sabse best hypervisor hai. Is topic mein hum step-by-step seekhenge ki kaise **Kali Linux (Attacker Machine)** aur **Metasploitable 2 (Victim Machine)** ko VMware mein setup aur connect karte hain.

---

## 1. Kyun Pre-built VMware Image best hai?
Hum Kali Linux ko ISO file se install nahi karenge. Kali Linux pre-built VMware images (.vmx files) deta hai. 
* **Fayda:** Isme aapko koi installation wizard nahi chalana padta. Sirf download karo, extract karo aur direct run karo! 2 minute mein machine ready ho jati hai.

---

## 2. Step-by-Step Installation Guide

### Step 1: Download and Install VMware
1. Google par search karein **"VMware Workstation Player Download"** (Yeh personal use ke liye free hai).
2. Ise download karke apne Windows PC par normal software ki tarah next-next karke install kar lein.

### Step 2: Download Kali Linux VMware Image
1. Go to: [Kali Linux Official Downloads](https://www.kali.org/get-kali/#kali-platforms)
2. Scroll karke **"Virtual Machines"** section par jayein.
3. **VMware** waale option ke download icon par click karein (lagbhag 3GB ki zip file hogi).
4. Download hone ke baad, use **7-Zip** ya **WinRAR** ka use karke kisi safe folder mein extract kar lein (jaise `D:\VMs\Kali-Linux`).

### Step 3: Run Kali Linux in VMware
1. **VMware Workstation** ko open karein.
2. Left pane mein **"Open a Virtual Machine"** par click karein.
3. Jo folder aapne extract kiya tha, uske andar jayein aur **`.vmx`** extension waali file ko select karein (e.g., `kali-linux-202X.X-vmware-amd64.vmx`).
4. Machine select hone ke baad, **"Power on this virtual machine"** par click karein.
5. Agar VMware aapse puche **"I copied it"** ya **"I moved it"**, toh hamesha **"I copied it"** par click karein.
6. **Default Login Credentials:**
   * **Username:** `kali`
   * **Password:** `kali`

---

## 3. Launching Metasploit inside Kali Linux

Ek baar Kali Linux start ho jaye, toh Metasploit open karna bohot easy hai:
1. Terminal kholo (`Ctrl + Alt + T`).
2. Type karo:
   ```bash
   sudo msfconsole
   ```
3. Root password maangega, toh enter karo: `kali`
4. Aapka Metasploit console start ho jayega!

---

## 4. Target Machine Setup (Metasploitable 2)
*Metasploit ka use karne ke liye hume ek vulnerable target chahiye jise hum safe tarike se hack kar sakein. Iske liye Rapid7 ne **Metasploitable 2** banaya hai.*

### Step 1: Download Metasploitable 2
1. Go to: [SourceForge Metasploitable Download](https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)
2. **`metasploitable-linux-2.0.0.zip`** download kar lein (approx 800MB).
3. Ise apne PC mein extract kar lein.

### Step 2: Import in VMware
1. VMware open karein -> **Open a Virtual Machine**.
2. Extracted folder mein se **`.vmx`** file select karein.
3. Machine power on karein (`I copied it` select karein).
4. **Default Login Credentials:**
   * **Username:** `msfadmin`
   * **Password:** `msfadmin`

> [!WARNING]
> Metasploitable 2 behad unsafe machine hai. Ise kabhi bhi Bridged network par ya public internet par directly connect na karein. Hamesha NAT mode use karein.

---

## 5. Crucial: VMware Network Configuration (NAT Mode)
Dono machines (Kali Linux aur Metasploitable) aapas mein connect ho sakein aur aapka main Windows network safe rahe, iske liye dono ka Network Adapter **NAT** par hona chahiye.

### Settings check karne ka tarika:
1. VMware mein virtual machine ke naam par right-click karein aur **Settings** mein jayein.
2. **Network Adapter** select karein.
3. Right side mein **"NAT: Used to share the host's IP address"** ko select karke OK kar dein.
4. Dono VMs mein check karein ki NAT select hai ya nahi.

---

## 6. How to verify Connection (Kali <-> Metasploitable)

1. **Metasploitable VM** par login karein (`msfadmin`/`msfadmin`) aur command chalayein:
   ```bash
   ifconfig
   ```
   *Yahan se iska IP note karein (e.g., `192.168.X.Y`).*

2. **Kali Linux VM** par terminal khol kar target IP ko ping karein:
   ```bash
   ping -c 4 <Metasploitable-IP>
   ```
   *Agar packets transfer ho rahe hain, toh aapka hacking lab setup 100% ready hai!*

---

## 7. Practice Exercises for Lab Verification

1. **Exercise 1 (IP Discovery):**  
   Apne network segment par target ka IP find karne ke liye Kali terminal se Nmap scan run karein:
   `nmap -sn 192.168.X.0/24` (Apne NAT IP range ke mutabik).
   
2. **Exercise 2 (Metasploit Launch):**  
   Kali par database service start karke `msfconsole` launch karein aur `db_status` verify karein.
