---
title: "Topic 14 - Access & Trunk Ports (VLAN Port Modes, 802.1Q, Native VLAN)"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 🔌 14. Access & Trunk Ports (VLAN Port Modes, 802.1Q, Native VLAN)

### 1. Access Port:
* Assigned to a single VLAN (e.g. VLAN 10).
* Used for PCs, routers.
* Traffic leaves the port **untagged** (normal frame).

### 2. Trunk Port:
* Connects Switch to Switch or Switch to Router.
* Carries multiple VLAN traffic.
* Uses **IEEE 802.1Q** tagging to add 4-byte tags with VLAN IDs to the frames.
* **Native VLAN:** Untagged traffic trunk link map.

### 🛠️ Cisco CLI commands:
```text
! Access port setup
interface Fa0/1
 switchport mode access
 switchport access vlan 10

! Trunk port setup
interface Gi0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20
```
---

> [!NOTE]
> Bhai, ye master note completely ready hai. Aap is note ke sections ko cross-reference links ke sath easily navigate kar sakte hain!

---