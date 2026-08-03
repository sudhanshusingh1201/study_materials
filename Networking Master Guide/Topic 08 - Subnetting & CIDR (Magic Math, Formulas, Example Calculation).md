---
title: "Topic 08 - Subnetting & CIDR (Magic Math, Formulas, Example Calculation)"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 🔪 8. Subnetting & CIDR (Magic Math, Formulas, Example Calculation)

Bhai, IP ranges ki wastage rokne ke liye ek bade network block ko borrow host bits ki madad se chote parts me divide karna **Subnetting** kahlata hai.

### 🧮 Formulas:
* **Subnets =** \(2^n\) *(n = borrowed network bits)*
* **Hosts per Subnet =** \(2^h - 2\) *(h = remaining host bits. -2 for Network & Broadcast ID)*
* **Block Size (Magic Number) =** \(256 - \text{Subnet Mask value}\)

### 📝 Example: `192.168.1.0/26`
* **CIDR `/26`:** 26 network bits = `255.255.255.192` (binary last octet: `11000000`).
* **Borrow bits (n):** Class C default `/24` tha, so \(n = 26 - 24 = 2\). Subnets = \(2^2 = 4\).
* **Remaining Host bits (h):** \(32 - 26 = 6\). Usable Hosts = \(2^6 - 2 = 62\).
* **Block Size:** \(256 - 192 = 64\). (Subnet steps: 0, 64, 128, 192).

---