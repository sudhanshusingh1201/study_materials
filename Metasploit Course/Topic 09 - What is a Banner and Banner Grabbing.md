# Topic 09 - What is a Banner and Banner Grabbing?

Cybersecurity aur general computing mein **"Banner"** term ke do alag-alag aur bohot important matlab hote hain. Is note mein hum dono meanings ko detail mein aur practical examples ke saath samjhenge.

---

## 1. Real-World Analogy: Shop Signboard (Dukan ka Board)

Maan lijiye aap market mein kisi dukan ke paas khade hain:
* **The Welcome Sign (Console Banner):** Dukan ke main gate par laga bada "WELCOME" board jo dukan ke andar aane par dikhta hai. Iska kaam sirf branding aur visual lagna hai.
* **The Info Board (Service Banner):** Counter par laga ek board jis par likha hai: *"Subway Restaurant, Outlet Version 4.2. Manager: Ramesh."*
  * **Hacker's perspective:** Is info board ko padh kar koi bhi chor ya customer bina kisi se puche samajh sakta hai ki yeh dukan kaun se brand ki hai, iska version kya hai, aur ise kaun handle kar raha hai.
  * **Banner Grabbing:** Uss info board ko chupke se padhne ki process ko hi cyber security mein **"Banner Grabbing"** kehte hain.

---

## 2. Meaning 1: Console / Application Banner (Branding)

Jab aap koi command-line application (jaise Metasploit, Nmap ya Sqlmap) start karte hain, toh shuruat mein jo bada ASCII graphics text ya welcome layout dikhta hai, use **Console Banner** kehte hain.
* Iska target system ko hack karne se koi lena-dena nahi hota. Yeh sirf look-and-feel ke liye hota hai.

### Practical Msfconsole Command:
`msfconsole` ke andar aap jitni baar niche di gayi command likh kar enter karoge, har baar ek naya ASCII art banner screen par badal kar aayega:
```text
msf6 > banner
```

---

## 3. Meaning 2: Service Banner (The Recon Concept)

Jab koi network service (jaise Web Server, SSH server, ya FTP server) kisi port par run karti hai, toh woh incoming connections ko accept karte waqt apni identity leak karti hai. Woh jo initial welcome greeting string bhejti hai, use **Service Banner** kehte hain.

* **Real Example of FTP Banner:**
  `220 vsFTPd 2.3.4`
  *(Yahan software ka name 'vsFTPd' aur uski version details '2.3.4' clear pata chal rahi hai).*

---

## 4. Hacking Technique: Banner Grabbing

**Banner Grabbing** reconnaissance (information gathering) ki ek technique hai jisme attacker target ports par connect karke unke service banners read karta hai taaki use software aur exact version pata chal sake.

### Practical Banner Grabbing Methods:

#### Method A: Using Netcat (nc)
Netcat se direct target port par raw connection banakar banner padhna:
```bash
nc -v 192.168.98.129 21
```
*Output:* `220 vsFTPd 2.3.4`

#### Method B: Using Metasploit Auxiliary Scanners
Metasploit ke paas specific banner scanners hote hain:
```text
msf6 > use auxiliary/scanner/ftp/ftp_version
msf6 auxiliary(scanner/ftp/ftp_version) > set RHOSTS 192.168.98.129
msf6 auxiliary(scanner/ftp/ftp_version) > run
```
*Output:* `[*] 192.168.98.129:21 - FTP Banner: '220 vsFTPd 2.3.4'`

#### Method C: Using Telnet
```bash
telnet 192.168.98.129 21
```

---

## 5. Defense: Banner Mutilation (Banner Chupana)

Security point of view se, open services ke actual version numbers leak karna dangerous hai (kyunki hacker ko direct pata chal jata hai ki kaun sa exploit use karna hai). 
* **Remediation:** System administrators servers ke banners ko edit ya spoof kar dete hain. 
* *Example:* SSH config file `/etc/ssh/sshd_config` mein banner parameters custom message (jaise `Debian OpenSSH` ke badle `Access Denied`) par redirect kar diye jaate hain.

---

## 6. Practice Exercises for Banner Grabbing

Perform these exercises on your local Kali Linux lab target (`192.168.98.129`):

1. **Exercise 1 (Console Banner cycle):**  
   `msfconsole` ke andar jaakar 3 baar `banner` command chalao aur check karo ki har baar unique ASCII graphics design kaisa dikh raha hai.

2. **Exercise 2 (FTP version check):**  
   Kali terminal se `nc` (Netcat) ka use karke target ki FTP port `21` ka banner fetch karne ki command chalao aur output copy karo.

3. **Exercise 3 (SSH Banner Grabbing):**  
   Target SSH service (Port 22) par Netcat connect karke check karein ki iska banner kya display ho raha hai. Command aur output likhein.

4. **Exercise 4 (HTTP Banner Grabbing):**  
   Web servers ke HTTP headers ke banner read karne ke liye Metasploit auxiliary scanner module ka path search query se locate karein (Hint: `search scanner/http/http_header`).

5. **Exercise 5 (SMTP Banner Scan):**  
   SMTP mail server (Port 25) par Netcat scan run karke verification output report karein.

6. **Exercise 6 (Nmap vs Netcat):**  
   Nmap scan query `nmap -sV -p 21 <target>` aur Netcat banner grabbing command mein data detail (information amount) ka main differences explain karein.

7. **Exercise 7 (Apache banner obfuscation):**  
   Windows ya Linux web servers (Apache/Nginx) par servers ke signature headers (banners) ko disable ya off karne ke liye web configuration file mein kis property setting ka use kiya jata hai? (Hint: check `ServerTokens Prod` configuration parameter).

8. **Exercise 8 (Identify Ports):**  
   Scan results ke database `services` command chala kar check karein ki kya target services banners database ports details mein store ho gaye hain ya nahi.
