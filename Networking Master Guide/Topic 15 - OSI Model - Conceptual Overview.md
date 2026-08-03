---
title: "Topic 15 - OSI Model - Conceptual Overview"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 🌐 15. OSI Model - Conceptual Overview

OSI stands for **Open Systems Interconnection**. Ye 1984 me ISO dwara banaya gaya ek theoretical reference model hai, jo batata hai ki data aakhir network par kaise travel karta hai.

### 🏛️ Why it was created?
Pehle har company ke devices proprietary standards use karte the (e.g. IBM computers only talked to IBM). Vendor compatibility ko standardise karne ke liye OSI model design kiya gaya.

### 📦 The Concept of Layering (Courier Analogy)
Pure communication ko **7 layers** me break kiya gaya hai.
* **Modularity:** Niche ki layer change hone par upar ki layer standard me koi farq nahi padta (e.g. Wi-Fi se Ethernet switch karne par Chrome web browser nahi badalna padta).
* **Easy Troubleshooting:** Har layer ka specialized work hai, isliye network problems easily identify ki ja sakti hain.

### 🔄 Data Encapsulation & Decapsulation
* **Encapsulation:** Sender side par data top-to-bottom flow karta hai aur har layer apna header wrap karti hai.
* **Decapsulation:** Receiver side par data bottom-to-top flow karta hai aur har layer check karke header strip/remove karti hai.