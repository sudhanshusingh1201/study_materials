---
title: "Topic 12 - LAN (Local Area Network) & How Its Connected"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🏢 12. LAN (Local Area Network) & How It's Connected

### 📝 Introduction (Intro)
**LAN (Local Area Network)** ek aisa computer network hai jo ek chote aur geographically limited area me digital devices (computers, printers, servers) ko aapas me connect karta hai. Ye limited range aapka ek room, ghar, school laboratory, office building, ya poora college campus ho sakta hai.

#### ⚙️ How It's Connected (LAN Kaise Connect Hota Hai?):
Ek local network ko physically aur logically connect karne ke liye niche likhe components aur steps use kiye jate hain:
1. **Physical Links (Cables & Wireless):** LAN me wired connections ke liye **Cat6 Ethernet cables** (Twisted pair) use hote hain jo devices ke NIC (Network Interface Card) me plug hote hain. Wireless links ke liye **Wi-Fi router/Access Points** radio waves broadcast karte hain.
2. **Central Node (The Switch):** LAN ka backbone ek hardware device hota hai jise **Network Switch** kehte hain. Saare computers aur network nodes ke wire is Switch se aakar connect hote hain. Switch local traffic ko direct manage karta hai using MAC Addresses.
3. **Gateway (The Router):** Switch local devices ko aapas me toh connect kar deta hai, par unhe external networks ya Internet se connect karne ke liye local network me ek **Router** add kiya jata hai. Router LAN aur WAN (Outside Internet) ke beech ek traffic coordinator (Gateway) ka kaam karta hai.
4. **Star Topology Setup:** Modern wired LAN me **Star Topology** structure use hota hai, jahan central key component Switch hota hai aur har computer independently usse connected rehta hai. Agar ek wire toot jaye, toh sirf wahi individual PC network se disconnect hota hai, baaki network normal chalta rehta hai.
5. **Logical IP Allocation:** Router me configured dynamic program **DHCP** har local device ko auto-mapping ke sath ek private IP (jaise `192.168.1.X` format) assign karta hai taaki local data exchange ho sake.

### ➕ Advantages (Fayde)
* **High-Speed Transmission:** LAN ka space limit bahut kam hota hai, isiliye isme network speeds 100 Mbps se lekar **10 Gbps** tak extremely fast ho sakti hain.
* **Resource Sharing Efficiency:** Ek expensive printer ya central storage array (NAS) ko office ke 100 employees share kar sakte hain, jisse huge infrastructure costs bachti hain.
* **Centralized Data Backups:** Saara important company database ek single central storage machine par host hota hai, jisse dynamic database logs aur updates protect karna easy ho jata hai.
* **Low Transmission Errors:** Short distance cabling aur structural isolation ke karan packet loss ya transmission noise na ke barabar hoti hai.

### ➖ Disadvantages (Nuksan)
* **Geographical Coverage Bounds:** LAN ki physical connectivity boundaries maximum **1 se 2 Kilometers** tak hi restrict rehti hain. Usse large scale ke liye MAN/WAN setups lagte hain.
* **Initial Setup Investments:** Switch, router, servers, and high-quality CAT cables purchase karne me shuruati hardware installations charges thode costly hote hain.
* **Security Cross-Contamination:** Agar LAN zone me ek bhi device hack ho jaye ya usme virus aa jaye, toh network parameters secure na hone par virus poore organization ke baaki devices me instantly clone/spread ho sakta hai.
* **Management Requirements:** Large scale corporate LANs ko custom domains aur file permissions ke sath regulate karne ke liye dedicated Network Administrator network operations manage karta hai.

### 📊 Diagram
Ye ek standard local network (LAN) setup ke physical connections aur layouts ko darshata hai:

```mermaid
graph TD
    Internet((Public Internet)) <--> Router[Router / Gateway Device]
    Router <--> Switch[Central LAN Switch]
    
    subgraph Local LAN (Wired Star Network)
        Switch <--> PC1[User Desktop PC 1]
        Switch <--> PC2[User Desktop PC 2]
        Switch <--> Server[(Central Storage Server - NAS)]
        Switch <--> Printer[Shared Laser Printer]
        Switch <--> AP[Wireless Access Point]
    end
    
    subgraph WLAN (Wireless Extension)
        AP -. Radio Waves .- Laptop[User Laptop]
        AP -. Radio Waves .- Mobile[Smartphone]
    end
```

### 💡 Real-world Example (Udaharan)
* **Office Cabin Analogy:**
  - **LAN:** Maan lijiye ek band cabin me 5 colleagues aapas me discussion kar rahe hain aur aapas me physical files exchange kar rahe hain. Ye communication behad fast aur free-of-cost hai bina kisi external telephone lines ke.
  - **Router:** Agar unhe cabin ke bahar kisi doosri city me call karni hai, toh unhe conference table par rakhe intercom/telephone system (Router) ka use karna padega.
* **Cyber Cafe Setup:** Ek computer lab jahan saare PCs rack me rakhe Switch se linked hote hain, aur sabhi local computers single printer aur single heavy internet server bandwidth ko aapas me share karte hain.

### 🚀 Application (Kahan use hota hai?)
* **Home Wi-Fi LANs:** Smart TVs, gaming consoles aur home devices ko internet router se connect karke internal casting/streaming run karna.
* **Intranet File Servers:** Office buildings me sensitive employee database aur confidential documents secure localized server par share karna.
* **Multiplayer LAN Gaming:** Cyber cafes me low latency peer-to-peer multiplayer games setup (jaise CS:GO local rooms) jahan zero delay server performance milta hai.
* **CCTV surveillance:** IP security cameras videos local storage NVR arrays me real-time transfer and record karte hain bina public internet limits waste kiye.

---