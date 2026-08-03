---
title: "Topic 07 - Classes of IP Addresses & IP Addressing (Classes A-E, Reserved IPs)"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 🏢 7. Classes of IP Addresses & IP Addressing (Classes A-E, Reserved IPs)

IPv4 addresses standard class divisions:

* **Class A:** `1.0.0.0` to `126.255.255.255` | Default Mask: `/8` (`255.0.0.0`) | 16M+ hosts.
* **Class B:** `128.0.0.0` to `191.255.255.255` | Default Mask: `/16` (`255.255.0.0`) | 65,534 hosts.
* **Class C:** `192.0.0.0` to `223.255.255.255` | Default Mask: `/24` (`255.255.255.0`) | 254 hosts.
* **Class D (Multicast):** `224.0.0.0` to `239.255.255.255` | No mask.
* **Class E (Experimental):** `240.0.0.0` to `255.255.255.255` | No mask.

### 🚫 Reserved Networks:
* **`127.0.0.0/8` (Loopback):** Local network diagnostics aur ping tests ke liye (e.g. `127.0.0.1`).
* **`169.254.0.0/16` (APIPA):** DHCP fail hone par system automatically ye IP le leta hai local communication ke liye.

---