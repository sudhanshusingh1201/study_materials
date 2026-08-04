# 🧪 Day 04 Lab: Cisco CLI Basic Configuration

Welcome to the **Cisco CLI Basic Configuration Lab** guide! Ye worksheet aapko switch par basic initial configuration commands ko line-by-line apply aur save karne ka step-by-step process pure Hinglish language mein samjhayega.

---

## 🛠️ 1. Lab Tasks to Perform
Is lab mein hum ek Cisco Switch (**S1**) par basic safety aur administrative settings config karenge:
1.  **Change Hostname:** Switch ka default hostname badalkar `S1` karein.
2.  **Enable Password:** Clear-text privilege mode password `cisco` set karein.
3.  **Enable Secret:** Strong encrypted privilege mode secret password `cisco123` set karein.
4.  **Secure Console Line:** Console port line par check verification ke liye password `cisco` lagayein.
5.  **Secure VTY Lines:** Remote login terminals (VTY lines 0 to 15) par login password `cisco` lagayein.
6.  **Configure Warning MOTD Banner:** Unauthorized entry login screen warnings set karein.
7.  **Save Configurations:** RAM ke content (`running-config`) ko NVRAM (`startup-config`) par copy karein.

---

## 💻 2. Copy-Pasteable Cisco CLI Configurations
Aap niche diye gaye configurations ko directly copy karke Packet Tracer ke **Switch CLI terminal** par right-click karke **Paste** kar sakte hain (Comments ignore ho jayenge):

```ios
enable
configure terminal

! -----------------------------------------------------------------
! Task 1: Change Hostname to S1
! -----------------------------------------------------------------
hostname S1

! -----------------------------------------------------------------
! Task 2: Configure Privilege Mode Passwords
! -----------------------------------------------------------------
enable password cisco
enable secret cisco123

! -----------------------------------------------------------------
! Task 3: Secure Physical Console Access
! -----------------------------------------------------------------
line console 0
password cisco
login
exit

! -----------------------------------------------------------------
! Task 4: Secure Remote Virtual Access (Telnet/SSH)
! -----------------------------------------------------------------
line vty 0 15
password cisco
login
exit

! -----------------------------------------------------------------
! Task 5: Configure Warning MOTD Banner
! -----------------------------------------------------------------
banner motd # WARNING: Unauthorized Access is Strictly Prohibited! #
exit

! -----------------------------------------------------------------
! Task 6: Copy Running configurations to NVRAM
! -----------------------------------------------------------------
copy running-config startup-config
! Note: CLI par command chalte hi press [Enter] to confirm filename.
```

---

## 🔍 3. Verification & Troubleshooting Commands
Configurations complete hone ke baad in commands ko run karke verify karein:

*   **Active configurations verify karein:**
    ```ios
    S1# show running-config
    ```
    *(Verify karein ki 'enable secret' encrypted hai, aur 'enable password' clear text mein show ho raha hai).*
*   **NVRAM saved settings check karein:**
    ```ios
    S1# show startup-config
    ```
*   **Logout karke lock testing check karein:**
    ```ios
    S1# exit
    ```
    *(Console prompt lock testing verify karein. Pehle console pass 'cisco' maangega, aur privileged command 'enable' type karne par secret password 'cisco123' maangega).*

---

## 📝 4. CCNA Day 04 Lab Practice Questions

Aap yahan questions ko read karke answers verify kar sakte hain (Answer dekhne ke liye click karein):

1.  **Q1: Jab hum console line config mode mein `password cisco` configure karte hain, toh kis additional command ke bina password verification logic execute nahi hoga?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **login** command. Is command ke bina line interface client input passwords ko bypass kar deta hai.
    </details>

2.  **Q2: Cisco CLI par `enable password` aur `enable secret` dono passwords set karne par priority order standard logic ke according kaun sa pass execute hoga?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **`enable secret`** (cisco123) login verification mein execute hoga kyunki ye system parameters par zyada priority rakhta hai.
    </details>

3.  **Q3: CLI configuration mode mein configuration files line writing terminal commands ke sath use hone wala banner standard syntax header message delimiter block character kya use karta hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **Any single character delimiter** (Jaise `#` ya `$`) jo warning statement text ke body content mein duplicate na ho.
    </details>

4.  **Q4: VTY line command configuring lines `line vty 0 15` mein parameter range integers "0 15" kis structure feature ko show karte hain?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **16 parallel logical connections/sessions** (remote connection channels) jo control and data operations access security manage kar sakte hain.
    </details>

5.  **Q5: Host terminal memory configuration database files configuration process save settings change command backup system standard destination filename parameter kya use karta hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **startup-config** (NVRAM storage).
    </details>

6.  **Q6: Dynamic startup terminal configurations status validation check commands execution ke liye default modes access standard prompt switch status kya show karta hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **Privileged EXEC Mode** (`S1#`).
    </details>

7.  **Q7: Cisco line configurations description system active RAM status files clean reload configuration command run karne ka execution state level kaun sa access method show karta hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **Privileged EXEC Mode** (Typing `reload` command).
    </details>

8.  **Q8: RAM runtime configuration profile database file copy systems standard structure target directory name path address parameter commands execute syntax kya command backup data trigger karega?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **`copy running-config startup-config`** (or shorthand `copy run start` / legacy `write`).
    </details>

9.  **Q9: Global Configuration mode commands navigation prompt `S1(config)#` level interface terminal parameters standard exit system command prompt mode status drop-down check level kya default load karega?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **Privileged EXEC Mode** (`S1#`).
    </details>

10. **Q10: Custom user configuration warning screen messages dynamic terminal login indicators standard terms parameter syntax standard term kya use karta hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **MOTD Banner** (Message of the Day).
    </details>
