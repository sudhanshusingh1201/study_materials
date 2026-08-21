---
title: "Topic 45 - Inside the Linux Shell (Builtins vs External, Shortcuts, Aliases, Env Variables)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🐚 Topic 45: Inside the Linux Shell (Builtins vs External, Shortcuts, Aliases, Env Variables)

Bhai, humne **Topic 14** me terminal basics aur commands chalana seekha tha. Lekin terminal sirf ek gate hai, uske peeche asli dimaag **Shell** (jaise Bash ya Zsh) ka hota hai. Hacking aur system administration me, shell ke inner mechanics (jaise environment variables, aliases, aur shortcuts) ko samajhna terminal speed ko 10x fast kar deta hai.

---

### 🏛️ 1. Shell Builtins vs External Commands

Linux commands do categories me divided hoti hain:
1. **Shell Builtins:** Ye commands shell interpreter ke andar hi embedded (built-in) hoti hain. Inhe execute karne ke liye shell ko kisi external file ko disk se load nahi karna padta.
   * *Examples:* `cd`, `echo`, `alias`, `exit`, `history`, `pwd`.
2. **External Commands:** Ye alag executable files (binaries) hoti hain jo disk (`/bin` ya `/usr/bin`) me stored hoti hain. Jab aap inhe run karte ho, shell inhe search karke execution ke liye load karta hai.
   * *Examples:* `ls`, `grep`, `ping`, `nmap`.
* **Kaise check karein?** Command ke aage **`type`** lagakar:
  ```bash
  type cd    # Output: cd is a shell builtin
  type grep  # Output: grep is /usr/bin/grep (External)
  ```

---

### ⚡ 2. Terminal Magic Shortcuts (Time Savers)
Hacker ki terminal typing speed in shortcuts ke kaaran bohot fast hoti hai:
* **`Tab` (Single/Double press):** Auto-completes command names aur file paths.
* **`Ctrl + A`:** Cursor ko line ke ekdum shuru (Start) me le jaata hai.
* **`Ctrl + E`:** Cursor ko line ke ekdum aakhir (End) me le jaata hai.
* **`Ctrl + U`:** Cursor ke peeche ki poori line ko clear/delete kar deta hai.
* **`Ctrl + K`:** Cursor ke aage ki poori line ko delete kar deta hai.
* **`Ctrl + R`:** Reverse search—purani history me se kisi command ko search karne ke liye (Bohot useful!).
* **`Ctrl + C`:** Running command ko force stop (kill) karna.
* **`Ctrl + L`:** Screen clear karna (Equivalent to `clear` command).

---

### 📍 3. Aliases (Shortcuts banana)
Agar aapko koi badi command (jaise update network commands) baar-baar chalani padti hai, toh aap uska chota shortcut alias bana sakte hain:
* **Alias set karna:**
  ```bash
  alias updateall='sudo apt update && sudo apt upgrade -y'
  ```
  *(Ab terminal par sirf `updateall` likhne par poori command chal jayegi).*
* **Active aliases dekhna:** Sirf `alias` type karein.
* **Alias delete karna:** `unalias updateall`.

---

### ⚙️ 4. Environment Variables & `$PATH` 🧬
Variables ka use temporary data save karne ke liye kiya jata hai.
* **Local Variables:** Sirf current shell session me active hote hain.
  ```bash
  myname="sudhanshu"
  echo $myname
  ```
* **Environment Variables:** Ye child processes (sub-shells) me bhi active hote hain. Inhe **`export`** se set karte hain:
  ```bash
  export target_ip="10.10.10.15"
  ```
* **💀 The `$PATH` Variable (Most Important!):**
  Jab aap terminal par `ls` type karte ho, toh system ko kaise pata chalta hai ki `ls` binary kahan saved hai? Wo `$PATH` me listed directories ke andar dhoondhta hai.
  ```bash
  echo $PATH
  ```
  *Output:* `/usr/local/bin:/usr/bin:/bin`
  *(Agar koi directory `$PATH` me listed nahi hai, toh wahan ki command run karne ke liye hume `./tool` chalana padta hai. Hackers privilege escalation ke liye `$PATH` variables ko modify/hijack karte hain).*

---

### 🔑 Real-World Analogy (The Chef and The Kitchen 🍳🐚)
* **Shell Builtins:** Jaise chef (shell) ke haath me pakdi hui knife ya spoon (jo hamesha haath me ready hai—quick).
* **External Commands:** Jaise pantry/store room me rakha blender ya toaster (use cupboard se nikal kar counter par laana padega execute karne ke liye—time consuming).
* **Aliases:** Cook ke apne code-words (jaise "dish A" bolte hi helper samajh jaye ki 10 ingredients milane hain).
* **`$PATH` Variable:** Chef ke kitchen drawers ki list. Jab helper ko "peeler" dhoondhne ko bolo, toh wo pehle list me likhe drawers (directories) me check karega. Agar list me drawer C ka naam nahi hai, toh helper wahan check nahi karega (shell file command not found error!).

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, shell configurations check karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** Check karein ki `cd`, `pwd`, `ls` aur `chmod` commands me se kaun-kaun si builtin hain aur kaun-si external: run `type cd pwd ls chmod`.
2. **Task 2:** terminal cursor positioning test karein: Ek badi command type karein, aur `Ctrl + A` aur `Ctrl + E` ka press karke cursor movements verify karein.
3. **Task 3:** History search filter check karne ke liye `Ctrl + R` dabayein, aur apne pichle tasks me se ek keyword (jaise `passwd` ya `chattr`) type karke command history recover karein.
4. **Task 4:** Apne terminal par `ls -la` ke liye ek temporary alias `ll` set karein: `alias ll='ls -la'`, aur use `ll` likhkar verify karein.
5. **Task 5:** Check karein ki kya terminal restart karne ke baad aapka `ll` alias abhi bhi chal raha hai. (Unalias testing).
6. **Task 6:** Apne system ke active environment variables dekhne ke liye command **`printenv`** ya **`env`** run karke verify karein.
7. **Task 7:** Ek target IP configuration variable set karein: `export TARGET="10.10.10.100"`. Phir check karein `ping -c 2 $TARGET` chalane par variable properly load ho raha hai ya nahi.
8. **Task 8:** System command lookup variable verify karne ke liye `echo $PATH` run karein aur columns ko separate karne wala delimiter inspect karein (`:` colon).
9. **Task 9:** Kisi external command file execution ka real source locate karne ke liye `which nmap` ya `which grep` run karke bin directories confirm karein.
10. **Task 10:** Hacking tools installation ke dauran `./exploit` (dot slash) kyu likhna padta hai jabki normal commands (jaise `cat`) ke bina dot-slash chal jaati hain? 2 lines me explain karein.

---
