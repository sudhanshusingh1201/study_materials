# Topic 15 - IP Parameters in Metasploit (RHOSTS, LHOST, SRVHOST)

Metasploit modules ko configure karte waqt alag-alag IP variables (jaise `RHOSTS`, `LHOST`, `SRVHOST`) set karne padte hain. Yeh samajhna bohot zaroori hai ki kis parameter mein kis machine (Kali Linux ya Metasploitable 2) ki IP daalni hai.

---

## 1. Quick Reference Cheat-Sheet

| Parameter | Meaning | Whose IP? (Kiski IP?) | Description |
| :--- | :--- | :--- | :--- |
| **`RHOSTS`** | Remote Host(s) | **Metasploitable 2** (Target) | Jis system par hum attack ya scan kar rahe hain. |
| **`LHOST`** | Local Host | **Kali Linux** (Attacker) | Attack/exploit hone ke baad reverse connection receive karne ke liye Kali ki IP. |
| **`SRVHOST`** | Server Host | **Kali Linux** (Attacker) or **`0.0.0.0`** | Agar Kali ko ek temporary server (like web server) banana ho, toh Kali ki listening interface. |

---

## 2. Detailed Explanation (With Logic)

### A. RHOSTS (Remote Hosts / Target IP)
* **Logic:** "R" stands for **Remote** (jo humse door hai, yaani victim).
* **Kyun?** Metasploit ko batana padta hai ki scan packets ya attack payloads kis machine par send karne hain.
* **Example Setting:**
  ```text
  set RHOSTS 192.168.98.129
  ```
  *(Here `192.168.98.129` is the Metasploitable 2 IP).*

### B. LHOST (Local Host / Attacker IP)
* **Logic:** "L" stands for **Local** (humara apna system, yaani Kali Linux).
* **Kyun?** Reverse shell payloads target machine ke andar chalne ke baad wapas attacker ko contact karte hain. Target ko batane ke liye ki use wapas kis system (Kali) par connect karna hai, hum `LHOST` use karte hain.
* **Example Setting:**
  ```text
  set LHOST 192.168.98.128
  ```
  *(Here `192.168.98.128` is the Kali Linux IP).*

### C. SRVHOST (Server Host / Listening IP)
* **Logic:** "SRV" stands for **Server**. Yeh tab use hota hai jab Kali ko ek server banana ho (e.g. browser exploit web page host karna).
* **Kyun?** Kyunki server Kali Linux par hi chalega, isliye yeh IP Kali ki local IP honi chahiye. Agar aap isme target (Metasploitable) ki IP daaloge, toh system `BindFailed` error dega (kyunki local machine doosri machine ke IP par listen nahi kar sakti).
* **Pro-Tip:** Ise humesha `0.0.0.0` (all local interfaces) par set rakhein, isse connection network errors nahi aate.
* **Example Setting:**
  ```text
  set SRVHOST 0.0.0.0
  ```

---

## 3. Practice Exercises

1. **Exercise 1 (Reverse TCP Concept):**  
   Agar aap windows target par reverse tcp exploit set kar rahe hain, toh target settings mein `LHOST` variable par Kali Linux ki IP set kyun ki jati hai? Logically explain karein.

2. **Exercise 2 (Identify Parameters):**  
   Browser exploit run karte waqt `SRVPORT` kya represent karta hai? (Attacker port ya victim port?).
