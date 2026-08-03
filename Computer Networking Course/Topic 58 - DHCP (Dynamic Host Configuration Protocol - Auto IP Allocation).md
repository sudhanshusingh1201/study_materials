---
title: "Topic 58 - DHCP (Dynamic Host Configuration Protocol - Auto IP Allocation)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🔌 58. DHCP (Dynamic Host Configuration Protocol - Auto IP Allocation)

### 📝 Introduction (Intro)
**DHCP (Dynamic Host Configuration Protocol)** ek Client-Server model par kaam karne wala **Application Layer (Layer 7)** protocol hai. Iska main kaam network par connect hone wali devices (laptops, phones, smart TVs) ko automatically IP addresses aur baki configuration parameters (Subnet Mask, Default Gateway, DNS Servers) assign karna hai. Ye **UDP Port 67 (Server)** aur **UDP Port 68 (Client)** use karta hai.

#### ⚙️ The DORA Process (How it Works):
Jab koi new client device network se connect hoti hai, toh vo IP address lene ke liye 4-step sequence complete karti hai jise **DORA** kehte hain:
1. **D - Discover (Broadcast):** Client network par ek "DHCP Discover" message broadcast (sabko send) karta hai: *"Kya network me koi DHCP Server hai? Mujhe ek IP address chahiye."*
2. **O - Offer (Unicast/Broadcast):** DHCP Server range check karke client ko ek "DHCP Offer" message bhejta hai: *"Haan, mere pass ye IP address `192.168.1.50` khali hai. Kya tum ye loge?"*
3. **R - Request (Broadcast):** Client baki servers ko inform karne aur confirmation ke liye "DHCP Request" message bhejta hai: *"Haan, mujhe ye IP `192.168.1.50` pasand hai. Please ise mere liye reserve kar do."*
4. **A - Acknowledge (Unicast/Broadcast):** Server transaction close karke "DHCP ACK" message bhejta hai: *"Done! Ye IP ab tumhara hai `Lease Time` (e.g., 24 hours) ke liye. Ye lo tumhara Subnet mask aur Default Gateway."*

### ➕ Advantages (Fayde)
* **Automated IP Management:** Network administrator ko manually har device ke pass jaakar static IP configuration likhne ki jarurat nahi padti, jisse hours of work save hota hai.
* **Zero IP Conflict Risks:** DHCP server internal records tracking database maintain rakhta hai, isliye do computer machines ko glti se same IP assign (IP conflict issue) nahi ho sakta.
* **Seamless Mobile Roaming:** Laptops/mobiles users jab ek network office building se disconnect hokar dusri building Wi-Fi network par jaate hain, toh unhe bina restart kiye instantly naya IP mil jata hai.

### ➖ Disadvantages (Nuksan)
* **Single Point of Failure:** Agar main DHCP Server network crashed/down ho jaye, toh koi bhi new device IP address obtain nahi kar payegi aur local network connection access completely band ho jayega.
* **Rogue DHCP Server Security Risk:** Agar hacker network me koi unauthorized/fake DHCP server connect kar de, toh vo clients ko galat default gateway aur fake DNS server range de sakta hai, jisse dynamic traffic redirect (Man-in-the-Middle attacks) ho sakte hain.
* **Address Pool Exhaustion:** Public spots (jaise Airport ya Cafes Wi-Fi) me agar high quantity devices connect/disconnect hoti hain, toh empty IPs pool range khatam ho sakti hai, jisse new users ko access nahi milta.

### 📊 Diagram
Ye layout DORA process ke messages flow timing aur ports usage sequence mappings ko show karta hai:

```
[ CLIENT DEVICE ]                                                [ DHCP SERVER ]
(UDP Port: 68)                                                   (UDP Port: 67)
       |                                                               |
       |========== 1. Discover (IP: 0.0.0.0 -> 255.255.255.255) ======>| (Broadcast)
       |                                                               |
       |<========= 2. Offer (Offered IP: 192.168.1.50) ===============| (Unicast/Broadcast)
       |                                                               |
       |========== 3. Request (Please lock 192.168.1.50) =============>| (Broadcast)
       |                                                               |
       |<========= 4. ACK (Confirmed! Lease starts now) ===============| (Unicast/Broadcast)
```

### 💡 Real-world Example (Udaharan)
* **University Hostel Room Allocation Desk Analogy:**
  - Maan lijiye aap university hostel (Network) me rahne aaye. Agar aap bina warden se puche seedhe kisi bhi room (IP address) me rahne chale jayein, toh ho sakta hai us room me pehle se koi reh raha ho, jisse jhagda (IP Address Conflict) ho jayega.
  - Isliye hostel administration ne ek warden office desktop setup kiya jise **Hostel Allocation Desk** (DHCP Server) kehte hain.
  - **Discover:** Aap desk par jaakar puchte hain: *"Warden, kya koi vacant room mil sakta hai?"*
  - **Offer:** Warden register book check karke bolta hai: *"Haan, Room 302 vacant hai. Uska ye key card hai."*
  - **Request:** Aap reply karte hain: *"Perfect! Warden, main Room 302 lock kar raha hun."*
  - **ACK:** Warden register me aapka naam likhta hai aur bolta hai: *"Done, ye room aapko 1 Semester (Lease Time) ke liye allot kiya jata hai. Uske baad renew karwana hoga."*

### 🚀 Application (Kahan use hota hai?)
* **Home Wi-Fi routers access pools:** Router's internal DHCP daemon automatically assigning IPs to newly connected smartphones.
* **Hotels / Airports Guest Wi-Fi Networks:** Dynamically sharing small ranges blocks of IPs for short lease periods.
* **Corporate Enterprise networks infrastructure:** Large scale MS Windows Server Active Directory DHCP role distributing DNS config to end user machines.

---