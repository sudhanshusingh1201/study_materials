---
title: "Topic 10 - Proxy Servers & Proxychains"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🔗 Topic 10: Proxy Servers & Proxychains

Bhai, network routing aur security testing me **Proxy Server** ek fundamental building block hai. Ye VPN se kafi milta-julta hai par iske kaam karne ka scale aur tarika thoda alag hota hai.

---

### 🔗 Proxy Server Kya Hai?
* **Proxy (Bicholiya):** Proxy server aapke computer aur internet ke beech ek intermediate (bridge) ki tarah khada rehta hai.
* Jab aap internet par koi site kholte ho, toh request direct website server par nahi jati. Pehle request proxy server ko milti hai, proxy server us page ko internet se apne behalf par fetch karta hai aur laakar aapko de deta hai.

```
Aapka PC ➡️ Request ➡️ Proxy Server ➡️ Internet (Web Server)
Aapka PC ⬅️ Response ⬅️ Proxy Server ⬅️ Internet (Web Server)
```

---

### 📂 Types of Proxies (Anonymity Levels Ke Base Par)

Hacker target system scan karte waqt kis type ki proxy use kar raha hai, ye unki anonymity level define karta hai:

1. **Transparent Proxy:**
   * Ye website to batati hai ki main proxy hoon aur ye **user ka asli IP address bhi site ko leak kar deti hai**. 
   * *Use case:* Schools ya offices me iska use websites block karne ya internet speed boost (caching) ke liye kiya jata hai.
2. **Anonymous Proxy:**
   * Ye target website ko batati hai ki main ek proxy hoon, lekin **user ka real IP address chhupa leti hai** (apna fake IP dikhati hai).
3. **Elite / High Anonymity Proxy (Best Choice) 🌟:**
   * Ye website ko batati hi nahi ki main proxy hoon, aur user ka real IP bhi fully hide kar deti hai. Website ko lagta hai ki koi aam user direct visit kar raha hai.

---

### 🔄 Forward Proxy vs. Reverse Proxy

| Category | Forward Proxy (Client-side) | Reverse Proxy (Server-side) |
| :--- | :--- | :--- |
| **Sits in front of...** | Clients (Users) | Servers (Websites) |
| **Main Goal** | User ki identity hide karna ya firewalls ko bypass karna. | Server ko protect karna, web traffic load design balance karna. |
| **Example** | Aapne school filter bypass karne ke liye proxy lagayi. | Cloudflare jo websites ke backend servers ko DDoS se bachata hai. |

---

### 🛠️ HTTP vs. SOCKS Proxies
* **HTTP/HTTPS Proxies:** Ye sirf Web (Browser) traffic (ports 80/443) ko interpret aur process kar sakti hain.
* **SOCKS Proxies (SOCKS4, SOCKS5):** Ye low-level network protocol proxies hoti hain. Ye bina data read kiye sabhi protocols (TCP, UDP, FTP, SMTP, SSH) ko process kar sakti hain. Hacking tools mostly **SOCKS5** protocol proxy prefer karte hain kyunki ye faster hoti hai aur dynamic connection paths support karti hai.

---

### ⛓️ Proxychains Tool in Kali Linux

Penetration testing me ek single proxy unsafe ho sakti hai (agar wo log leak kar de). Isliye hackers **Proxychains** ka use karte hain. 

**Proxychains** ek aisi utility hai jo kisi bhi command tool ke traffic ko multiple proxy servers ki chain (line) se pass hone ke liye bypass karti hai.

```
Aapka PC ➡️ Proxy 1 (US) ➡️ Proxy 2 (Germany) ➡️ Proxy 3 (Japan) ➡️ TARGET
```

#### 💻 Config Configuration:
Proxychains ki main configuration file Kali Linux me yahan hoti hai:
`/etc/proxychains4.conf`
*(Is file ke end me hum custom proxies add karte hain, jaise `socks5 127.0.0.1 9050`).*

#### 💻 Execution Command Example:
Kisi tool ko proxychains ke network base par chalane ke liye command ke aage `proxychains` prefix add kiya jata hai:
```bash
proxychains nmap -sT -Pn 192.168.1.100
```
* **Why `-sT`?** Proxychains standard TCP connections ko hi route kar sakta hai. Nmap ka default SYN scan (`-sS`) raw packets use karta hai jo proxies bypass nahi kar pate. Isliye TCP Connect Scan (`-sT`) run karna mandatory hota hai.

---