# Topic 03 - Metasploit File System and Directories

Metasploit Framework ka file system iske dynamic nature ko control karta hai. Is note mein hum dekhenge ki Metasploit ka actual system code aur configuration folders Kali Linux mein kahan store hote hain.

---

## 1. Real-World Analogy: Metasploit File System Kya Hai?

Maan lijiye aap ek bade warehouse/factory ke manager hain:
* **The Main Vault (System Files):** Ek specific area jahan machinery, default blueprints, aur tools safe rakhe hain jo saare workers share karte hain. Ise change karna normal workers ke liye forbidden hai (Kyunki engine kharab ho sakta hai).
* **Worker's Personal Locker (User Files):** Har worker ka apna personal space jahan woh apna lunchbox, personal diaries, aur custom customized tools rakhta hai jo sirf use chahiye.
* **Metasploit File System:**
  * **Main Vault:** `/usr/share/metasploit-framework/` (Core files).
  * **Personal Locker:** `~/.msf4/` (User files & configurations).

---

## 2. The Main Vault: `/usr/share/metasploit-framework/`

Apne Kali terminal par is path par jaane ke liye command run karein:
`cd /usr/share/metasploit-framework/ && ls -l`

Yahan jo main folders hain, unki system logic niche hai:

### A. `modules/` (Sabse Important)
Iske andar saara executable hacking code hota hai jo dynamic categories mein split hota hai:
* `exploits/`: Vulnerabilities ko compromise karne waale main programs (divided by target platform: windows, linux, android).
* `payloads/`: Hack ke baad target par chalne waale shells ya meterpreters.
* `auxiliary/`: Security scanning, brute-forcing, aur fingerprinting scripts.
* `post/`: Access milne ke baad target ke andar information gather karne wale tools.
* `encoders/`: AV (Anti-virus) bypass karne ke liye algorithms (e.g. `shikata_ga_nai`).
* `evasion/`: Raw binaries generate karne ke bypass modules.

### B. `lib/`
Yeh engine ka dil hai. Metasploit Framework ka **Core Ruby Language libraries** code isi folder mein store hota hai. Yahan framework API design aur base features define kiye gaye hain.

### C. `tools/`
Hacking utilities aur tools jo standalone terminal scripts ki tarah run ho sakte hain:
* *Example:* **`pattern_create.rb`** (Buffer overflow vulnerability test karte waqt random unique pattern generate karne ke liye).

### D. `data/`
Yahan templates, resource scripts, aur custom settings stored hoti hain. Jaise android apk payload template, custom wordlists, aur meterpreter client binaries.

### E. `plugins/`
Extensions jo Metasploit ke launch behavior ko load time par mod karti hain (e.g. database controllers, connection helpers).

---

## 3. Worker's Personal Locker: `~/.msf4/` (Hidden Space)

Home path ke andar ek hidden directory hoti hai jo user configurations aur custom modules manage karti hai:
* **Path:** `/home/kali/.msf4/` (Normal user) ya `~/.msf4/` (Root user).

### Key Files in `~/.msf4/`:
1. **`history`:** `msfconsole` shell ke andar aapne jo bhi commands likhi thin, unka backup isi file mein save hota hai.
2. **`logs/`:** Debugging logs (agar Metasploit crash hota hai toh checks yahan hote hain).
3. **`modules/`:** Agar aapne GitHub se koi naya third-party ruby exploit code download kiya hai, toh use is folder mein copy karein:
   * **Path:** `~/.msf4/modules/exploits/custom/my_exploit.rb`
   * *Fayda:* Metasploit framework update hone par aapka custom code delete nahi hoga!

---

## 4. Practical Terminal Exploration

Apne Kali terminal par yeh commands execute karke manual checks karke system ko samjhein:

### Exercise 1: Exploring SMB Exploit Path
Windows SMB modules ko investigate karne ke liye check karein:
```bash
ls -lh /usr/share/metasploit-framework/modules/exploits/windows/smb/
```
*(Aapko yahan `ms17_010_eternalblue.rb` aur doosre files dikhai denge).*

### Exercise 2: Viewing Module Code
Metasploit ke exploits regular text base Ruby (.rb) scripts hoti hain. Aap unhe read kar sakte hain:
```bash
cat /usr/share/metasploit-framework/modules/exploits/windows/smb/ms17_010_eternalblue.rb | grep "Name" -A 5
```
*(Yeh command Eternalblue exploit code ke framework info block ko read karegi).*

---

## 5. Practice Exercises for File System Mastery

1. **Exercise 1 (Custom Module Directory):**
   Maan lijiye aapne GitHub se ek naya exploit script `hack_tool.rb` download kiya. Ise bina default systems ko touch kiye kis directory path par place karenge taaki msfconsole use load kar sake?

2. **Exercise 2 (Tool Verification):**
   `/usr/share/metasploit-framework/tools/` directory ke andar jaakar check karein ki kaun-kaun si helper ruby scripts available hain. Kisi bhi ek script ka name aur use batayein.
