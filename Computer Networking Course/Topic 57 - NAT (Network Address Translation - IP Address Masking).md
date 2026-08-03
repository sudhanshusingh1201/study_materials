---
title: "Topic 57 - NAT (Network Address Translation - IP Address Masking)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🌐 57. NAT (Network Address Translation - IP Address Masking)

### 📝 Introduction (Intro)
**NAT (Network Address Translation)** ek aisi networking technology hai jo **Network Layer (Layer 3)** aur **Transport Layer (Layer 4)** par kaam karti hai. Iska main kaam local private networks me use hone wale **Private IP addresses** ko internet par transmit hone wale **Public IP addresses** me translate/convert karna hai.

* **Why we need NAT:**
  - **IPv4 Shortage:** Duniya me billions of devices hain par IPv4 addresses sirf 4.3 billion hi hain. NAT ki madad se ek single Public IP address ko multiple devices aapas me share karke internet chala sakti hain.
  - **Security Barrier:** Private IP addresses (`192.168.x.x`, `10.x.x.x`, `172.16.x.x`) internet par routable nahi hote. NAT router in local IPs ko hide rakhta hai taaki outside world direct internal systems ko ping/hack na kar sake.
* **Primary Types of NAT:**
  1. **Static NAT (1-to-1):** Ek single Private IP ko permanently ek single Public IP me map kiya jata hai (mostly used for web hosting servers).
  2. **Dynamic NAT (Pool-to-Pool):** Router ke pass public IPs ka ek pool hota hai. Jab koi local device request bhejti hai, toh pool me se jo public IP free hoti hai, vo use temporary allocate ho jati hai.
  3. **PAT (Port Address Translation) / NAT Overload:** Sabse popular type. Isme local network ki hundreds of devices ko **sirf ek single Public IP** par map kar diya jata hai. Har device ke sessions ko unique **Source Port Numbers** (Layer 4) dekar differ kiya jata hai.

### ➕ Advantages (Fayde)
* **Conservation of IPv4 Space:** Ek single internet connection link line par pure home ya office local networks share ho jate hain, jisse public IPs waste nahi hote.
* **Network Security Isolation:** External scans database local clients IP structure read nahi kar sakte, since public networks me sirf router public address visible hota hai.
* **Flexibility in Internal Addressing:** Agar hum local devices ke IP scheme change karte hain, toh hume bahar public range registers update karne ki jarurat nahi padti.

### ➖ Disadvantages (Nuksan)
* **Translation Latency (Delay):** Router memory engine ko continuous packets incoming/outgoing headers parse karke Source IP aur Port addresses rewrite recalculate (checksum updates) karne padte hain, jisse minor transmission delay aata hai.
* **End-to-End Traceability Loss:** Packet trace history logs (tracert) check karne par destination se original sender host machine address determine karna complex ho jata hai.
* **Issues with IPsec & VoIP Protocols:** Kuch protocols (jaise SIP/VoIP calls, IPsec VPN tunnels) IP/Port bindings security checks verify karte hain, jo NAT translational modifications ke chalte block crash ho jate hain.

### 📊 Diagram
Ye layout local LAN devices ka PAT/NAT overload translate sequence public network routing step mappings ko show karta hai:

```
[ LOCAL PRIVATE NETWORK ]           [ NAT ROUTER ]               [ PUBLIC INTERNET ]
(Private IPs - Local LAN)           (NAT Table Map)             (Public IP Target)
                                           |
  PC 1 (192.168.1.5:8000) ---------------> | Converts source to:
                                           | [103.45.67.8:9001] ========> Web Server (Google)
  PC 2 (192.168.1.8:8000) ---------------> | Converts source to:
                                           | [103.45.67.8:9002] ========> Web Server (Google)

  -------------------------------------------------------------------------------------
  | Local IP (Private)    | Local Port  | Translated IP (Public) | Translated Port    |
  |-----------------------|-------------|------------------------|--------------------|
  | 192.168.1.5           | 8000        | 103.45.67.8            | 9001               |
  | 192.168.1.8           | 8000        | 103.45.67.8            | 9002               |
  -------------------------------------------------------------------------------------
```

### 💡 Real-world Example (Udaharan)
* **Corporate Office Telephone System Metaphor:**
  - Maan lijiye ek bade building office me 100 employees baithe hain. Har employee ke desk par ek intercom telephone unit (Private IP) hai, jiska extension number 101, 102... hai. In numbers par bahar ka koi insaan direct dial call nahi kar sakta.
  - Company ke pass sirf ek hi main public telephone number: **9876543210** (Public IP) hai.
  - Jab employee 101 bahar call karega, toh receptionist switchboard panel (NAT Router) local extension number ko hide karke main office number aur call index (Port extension) map karke call forward karega.
  - Bahar ke insaan ko caller ID me sirf main office number dikhega. Jab wo wapas call karega, toh switchboard operator check karega ki kis extension ke liye reply aaya hai aur use us target desk line (Private IP) par ring transfer kar dega.

### 🚀 Application (Kahan use hota hai?)
* **Home Wi-Fi Routers:** Allowing all mobile/laptops in home to connect internet via single ISP optical line subscription IP.
* **Cloud VPC Architecture Gateways:** NAT Gateways routing private instances databases internet requests to fetch updates.
* **Container Virtualization (Docker):** Forwarding docker bridge network traffic through virtual interface hosts to host physical connections.

---