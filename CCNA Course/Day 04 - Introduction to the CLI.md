---
title: "Day 04 - Introduction to the CLI"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🔌 Day 04: Introduction to the CLI

Welcome to the notes for **Day 4: Intro to the CLI** ! Ye note aapko Cisco IOS Command-Line Interface (CLI) ke basics, console connectivity, CLI modes navigation, configuration management, aur shortcuts ko detailed visual illustrations aur real-world examples ke sath pure Hinglish language mein samjhayega.

---

## 💻 1. Cisco Device se Kaise Connect Karein? (Connecting to CLI)

Cisco switch ya router ko configure karne ke liye hum **Command-Line Interface (CLI)** ka use karte hain. Naye device ke initial setup ke liye koi default IP address ya web screen nahi hoti, isliye hume console port ke zariye physical connection banana padta hai.

### Requirements:
1.  **Console Cable (Rollover Cable):** Standard sky-blue color ki cable hoti hai jiske ek side RJ45 connector hota hai (jo device ke console port par lagta hai) aur doosri side DB9/USB connector hota hai (jo laptop par lagta hai).
2.  **Terminal Emulator:** Ek software jo device ke system commands ko console line ke zariye hamare computer keyboard par show karta hai (Jaise PuTTY, Tera Term, SecureCRT).

![Console Connection](../images/console_connection.jpg)

### Default Serial Connection Settings:
Terminal emulator mein serial connection start karte waqt niche diye gaye standard parameters match hone chahiye:
*   **Baud Rate (Speed):** `9600` bits/second
*   **Data Bits:** `8` data bits
*   **Stop Bits:** `1` stop bit
*   **Flow Control:** None

---

## 🧭 2. Cisco CLI Modes & Navigation

Cisco IOS CLI security aur command limitations ke liye alag-alag hierarchical levels par kaam karta hai jise **Modes** kehte hain.

![CLI Modes Flowchart](../images/cli_flowchart.jpg)

### A. User EXEC Mode
*   **Prompt:** `Router>` ya `Switch>`
*   **Kaam:** Ye basic basic login landing page hai jisme security level lowest hota hai. Aap sirf basic status check aur ping/traceroute check kar sakte hain, configuration mein koi change nahi kar sakte.
*   **Navigation:** Is mode se upar privileged mode mein jaane ke liye type karein: `enable`.
*   #### 💡 Real-world Analogy (Udaharan):
    *   **Office Reception Lobby:** Jaise kisi badi office building ka public reception lobby. Koi bhi guest aakar reception board par check kar sakta hai ki building mein kaun se department hain (basic monitoring) par wo bina card ke kisi specific executive office room mein enter nahi ho sakta.

### B. Privileged EXEC Mode (Enable Mode)
*   **Prompt:** `Router#` ya `Switch#`
*   **Kaam:** Is mode mein user ke paas system details read karne ki full rights hoti hain (jaise active hardware ports ya system memory check karna). Aap configuration file ko read ya reboot kar sakte hain, par dynamically parameters modify nahi kar sakte.
*   **Navigation:**
    *   Niche User mode mein wapas jaane ke liye: `disable`.
    *   Upar configuration mode mein jaane ke liye: `configure terminal` (shortcut `conf t`).
*   #### 💡 Real-world Analogy (Udaharan):
    *   **Building Inspector/Supervisor:** Jaise building security supervisor jiske paas har room ki master key hai. Wo har office room ke file rack ko open karke check kar sakta hai, inspect kar sakta hai, aur files read kar sakta hai (troubleshoot show commands), par wo building ke wall structures ko change nahi kar sakta.

### C. Global Configuration Mode
*   **Prompt:** `Router(config)#` ya `Switch(config)#`
*   **Kaam:** Is mode mein entered commands global level par implement hoti hain (jaise switch IP set karna, hostname change karna, enable passwords configure karna).
*   **Navigation:**
    *   Privileged EXEC mode mein wapas jaane ke liye: `exit` type karein.
    *   Direct Privileged EXEC mode (root level) par aane ke liye press karein: `end` ya shortcut `Ctrl + Z`.
*   #### 💡 Real-world Analogy (Udaharan):
    *   **Building Architect/Owner:** Jaise building architect ya owner, jo deewarein tod kar naya room bana sakta hai (VLAN structure), routing corridors badal sakta hai, ya door locks change kar sakta hai.

### D. Sub-Configuration Modes (Specific Modes)
Global configuration se specific ports ya physical lines select karke unke config modes mein jata hai:
*   **Interface Configuration Mode:** Specific ports (jaise port FastEthernet 0/1) config karne ke liye.
    *   *Command:* `interface FastEthernet 0/1` (shortcut `int fa0/1`) -> Prompt: `Router(config-if)#`
*   **Line Configuration Mode:** Device console line ya remote network access lines configure karne ke liye.
    *   *Command:* `line console 0` -> Prompt: `Router(config-line)#`

---

## ⚡ 3. Useful CLI Features & Shortcuts

Cisco CLI ko fast aur error-free chalane ke liye system mein shortcuts hotey hain:

### A. Help and Completion:
*   **Tab Key:** Kisi bhi half-written command ko complete karne ke liye (Jaise `conf` likh kar Tab dabane par wo `configure` ho jayega).
*   **Question Mark (?) Help:**
    *   `?` : Sabhi available commands ki list dekhne ke liye.
    *   `sh?` : Un sabhi commands ko list karega jo 'sh' se start hote hain (jaise show).
    *   `show ?` : `show` command ke sath aane wale parameters aur variables ki list show karega.

### B. Common Error Messages:
*   `% Ambiguous command:` CLI ko samajh nahi aaya ki aap kaun si command run karna chahte hain kyunki us short phrase se multiple commands start hoti hain (e.g. `c` likhne par clear, configure dono ho sakte hain).
*   `% Incomplete command:` Command toh sahli hai par aapne requirements ke according aage ke parameters (e.g., interface ID) nahi likhe.
*   `% Invalid input detected at '^' marker:` Command syntax mein error hai. '^' marker exact point show karta hai jahan typing error hui hai.

---

## 💾 4. Configuration Management: RAM vs NVRAM

Cisco devices mein switch/router settings do main positions par store hoti hain:

![Running vs Startup Config](../images/running_vs_startup.jpg)

### 1. Running Configuration:
*   **Location:** RAM (Random Access Memory).
*   **Status:** Volatile (temporarily loaded). Agar device switch off (reboot) ho jaye, toh saara active configuration content delete ho jayega.
*   **File Name:** `running-config`
*   #### 💡 Real-world Analogy (Udaharan):
    *   **Classroom Whiteboard:** Jaise class chalte waqt whiteboard par rough notes likhna. Jab tak class chal rahi hai (device running state mein hai), data safe hai, par jaise hi class over hui ya kisi ne cleaner se wipe kiya (power off/reboot), whiteboard poora blank ho jayega!

### 2. Startup Configuration:
*   **Location:** NVRAM (Non-Volatile RAM).
*   **Status:** Non-volatile (persistently saved). Device restart hone par bhi data delete nahi hota. Boot process par system is file ko select karke execute karta hai.
*   **File Name:** `startup-config`
*   #### 💡 Real-world Analogy (Udaharan):
    *   **Student Notebook:** Whiteboard par likhe rough notes ko permanent pen se notebook par note down karna. Notebook par likha data hamesha permanent rahega, chahe classroom switch off ho jaye ya lights off ho jayein.

### Configurations Save Kaise Karein?
Whiteboard ke active text ko notebook mein copy karne ke process ko saving kehte hain:
*   *Command:* `copy running-config startup-config` (shortcut `copy run start`)
*   *Legacy/Common Alternate:* `write` (shortcut `wr`)

---rtcut `wr`)

---

## 🧪 5. Day 04 Lab: Cisco CLI Basic Configuration Walkthrough

Jeremy's Day 4 Lab mein hum ek switch (S1) par basic security aur administrative configurations implement karte hain. Niche is lab ke saare tasks aur unke solutions diye gaye hain:

### Tasks to Perform:
1.  **Change Hostname:** Switch ka default name badalkar `S1` karein.
2.  **Enable Password:** Cleartext enable password set karein `cisco`.
3.  **Enable Secret:** Encrypted enable secret password set karein `cisco123`.
4.  **Security Testing:** Dono passwords configure karne ke baad verify karein ki login ke waqt kaun sa password work karta hai.
5.  **Secure Console Line:** Console port access ko password `cisco` se secure karein.
6.  **Secure VTY Lines:** Remote access lines (VTY 0 to 15) ko password `cisco` se secure karein.
7.  **Configure MOTD Banner:** Unauthorized access warning message set karein.
8.  **Save Changes:** Configurations ko running-config se startup-config (NVRAM) mein copy karein.

---

### Step-by-Step CLI Solutions:

#### Step 1: Hostname Badlein
```ios
Switch> enable
Switch# configure terminal
Switch(config)# hostname S1
S1(config)#
```

#### Step 2: Enable Passwords (Password vs Secret) Configure Karein
```ios
S1(config)# enable password cisco
S1(config)# enable secret cisco123
```
> [!IMPORTANT]
> **Key Concept:** `enable secret` password strongly encrypted (MD5/SHA) hota hai aur ye `enable password` (clear-text) ko overrides kar deta hai. Jab aap next time mode change karenge, toh aapko `cisco123` hi enter karna hoga, `cisco` work nahi karega.

#### Step 3: Console Port ko Secure Karein (Physical Line Security)
Console line par password prompt enable karne ke liye password ke sath `login` command lagana mandatory hai:
```ios
S1(config)# line console 0
S1(config-line)# password cisco
S1(config-line)# login
S1(config-line)# exit
```

#### Step 4: VTY Lines ko Secure Karein (Remote Connection Security)
Virtual lines (VTY) Telnet/SSH connections ke liye hoti hain:
```ios
S1(config)# line vty 0 15
S1(config-line)# password cisco
S1(config-line)# login
S1(config-line)# exit
```

#### Step 5: Banner MOTD Set Karein
Warning message config karne ke liye text ko delimiters (jaise `#` ya `$`) ke beech wrap karein:
```ios
S1(config)# banner motd # WARNING: Unauthorized Access is Strictly Prohibited! #
S1(config)# exit
```

#### Step 6: Verify and Save to NVRAM
Apne changes verify karne ke liye Privileged EXEC mode mein `show running-config` run karein aur use save karein:
```ios
S1# show running-config
! (Yahan aapko 'enable secret' encrypted aur 'enable password' clear text mein dikhega)

S1# copy running-config startup-config
Destination filename [startup-config]? [Enter]
Building configuration...
[OK]
```

---

## 📝 6. CCNA Day 04 Practice Questions (Self-Practice Quiz)

Aap yahan questions ko read karke answers verify kar sakte hain (Answer dekhne ke liye click karein):

1.  **Q1: Naye Cisco device ko initial level par configure karne ke liye use hone wali rollover cable laptop ke USB port se switch ke kis port par connect hoti hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **Console Port**
    </details>

2.  **Q2: Terminal Emulator software mein Cisco device console connection access karne ke liye standard Baud Rate speed default settings kya hoti hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **9600 bits per second (9600 baud)**
    </details>

3.  **Q3: Cisco CLI system ko boot karte hi screen par `Switch>` prompt dikhai deta hai. Ye prompt kis mode ko represent karta hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **User EXEC Mode**
    </details>

4.  **Q4: User EXEC mode se Privileged EXEC mode (`Switch#`) mein switch-over karne ke liye hum console par kis command ka use karte hain?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **enable command**
    </details>

5.  **Q5: Global Configuration Mode (`Switch(config)#`) se drop-down hokar direct Privileged EXEC Mode (`Switch#`) par aane ke liye keyboard shortcut kya hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **Ctrl + Z** ya **end command** typing.
    </details>

6.  **Q6: Console par write karte waqt kisi unknown spelling error par CLI console screen par `% Invalid input detected at '^' marker` show karta hai. Is error mein '^' sign ka kya purpose hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** Ye marker precise location show karta hai jahan syntax error (typing mistake) hui hai.
    </details>

7.  **Q7: RAM mein loaded temporary active settings (running-config) ko device reboots se save karne ke liye hum use kis memory location par copy karte hain?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **NVRAM (Non-Volatile RAM)**, jahan **startup-config** save hota hai.
    </details>

8.  **Q8: Cisco Switch configuration settings ko RAM se NVRAM mein save karne ka standard standard syntax command kya hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **`copy running-config startup-config`** (ya simple shortcut `write`/`wr`).
    </details>

9.  **Q9: Cisco IOS command line editor par command typing shortcut `conf t` se access hone wala CLI configuration level kaun sa hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **Global Configuration Mode** (`configure terminal`).
    </details>

10. **Q10: `Switch(config-line)#` aur `Switch(config-if)#` prompts Cisco CLI ke kis level of structure command modes ke parts hain?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **Sub-Configuration Modes** (Line Configuration mode aur Interface Configuration mode).
    </details>
