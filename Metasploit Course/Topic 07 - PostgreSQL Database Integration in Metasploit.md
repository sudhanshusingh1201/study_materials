# Topic 07 - PostgreSQL Database Integration in Metasploit

Metasploit bina database ke chal sakta hai, lekin professional penetration testing mein target network bada hota hai (hazaron IPs, ports aur protocols). Is information ko manage, store aur query karne ke liye Metasploit **PostgreSQL** database use karta hai.

Is note mein hum dekhenge ki database integration kaise kaam karta hai, iska command workflow kya hai, aur data export-import kaise kiya jata hai.

---

## 1. Real-World Analogy: Database Kyun Zaroori Hai?

Maan lijiye aap ek intelligence investigator hain jo ek bohot bade gang/network par surveillance rakh raha hai:
* **Manual Note-taking:** Aap paper par likhte hain, "Host A ka port 21 open hai, Host B ka port 22 open hai." Agar gang bada ho gaya toh paper ghum jayega aur aap track nahi rakh payenge.
* **The Intelligence Black-Book (Database):** Aapke paas ek digital system hai jahan aap host details, unki vulnerabilities, aur unke churae gaye passwords (credentials) ko tabular form mein save karte hain. Jab chahe aap search kar sakte hain: "Mujhe sirf woh targets dikhao jinki port 445 (SMB) open hai."
* **PostgreSQL Metasploit ke liye wahi digital black-book hai.**

---

## 2. PostgreSQL and Metasploit Architecture

Metasploit background mein PostgreSQL running instance se connect karta hai.
* **Config File Path:** `~/.msf4/database.yml` (Is file mein database host, username, password aur port store hote hain).
* **`msfdb` utility:** Rapid7 ka helper tool jo database configuration, initialization aur restarts ko command-line se handle karta hai.

---

## 3. Database Administration Commands

Terminal par database check aur manage karne ke practical commands:

```bash
# 1. PostgreSQL system service start karna
sudo systemctl start postgresql

# 2. Service check karna ki running hai ya nahi
sudo systemctl status postgresql

# 3. Metasploit Database pehli baar create/configure karna
sudo msfdb init

# 4. Database configuration reset aur delete karke fresh deploy karna
sudo msfdb reinit

# 5. Database start karke automatic msfconsole open karna (Pro-Tip)
sudo msfdb run
```

---

## 4. Msfconsole Database Commands (Data Querying)

Jab console database se successfully connect ho jata hai (`db_status` -> Connected), toh hum in commands se data manipulate karte hain:

### A. Performing Scans (`db_nmap`)
Nmap scan run karein, result direct database mein save ho jayega:
```text
msf6 > db_nmap -sV -p 21,22,80 192.168.98.129
```

### B. Filtering Targets (`hosts` & `services`)
* **List all hosts in DB:**
  ```text
  msf6 > hosts
  ```
* **Filter hosts and add custom comments/tags:**
  ```text
  msf6 > hosts -c address,os_name,info
  ```
* **List services of all hosts:**
  ```text
  msf6 > services
  ```
* **Filter only hosts having port 21 open:**
  ```text
  msf6 > services -p 21 -u
  ```
  *(Here `-u` shows only up services).*

### C. Viewing Loot (`creds` & `vulns`)
* **List cracked/extracted passwords and usernames:**
  ```text
  msf6 > creds
  ```
* **List verified vulnerabilities of target hosts:**
  ```text
  msf6 > vulns
  ```

### D. Exporting & Importing Data (`db_export` / `db_import`)
Agar aapko apne scan results doosre teammate ke sath share karne hain:
* **Export DB results to XML file:**
  ```text
  msf6 > db_export -f xml /home/kali/Desktop/lab_scan.xml
  ```
* **Import XML results from external scan (e.g. Nmap XML output):**
  ```text
  msf6 > db_import /home/kali/Desktop/external_nmap_scan.xml
  ```

---

## 5. Practice Exercises for Database Mastery

Perform these tasks in your local lab and write your answers:

1. **Exercise 1 (Status Check):**  
   Msfconsole ke andar `db_status` command run karein aur screen par aane wale connection type aur database parameters ko note karein.

2. **Exercise 2 (Target Commenting):**  
   `hosts` command ka use karke target IP `192.168.98.129` par custom comment add karne ka command set karein (Hint: use `hosts -n "Metasploitable Lab" <IP>`).

3. **Exercise 3 (Port Filtering):**  
   Database query ka use karke check karein ki scanned list mein se kitne systems par port `80` (HTTP) open mili hai. Filter parameters batayein.

4. **Exercise 4 (Credential Inspection):**  
   Brute-force scan ke baad harvested passwords ki list display karne ke liye kaun si command use hoti hai?

5. **Exercise 5 (Exporting Data):**  
   Apne current scan database ko JSON ya XML format mein Kali desktop par save karne ki command run karke output verify karein.

6. **Exercise 6 (Workspace Check):**  
   Metasploit mein alag-alag targets ke liye alag-alag logical database environment (Workspaces) banane ke liye kis command ka use kiya jata hai? (Hint: search `workspace` command inside msfconsole).

7. **Exercise 7 (Importing External Scan):**  
   Kali Linux terminal par simple nmap scan xml output file generate karein (`nmap -oX scan.xml <target-ip>`) aur use msfconsole ke database mein import karne ke steps likhein.

8. **Exercise 8 (PostgreSQL restart):**  
   Agar database connectivity validation error throw kare, toh database service ko system level par restart karne ka commands check karein.
