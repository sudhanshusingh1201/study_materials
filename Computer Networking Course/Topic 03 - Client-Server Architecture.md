---
title: "Topic 03 - Client-Server Architecture"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🖥️ 3. Client-Server Architecture

### 📝 Introduction (Intro)
**Client-Server Architecture** ek network model hai jisme network ke saare tasks aur workloads ko do main components me divide kiya jata hai:
* **Client (The Requester):** Ye wo device ya application hai jo kisi resource ya service ke liye request bhejta hai. Jaise aapka laptop, mobile phone, ya Google Chrome web browser.
* **Server (The Provider):** Ye ek powerful computer ya program hota hai jo hamesha "waiting/listening" state me rehta hai. Jab bhi koi client isse contact karta hai, server request ko process karta hai aur response (data/service) wapas bhejta hai.

Is model me sara data communication **Request-Response** cycle par chalta hai.

### ➕ Advantages (Fayde)
* **Centralization:** Saara database aur services ek single high-performance machine (server) par host hoti hain. Is wajah se data ko update aur manage karna bahut easy hota hai.
* **Security:** Server par advance firewall aur access control policies lagayi ja sakti hain. Client agar hack bhi ho jaye, tab bhi database secure rehta hai.
* **Scalability (Badhava):** Agar clients ki sankhya badhe, toh server ki RAM/CPU upgrade ki ja sakti hai (Vertical Scaling) ya multiple servers add kiye ja sakte hain (Horizontal Scaling).
* **Automatic Backups:** Poore organization ke files aur documents ka backup client devices ke bajaye seedhe server par aasaani se schedule kiya ja sakta hai.

### ➖ Disadvantages (Nuksan)
* **Single Point of Failure:** Agar main server crash ya offline ho jaye, toh koi bhi client uski services ko use nahi kar payega. Poora network band ho jata hai.
* **High Setup & Maintenance Cost:** Server class hardware aur operating systems normal computers ke comparison me bahut costly hote hain. Unhe continuous electricity aur Cooling (AC) ki zaroorat hoti hai.
* **Traffic Bottlenecks (Congestion):** Jab ek sath millions of clients request bhejte hain, toh server overflow ho sakta hai. Jaise exam result aane par website server slow ya crash ho jata hai.

### 📊 Diagram
Ye client aur server ke aapas ke communication flow ko darshata hai:

```mermaid
graph LR
    subgraph Clients (Requesters)
        Browser[Google Chrome]
        App[Mobile Instagram App]
    end

    subgraph Server Side (Providers)
        WebServer[Web/App Server] <--> DB[(Database Server)]
    end

    Browser -- 1. HTTP Request (Read Post) --> WebServer
    App -- 1. HTTP Request (Like Post) --> WebServer
    WebServer -- 2. Response (Post Content) --> Browser
    WebServer -- 2. Response (Like Confirmed) --> App
```

### 💡 Real-world Example (Udaharan)
* **Restaurant Analogy:** 
  - **Client (Aap):** Jo seat par baithkar khane ka order deta hai.
  - **Request (Order):** Jo aapne waiter ko likhwaaya.
  - **Server (Kitchen / Cook):** Jahan saara khana banta hai aur store kiya jata hai.
  - **Response (Khana):** Jo cook ne banakar aapke table par serve kiya.
* **ATM machine:** ATM machine ek client hai jo check karti hai ki aapke account me kitne paise hain. Wo request bank ke central database server ko bhejti hai, jo bank balance deduct karke cash withdraw ki details client ATM ko respond karta hai.

### 🚀 Application (Kahan use hota hai?)
* **Web Browsing (HTTP/HTTPS):** Chrome/Safari clients ke jariye apache/nginx web servers se web pages download karna.
* **Email Communication:** Outlook/Gmail apps (clients) ke jariye SMTP/IMAP servers par mail send aur receive karna.
* **Online Gaming:** PUBG ya Valorant game client aapke phone/PC par chalta hai, par sabhi players ki positions central game server update karta hai.
* **Cloud Storage:** Google Drive ya Dropbox apps ke jariye remote servers par files upload/download karna.

---