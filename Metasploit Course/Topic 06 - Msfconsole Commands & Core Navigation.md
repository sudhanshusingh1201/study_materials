# Topic 06 - Msfconsole Commands & Core Navigation

Metasploit Console (`msfconsole`) hi humara main workspace hai. Is note mein hum msfconsole ke andar use hone waale sabse zaroori aur important commands ko detail mein, practical usage ke saath samjhenge.

---

## 1. Core msfconsole Commands (Cheat-sheet with Examples)

| Command | Usage / Description | Example |
| :--- | :--- | :--- |
| **`search`** | Modules ko keyword ya filters ke saath search karna. | `search platform:windows rank:excellent` |
| **`use`** | Kisi specific module ko select karke load karna. | `use exploit/unix/ftp/vsftpd_234_backdoor` |
| **`info`** | Loaded module ki details (CVE, Author, Description) dekhna. | `info` *(module use karne ke baad)* |
| **`show`** | Options, Payloads, Targets ya Advanced variables dekhna. | `show options` / `show payloads` |
| **`set`** | Kisi option ki local value set karna. | `set RHOSTS 192.168.98.129` |
| **`setg`** | Kisi option ki value **globally** set karna (baar-baar set nahi karna padega). | `setg RHOSTS 192.168.98.129` |
| **`unset`** | Local variables ko clear/reset karna. | `unset RHOSTS` |
| **`back`** | Module se bahar aakar normal prompt par aana. | `back` |
| **`exploit` / `run`** | Exploit ya Scanner module ko execute karna. | `exploit` (exploits ke liye) / `run` (auxiliary ke liye) |
| **`jobs`** | Background mein chal rahe scripts/listeners ko check karna. | `jobs -l` / `jobs -k <job-id>` *(kill job)* |
| **`sessions`** | Open shells/Meterpreter connections ko control karna. | `sessions -l` *(list)* / `sessions -i 1` *(interact)* |

---

## 2. Advanced Navigation Techniques (Mastery Level)

### A. Searching like a Pro (`search`)
Search command ke andar filters use karne se hume specific aur safe exploits milte hain:
* **Platform Filter:** `search platform:linux type:exploit`
* **Name & Rank Filter:** `search name:smb rank:excellent`
* **CVE Filter:** `search cve:2020`

### B. Global Variables (`setg`)
Agar aap pure session mein ek hi target test kar rahe ho, toh har module mein alag se target IP set karne ki zaroorat nahi hai.
* Type: `setg RHOSTS 192.168.98.129`
* Iske baad aap jo bhi exploit ya scanner use karoge, `RHOSTS` automatically set rahega.
* *Note: Globally save config dekhne ke liye `show options` karein.*

### C. Active Session Management (`sessions`)
Jab target machine exploit ho jati hai, toh connection background mein chala jata hai ya active shell open ho jata hai:
* **Background session send karna:** Exploit shell ke andar `Ctrl + Z` press karke `y` enter karein.
* **Sessions list check karna:**
  ```text
  msf6 > sessions -l
  ```
* **Wapas session mein interact karna:**
  ```text
  msf6 > sessions -i 1
  ```
  *(1 session ID hai jo list se pata chalti hai).*

---

## 3. Practical Exercises

### Exercise 1: Session Management Practical
Hum seekhenge ki bina actual hack ke ek test connection (Session) kaise create aur manage karte hain:

1. **Msfconsole open karein:** `sudo msfdb run`
2. **Listener (multi/handler) load karein:**
   ```text
   msf6 > use exploit/multi/handler
   ```
3. **Payload configure karein:**
   ```text
   msf6 exploit(multi/handler) > set PAYLOAD generic/shell_reverse_tcp
   ```
4. **Local Host/IP check karke set karein:**
   ```text
   msf6 exploit(multi/handler) > set LHOST 192.168.98.128
   msf6 exploit(multi/handler) > set LPORT 4444
   ```
5. **Background job ke roop mein run karein (Listen mode):**
   ```text
   msf6 exploit(multi/handler) > run -j
   ```
   *(Yahan `-j` run command ko background job bana deta hai).*
6. **Job check karein:**
   ```text
   msf6 exploit(multi/handler) > jobs -l
   ```
   *(Aapko 4444 port par chal raha listener active job dikhega).*
7. **Job kill karein:**
   ```text
   msf6 exploit(multi/handler) > jobs -k 0
   ```
   *(Jo job sequence ID ho, use kill kar dein).*
