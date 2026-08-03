---
title: "Topic 14 - Linux Terminal - Basic Commands & Concepts"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 💻 Topic 14: Linux Terminal - Basic Commands & Concepts

Bhai, Kali Linux operating system aur hacking tools ka asli power uske desktop me nahi, balki uske **Terminal** me hota hai. Agar aap hacking ya cyber security me excel karna chahte hain, toh terminal par strong command hona sabse zaroori hai.

---

### 💻 Terminal vs. Shell (Basic Difference)
* **Terminal (Emulator):** Ye wo screen/window software hai jo hume open hoti hai jisme hum text type karte hain (e.g., QTerminal in Kali, Gnome Terminal).
* **Shell:** Ye terminal ke background me chalne wala program hai jo hamare type kiye commands ko parse karta hai, system commands execute karta hai aur kernel se response laakar terminal screen par print karta hai (e.g., **Bash** aur **Zsh** Kali Linux ke default shells hain).

---

### 🆔 Understanding the Shell Prompt (Prompt Ka Kya Matlab Hai?)

Jab aap terminal open karte ho, toh ye line dikhti hai:
`kali@kali:~$`
* **`kali` (Pehla):** User account ka name.
* **`kali` (Dusra):** System name (Hostname).
* **`~` (Tilde):** Represent karta hai ki aap abhi current user ki **Home Directory** (`/home/kali`) ke andar hain.
* **`$` (Dollar Symbol):** Iska matlab hai aap ek **Normal User** hain jiske paas normal restrictions hain.
* **`#` (Hash Symbol):** Agar prompt me end me `#` dikhe (jaise `root@kali:~#`), iska matlab hai aap **Root User** (Super-Administrator) hain jiske paas system file changes ke unlimited rights hain.

---

### 🛠️ Top 10 Essential Linux Commands (Har Beginner Ke Liye)

Apne navigation aur control ke liye ye commands yaad rakhein:

1. **`pwd` (Print Working Directory):**
   * *"Main abhi computer ke kis folder me khada hoon?"* Ye us file path ko screen par print karega.
2. **`ls` (List):**
   * Current folder me kitni files aur sub-folders hain unki list show karta hai.
   * `ls -la` (Hidden files aur read/write file permissions details show karne ke liye best command).
3. **`cd` (Change Directory):**
   * Ek folder se doosre folder me move karna (jaise: `cd Documents`).
   * `cd ..` (Folder se ek level piche / parent folder me wapas aane ke liye).
4. **`cat` (Concatenate):**
   * Kisi file ko bina edit mode me khole, uske texts ko direct screen par print karne ke liye (e.g., `cat target_ips.txt`).
5. **`sudo` (Superuser Do):**
   * Kisi command ko system level control permissions (as a Root User) ke sath run karna. Iske baad system aapse admin password mangega. (e.g., `sudo apt update`).
6. **`mkdir` & `touch` (Create folders/files):**
   * `mkdir hack_lab` (Ek naya directory/folder banayega).
   * `touch info.txt` (Ek khali blank text file generate karega).
7. **`chmod` (Change Mode - Permissions control):**
   * Hacking me script files (.sh, .py, etc.) download karne ke baad unhe execute karne ke permissions setup dynamic change karne hote hain:
   * `chmod +x payload.sh` (Isse file execute hone ke liye executable ban jati hai, file ka color terminal me red/white se green ho jata hai).
8. **`grep` (Filter Search):**
   * Bohot saare output contents me se specific words filter dhoondhna:
   * `cat list.txt | grep "admin"` (Sirf wahi line dikhayega jisme "admin" word present ho).
9. **`man` (Manual Book):**
   * Kisi command ya tool ke flags kaise use karein, uski complete documentation padhne ke liye.
   * `man nmap` (Nmap usage instructions text guide display).
10. **`rm` (Remove/Delete):**
    * `rm file.txt` (File delete karne ke liye).
    * `rm -rf folder_name` (Folder aur uske andar ke files ko force recursively delete karne ke liye).

---

### ⛓️ Piping (`|`) & Redirections (`>`, `>>`)

Ye symbols terminal outputs ko manage karne me extra features add karte hain:

* **Piping (`|`):** Ek command ke output stream ko input ki tarah doosre command me forward karna.
  * *Example:* `ls -la | grep "notes.txt"`
* **Overwrite Redirection (`>`):** Kisi command ke output logs ko file me save karna (purana content delete ho jayega).
  * *Example:* `echo "admin_pass123" > secrets.txt`
* **Append Redirection (`>>`):** Output data ko existing file ke end me add karna (purana data safe rahega).
  * *Example:* `echo "user_pass321" >> secrets.txt`

---