---
title: "Topic 02 - How it Started (History of Networking)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 📜 2. How it Started (History of Networking)

### 📝 Introduction (Intro)
Computer networking ki shuruaat late 1950s aur 1960s me US Department of Defense ke **ARPA (Advanced Research Projects Agency)** dwara hui thi. 

Cold War (sheet yudh) ke dauran, US military ko ek aise communication network ki zaroorat thi jo safe aur decentralized ho. Agar nuclear attack me koi ek shahar (node) tabah bhi ho jaye, toh baaki network chalta rahe. Is zarurat se janam hua **ARPANET** (Advanced Research Projects Agency Network) ka, jo aaj ke modern Internet ka dada-par-dada hai.

* **The First Milestone (1969):** UCLA (University of California, Los Angeles) se SRI (Stanford Research Institute) ko pehla message bheja gaya tha: `"LOGIN"`. Lekin system crash hone ki wajah se pehli baar me sirf `"LO"` hi transmit ho paya! Baad me ise correct karke pura message bheja gaya.
* **Packet Switching & TCP/IP:** ARPANET pehla aisa network tha jisne **Packet Switching** (data ko small packets me baant kar bhejna) ka use kiya, aur baad me **TCP/IP** protocol ko standard banaya.

### ➕ Advantages (Fayde)
* **Decentralized Architecture:** Koi single central point nahi tha. Agar ek path block ya destroy ho jaye, toh network dynamic routing ke jariye doosra path dhoond leta tha.
* **Packet Switching (Efficiency):** Ek hi transmission line par multiple users ke data packets ko mix karke bheja ja sakta tha (multiplexing), jisse bandwidth waste nahi hoti thi.
* **Resource Sharing:** Door-daraz baithe scientists aur researchers supercomputers aur data resources ko aapas me share kar paaye.
* **Interoperability:** TCP/IP protocol ne alag-alag companies ke computer operating systems ko ek common language di jisse wo aapas me communicate kar sakein.

### ➖ Disadvantages (Early Network ki Limitations)
* **Extremely Slow Speed:** Shuruati links ki speed bahut kam thi, lagbhag **56 Kbps** (aaj ke 4G/5G se hazaron guna dheemi).
* **Low Reliability:** Purani hardware technologies aur copper wires ki wajah se systems aksar crash ho jate the aur signals me noise bahut aati thi.
* **Highly Restricted:** Ye public ke liye nahi tha. Sirf military departments, select universities, aur high-profile government research labs ke log hi ise use kar sakte the.
* **No Security / Encryption:** Shuruaat me security aur encryption ke koi protocols nahi the. Maana jata tha ki network par connected sabhi users trusted scientists aur researchers hi hain.

### 📊 Diagram
Ye ARPANET ke shuruati nodes ka decentralized mesh structure hai:

```mermaid
graph TD
    subgraph ARPANET Early Nodes (1969)
        UCLA[UCLA Node] <--> SRI[Stanford Research Inst.]
        SRI <--> Utah[University of Utah]
        UCLA <--> UCSB[UC Santa Barbara]
        UCSB <--> Utah
    end
```

### 💡 Real-world Example (Udaharan)
* **Phone Call vs. Postcard:** Purana telephone network (Circuit Switching) railway track ki tarah tha—jab tak aap baat kar rahe hain, line booked hai aur doosra koi use nahi kar sakta. ARPANET ka Packet Switching **Postcards** ki tarah tha—aapne lambe khat ko 4 postcards me likha, wo alag-alag postal routes se travel karke recipient ke paas pahunche aur unhone unhe line se jod kar padh liya.

### 🚀 Application (Kahan use hota hai?)
* **Military Projects:** Cold War ke dauran secure communication channels banane ke liye.
* **Academic Collaboration:** Universities ke beech research papers aur calculations share karne ke liye.
* **Email ka Janam (1971):** Ray Tomlinson ne isi network par pehli baar `@` symbol ka use karke email bheja.
* **Modern Internet Protocol:** Aaj hum jo TCP/IP use karte hain, uski foundation isi research par rakhi gayi thi.

---