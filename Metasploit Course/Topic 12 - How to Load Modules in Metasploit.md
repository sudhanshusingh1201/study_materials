# Topic 12 - How to Load Modules in Metasploit

Metasploit mein kisi exploit, scanner, ya auxiliary module par kaam karne ke liye use active memory execution workspace mein load karna padta hai. Is note mein hum loaded states, loading command syntax, index selection, aur custom module loading ko detail mein aur practical examples ke saath samjhenge.

---

## 1. Real-World Analogy: Retro Video Game Console (Sega/NES)

Maan lijiye aapke paas ek purana video game console (jaise Sega ya Mario Console) hai aur aapke paas 50 alag-alag games ki cassettes (cartridges) hain:
* **The Library:** Saari cassettes rack mein rakhi hain. Jab tak woh rack mein hain, aap unhe play nahi kar sakte.
* **Loading the Game (Load Module):** Aap rack se ek specific game (e.g. "Contra") uthate hain, use console ke slot mein dalte hain aur power switch dabate hain. Ab aap us game ke environment mein hain aur use configure/play kar sakte hain.
* **Unloading/Switching (Exit Module):** Agar aapko doosra game (e.g. "Mario") khelna hai, toh aapko pehle use slot se nikalna hoga aur doosra dalna hoga.
* **Metasploit modules bhi bilkul isi tarah kaam karte hain.** Metasploit library se module ko active slot mein lagane ki process ko hi "Loading a Module" kehte hain.

---

## 2. Methods of Loading Modules inside Msfconsole

Metasploit console mein modules load karne ke teen main methods hain:

### Method A: Direct Module Path selection (`use <path>`)
Agar aapko module ka exact path pata hai:
```text
msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
```
*Output prompt change ho jayega:*
```text
msf6 exploit(unix/ftp/vsftpd_234_backdoor) >
```
*(Iska matlab module active slot mein load ho chuka hai).*

### Method B: Loading via Search Index Numbers (Sabsay Fast!)
Agar aapne koi keyword search kiya hai:
```text
msf6 > search vsftpd
```
*Search results check karein:*
```text
#   Name                                         Disclosure Date  Rank       Check  Description
-   ----                                         ---------------  ----       -----  -----------
0   exploit/unix/ftp/vsftpd_234_backdoor         2011-07-03       excellent  No     vsftpd v2.3.4 Backdoor...
```
Aapko poora lamba path type karne ki zaroorat nahi hai. Aap direct serial index number se load kar sakte hain:
```text
msf6 > use 0
```
*(Yeh index check karke module automatically load kar dega).*

### Method C: Loading Custom Third-Party Modules
Agar aapne internet se koi custom ruby module download kiya hai aur use custom path (`~/.msf4/modules/exploits/custom/my_exploit.rb`) par rakha hai:
1. Console ko check karne ke liye batayein ki database reload ho jaye:
   ```text
   msf6 > reload_all
   ```
   *(Yeh command saare paths ko rescan karegi aur naye custom modules ko console memory mein load kar degi).*
2. Naye custom module ko select karein:
   ```text
   msf6 > use exploit/custom/my_exploit
   ```

---

## 3. How to Unload / Switch Modules

* **Dooosra Module Load karna:** Agar aap already ek module ke andar hain aur doosra module load karna chahte hain, toh aapko pehle waale ko close karne ki zaroorat nahi hai. Direct `use <new-module>` type karein, purana automatically unload ho jayega.
* **Main Prompt par wapas jaana:** Loaded context se exit karne ke liye:
   ```text
   msf6 exploit(...) > back
   ```
   *(Aapka prompt wapas normal `msf6 >` par aa jayega).*

---

## 4. Practical: Navigation Walkthrough

Apne terminal/msfconsole par jaakar in commands ko chala kar verify karein:

1. **Search module:**
   ```text
   msf6 > search eternalblue
   ```
2. **Index number se load karein (jo serial number ho, e.g. 1):**
   ```text
   msf6 > use 1
   ```
3. **Verify verify check options:**
   ```text
   msf6 exploit(windows/smb/ms17_010_eternalblue) > show options
   ```
4. **Peeche wapas normal workspace par aane ke liye:**
   ```text
   msf6 exploit(...) > back
   ```

---

## 5. Practice Exercises for Loading Modules

1. **Exercise 1 (Index Loading):**  
   `search auxiliary/scanner/portscan` run karein aur filter parameters check karke serial index number list check karein. Kisi ek index list ko use karke load karein.

2. **Exercise 2 (Unload Verification):**  
   Ek exploit load karein. `back` command run karke check karein ki prompt variable output kaisa display ho raha hai.

3. **Exercise 3 (Direct Loading):**  
   SSH login testing module `auxiliary/scanner/ssh/ssh_login` ko direct path syntax se load karne ka command execute karein.

4. **Exercise 4 (Check reload function):**  
   Console database module database reset rescan karne ke liye active refresh commands type `reload_all` verify check parameters ko check karein.

5. **Exercise 5 (Verify payload loading):**  
   Exploit select load hone par active payload load karne ke parameters aur automatic checks settings identify karein.

6. **Exercise 6 (Switching Context):**  
   Load check exploit target `vsftpd_234_backdoor` ke active contextual area se direct normal auxiliary/scanner loading context switch karne ke commands write karein.

7. **Exercise 7 (Verify loaded path error):**  
   Agar aapne galat path type kiya `use exploit/wrong_path`, toh Metasploit error terminal messages kya show karta hai?

8. **Exercise 8 (Verify status loaded stats):**  
   Naye modules database reload function check status verification check parameters write check list karein.
