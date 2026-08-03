---
title: Nmap Kali Linux Interactive Learning Journal
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
created: 2026-07-24
type: journal
---

# 🐧 Nmap Kali Linux Interactive Learning Journal

Ye notebook hamare live learning sessions ko track karne ke liye hai. Yahan sabhi topics, Kali Linux ke practical commands, quizzes, aur assignments save hote rahenge.

---

## 📚 Table of Contents (TOC)

Niche hamare ab tak ke cover kiye gaye sabhi **36 topics** ki index list hai:

- **Topic 1:** 🌐 [[Nmap Learning Session/Topic 01 - What is Nmap|What is Nmap?]]
- **Topic 2:** 🌐 [[Nmap Learning Session/Topic 02 - What is a Port Scan|What is a Port Scan?]]
- **Topic 3:** 🌐 [[Nmap Learning Session/Topic 03 - What is ifconfig|What is ifconfig?]]
- **Topic 4:** 🌐 [[Nmap Learning Session/Topic 04 - What is Wireshark|What is Wireshark?]]
- **Topic 5:** 🌐 [[Nmap Learning Session/Topic 05 - What is eth0|What is eth0?]]
- **Topic 6:** 🌐 [[Nmap Learning Session/Topic 06 - Nmap UDP Scan (-sU)|Nmap UDP Scan (-sU)]]
- **Topic 7:** 🌐 [[Nmap Learning Session/Topic 07 - Nmap TCP Connect Scan (-sT)|Nmap TCP Connect Scan (-sT)]]
- **Topic 8:** 🌐 [[Nmap Learning Session/Topic 08 - Nmap Scan All Ports (-p-)|Nmap Scan All Ports (-p-)]]
- **Topic 9:** 🌐 [[Nmap Learning Session/Topic 09 - Host Discovery with Ping Sweep (-sn)|Host Discovery with Ping Sweep (-sn)]]
- **Topic 10:** 🌐 [[Nmap Learning Session/Topic 10 - Host Discovery Techniques & Flags (Deep Dive)|Host Discovery Techniques & Flags (Deep Dive)]]
- **Topic 11:** 🌐 [[Nmap Learning Session/Topic 11 - Nmap No Port Scan (-sn) - Deep Dive|Nmap No Port Scan (-sn) - Deep Dive]]
- **Topic 12:** 🌐 [[Nmap Learning Session/Topic 12 - Linux Piping & Grepping (man nmap grep sn)|Linux Piping & Grepping (man nmap | grep sn)]]
- **Topic 13:** 🌐 [[Nmap Learning Session/Topic 13 - Linux Case-Insensitive Search & Nmap Ping Options (man nmap grep -i ping)|Linux Case-Insensitive Search & Nmap Ping Options (man nmap | grep -i "ping")]]
- **Topic 14:** 🌐 [[Nmap Learning Session/Topic 14 - Nmap -Pn (No Ping) Scan with Real IP Address Example|Nmap -Pn (No Ping) Scan with Real IP Address Example]]
- **Topic 15:** 🌐 [[Nmap Learning Session/Topic 15 - OS and Service Version Scanning (-O, -sV, -A)|OS and Service Version Scanning (-O, -sV, -A)]]
- **Topic 16:** 🌐 [[Nmap Learning Session/Topic 16 - OS & Service Version Scan on Localhost (nmap -O -sV localhost)|OS & Service Version Scan on Localhost (nmap -O -sV localhost)]]
- **Topic 17:** 🌐 [[Nmap Learning Session/Topic 17 - Nmap Aggressive Scan (-A)|Nmap Aggressive Scan (-A)]]
- **Topic 18:** 🌐 [[Nmap Learning Session/Topic 18 - TCP Connect Scan vs TCP SYN Stealth Scan (-sT vs -sS)|TCP Connect Scan vs TCP SYN Stealth Scan (-sT vs -sS)]]
- **Topic 19:** 🌐 [[Nmap Learning Session/Topic 19 - Nmap Output Formats & Verbosity Levels (-oN, -oX, -oG, -oA, -v, -d)|Nmap Output Formats & Verbosity Levels (-oN, -oX, -oG, -oA, -v, -d)]]
- **Topic 20:** 🌐 [[Nmap Learning Session/Topic 20 - How to navigate Nmap Manual Pages (man nmap)|How to navigate Nmap Manual Pages (man nmap)]]
- **Topic 21:** 🌐 [[Nmap Learning Session/Topic 21 - Linux Directory Listing (ls -al)|Linux Directory Listing (ls -al)]]
- **Topic 22:** 🌐 [[Nmap Learning Session/Topic 22 - Reading Grepable Nmap Files (cat nmap_stealth.gnmap)|Reading Grepable Nmap Files (cat nmap_stealth.gnmap)]]
- **Topic 23:** 🌐 [[Nmap Learning Session/Topic 23 - Nmap Normal Output Format (-oN)|Nmap Normal Output Format (-oN)]]
- **Topic 24:** 🌐 [[Nmap Learning Session/Topic 24 - Inverse TCP Flag Scanning (-sN, -sF, -sX)|Inverse TCP Flag Scanning (-sN, -sF, -sX)]]
- **Topic 25:** 🌐 [[Nmap Learning Session/Topic 25 - Nmap FIN Scan & TCP FIN Flag (-sF)|Nmap FIN Scan & TCP FIN Flag (-sF)]]
- **Topic 26:** 🌐 [[Nmap Learning Session/Topic 26 - Nmap Xmas Scan (-sX)|Nmap Xmas Scan (-sX)]]
- **Topic 27:** 🌐 [[Nmap Learning Session/Topic 27 - Nmap Null Scan (-sN)|Nmap Null Scan (-sN)]]
- **Topic 28:** 🌐 [[Nmap Learning Session/Topic 28 - Nmap Reason Flag (--reason)|Nmap Reason Flag (--reason)]]
- **Topic 29:** 🌐 [[Nmap Learning Session/Topic 29 - Nmap Firewall Detection with TCP ACK Scan (-sA)|Nmap Firewall Detection with TCP ACK Scan (-sA)]]
- **Topic 30:** 🌐 [[Nmap Learning Session/Topic 30 - Nmap Firewall Evasion (Decoys, MTU, and Fragmentation)|Nmap Firewall Evasion (Decoys, MTU, and Fragmentation)]]
- **Topic 31:** 🌐 [[Nmap Learning Session/Topic 31 - Nmap Scan Timing and Performance Templates (-T0 to -T5)|Nmap Scan Timing and Performance Templates (-T0 to -T5)]]
- **Topic 32:** 🌐 [[Nmap Learning Session/Topic 32 - Nmap Parallelism & Performance Customization (--min-parallelism, --max-parallelism)|Nmap Parallelism & Performance Customization (--min-parallelism, --max-parallelism)]]
- **Topic 33:** 🌐 [[Nmap Learning Session/Topic 33 - Nmap Host Group Sizes (--min-hostgroup, --max-hostgroup)|Nmap Host Group Sizes (--min-hostgroup, --max-hostgroup)]]
- **Topic 34:** 🌐 [[Nmap Learning Session/Topic 34 - Nmap Host Timeout (--host-timeout)|Nmap Host Timeout (--host-timeout)]]
- **Topic 35:** 🌐 [[Nmap Learning Session/Topic 35 - Nmap Scan Delay (--scan-delay, --max-scan-delay)|Nmap Scan Delay (--scan-delay, --max-scan-delay)]]
- **Topic 36:** 🌐 [[Nmap Learning Session/Topic 36 - Nmap Packet Rate Controls (--min-rate, --max-rate)|Nmap Packet Rate Controls (--min-rate, --max-rate)]]

---
