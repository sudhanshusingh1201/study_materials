---
title: "Topic 11 - Tor Network (The Onion Router)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🧅 Topic 11: Tor Network (The Onion Router)

Bhai, cyber security aur internet anonymity ki duniya me **Tor** se badha koi naam nahi hai. Agar proxy aur VPN aam security hain, toh Tor high-level privacy shield hai.

---

### 🧅 Tor Kya Hai? (The Onion Concept)
* **Tor:** **T**he **O**nion **R**outer. Ye ek decentralized volunteer-run network system hai jo users ke traffic ko globally dynamic encryption ke sath secure routing provide karta hai.
* **Onion (Pyaaz) Kyu?** Pyaaz me jaise multiple layers hoti hain, thik waise hi Tor me data packet par **multiple layers of encryption** wrap kiye jate hain. 

---

### 🔄 Tor Circuit (Kaam Kaise Karta Hai?)

Normal proxy me data ek hi intermediate server se jata hai (jise user aur destination dono pata hote hain). Tor me connection direct na hokar **3 Random Relays (Nodes)** ke circuit se pass hota hai:

```
[Aapka PC] 
   ➡️ (Encrypted data)
[1. Entry Node (Guard)] ➡️ (Knows User IP, doesn't know Website)
   ➡️ (Re-encrypted data)
[2. Middle Node]        ➡️ (Knows only Entry & Exit, fully blind)
   ➡️ (Decrypted last layer)
[3. Exit Node]          ➡️ (Knows target site, doesn't know User IP)
   ➡️ (Clear Text)
[Target Website]
```

1. **Entry Node (Guard Node):** 
   * Ye node aapke real computer se connect hota hai, isliye **ise aapka original IP address pata hota hai**.
   * Par ye ye nahi dekh sakta ki aap andar kya data bhej rahe hain aur kis site par ja rahe hain. Ye use next node ko forward kar deta hai.
2. **Middle Node:**
   * Ye node sabse secure layer hai. Ise na toh user ka real IP pata hai (kyunki iske paas data Entry node se aaya), na hi ise target website pata hai (kyunki iske aage Exit node hai). Ye bas blind packet forwarding karta hai.
3. **Exit Node (SABSE IMPORTANT):**
   * Ye node circuit ka end point hai. Ye final layer ko decrypt karke traffic ko standard website (target site) par bhej deta hai.
   * **Target site ko lagta hai ki request Exit Node ke IP se aa rahi hai** (aapka original IP fully masked hai). Exit node ko target site pata hoti hai par request kisne bheji (User IP), ye nahi pata hota.

> [!IMPORTANT]
> **Core Principle:** Tor network ke kisi bhi ek individual node ke paas poori information nahi hoti ki **User kaun hai (IP)** aur wo **kya browse kar raha hai (Destination)**. 

---

### 🌐 Tor Services (.onion sites)
Tor network me regular extensions (jaise `.com`, `.org`) ke alawa special encrypted local domains generate hote hain jinke end me **`.onion`** laga hota hai. Inhe **Tor Hidden Services (Dark Web)** kehte hain. Inke host servers ki locations hide rehti hain aur ye standard web browsers par nahi open hote.

---

### 🛠️ Using Tor in Kali Linux (Integration)

Kali Linux me dynamic terminal commands ko Tor network se route karne ke liye hum use karte hain:

#### 1. Tor Daemon Start Karna:
Kali me local Tor routing daemon process default off hoti hai. Ise start karne ke liye:
```bash
sudo systemctl start tor
```
*(Ye command system background me port `9050` par local SOCKS5 proxy configure kar deti hai).*

#### 2. Proxychains Configuration (Tor Stack):
Tor and proxychains dono ko combine karke full anonymity secure ki jati hai.
* File `/etc/proxychains4.conf` open karke check karein aur uske last link me change/add karein:
```text
socks5 127.0.0.1 9050
```

#### 3. Execution:
Ab browser ya search tools ko run karein command ke aage prefix lagakar:
```bash
proxychains firefox
```
*(Ab aapka firefox web browser direct open hone ke bajaye local Tor SOCKS5 network se connect hokar full anonymous route banayega).*

---