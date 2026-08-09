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

## 5. Practice Exercises

1. **Exercise 1 (Session Backgrounding):**
   `exploit/multi/handler` ko use karke check karein aur use background job (`-j`) ki tarah start karein. `jobs` command ka output verify karke batayein.

2. **Exercise 2 (Database Filtering):**
   Apne lab target scan hone ke baad msfconsole mein sirf port 21 (FTP) aur port 22 (SSH) ke services filter karke dekhne ka command likhein.
