---
title: "Topic 12 - ARP Spoofing Poisoning & Security (MITM, DAI)"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# ☠️ 12. ARP Spoofing / Poisoning & Security (MITM, DAI)

ARP has no authentication. Attacker iski stateless vulnerability ka advantage leta hai.

### ⚔️ The MITM Attack:
Hacker fake ARP replies send karta hai:
* Victim ko bolta hai: *"I am the Gateway/Router, my MAC is HH (Hacker)."*
* Router ko bolta hai: *"I am the Victim, my MAC is HH."*
Both caches poison ho jate hain aur sara traffic hacker ke device se route hone lagta hai (**Man-in-the-Middle**).

### 🛡️ Defenses:
* **DAI (Dynamic ARP Inspection):** Switch interfaces validated against trusted DHCP snooping databases to drop fake ARP replies.
* **Static ARP:** Manual bindings.
* **VPN:** Data payloads encryption.

---