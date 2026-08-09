# Topic 04 - Metasploit File System & Directories

Metasploit ka actual filesystem samajhna un logo ke liye bohot zaroori hai jo isme **Mastery** chahte hain. Is note mein hum dekhenge ki Metasploit ka raw code, tools, aur modules Kali Linux mein kahan store hote hain aur inka directory structure kya hai.

---

## 1. System Directory: `/usr/share/metasploit-framework/`

Kali Linux mein Metasploit ka poora system software isi directory ke andar installed hota hai. Is directory ko explore karne ke liye apne Kali terminal par type karein:
`cd /usr/share/metasploit-framework/ && ls -l`

Yahan jo main folders hain, unki detail niche hai:

### A. `modules/` (Sabse Important)
Is folder mein saare active exploits, payloads, auxiliaries, aur encoders hote hain. Yeh niche diye gaye structure mein divided hai:
* `modules/exploits/`: Target systems ko compromise karne ke liye actual exploit scripts.
* `modules/payloads/`: Target ko hack karne ke baad execute hone waale codes (e.g., shell access, meterpreter).
* `modules/auxiliary/`: Scanners, sniffers, fuzzers aur vulnerability testers.
* `modules/encoders/`: Anti-virus detect na kar sake iske liye obfuscation algorithms.
* `modules/post/`: Exploitation ke baad system se sensitive data churaney ke tools.

### B. `tools/` (Helpers)
Is folder mein Metasploit development aur penetration testing ke liye useful scripts hoti hain.
* *Example:* **`pattern_create.rb`** aur **`pattern_offset.rb`** (Buffer Overflow exploit develop karte waqt buffer space calculate karne ke liye).

### C. `data/`
Is folder mein supporting materials hote hain, jaise:
* Exploiting templates (Meterpreter keyloggers, android templates).
* Wordlists (brute-forcing ke liye dictionary files).
* Binaries jo payload generation mein auxiliary files ki tarah use hoti hain.

### D. `lib/`
Yahan Metasploit Framework ka **Core Ruby Engine** code rehta hai. Modules jo APIs call karte hain, unki main logic isi folder ke ruby files mein hoti hai.

### E. `plugins/`
Aisi scripts jo console ke loading behavior ko modify karti hain aur open-source software (jaise OpenVAS, Nessus) ko direct msfconsole se link karti hain.

---

## 2. User Directory: `~/.msf4/` (Hidden Space)

Metasploit run karte waqt, har individual user ke liye home directory mein ek hidden folder ban jata hai.
* **Path:** `/home/kali/.msf4/` (ya fir direct root shell par `~/.msf4/`)

### Yeh kis liye use hota hai?
1. **No Admin Overwrite:** Agar aap `/usr/share/metasploit-framework` mein changes karoge toh update hone par woh delete ho jayenge. Lekin `~/.msf4` ke data ko updates delete nahi karte.
2. **Custom Modules:** Agar aapne GitHub se koi naya exploit download kiya hai ya apna khud ka exploit script likha hai, toh aap use yahan save kar sakte hain:
   * **Path:** `~/.msf4/modules/exploits/custom_exploit.rb`
3. **Database Config:** database connect karne ke credentials `database.yml` file mein save hote hain jo isi folder mein hoti hai.
4. **History:** Msfconsole mein likhi gayi commands ki history `~/.msf4/history` file mein save hoti hai.

---

## 3. Practical Exercises (Mastery Level)

Apne Kali Linux terminal par in tasks ko perform karein aur unke results observe karein:

### Exercise 1: Finding Exploit Codes
Hum terminal se direct explore karenge ki exploits kahan par hain:
1. Directory change karein:
   ```bash
   cd /usr/share/metasploit-framework/modules/exploits/
   ```
2. Check karein ki iske andar kitne operating systems ke folders hain:
   ```bash
   ls
   ```
3. Windows ke SMB modules dekhne ke liye is path par jao:
   ```bash
   ls windows/smb/
   ```
   *(Aapko yahan famous exploits jaise `ms17_010_eternalblue.rb` dikhega).*

### Exercise 2: Searching inside Core Files
Agar aapko kisi exploit ka source code dekhna hai, toh aap direct terminal par use read kar sakte ho (Metasploit ke exploits pure Ruby language mein hote hain):
```bash
cat /usr/share/metasploit-framework/modules/exploits/windows/smb/ms17_010_eternalblue.rb | head -n 30
```
*(Is command se aapko exploit ke basic info aur code details screen par dikh jayenge).*

---

## 4. Summary Cheat-Sheet
* **Core Code Location:** `/usr/share/metasploit-framework/`
* **Custom Code/History Location:** `~/.msf4/`
* **Exploit Script Language:** Ruby (`.rb`)
