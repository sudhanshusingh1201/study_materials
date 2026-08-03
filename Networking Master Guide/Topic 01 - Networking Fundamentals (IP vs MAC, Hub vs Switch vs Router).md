---
title: "Topic 01 - Networking Fundamentals (IP vs MAC, Hub vs Switch vs Router)"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 🌐 1. Networking Fundamentals (IP vs MAC, Hub vs Switch vs Router)

Networking ka matlab hai: **"Computers ka aapas me judna aur data share karna."**

### 🆔 IP Address vs. MAC Address (Mailing Address vs. DNA)
* **MAC Address (Physical Address):** 
  - Ye aapke device ke NIC card ka permanent address hai. 
  - **Analogy:** Ye aapke computer ka **Aadhar Card number** hai. Ye factory se burn hokar aata hai aur change nahi hota (48-bit hex format, e.g., `00:1A:2B:3C:4D:5E`).
* **IP Address (Logical Address):** 
  - Ye device ka current network address hai. 
  - **Analogy:** Ye aapke **current home address** ki tarah hai. Agar aap Delhi se Mumbai shift ho gaye, toh house address change ho jayega par Aadhar Card (MAC) wahi rahega! (IPv4: 32-bit, IPv6: 128-bit).

### 🔀 Hub vs. Switch vs. Router (The Connectors)

| Device | Dimaag | Kya Karta Hai? | Real-world Analogy |
| :--- | :--- | :--- | :--- |
| **Hub** | 0% (Duffer) | Jo data iske paas aata hai, ye sabhi ports par broadcast (bhej) deta hai. | Ek aisa dost jo group me secret baat bhi chilla kar sabko batata hai. |
| **Switch** | 50% (Smart) | MAC Address yaad rakhta hai aur data sirf usi specific destination port ko bhejta hai. | Class monitor jo usi bachhe ko letter deta hai jiska naam upar likha ho. |
| **Router** | 100% (Master) | Do alag networks को IP Address ke basis par connect karta hai. Best path choose karta hai. | Post Office jo ek city se doosri city mail transfer karta hai. |

---