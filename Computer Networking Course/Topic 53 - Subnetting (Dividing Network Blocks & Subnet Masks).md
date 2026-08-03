---
title: "Topic 53 - Subnetting (Dividing Network Blocks & Subnet Masks)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# ✂️ 53. Subnetting (Dividing Network Blocks & Subnet Masks)

### 📝 Introduction (Intro)
**Subnetting** ek aisi networking technique hai jisme ek single large network address block (IP space) ko multiple smaller logical sub-networks (jinhe **Subnets** kehte hain) me divide/split kiya jata hai. Ye **Network Layer (Layer 3)** level par IP address optimization aur performance improvement ke liye use hota hai.

* **Why we do Subnetting:**
  - **Classful IP Wasting:** Purane Class system me agar kisi company ko 500 IPs chahiye hote toh unhe Class B (`65,536` IPs) lena padta tha, jisse baki saari IPs waste ho jati thi. Subnetting is waste ko rokti hai.
  - **Broadcast Domains Limitation:** Ek bade network me jab ek computer broadcast (sabko message) bhejta hai, toh thousands of systems par background traffic congestion (Broadcast Storm) ho jata hai. Subnetting is domain size ko limit karti hai.
* **The Math behind Subnetting (CIDR Notation):**
  - Subnetting me hum **Host bits** me se borrow karke **Network bits** ko bada karte hain.
  - **Subnet Mask** (e.g. `255.255.255.128` or `/25` CIDR) ye define karta hai ki IP address ka kitna portion network ka hai aur kitna portion hosts ka hai.
  - Formula for Total Usable Hosts per subnet:
    $$\text{Usable Hosts} = 2^{(32 - n)} - 2$$
    *(where $n$ is CIDR subnet mask bits, and we subtract 2 for **Network ID** and **Broadcast ID** which cannot be assigned to hosts).*

### ➕ Advantages (Fayde)
* **Enhanced Network Performance:** Local broadcast traffic restrict hone se collision domains small rehte hain aur net speed bandwidth stable hoti hai.
* **Improved Security:** Subnets ko isolate kiya ja sakta hai. Jaise Finance department aur Guest Wi-Fi subnet ko router level firewall lagakar block kiya ja sakta hai.
* **Efficient IP Address Management:** IP addresses waste nahi hote. Company local requirements ke base par sizes allocate kar sakti hai.

### ➖ Disadvantages (Nuksan)
* **Wastage of Network/Broadcast IPs:** Har subnet split hone par 2 critical IP addresses (Network ID - first address, aur Broadcast ID - last address) system allocations ke liye block ho jate hain (e.g. splitting 1 block into 4 subnets wastes 8 IPs).
* **Management & Configuration Complexity:** Administrator ko complex IP calculations (subnets, ranges, subnet masks) dhyan rakhni padti hain.
* **Hardware dependency:** Subnets ke aalawa aapas me communication karne ke liye **Routers (Layer 3 device)** ki requirement hoti hai.

### 📊 Diagram
Ye layout ek single Class C network block `192.168.1.0/24` ko two subnets `/25` me divide karne ka structure show karta hai:

```
                  [ ORIGINAL IP BLOCK: 192.168.1.0/24 ]
                    (Allows 256 IPs: 0 to 255 total)
                                  |
                                  v (Subnetted by /25)
         /-------------------------------------------------\
        |                                                 |
[ SUBNET 1: 192.168.1.0/25 ]                      [ SUBNET 2: 192.168.1.128/25 ]
- Subnet Mask: 255.255.255.128                    - Subnet Mask: 255.255.255.128
- Network ID: 192.168.1.0                         - Network ID: 192.168.1.128
- Broadcast ID: 192.168.1.127                     - Broadcast ID: 192.168.1.255
- Usable IPs: 192.168.1.1 to .126                 - Usable IPs: 192.168.1.129 to .254
- Total Usable Hosts: 126                         - Total Usable Hosts: 126
```

### 💡 Real-world Example (Udaharan)
* **Big Office Hall Partitions Metaphor:**
  - Maan lijiye ek bahut bada building floor hall (Single Network) hai jisme 200 log baithe hain. Agar wahan koi boundary partition (No subnetting) na ho, toh jab bhi koi ek insan jor se chillayega (Broadcast), baki 199 log disturb honge (Network lag/Broadcast Storm).
  - Humne hall ke beech me wooden partitions and walls laga kar 4 small rooms (Subnets: HR room, Sales room, Tech room, Finance room) me divide kar diya. Ab HR room ka shor baki rooms me nahi jayega (Traffic optimization).
  - Agar HR worker ko Finance worker se baat karni hai, toh use room door se nikal kar corridor pass karna hoga. Yahan door/corridor humara **Router** hai.

### 🚀 Application (Kahan use hota hai?)
* **Corporate IT Infrastructure:** Separating Employee, Servers, Printers, and Guest networks.
* **Cloud VPC Subnetting (AWS/GCP/Azure):** Creating Public subnets (web servers) and Private subnets (databases).
* **ISP Customer Allocations:** Subnetting a massive block to assign customized IP chunks to clients.

---