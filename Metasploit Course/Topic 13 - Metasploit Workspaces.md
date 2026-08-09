# Topic 13 - Metasploit Workspaces

Metasploit database connect hone ke baad saara scan data aur credentials automatically store hote rehte hain. Lekin agar aap ek saath multiple companies ya target networks par pentesting kar rahe ho, toh unka data aapas mein mix na ho, iske liye **Workspaces** use kiya jata hai.

Is note mein hum Workspaces ke concept, basic commands, aur multiple projects manage karne ke practical flow ko details mein samjhenge.

---

## 1. Real-World Analogy: Project Filing Cabinets (Daftar ki Files)

Maan lijiye aap ek freelance cybersecurity auditor hain aur aapko ek hi hafte mein teen alag-alag companies ka assessment karna hai:
* **Miscalibrated Organization:** Aap sabhi companies ke network scans, server IPs, aur churae gaye passwords ko ek hi bade box mein throw kar dete hain. Jab report likhne ki baari aayegi, toh aap confuse ho jayenge ki kaun si port kis company ki thi, jis-se report kharab ho sakti hai.
* **The Filing Cabinet (Workspaces):** Aap apne desk par teen alag files banate hain—`Company_A`, `Company_B`, aur `Company_C`. 
  * Jab aap `Company_A` file kholenge, toh usme sirf usi company ka data milega. 
  * `Company_B` par switch karte hi `Company_A` ka data hide ho jayega aur sirf `Company_B` ki details samne aayengi.
* **Metasploit Workspaces wahi filing cabinets hain.**

---

## 2. Default Workspace State

Jab aap pehli baar `msfdb run` chalate hain, toh Metasploit automatically ek workspace select karta hai jiska naam hota hai **`default`**.
* Jo bhi scans ya actions aap default settings ke sath chalayenge, woh isi workspace mein save honge.
* Active workspace ke aage humesha ek asterisk **`*`** mark laga hota hai.

---

## 3. Core Workspace Commands (Cheat-sheet)

Msfconsole prompt par in commands ka use karke workspaces ko manage karein:

| Command | Action (Kya kaam karta hai) | Example |
| :--- | :--- | :--- |
| **`workspace`** | Available workspaces ki list check karna aur active workspace dekhna. | `workspace` |
| **`workspace -a`** | Ek naya custom workspace create/add karna. | `workspace -a company_alpha` |
| **`workspace <name>`** | Kisi doosre workspace par switch karna. | `workspace company_alpha` |
| **`workspace -d`** | Kisi workspace aur uske andar ke pure database entries ko delete karna. | `workspace -d company_alpha` |
| **`workspace -r`** | Existing workspace ko rename karna. | `workspace -r old_name new_name` |
| **`workspace -h`** | Workspaces ke advanced flags aur options dekhna. | `workspace -h` |

---

## 4. Practical: Isolating Target Scans

Chalo ek real target data isolation scan process execute karke verify karte hain:

1. **Msfdb console launch karein:** `sudo msfdb run`
2. **Current active workspace check karein:**
   ```text
   msf6 > workspace
   ```
   *(Output: `* default`)*
3. **Naya workspace banayein:**
   ```text
   msf6 > workspace -a lab_practice
   ```
4. **Naye workspace par switch karein:**
   ```text
   msf6 > workspace lab_practice
   ```
   *(Ab active workspace `* lab_practice` ho gaya hai).*
5. **Target scan run karein (NAT IP range check ke saath):**
   ```text
   msf6 > db_nmap -sV 192.168.98.129
   ```
6. **Hosts verify karein:**
   ```text
   msf6 > hosts
   ```
   *(Yahan aapko target machine ki IP `192.168.98.129` display hogi).*
7. **Wapas default workspace par switch karein:**
   ```text
   msf6 > workspace default
   ```
8. **Check default hosts list:**
   ```text
   msf6 > hosts
   ```
   *(Aapko hosts empty dikhegi! Kyunki target scan data humne `lab_practice` file ke locker mein save kiya tha, default mein nahi).*

---

## 5. Practice Exercises for Workspaces Mastery

Perform these tasks on your local Kali system:

1. **Exercise 1 (Workspace Listing):**  
   Msfconsole ke andar `workspace` run karke default active database status note karein.

2. **Exercise 2 (Create Workspace):**  
   Naya workspace `internal_audit` create karne aur usme switch karne ka command line syntax likhein.

3. **Exercise 3 (Rename Workspace):**  
   Existing workspace `internal_audit` ko rename karke `dmz_network` karne ka command verify karein.

4. **Exercise 4 (Data Check after switch):**  
   Naye workspace par switch karne ke baad `hosts` ya `services` type karne par framework database kya return karta hai agar koi scan run na kiya gaya ho?

5. **Exercise 5 (Delete Workspace):**  
   Kaam complete hone par workspace `dmz_network` aur uske scan records ko permanent delete karne ke steps batayein.

6. **Exercise 6 (Workspace Help documentation):**  
   `workspace -h` chala kar check karein ki workspace configurations check karne ke flags and switches list kya-kya hain.

7. **Exercise 7 (Switch back logic):**  
   Custom workspaces se exit karke wapas primary core database space par aane ke default commands verification steps write karein.

8. **Exercise 8 (Verify databases status):**  
   Check karein ki workspaces delete karne par system PostgreSQL databases parameters file clean hoti hai ya internal references remove hote hain.
