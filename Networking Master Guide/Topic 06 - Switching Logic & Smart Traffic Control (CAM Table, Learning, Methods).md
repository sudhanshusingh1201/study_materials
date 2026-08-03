---
title: "Topic 06 - Switching Logic & Smart Traffic Control (CAM Table, Learning, Methods)"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 🔀 6. Switching Logic & Smart Traffic Control (CAM Table, Learning, Methods)

Switches smart routing ke liye **CAM (Content Addressable Memory) Table** update karte hain.

### 🔄 The 4 Core Actions:
1. **Learn:** Frame ke **Source MAC** ko dekh kar use incoming port ke sath CAM table me register karna.
2. **Forward:** **Destination MAC** table me milne par, use sirf usi specific target port par bhejna.
3. **Filter:** Agar source aur destination dono ek hi port par hain, toh data aage forward na karke drop karna.
4. **Flood:** Agar Destination MAC table me nahi hai (**Unknown Unicast**) ya Broadcast address (`FF:FF:FF:FF:FF:FF`) hai, toh incoming port chhod kar baki sabhi ports par forward karna.

### ⚡ Switching Forwarding Methods:
* **Store-and-Forward:** Pure frame ko buffer me receive karke FCS error-check karta hai, fir forward karta hai. (Sabse safe, high latency).
* **Cut-Through:** Sirf first 6 bytes (Destination MAC) read karte hi forwarding start kar deta hai. (Fastest, does not check errors).
* **Fragment-Free:** First 64 bytes check karke forward karta hai taaki collision errors se bacha ja sake. (Good middle ground).

---