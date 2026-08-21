---
title: Course on Kali Linux
tags:
  - kali-linux
  - cybersecurity
  - ethical-hacking
  - learning-session
created: 2026-07-29
type: course
status: In Progress
---

# 🐧 Course on Kali Linux (Hinglish)

Bhai, ye aapka **Kali Linux Course** note hai! 🚀
Yahan hum Kali Linux ke saare basic se advanced levels tak ke topics ko full detail me cover karenge. Aap jo bhi topic doge, main use simple Hinglish me, badhiya real-world analogies, code blocks aur step-by-step guides ke sath explain karke yahan update karta jaunga.

---

## 🗺️ Course Visual Roadmap

Aapke course topics ka visual mind-map niche diya gaya hai. Aap is visual roadmap se poore course ka path samajh sakte hain:

```mermaid
flowchart TD
    classDef cybersecurity fill:#ff4444,stroke:#330000,stroke-width:2px,color:#fff;
    classDef network fill:#33bbee,stroke:#002244,stroke-width:2px,color:#fff;
    classDef linux fill:#00cc66,stroke:#003311,stroke-width:2px,color:#fff;
    classDef command fill:#ffaa00,stroke:#332200,stroke-width:2px,color:#fff;

    Main["🎓 Kali Linux Mastery Roadmap"] --> Mod1["💀 Cyber Security Basics"]
    Main --> Mod2["🌐 Networking & Anonymity"]
    Main --> Mod3["💻 Linux OS Basics"]
    Main --> Mod4["🛠️ Essential Commands"]

    %% Group 1: Cyber Security Basics
    Mod1 --> T1["Topic 1: What is Hacking"]:::cybersecurity
    Mod1 --> T2["Topic 2: Reconnaissance"]:::cybersecurity
    Mod1 --> T3["Topic 3: DoS & DDoS"]:::cybersecurity
    Mod1 --> T4["Topic 4: FUD Payloads"]:::cybersecurity
    Mod1 --> T5["Topic 5: RAT"]:::cybersecurity
    Mod1 --> T6["Topic 6: Rootkits"]:::cybersecurity
    Mod1 --> T7["Topic 7: Phishing"]:::cybersecurity
    Mod1 --> T8["Topic 8: SQL Injection"]:::cybersecurity
    Mod1 --> T13["Topic 13: Keyloggers"]:::cybersecurity

    %% Group 2: Networking & Anonymity
    Mod2 --> T9["Topic 9: VPN"]:::network
    Mod2 --> T10["Topic 10: Proxies"]:::network
    Mod2 --> T11["Topic 11: Tor Network"]:::network
    Mod2 --> T12["Topic 12: VPS"]:::network
    Mod2 --> T15["Topic 15: Firewalls"]:::network

    %% Group 3: Linux OS Basics
    Mod3 --> T14["Topic 14: Linux Terminal"]:::linux
    Mod3 --> T17["Topic 17: Update Kali"]:::linux
    Mod3 --> T29["Topic 29: Shell Scripts"]:::linux
    Mod3 --> T38["Topic 38: File Hierarchy (FHS)"]:::linux

    %% Group 4: Essential Commands
    Mod4 --> T18["cd (Change Dir)"]:::command
    Mod4 --> T19["ls (List)"]:::command
    Mod4 --> T20["pwd (Current Path)"]:::command
    Mod4 --> T21["cp (Copy)"]:::command
    Mod4 --> T22["cat (Read/Write)"]:::command
    Mod4 --> T23["nano (Editor)"]:::command
    Mod4 --> T24["less (Pager)"]:::command
    Mod4 --> T25["grep (Search)"]:::command
    Mod4 --> T26["echo (Print)"]:::command
    Mod4 --> T27["chown (Owner)"]:::command
    Mod4 --> T28["chmod (Permissions)"]:::command
    Mod4 --> T30["rm (Delete)"]:::command
    Mod4 --> T31["man/help"]:::command
    Mod4 --> T32["mv (Move/Rename)"]:::command
    Mod4 --> T16["Topic 16: Reverse Shells"]:::command
    Mod4 --> T33["file (File Type)"]:::command
    Mod4 --> T34["touch (Create/Timestamp)"]:::command
    Mod4 --> T35["rename (Bulk Rename)"]:::command
    Mod4 --> T36["man sections (Search)"]:::command
    Mod4 --> T37["file contents (head/tail)"]:::command
```

## 📚 Table of Contents (TOC)

Niche hamare course ke topics ki index list hai. Kisi bhi topic par click karke aap uske notes padh sakte hain:

- **Topic 1:** 💀 [[Kali Linux Course/Topic 01 - What is Hacking|What is Hacking?]]
- **Topic 2:** 🔍 [[Kali Linux Course/Topic 02 - Footprinting & Reconnaissance|Footprinting & Reconnaissance]]
- **Topic 3:** 💥 [[Kali Linux Course/Topic 03 - DoS & DDoS Attacks|DoS & DDoS Attacks]]
- **Topic 4:** 🛡️ [[Kali Linux Course/Topic 04 - FUD Payloads (Fully Undetectable Malware)|FUD Payloads (Fully Undetectable Malware)]]
- **Topic 5:** 🐀 [[Kali Linux Course/Topic 05 - RAT (Remote Access Trojan)|RAT (Remote Access Trojan)]]
- **Topic 6:** 👻 [[Kali Linux Course/Topic 06 - Rootkits (Stealth & Persistence Malware)|Rootkits (Stealth & Persistence Malware)]]
- **Topic 7:** 🎣 [[Kali Linux Course/Topic 07 - Phishing (Social Engineering Attacks)|Phishing (Social Engineering Attacks)]]
- **Topic 8:** 🗄️ [[Kali Linux Course/Topic 08 - SQL Injection (SQLi)|SQL Injection (SQLi)]]
- **Topic 9:** 🌐 [[Kali Linux Course/Topic 09 - VPN (Virtual Private Network)|VPN (Virtual Private Network)]]
- **Topic 10:** 🔗 [[Kali Linux Course/Topic 10 - Proxy Servers & Proxychains|Proxy Servers & Proxychains]]
- **Topic 11:** 🧅 [[Kali Linux Course/Topic 11 - Tor Network (The Onion Router)|Tor Network (The Onion Router)]]
- **Topic 12:** 🖥️ [[Kali Linux Course/Topic 12 - VPS (Virtual Private Server)|VPS (Virtual Private Server)]]
- **Topic 13:** ⌨️ [[Kali Linux Course/Topic 13 - Keyloggers (Keystroke Loggers)|Keyloggers (Keystroke Loggers)]]
- **Topic 14:** 💻 [[Kali Linux Course/Topic 14 - Linux Terminal - Basic Commands & Concepts|Linux Terminal - Basic Commands & Concepts]]
- **Topic 15:** 🧱 [[Kali Linux Course/Topic 15 - Firewalls (Network Security Filters)|Firewalls (Network Security Filters)]]
- **Topic 16:** 🐚 [[Kali Linux Course/Topic 16 - Reverse Shells (Connect-Back Shells)|Reverse Shells (Connect-Back Shells)]]
- **Topic 17:** 🔄 [[Kali Linux Course/Topic 17 - How to Update Kali Linux & Packages|How to Update Kali Linux & Packages]]
- **Topic 18:** 📁 [[Kali Linux Course/Topic 18 - Linux Command cd (Change Directory)|Linux Command: cd (Change Directory)]]
- **Topic 19:** 👁️ [[Kali Linux Course/Topic 19 - Linux Command ls (List Directory Contents)|Linux Command: ls (List Directory Contents)]]
- **Topic 20:** 📍 [[Kali Linux Course/Topic 20 - Linux Command pwd (Print Working Directory)|Linux Command: pwd (Print Working Directory)]]
- **Topic 21:** 📄 [[Kali Linux Course/Topic 21 - Linux Command cp (Copy Files and Directories)|Linux Command: cp (Copy Files and Directories)]]
- **Topic 22:** 📣 [[Kali Linux Course/Topic 22 - Linux Command cat (Concatenate)|Linux Command: cat (Concatenate)]]
- **Topic 23:** 📝 [[Kali Linux Course/Topic 23 - Linux Terminal Editor nano|Linux Terminal Editor: nano]]
- **Topic 24:** 📖 [[Kali Linux Course/Topic 24 - Linux Command less (Terminal Pager)|Linux Command: less (Terminal Pager)]]
- **Topic 25:** 🔍 [[Kali Linux Course/Topic 25 - Linux Command grep (Global Regular Expression Print)|Linux Command: grep (Global Regular Expression Print)]]
- **Topic 26:** 🗣️ [[Kali Linux Course/Topic 26 - Linux Command echo (Print Text)|Linux Command: echo (Print Text)]]
- **Topic 27:** 👑 [[Kali Linux Course/Topic 27 - Linux Command chown (Change Owner)|Linux Command: chown (Change Owner)]]
- **Topic 28:** 🔑 [[Kali Linux Course/Topic 28 - Linux Command chmod (Change Permissions)|Linux Command: chmod (Change Permissions)]]
- **Topic 29:** 🐚 [[Kali Linux Course/Topic 29 - What is a Shell Script (.sh) and How to Run it|What is a Shell Script (.sh) and How to Run it?]]
- **Topic 30:** 🗑️ [[Kali Linux Course/Topic 30 - Linux Command rm (Remove Files and Directories)|Linux Command: rm (Remove Files and Directories)]]
- **Topic 31:** 📖 [[Kali Linux Course/Topic 31 - How to Get Help in Linux man Pages & --help Flag|How to Get Help in Linux: man Pages & --help Flag]]
- **Topic 32:** 📦 [[Kali Linux Course/Topic 32 - Linux Command mv (Move and Rename)|Linux Command: mv (Move and Rename)]]
- **Topic 33:** 🔍 [[Kali Linux Course/Topic 33 - Linux Command file (Determine File Type)|Linux Command: file (Determine File Type)]]
- **Topic 34:** 👆 [[Kali Linux Course/Topic 34 - Linux Command touch (Create and Modify Timestamps)|Linux Command: touch (Create Files & Modify Timestamps)]]
- **Topic 35:** 🔄 [[Kali Linux Course/Topic 35 - Linux Command rename (Bulk Rename with Patterns)|Linux Command: rename (Bulk Rename Files using Patterns)]]
- **Topic 36:** 📖 [[Kali Linux Course/Topic 36 - Linux Manual Sections and Advanced Man Searches (man 1-8, apropos, whatis)|Linux Manual Sections & Advanced Man Searches (man 1-8, apropos, whatis)]]
- **Topic 37:** 📖 [[Kali Linux Course/Topic 37 - Linux Commands file Content Inspection (head, tail, strings, hexdump, tac)|Linux Commands: File Content Inspection (head, tail, strings, hexdump, tac)]]
- **Topic 38:** 🏢 [[Kali Linux Course/Topic 38 - Linux File System Hierarchy Standard (FHS)|Linux File System Hierarchy Standard (FHS)]]

---
