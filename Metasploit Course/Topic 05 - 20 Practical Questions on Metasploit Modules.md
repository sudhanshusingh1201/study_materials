# Topic 05 - 20 Practical Questions on Metasploit Modules

Yeh practice sheet aapke Metasploit modules ke practical concepts ko check aur strong karne ke liye design ki gayi hai. Apne Kali Linux terminal aur `msfconsole` par in tasks ko perform karein aur inke answers note karein.

---

## Part 1: Module Searching & Metadata Checks (Q1 - Q4)

1. **Question 1 (Exploit File Path):**  
   Kali Linux terminal (not msfconsole) ka use karke famous Windows exploit **EternalBlue (ms17_010)** ki `.rb` file ka absolute directory path dhoondo.

2. **Question 2 (HTTP Scanners Search):**  
   `msfconsole` ke andar ek aisi search query chalao jo sirf **Auxiliary** category ke modules dikhaye jo **HTTP** protocol scan karte hain. (Hint: Use `type:` and `name:` filters).

3. **Question 3 (CVE ID Verification):**  
   Vulnerability **BlueKeep (CVE-2019-0708)** ke exploit module ka path aur uski Rank (Excellent, Great, Good, etc.) find karo.

4. **Question 4 (Author Filter):**  
   Metasploit ke creator **"hdmoore"** dwara likhe gaye saare modules dhoondne ke liye search query chalao. Unke likhe exploits ka rank kya hai?

---

## Part 2: Module Loading & Configuration (Q5 - Q8)

5. **Question 5 (Info Command):**  
   Module `exploit/unix/ftp/vsftpd_234_backdoor` ko select karo. **`info`** command chala kar check karo ki yeh kis network port par attack karta hai aur iski disclosure date kya thi.

6. **Question 6 (Local vs Global Variables):**  
   `use` command se ek exploit load karo aur `set RHOSTS 192.168.98.129` chalao. Ab `back` command se peeche jao aur doosra module load karo. Kya RHOSTS ab bhi set hai? Kyun?

7. **Question 7 (Global Variable Configuration):**  
   Metasploit mein **`setg`** command ka use karke target IP `192.168.98.129` ko globally set karo. Kisi doosre module ko load karke check karo ki kya value automatically apply ho gayi hai.

8. **Question 8 (Unset Variables):**  
   Globally set kiye gaye RHOSTS ko reset karne ke liye kaun si command run karenge?

---

## Part 3: Payload Selection & Verification (Q9 - Q11)

9. **Question 9 (Compatible Payloads):**  
   Module `exploit/windows/smb/ms17_010_eternalblue` ko select karne ke baad **`show payloads`** chalao. Is exploit ke sath compatible kitne payloads display ho rahe hain?

10. **Question 10 (Payload Types):**  
    Upar ki compatible list mein se koi ek **Single/Inline** payload aur koi ek **Staged** payload identify karke unka difference batayein (naming convention se).

11. **Question 11 (Payload Options):**  
    Staged payload `windows/x64/meterpreter/reverse_tcp` select karein aur `show options` run karein. Is payload ko work karne ke liye `RHOSTS` ke alawa kaun se do settings (LHOST/LPORT) mandatory hain?

---

## Part 4: Auxiliary Scanners (Q12 - Q15)

12. **Question 12 (SMB Version Scan):**  
    Target machine ka SMB protocol version detect karne ke liye kaun sa auxiliary module use kiya jata hai? Path dhoondo.

13. **Question 13 (Port Scanner Threading):**  
    `auxiliary/scanner/portscan/tcp` scanner select karein. Iske options mein `THREADS` parameter ka default count kya hai, aur thread badhane se scanner ki performance par kya impact padega?

14. **Question 14 (FTP Anonymous Login):**  
    Target server par checks lagane ke liye ki kya Anonymous FTP login allow hai, kaun sa auxiliary scanner script use hota hai?

15. **Question 15 (SSH Brute Force Helper):**  
    SSH service par username/password brute force scan chalane ke liye auxiliary scanner module search karke select karo.

---

## Part 5: Advanced Modules & Database (Q16 - Q20)

16. **Question 16 (Post-Exploitation Search):**  
    Windows system se logs clear karne ke liye kaun se **Post-Exploitation** modules available hain? (Hint: search command filter `platform:windows type:post`).

17. **Question 17 (Encoders List):**  
    Metasploit mein saare available **encoders** ki list dekhne ke liye kaun sa command execute karenge?

18. **Question 18 (Evasion Modules Check):**  
    Windows Defender ko bypass karne ke liye design kiya gaya evasion module select karke check karein. Iska target file extension kya hota hai?

19. **Question 19 (Database Troubleshooting):**  
    Agar database initialized hai par connected nahi hai, toh use configure karne ki database script files user directory (`~/.msf4`) mein kis naam se saved rehti hai?

20. **Question 20 (Integrate db_nmap):**  
    `db_nmap -p 80 <Target-IP>` command run karein. Iske baad database se check karne ke liye ki port 80 open mili ya nahi, msfconsole ke andar kaun sa single-word command execute karenge?
