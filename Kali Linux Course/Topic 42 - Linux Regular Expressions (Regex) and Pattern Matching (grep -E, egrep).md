---
title: "Topic 42 - Linux Regular Expressions (Regex) & Pattern Matching"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🔍 Topic 42: Linux Regular Expressions (Regex) & Pattern Matching (grep -E, egrep)

Bhai, Linux CLI me raw text data se specific logs, IP addresses, emails ya password formats dhoondhne ke liye hum **Regular Expressions (Regex)** ka use karte hain. Hacking me jab hume huge data leaks ya logs me se patterns extract karne hote hain, toh Regex sabse bada asset hota hai.

---

### ⚠️ Globbing (Wildcard) vs Regex (Bade Confusions! 🤯)
* **Globbing (Shell Wildcards):** Ye shell dwara **Filenames** ko match karne ke liye use hota hai (jaise `ls *.txt` me `*` ka matlab hai sabhi files).
* **Regex (Regular Expressions):** Ye files ke **ANDAR ke text data** me patterns search karne ke liye `grep`, `sed`, ya `awk` dwara use kiya jata hai.

---

### 🏛️ Basic Regex Symbols (Metacharacters Cheat Sheet)

#### 1. Position Anchors (Boundary checkers)
* **`^` (Caret - Starting with):** Line kis character se start ho rahi hai check karta hai.
  * *Example:* `^admin` *(Matches only those lines that start with the word "admin").*
* **`$` (Dollar - Ending with):** Line kis character se end ho rahi hai check karta hai.
  * *Example:* `false$` *(Matches only those lines that end with the word "false").*

#### 2. Character Matching
* **`.` (Dot):** Kisi bhi **single character** (number, letter, symbol) ke liye boundary checker.
  * *Example:* `d.g` *(Matches dig, dog, dug, d4g, d-g, etc.).*
* **`[abc]` (Character Set):** Bracket ke andar likhe characters me se koi bhi **ek character** match hoga.
  * *Example:* `d[ou]g` *(Matches dog and dug, but not dig).*
* **`[^abc]` (Negated Set):** Bracket ke characters ko **chhodkar** baaki sabhi match karega.
  * *Example:* `d[^o]g` *(Matches dig and dug, but not dog).*

#### 3. Quantifiers (Character Repetition - Extended Regex `-E`)
*Extended regex patterns chalane ke liye terminal par **`grep -E`** ya **`egrep`** ka use kiya jata hai.*
* **`*` (Asterisk):** Preceding character **0 ya usse zyada** baar repeat ho sakta hai.
* **`+` (Plus):** Preceding character **1 ya usse zyada** baar repeat hona chahiye.
  * *Example:* `ca+t` *(Matches cat, caat, caaat, but not ct).*
* **`?` (Question Mark):** Preceding character **optional (0 ya 1 baar)** hai.
  * *Example:* `colou?r` *(Matches color and colour).*
* **`{n}` (Exact Count):** Preceding character exactly `n` baar aana chahiye.
  * *Example:* `[0-9]{3}` *(Matches exactly 3 digit numbers, jaise 123, 999).*

#### 4. Escaping Special Characters
Agar aapko text ke andar sach me dot (`.`) ya dollar (`$`) dhoondhna hai, toh uske aage backslash `\` lagana padega:
* *Example:* `google\.com` *(Literal dot matches, not any character).*

---

### 🕵️‍♂️ Real-World Cybersecurity Regex Examples

1. **IP Addresses extract karna:**
   ```bash
   grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}" logs.txt
   ```
   *(Ye logs me se specific IP address structures like `192.168.1.1` ko dynamically pull karke print kar dega).*

2. **Web logs me SQL Injection matching simulation:**
   ```bash
   grep -i -E "select|union|insert|or 1=1" access.log
   ```
   *(Web Server logs me unauthorized SQL statements inject karne wale attacker records verify karne ke liye).*

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, Regex rules aur syntax verify karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** `/etc/passwd` file me un lines ko check karein jo start hoti hain **"root"** se: `grep "^root" /etc/passwd`.
2. **Task 2:** `/etc/passwd` me default login shells check karne ke liye un lines ko filter karein jo end hoti hain **"nologin"** se: `grep "nologin$" /etc/passwd`.
3. **Task 3:** Ek test file `regex_sample.txt` banayein jisme ye words likhein: `cat`, `cot`, `cut`, `ct`, `coat`.
4. **Task 4:** `regex_sample.txt` me character set configuration check karein: `grep "c[au]t" regex_sample.txt` chalayein aur observe karein kaunse words match hue.
5. **Task 5:** `regex_sample.txt` me check karein `grep -E "ca+t" regex_sample.txt` chalane par `ct` match ho raha hai ya nahi, aur kyun?
6. **Task 6:** Ek test logs file `logs_test.txt` banayein jisme 3 fake IP addresses (jaise `10.10.1.5`, `192.168.0.105`, `abc.def.ghi`) likhein.
7. **Task 7:** `logs_test.txt` me se valid IP formats dynamically extract karne ke liye appropriate **`grep -E -o`** command run karein.
8. **Task 8:** `/etc/ssh/sshd_config` file (agar system me ho, ya normal config files) me comment lines (starting with `#`) ko completely filter/remove karke saaf config check karne ke liye command structure verify karein: `grep -v "^#" /etc/passwd` (ya comments check filter).
9. **Task 9:** Dot boundary check parameters verify karne ke liye `grep "c.t" regex_sample.txt` chala kar outputs note karein.
10. **Task 10:** Log analysis and intrusion detection systems (IDS/IPS rules) me regular expressions (regex) engines are signature databases ka kya correlation hai? 2 lines me explain karein.

---
