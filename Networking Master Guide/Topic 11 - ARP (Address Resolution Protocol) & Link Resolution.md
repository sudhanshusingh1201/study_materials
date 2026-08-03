---
title: "Topic 11 - ARP (Address Resolution Protocol) & Link Resolution"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 🕵️‍♂️ 11. ARP (Address Resolution Protocol) & Link Resolution

Layer 2 MAC aur Layer 3 IP ke coordinates ko resolve karne ka protocol.

### 🔄 The ARP Flow (PC A wants to talk to PC B):
1. **ARP Request:** PC A sends a broadcast frame (`FF:FF:FF:FF:FF:FF`) asking: *"Who has IP 192.168.1.20? Tell PC A."*
2. **ARP Reply:** PC B sees its IP, sends a direct **unicast** reply back to A with its MAC address.
3. **ARP Cache:** PC A saves this mapping in its local cache (view using `arp -a`) to avoid redundant broadcasts.
4. **Gratuitous ARP:** Device alerts the LAN about its own IP/MAC mapping without request (IP conflict detection).

---