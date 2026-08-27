---
title: "Day 62 - Configuration Management"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🤖 Day 62: Configuration Management (Ansible, Puppet, and Chef)

Welcome to the notes for **Day 62: Configuration Management** of Jeremy's IT Lab CCNA Complete Course! Aaj hum **Module 7: Network Automation & Programmability** ke final topic—**Configuration Management Tools**—ke baare mein seekhenge. Hum seekhenge ki Declarative versus Imperative methods kya hote hain, Idempotency kya hai, Push vs Pull architectures ke logical models kya hote hain, aur Cisco CCNA core tools—**Ansible, Puppet, aur Chef**—ki comparison characteristics, files naming (Playbooks, Manifests, Cookbooks), coding languages, aur operational mechanisms ko tables aur points ke sath cover karenge. Ye notes Hinglish language aur English/Latin script mein hain.

---

## 🚦 1. Core Configuration Management Concepts

Configuration Management tools ka primary objective network devices aur servers ke states ko standardized, consistent, aur automated tarike se maintain karna hai taaki configuration drift ko bypass kiya ja sake.

### A. Declarative vs. Imperative Models:
*   **Imperative Approach (How):**
    *   Admin tool ko step-by-step commands specify karta hai ki configuration kaise lagani hai (jaise normal CLI configuration script: "interface Gi0/1, shutdown, ip address...").
    *   *Risk:* Agar router par task pehle se completed ho, toh commands dobara chalakar configurations crash or overwrite ho sakti hain.
*   **Declarative Approach (What):**
    *   Admin sirf **final desired state** define karta hai (e.g., "Interface GigabitEthernet0/1 should be UP and IP should be 192.168.1.1").
    *   *Mechanism:* Tool pehle device ka current state scan karta hai. Agar router state match ho, toh tool kuch nahi karta. Agar mismatch ho, toh tool automatically necessary commands generate karke run kar deta hai. **Modern config tools declarative use karte hain.**

---

### B. Idempotency (Sabse Core Feature):
*   **Definition:** Ek script ya action ko aap chahe 1 baar run karein ya 1000 baar, **iska end result hamesha exact same rahega** aur device par koi duplicate changes or errors trigger nahi honge.
*   *Why it matters:* Agar configuration task router par pehle se active ho, toh idempotent tool changes bypass (skip) kar deta hai aur resource usage low rakhta hai.

---

## 🏛️ 2. Push vs. Pull Operational Models

Centralized controller network devices tak configuration files kaise transit karta hai, iske do methods hain:

```text
       PUSH MODEL (Ansible)                       PULL MODEL (Puppet/Chef)
  +---------------------------+              +---------------------------+
  |    Ansible Control Node   |              |    Central Master Server  |
  +---------------------------+              +---------------------------+
               |                                           ^
               | SSH/API Push                              | Pulls Config (Periodic)
               v                                           |
  +---------------------------+              +---------------------------+
  | Managed Device (Agentless)|              |  Managed Device (Agent)   |
  +---------------------------+              +---------------------------+
```

1.  **Push Model:**
    *   *Action:* Central server/control machine active connections create karta hai aur configs directly end-devices par push (send) karta hai.
    *   *Agentless:* End-devices par koi special agent software daemon running hona zaroori nahi hota. Standard connection methods (like SSH or HTTP APIs) use hote hain.
2.  **Pull Model:**
    *   *Action:* Managed network devices (clients) par ek small software daemon (**Agent**) run karta hai. Ye agent periodic timers (e.g. every 30 minutes) par central server master ko contact karta hai, config files pull (download) karta hai, aur use locally apply karta hai.
    *   *Agent-based:* Clients par agent client running hona mandatory hai.

---

## 🧭 3. The Big Three: Ansible, Puppet, and Chef

CCNA exam ke liye niche diye gaye characteristics aur differences memory mein hona mandatory hai:

### A. Ansible:
*   **Push / Pull:** **Push Model**.
*   **Agent Requirement:** **Agentless** (No agent software on switches/routers; uses standard SSH or NETCONF).
*   **Language written in:** Python.
*   **Config Files (Format):** **Playbooks** (YAML format, `.yml`/`.yaml`).
*   **Inventory:** Configuration targets groups represent karne ke liye standard **Inventory** file INI/YAML use karta hai.

---

### B. Puppet:
*   **Push / Pull:** **Pull Model** (Master-Agent architecture).
*   **Agent Requirement:** **Agent-based** (Requires Puppet Agent on client).
*   **Language written in:** Ruby.
*   **Config Files (Format):** **Manifests** (Proprietary Puppet DSL language, `.pp` file extension).

---

### C. Chef:
*   **Push / Pull:** **Pull Model** (Client-Server architecture).
*   **Agent Requirement:** **Agent-based** (Requires Chef-Client daemon on client).
*   **Language written in:** Ruby.
*   **Config Files (Format):** **Recipes** (combined into **Cookbooks**) written in Ruby DSL.

---

## 📊 4. Comparison Table (CCNA Core Summary)

| Feature / Criteria | Ansible | Puppet | Chef |
| :--- | :--- | :--- | :--- |
| **Model** | **Push** (Client initiates push) | **Pull** (Agent pulls) | **Pull** (Agent pulls) |
| **Agent State** | **Agentless** | **Agent-based** | **Agent-based** |
| **Written In** | Python | Ruby | Ruby |
| **Config Language** | YAML (Human readable) | Puppet DSL | Ruby DSL |
| **Key Config File** | **Playbook** | **Manifest** | **Recipe / Cookbook** |
| **Primary Connection** | SSH / NETCONF APIs | HTTP(S) SSL/TLS | HTTP(S) SSL/TLS |

---

## 📝 5. CCNA Day 62 Practice Questions

1. **Q1: Configuration Management ke context mein, 'Declarative' approach aur 'Imperative' approach mein key operational difference kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Imperative model mein admin ko step-by-step procedure/commands (How) specify karni padti hai, jabki Declarative model mein admin sirf desired end-state (What) define karta hai aur tool automatic necessary actions perform karta hai.
   </details>

2. **Q2: Automation scripts mein 'Idempotency' feature execution kya rules represent karta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Idempotent tool ko multiple times run karne par bhi link state same rehti hai aur system configurations par koi unwanted duplicate changes ya duplicate processes generate nahi hote (safe to run multiple times).
   </details>

3. **Q3: Push Model aur Pull Model of configuration management mein devices agent state requirements kya change values show karti hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Push models typically **Agentless** hote hain (e.g. Ansible over SSH), jabki Pull models mandatory **Agent-based** systems specify karte hain (client software runs on hosts to poll master server).
   </details>

4. **Q4: CCNA parameters par, Ansible kis base programming language me code kiya gaya hai aur iske configurations configs kis file type par scale kiye jate hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Python written and configuration code matches **YAML Playbooks**.
   </details>

5. **Q5: Puppet configuration management systems me configuration script code files ko kis name and extension format se identify kiya jata hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Manifests** (file extension: **`.pp`**).
   </details>

6. **Q6: Chef systems configurations code collections folders segments ko kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Recipes** (jo execute huye code compile mapping hold karte hain) aur unke containers ko **Cookbooks** bolte hain.
   </details>

7. **Q7: Ansible server nodes target configurations hosts check list execute links variables define data database ko kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Inventory** file (INI/YAML syntax).
   </details>

8. **Q8: Ansible agentless switches communication target path set karne ke liye primary transport layer 4 port aur protocols criteria kya use karta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **SSH (Port 22)** CLI or NETCONF/RESTCONF dynamic APIs connections.
   </details>

9. **Q9: Chef configuration tools background execution kis core programming framework language par rely karti hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Ruby**.
   </details>

10. **Q10: Switches/Routers deployments par traditional agent-based pull tools (Puppet/Chef) kyu easily run nahi ho pate?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** Kyunki network switches and routers closed firmware (Cisco IOS) run karte hain jahan customer easily third-party agent applications daemons install aur compile nahi kar sakta. Isliye network devices ke liye Agentless push systems (like Ansible) preferred hote hain.
    </details>
