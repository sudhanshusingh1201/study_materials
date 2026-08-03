---
title: "Topic 35 - Network Sockets (Endpoint Communication)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🔌 35. Network Sockets (Endpoint Communication)

### 📝 Introduction (Intro)
**Socket** (Network Socket) ek software structure/endpoint hai jo network par chal rahe do different programs ya processes ke beech bidirectional (dono side se) communication link set karne ka kaam karta hai.

* **The Socket Equation:** Network sockets ko identify karne ka standard formula hai:
  $$\text{Socket} = \text{IP Address} + \text{Port Number}$$
  *Jaise:* Agar aapke system ka local IP address `192.168.1.50` hai aur user process port `54321` par data receive kar raha hai, toh client socket value `192.168.1.50:54321` banegi.
* **Client-Server Pair:** Ek complete network connection banne ke liye do sockets (a socket pair) ki zarurat hoti hai: ek **Client Socket** (connection initiate karne wala) aur ek **Server Socket** (connection request listen aur accept karne wala).

### ➕ Advantages (Fayde)
* **Standard BSD Socket APIs:** Sockets programming interfaces (BSD libraries) universal hain. Lagbhag har standard programming languages (Python, Java, C++, Go) aur OS platform par iski APIs dynamic support detin hain.
* **Process-to-Process Delivery:** Ye ensure karta hai ki dynamic data packets correct system ke correct targeted background application process window tak hi bypass hon.
* **Bi-directional data flow:** Sockets ek single socket stream ke through simultaneous data read and write (send/receive) actions allow karte hain.

### ➖ Disadvantages (Nuksan)
* **Low-Level Abstraction:** Sockets developer ko raw, unparsed data stream handover karte hain. Isme HTML format layout formatting, automatic SSL handshake, ya direct parsing systems built-in nahi hote; complete parsing software programming levels par karni padti hai.
* **Resource Leakage Vulnerability:** Sockets file system descriptors open rakhte hain. Agar work complete hone ke baad programmer socket links compile close na kare, toh OS process tables limit crash (Socket resource leak) ho sakti hai.
* **Firewall Port Blocks:** Security configurations me custom sockets ports run karne par network firewalls communication line drop/block kar dete hain.

### 📊 Diagram
Ye layout Client Socket aur Server Socket connection interface tunnels details ko state karta hai:

```mermaid
graph LR
    subgraph Client Machine (IP: 192.168.1.50)
        ClientSocket["Client Socket <br> 192.168.1.50 : 54321"]
    end

    ClientSocket <===>|Established Bidirectional Connection| ServerSocket

    subgraph Remote Web Server (IP: 104.22.8.12)
        ServerSocket["Server Socket <br> 104.22.8.12 : 443 (HTTPS)"]
    end
```

### 💡 Real-world Example (Udaharan)
* **Apartment and Mail Box Metaphor:**
  - **IP Address = Apartment Building Location:** Jaise "Asha Apartments, Gali No. 4". Courier boy building tak toh pahunch jayega, par use target room nahi pata.
  - **Port Number = Flat Number:** Jaise "Flat 302".
  - **Socket = Door Name Plate (Flat 302, Asha Apartments):** Dono ko join karne ke baad courier directly flat 302 ke user ko handover ho jata hai (Process communication complete).
* **Electrical Wall Plug Socket:** Aapke room wall me ek electricity socket point hota hai jahan dynamic plug push karne se machine lines coordinate ho jati hain. Software context me sockets wahi plugs hain jo network stream connect karte hain.

### 🚀 Application (Kahan use hota hai?)
* **Socket Programming Scripts:** Python server systems or custom chat nodes design programs run karne me.
* **Real-time Web updates:** Chat applications (jaise WhatsApp / Telegram desktop updates WebSockets structures use karte hain).
* **Multiplayer Online Gaming:** Live shooter games (PUBG, Valorant) jahan real-time location vectors updates sync milliseconds me sockets tunnels ke through run hote hain.

---