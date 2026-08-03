---
title: "Topic 28 - Nmap Reason Flag (--reason)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 28: Nmap Reason Flag (--reason)

### 1. Explanation (Hinglish)
Nmap mein **`--reason`** flag ek bohot hi important debugging aur networking flag hai. Iska use scan results mein har ek port ke decision factors (kis packet reply ke base par state decide hui) ko analyze karne ke liye kiya jata hai.

Default Nmap scans mein aapko sirf final report dikhti hai:
- Port 80: **open**
- Port 22: **closed**
Lekin hume exact packet configuration flow ka pata nahi chalta. `--reason` flag add karte hi Nmap output table mein ek extra **"REASON"** column add kar deta hai jo is decision ki technical wajah batata hai.

---

### 📊 Common Nmap decision reasons:

| Port State | REASON status | Target Response Behavior |
| :--- | :--- | :--- |
| **Open** | `syn-ack` | Target system ne scanner ki SYN request ke reply mein SYN-ACK bhej kar connection accept kiya. |
| **Closed** | `conn-refused` | Target system ne direct **RST (Reset)** packet bhejkar connection setup reject kar diya. |
| **Filtered** | `no-response` | Target or firewall se koi reply nahi mila (packets silently dropped). |
| **Filtered** | `admin-prohibited` | Firewall/Router ne ICMP destination unreachable message send kiya block validation ke liye. |

---

#### 🚪 Real-world Analogy: The Inspector's Reasoning Notes
Socho aap ek security supervisor ho:
- **Without `--reason`:** Guard aakar simple list deta hai: *"Flat 101 open hai, aur Flat 102 closed hai."* (Only final report).
- **With `--reason`:** Guard detailed check-up reasons notes ke sath file submit karta hai:
  - *"Flat 101 open hai (Kyunki gatekeeper ne hume greeting smile SYN-ACK di)."*
  - *"Flat 102 closed hai (Kyunki hume counter gate keeper ne gate refuse signal RST card diya)."*
  - *"Flat 103 filtered hai (Kyunki humne knock kiya aur andar se ghanto tak koi reply "no-response" nahi mila)."*

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par reason analysis verify karne ke steps:

**Task 1: Reason flag ke sath active test scan execute karna:**
```bash
nmap --reason scanme.nmap.org
```
*(Scan complete hone par check karein main port listings ke right side mein load hua naya **REASON** column).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap scan output display table mein ek extra column add karne ke liye, jo batata hai ki target se kaun sa specific packet (jaise syn-ack ya conn-refused) receive hone par decision liya gaya, kis flag ka use kiya jata hai?
- **A)** `-sV`
- **B)** `--reason`
- **C)** `-oN`

#### 🎯 Assignment
1. Kali Linux terminal par run karein: `nmap --reason localhost`
2. Output table check karke batayein:
   - Open ports aur Closed ports ke aage decision reasons column mein kya packet messages show ho rahe hain?
3. Quiz ka answer aur assignment logs updates mujhe chat mein share karein!

---