# Topic 11 - Mastering the Show Command in Metasploit

Msfconsole ke andar **`show`** command sabse versatile aur commonly use hone wali command hai. Yeh context-sensitive command hai, yaani iska behavior is baat par depend karta hai ki aap isko normal prompt par chala rahe ho ya kisi specific module ke andar.

Is note mein hum `show` command ke different filters, scope aur usage ko details mein samjhenge.

---

## 1. Real-World Analogy: E-Commerce App Filters

Maan lijiye aap Amazon ya Flipkart par shopping kar rahe hain:
* **Global Search (Global Show):** Aapne select kiya "Watches". App aapko duniya bhar ki saari watches dikha degi. Yeh bohot badi list hogi jise browse karna mushkil hoga.
* **Context Filter (Local Show):** Ab aapne specific watch (jaise "Casio G-Shock") select kar li aur product page par chale gaye. Wahan aap check karte hain:
  * *"Show colors"* (is model ke colors dekhna).
  * *"Show sizes"* (dial size check karna).
  * *"Show delivery options"* (required parameters check karna).
* **Metasploit ka show command bhi bilkul aise hi filters apply karta hai.** Normal terminal par chaloge toh sab kuch dikhayega, aur loaded module ke andar chaloge toh sirf us module se compatible options dikhayega.

---

## 2. Global Scope: Normal Terminal par `show` (`msf6 >`)

Jab aap bina koi exploit select kiye main menu par `show` chalate hain, toh yeh Metasploit ke pure library database ko print karta hai:

* **`show exploits`:** Framework ke saare exploits ki list. (Warning: Isme thoda waqt lag sakta hai kyunki 2600+ entries scroll hongi).
* **`show auxiliary`:** Saare scan aur helper modules ki list.
* **`show payloads`:** Metasploit mein available saare 2000+ payloads ki list.
* **`show encoders`:** Payloads ko obfuscate/encrypt karne waale tools ki list.
* **`show nops`:** CPU memory registers slide check options.
* **`show evasion`:** Windows Defender bypass techniques build settings.

---

## 3. Local Scope: Module ke Andar `show` (`msf6 exploit(...) >`)

Jab aap kisi specific exploit ko load (`use`) kar lete ho, toh `show` command us module ke context mein chalne lagti hai:

### A. `show options` (Sabse Important)
Loaded module ko run hone ke liye kaun se variables set karne hain unki list dikhata hai.
* *Example:* target IP (`RHOSTS`), local listener IP (`LHOST`), port (`RPORT`), etc.

### B. `show payloads` (Compatible Payloads Only)
Pure library ke payloads nahi dikhata, balki sirf woh payloads dikhata hai jo us loaded exploit ke architecture aur platform ke sath **100% compatible** hain.
* *Example:* Windows exploit ke andar `show payloads` karne par target specific reverse shells aur Meterpreter windows files hi dikhegi, Linux payloads automatic hide ho jayenge.

### C. `show targets` (OS Compatibility)
Vulnerability kis exact Windows/Linux/Android service pack ya kernel version par success rate rakhti hai, unki certification list dikhata hai.
* *Example:* Target 0 for Automatic, Target 1 for Windows 7 SP1, Target 2 for Windows Server 2008.

### D. `show advanced`
Hidden properties jaise proxies settings, retry connections rate, check headers rate, encryption keys details setup parameters list.

---

## 4. Practical: Using Show Filters

Apne `msfconsole` par jaakar is walkthrough ko check karein:

1. **FTP Exploit use karein:**
   ```text
   msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
   ```
2. **Dekhein is exploit ke liye kya-kya settings required hain:**
   ```text
   msf6 exploit(unix/ftp/vsftpd_234_backdoor) > show options
   ```
3. **Is dynamic application ke compatible targets list check karein:**
   ```text
   msf6 exploit(unix/ftp/vsftpd_234_backdoor) > show targets
   ```
   *(Aapko isme compatible OS type and configurations target list dikh jayegi).*

---

## 5. Practice Exercises for Show Command

Perform these exercises on your local Kali console and write the outputs:

1. **Exercise 1 (Global Payload list):**  
   Global console prompt (`msf6 >`) par `show payloads` run karein aur checks note karein ki kitne time mein layout fetch ho raha hai.

2. **Exercise 2 (Target Verification):**  
   Module `use exploit/windows/smb/ms17_010_eternalblue` load karein aur `show targets` run karein. Is exploit mein default target index number `0` par kaun si target OS specifications configuration settings active hai?

3. **Exercise 3 (Compatible Payloads):**  
   Eternalblue exploit module ke andar `show payloads` run karein aur verify karein ki kya linux shell payloads display ho rahe hain? Is behavior ka reason batayein.

4. **Exercise 4 (Show Options Check):**  
   Loaded exploit `exploit/unix/ftp/vsftpd_234_backdoor` mein `show options` run karein aur verify karein ki kya port 21 default set hai?

5. **Exercise 5 (Advanced Settings View):**  
   `show advanced` command run karke check karein ki connection timeout aur validation retry variables default configurations kis standard check values par set hain.

6. **Exercise 6 (Encoder Analysis):**  
   Global prompt par `show encoders` command run karein aur check karein ki list mein rank wise highest excellent rank encoders ka dynamic name description kya hai.

7. **Exercise 7 (Evasion check command):**  
   Evasion builders check karne ke liye load time par `show evasion` command verify karke outputs analyze karein.

8. **Exercise 8 (Toggle list pagination):**  
   Show commands ke scroll length check parameters console display settings check verify check karein.
