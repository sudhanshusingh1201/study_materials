# Topic 10 - How to Get Help and Use Documentation in Metasploit

Metasploit ek bohot bada framework hai jisme hazaron commands aur modules hain. Professional penetration testing karte waqt aap saari commands yaad nahi rakh sakte. Is note mein hum seekhenge ki msfconsole ke built-in **Help Systems** aur documentation utilities ka use kaise kiya jata hai.

---

## 1. Real-World Analogy: The Built-in Index Manual

Maan lijiye aapne ek complex high-tech machine kharidi hai (jaise ek advanced DSLR camera ya 3D Printer):
* **Normal Behavior:** Aap jab bhi kisi feature mein phaste hain, toh online manual search karte hain ya customer support ko call karte hain.
* **The Built-in Help Screen:** Camera ke display screen par hi ek `[?]` button hai jise kisi bhi setting par click karke aap us setting ka live tutorial padh sakte hain bina camera band kiye.
* **Metasploit ka help system wahi built-in screen hai.** Yeh bina internet ya Google ke aapko terminal par hi command details aur syntax bata deta hai.

---

## 2. General Help Commands: `help` and `?`

Msfconsole open karne ke baad agar aapko saari commands ki dictionary list dekhni hai:

```text
msf6 > help
```
ya fir:
```text
msf6 > ?
```

### Categorized Help List:
Yeh command execute karte hi aapko terminal par commands groups mein sorted dikhegi:
1. **Core Commands:** Navigation aur system settings (`use`, `set`, `show`, `version`).
2. **Database Backend Commands:** Target reports aur scans save karne wale parameters (`hosts`, `services`, `creds`).
3. **Session Commands:** Open connections control commands (`sessions`, `kill`).
4. **Developer Commands:** Module development helpers (`reload_all`, `edit`).

---

## 3. Specific Command Help (Contextual Help)

Agar aapko kisi specific command ka exact syntax aur options dekhna hai, toh command ke aage `help` suffix ya prefix laga sakte hain.

* **Syntax:** `help <command-name>` ya `<command-name> -h`

### Examples:

#### A. Search Command ka syntax check karna:
```text
msf6 > help search
```
*(Yeh aapko batayega ki `platform`, `cve`, `author` filters kaise aur kahan apply karne hain).*

#### B. Sessions Command ke details verify karna:
```text
msf6 > help sessions
```
*(Yeh show karega ki list dekhne ke liye `-l`, session interact ke liye `-i`, aur interactive shell upgrade ke liye `-u` use karna hai).*

---

## 4. Module-Level Documentation (`info`)

Jab koi exploit load hota hai, toh uski complete manual check karne ke liye **`info`** command chalayi jaati hai:

```text
msf6 > use exploit/unix/ftp/vsftpd_234_backdoor
msf6 exploit(...) > info
```
### Info Block Details:
* **References:** Vulnerability ke CVE ID links.
* **Targets:** Yeh exploit kis-kis OS build par successfully run ho sakta hai (e.g. Linux x86/x64).
* **Description:** Exploit background mein kaun se packets bhej kar trigger hota hai uski details.

---

## 5. Practice Exercises for Help System

Perform these exercises on your local Kali terminal:

1. **Exercise 1 (General Help):**  
   `msfconsole` ke andar `help` command run karke general output scroll checks check karein.

2. **Exercise 2 (Connect command analysis):**  
   Msfconsole ke andar `help connect` run karein aur batayein ki is command ka description kya hai aur isse target connection port check kaise karte hain?

3. **Exercise 3 (Search documentation):**  
   `help search` command ka use karke search keyword filters ki full list identify karein aur check karein ki isme `rank` parameter filter details kaise use hoti hain.

4. **Exercise 4 (Sessions option checks):**  
   `help sessions` chalao aur specify karein ki target background session `kill` karne ke liye kis variable flag (option) ka use kiya jata hai.

5. **Exercise 5 (Info extraction):**  
   Vulnerability exploit module `exploit/windows/smb/ms17_010_eternalblue` load karein aur `info` run karke check karein ki iske actual software authors/creators ke names kya hain.

6. **Exercise 6 (Developer debug tools):**  
   Console modules check load reload command list explore karein aur database update check karne ke liye developer list commands find karein (Hint: check `reload_all` description).

7. **Exercise 7 (Advanced view):**  
   `show advanced` command ke help specifications check karein aur system level payload properties analyze karne ke parameter options verify karein.

8. **Exercise 8 (Interactive help):**  
   Msfconsole prompt par direct terminal command execution commands (using `!`) ke systems help features verify karein.
