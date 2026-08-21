---
title: "Topic 44 - Advanced Linux File Security (SUID, SGID, Sticky Bit, chattr, ACLs)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🛡️ Topic 44: Advanced Linux File Security (SUID, SGID, Sticky Bit, chattr, ACLs)

Bhai, humne basic file permissions (Read `r`, Write `w`, Execute `x`) and ownership commands (`chmod` aur `chown`) seekhi thi. Lekin Linux me enterprise-level security aur custom privilege management ke liye **Advanced File Security Features** use hote hain. 

Cybersecurity me, SUID configurations privilege escalation ke sabse bade leaks hote hain, jabki file attributes (`chattr`) system binaries ko hackers dwara tampering se bachane ke liye use kiye jaate hain.

---

### 🏛️ 1. Special Permissions (SUID, SGID, Sticky Bit)

Linux me standard permissions ke upar ye 3 special bits lagaye ja sakte hain:

#### A. SUID (Set User ID - Value 4) 💀
Jab kisi executable file par SUID set hota hai, toh jab bhi koi normal user use execute karega, wo file **file owner (usually Root)** ke privileges ke sath run hogi, na ki us user ke privileges ke sath.
* *Permissions visual representation:* `rwsr-xr-x` *(Owner position me `x` ki jagah `s` dikhta hai).*
* *Classic Example:* `/usr/bin/passwd` binary par SUID set hota hai taaki normal user apna password change karne ke liye `/etc/shadow` file me new hash write kar sake (jo normal user directly nahi kar sakta).
* *SUID Set karna:* `chmod u+s filename` ya `chmod 4755 filename`.

#### B. SGID (Set Group ID - Value 2) 👥
SGID executable par hone se wo group owner privileges ke sath chalti hai. Agar kisi directory par SGID laga hai, toh us directory ke andar jo bhi naye folders/files banenge, unka group owner automatic parent directory ka group ban jayega.
* *SGID Set karna:* `chmod g+s filename` ya `chmod 2755 filename`.

#### C. Sticky Bit (Value 1) 📌
Ye directory par lagaya jata hai. Agar kisi folder par Sticky Bit set hai, toh uske andar ki files ko sirf **woh user jisne file banayi hai (Owner)** ya **Root user** hi delete/rename kar sakta hai. Koi teesra user file edit kar sakta hai lekin delete nahi kar sakta.
* *Permissions visual representation:* `rwxrwxrwt` *(Others position me `x` ki jagah `t` dikhta hai).*
* *Classic Example:* `/tmp/` directory me system ke sabhi users files save karte hain, wahan Sticky Bit default roop se active hota hai taaki koi user kisi doosre user ki temp file delete na kar sake.
* *Sticky Bit Set karna:* `chmod +t directory/` ya `chmod 1777 directory/`.

---

### 🔒 2. File Attributes: `chattr` & `lsattr` (Immutable Files)
Kuch files aisi hoti hain jinhe hum chahte hain ki **Root user** bhi delete ya modify na kar sake (jaise system authorization logs ya crucial system configuration directories).
* **`chattr +i <file>` (Make Immutable):** File ko lock kar deta hai. Lock hone ke baad file ko na toh delete kiya ja sakta hai, na rename, na edit, chahe aap `sudo` chala rahe hon!
  ```bash
  sudo chattr +i critical_backup.txt
  ```
* **`chattr -i <file>` (Remove Lock):** Lock hatane ke liye.
* **`chattr +a <file>` (Append-Only):** File me sirf naya data niche add kiya ja sakta hai (`>>`), purana data change ya delete nahi kiya ja sakta (Web security audit logs ke liye useful).
* **`lsattr <file>` (List Attributes):** Attributes check karne ke liye.
  * *Output:* `----i--------- critical_backup.txt`

---

### 🔗 3. ACLs (Access Control Lists)
Traditional Linux me hum sirf ek Owner, ek Group aur baki sab ke liye permissions set kar sakte hain. Lekin agar hume **ek specific file par user `bob` ko read/write dena hai, user `alice` ko read-only dena hai, aur baaki sab ko block karna hai**, toh hum ACLs use karte hain:
* **`getfacl <file>` (Get File ACL):** File ki deep permissions list dekhna.
* **`setfacl -m u:<user>:<permissions> <file>` (Modify ACL):** Custom rule lagana.
  ```bash
  setfacl -m u:bob:rw target_file.txt
  ```

---

### 🔑 Real-World Analogy (The Bank Vault 🏦🔐)
* **SUID:** Jaise bank ka self-service deposit machine. Jab customer paise deposit karta hai, machine temporary system manager privilege (Root rights) use karti hai vault open karne ke liye.
* **Sticky Bit:** Jaise office pantry ka fridge. Har employee apna dabba fridge me rakh sakta hai, par koi doosra aapka lunchbox fenk ya delete nahi kar sakta, sirf admin ya owner hi kar sakta hai.
* **`chattr +i` (The Concrete Cast):** File ko cement ke dhache me fit kar dena. Ab use koi tod nahi sakta, modify nahi kar sakta jab tak cement ka cast (`-i`) na hataya jaye.
* **ACLs:** Jaise VIP building security register. Har visitor (user) ke aage alag-alag permissions specify likhi hoti hain ki kaun kis room me ja sakta hai.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, file security setups verify karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** Ek dummy script banayein `sec_test.sh` aur use executables permission dekar SUID bit lagayein: `chmod u+s sec_test.sh`. Check karein `ls -la` me user execution position me `s` show ho raha hai ya nahi.
2. **Task 2:** SUID bit remove karne ke liye sahi syntax script execution command chalayein (`chmod u-s sec_test.sh`).
3. **Task 3:** `/tmp` directory ke absolute permissions verify karein: `ls -ld /tmp` aur check karein ki kya aakhri column me `t` (Sticky Bit) set hai.
4. **Task 4:** Ek naya file touch karein `immutable_test.txt` aur use root permission se immutable lock lagayein: `sudo chattr +i immutable_test.txt`.
5. **Task 5:** `immutable_test.txt` ko delete karne ki koshish karein `rm -f immutable_test.txt` (ya `sudo rm -f`). Check karein kya error aata hai (Operation not permitted).
6. **Task 6:** Lock file ke attributes verify karne ke liye command run karein: `lsattr immutable_test.txt`.
7. **Task 7:** `immutable_test.txt` ka lock hatayein: `sudo chattr -i immutable_test.txt`, aur check karein ki kya ab file delete ho rahi hai.
8. **Task 8:** File par custom target ACLs parameters verify karne ke liye `getfacl welcome.txt` command execute karein.
9. **Task 9:** Kisi regular secondary user account ko target file par read permission dene ke liye ACL command run check karein: `setfacl -m u:kali:r welcome.txt`.
10. **Task 10:** Hacking local privilege escalation attacks (PrivEsc) me `/usr/bin/find` ya custom binaries par SUID bit set hona kaise exploitation vectors banta hai? 2 lines me explain karein.

---
