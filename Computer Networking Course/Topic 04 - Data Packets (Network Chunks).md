---
title: "Topic 04 - Data Packets (Network Chunks)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 📦 4. Data Packets (Network Chunks)

### 📝 Introduction (Intro)
Jab hum computer network par koi bada data (jaise image, video, file, email) bhejte hain, toh wo ek single piece me nahi jata. Network us poore data ko chote-chote chunks (hisson) me break kar deta hai. In tiny logical blocks of data ko hum **Packets** (ya Data Packets) kehte hain.

Ek standard packet ke teen main parts hote hain:
1. **Header (The Cover):** Isme control information hoti hai, jaise Source IP (kisne bheja), Destination IP (kisko bheja), Packet Sequence Number (kis sequence me judenge), aur TTL (Time To Live).
2. **Payload (The Letter):** Actual data jo hum send kar rahe hain (original file ka chhota sa tukda).
3. **Trailer/Footer (The Seal):** Isme error-checking bits hote hain (jaise CRC/Checksum) jo ensure karte hain ki packet transfer ke dauran damage ya change na ho.

### ➕ Advantages (Fayde)
* **Bandwidth Efficiency:** Ek bada data transfer line ko block nahi karta. Dusre devices ke data packets bhi usi line se aapas me mix hokar simultaneously travel kar sakte hain (**Multiplexing**).
* **Smart Error Recovery:** Agar network error ke karan koi packet lost ya damage ho jaye, toh poori file wapas bhejne ki zaroorat nahi hoti. Client sirf wahi ek damaged packet wapas mangwata hai.
* **Dynamic Routing:** Har packet independently best available path choose kar sakta hai. Agar koi router fail ho jaye, toh baaki packets doosra route lekar destination tak pahunch sakte hain.

### ➖ Disadvantages (Nuksan)
* **Header Overhead:** Har ek packet ke sath 20-40 bytes ka header data lagta hai. Is redundant information ki wajah se total file size se zyada data network par travel karta hai.
* **Out-of-Order Delivery & Jitter:** Packets alag-alag routes se travel karne ke karan destination par aage-piche pahunch sakte hain. Agar reassembly me time lage, toh video ya audio call me lag (jitter) mehsus hota hai.
* **Packet Loss:** High network congestion (traffic) hone par routers packets ko drop (delete) kar dene hain, jisse re-transmission delay hota hai.

### 📊 Diagram
Ye ek file ke packets me split hone, different routes se travel karne aur wapas reassemble hone ke process ko darshata hai:

```mermaid
graph TD
    subgraph Sender Side
        File[Original File: 300KB] -->|Split| P1[Packet 1: 100KB]
        File -->|Split| P2[Packet 2: 100KB]
        File -->|Split| P3[Packet 3: 100KB]
    end

    subgraph Network (Dynamic Routing)
        P1 --> RouterA[Router A] --> Receiver[Receiver Interface]
        P2 --> RouterB[Router B] --> Receiver
        P3 --> RouterA --> Receiver
    end

    subgraph Receiver Side
        Receiver -->|Reassemble by Seq Num| ReFile[Original File Restored]
    end

    subgraph Inside a Data Packet
        H[Header: IP & Seq Num] --- Pay[Payload: Actual Data] --- T[Trailer: Checksum]
    end
```

### 💡 Real-world Example (Udaharan)
* **Postcard Analogy:** Maan lijiye aapko apne dost ko ek badi book bhejni hai par aapke paas itna bada envelope nahi hai. Aap book ke har ek page ko alag-alag envelope me daalte hain. Har envelope par sender-receiver address, page number (Sequence Number), aur signature (Trailer Checksum) lagate hain aur post kar dete hain. Dost ke paas envelopes alag-alag din pahunchenge par wo page numbers dekh kar unhe wapas line se laga kar book padh lega.

### 🚀 Application (Kahan use hota hai?)
* **Internet Communication (IP/TCP):** Internet par browse hone wali har website packets ki form me hi hamare computer par load hoti hai.
* **VoIP (Voice over IP):** Skype, Zoom, WhatsApp calls me hamari aawaz real-time audio packets me break hokar travel karti hai.
* **Online Streaming:** Netflix ya YouTube par videos packets me buffer hoti rehti hain taaki smooth playback mile.
* **File Transfers (FTP/SFTP):** Badi ISO files ya software setups download karte waqt wo packets me divide hokar aate hain.

---