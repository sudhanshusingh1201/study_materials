---
title: "Topic 10 - IP Header Fields (32-Bit Grid, Fragmentation, TTL)"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 📦 10. IP Header Fields (32-Bit Grid, Fragmentation, TTL)

IPv4 Header row-by-row structural breakdown:

* **Version (4b):** IPv4 identity (`0100`).
* **IHL (4b):** Internet Header Length (Minimum 5 words = 20 Bytes, Max 15 = 60 Bytes).
* **ToS/DSCP (8b):** QoS packet prioritization.
* **Total Length (16b):** Packet + data size (Max 65,535 bytes).
* **Identification (16b) + Flags (3b) + Fragment Offset (13b):** Packet fragmentation aur reassembly controls.
  - **DF Flag:** Don't Fragment (1 = restrict fragmentation).
  - **MF Flag:** More Fragments (1 = fragments remaining, 0 = last piece).
* **TTL (8b):** Time to Live. Loops check karne ke liye. Har hop par `-1` hota hai. `0` hone par drop.
* **Protocol (8b):** Upper layer type (TCP = 6, UDP = 17, ICMP = 1).
* **Header Checksum (16b):** Header errors dynamic testing.
* **Source/Destination IP (32b each):** Routing addresses.

---