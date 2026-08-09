# Topic 06 - Msfconsole Commands and Core Navigation

Metasploit Console (`msfconsole`) hi humara main terminal workspace hai jahan se saare exploits, payloads, aur tools control hote hain. Is note mein hum msfconsole ke essential commands, active session management, aur database commands ko details mein samjhenge.

---

## 1. Real-World Analogy: Msfconsole Kya Hai?

Maan lijiye aap ek modern spaceship ke captain hain:
* **The Cockpit Dashboard:** Space control panel par bohot saare switch aur screens hain. Aap yahin se targets (planets/asteroids) lock karte hain, scan sensors chalate hain, weapons load karte hain, aur live drones ko direct commands dete hain.
* **Msfconsole wahi spaceship cockpit hai.** Aap yahin se vulnerable targets lock karte hain (`set RHOSTS`), scanner launch karte hain (`run`), payload drop karte hain (`exploit`), aur targets ke shells ko background/foreground mein control karte hain (`sessions`).

---

## 2. Core Navigation & Workspace Commands

| Command | Purpose (Kya kaam karta hai) | Practical Example |
| :--- | :--- | :--- |
| **`use`** | Kisi specific category ya module ko load karna. | `use exploit/multi/handler` |
| **`back`** | Loaded module se exit karke main directory path par aana. | `back` |
| **`info`** | Module ki compatibility, options, description aur references dekhna. | `info` *(loaded module mein)* |
| **`show options`** | Module ko chalane ke liye required settings dekhna. | `show options` |
| **`show advanced`**| Hidden advanced settings (timeouts, bypasses, checks) dekhna. | `show advanced` |
| **`set` / `setg`** | Single target ke liye local variable set karna (`set`) ya global variable set karna (`setg`). | `set RHOSTS 192.168.98.129` |
| **`unset`** | Local variables ko clear/reset karna. | `unset RHOSTS` |
| **`run` / `exploit`** | Auxiliaries ko chalane ke liye `run`, aur exploits chalane ke liye `exploit` command use hoti hai. | `exploit` |

---

## 3. Session & Background Job Control (Advanced Navigation)

Jab hum reverse shell ya background tasks run karte hain, tab in commands ka use hota hai:

### A. Jobs (Background Tasks)
Agar aapko koi service scan ya listener background mein bina terminal hold kiye chalana hai, toh `-j` flag lagaya jata hai:
* **Run in background:**
  ```text
  msf6 exploit(multi/handler) > exploit -j
  ```
* **Active jobs check karna:**
  ```text
  msf6 > jobs -l
  ```
* **Specific job kill karna:**
  ```text
  msf6 > jobs -k 0
  ```

### B. Session Management
Exploitation successful hone par active systems ko control karne ke liye `sessions` command use hoti hai:
* **Shell ko background bhejna (without closing it):**
  Terminal shell ke andar `Ctrl + Z` press karein, phir `y` enter karein.
* **Saare active sessions ki list dekhna:**
  ```text
  msf6 > sessions -l
  ```
* **Kisi session ke andar interact/wapas enter karna:**
  ```text
  msf6 > sessions -i 1
  ```
  *(1 session database sequence id hai).*
* **Shell session ko Meterpreter mein upgrade karna:**
  ```text
  msf6 > sessions -u 1
  ```

---

## 4. Database Commands inside msfconsole

Kyunki humara database connected hai (`db_status`), hum in commands ka use scan data retrieve karne ke liye kar sakte hain:

* **`hosts`:** Database mein scanned jitne bhi targets save hain unki IP aur OS details dikhata hai.
* **`services`:** Target IP ke open ports aur versions display karta hai. Filter: `services -p 80` (sirf port 80 check karna).
* **`creds`:** Target scan ya exploitation se churae gaye usernames/passwords credentials ki database list.
* **`vulns`:** Verified vulnerable ports jo target par scan ke dauran confirmed mili hain unki list.

---

## 5. Practice Exercises for Console Mastery

Perform these tasks on your Kali Linux terminal and `msfconsole` to gain muscle memory and command proficiency:

1. **Exercise 1 (Job Management):**  
   `exploit/multi/handler` module ko loaded karein. Is listener ko background job (`-j`) ki tarah port `5555` aur generic reverse shell payload ke saath run karein. `jobs -l` command chala kar confirmation output screenshot/text verify karein.

2. **Exercise 2 (Database Service Queries):**  
   Database commands ka use karke sirf target ports `22` (SSH) aur `445` (SMB) ke hosts aur details filter karne ki command likhein.

3. **Exercise 3 (Module Info Inspection):**  
   Exploit module `exploit/windows/smb/ms17_010_eternalblue` load karein aur `info` run karein. Is exploit ki reliability (Rank) kya hai aur isme details mein kaun si dynamic dependency library ka mention kiya gaya hai?

4. **Exercise 4 (Global Variable Propagation):**  
   `setg LPORT 9999` chala kar use globally set karein. `use auxiliary/scanner/portscan/tcp` command se new category explore karein aur options check karein ki kya LPORT automatically update hua hai.

5. **Exercise 5 (Interactive Session Control):**  
   Maan lijiye aapke paas 3 active background sessions chal rahe hain. Session number `2` ke shell mein enter karne ke liye aur phir wahan se bina disconnect hue shell ko background bhejne ke liye commands ka sequence batayein.

6. **Exercise 6 (Upgrading Sessions):**  
   Session number `1` par chal rahe aam unix command shell ko Meterpreter shell ke roop mein upgrade/promote karne ka command verify karein.

7. **Exercise 7 (Advanced Parameter View):**  
   `use exploit/unix/ftp/vsftpd_234_backdoor` select karein. Is exploit ke underlying standard timeout configurations ko dekhne ke liye kis command ka use karenge?

8. **Exercise 8 (Session Termination):**  
   Kaam khatam hone par saare background running sessions ko ek baar mein terminate/kill karne ke liye kis command ka check chalate hain?
