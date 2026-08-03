---
title: "Topic 42 - Checksum (Error Detection Mechanism)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🧮 42. Checksum (Error Detection Mechanism)

### 📝 Introduction (Intro)
**Checksum** ek fundamental error detection method hai jo computer networks me travel karne wale data packets ki integrity check karne ke liye use kiya jata hai. Ye mostly **Transport Layer (Layer 4)** protocols (jaise TCP & UDP) aur **Network Layer (Layer 3)** protocols (IPv4) ke header checksum calculations me use hota hai.

#### ⚙️ How Checksum works (Sender & Receiver Steps):
* **At Sender Side:**
  1. Data unit (payload) ko $k$-bit segment blocks (normally 16-bit blocks) me divide kiya jata hai.
  2. In saare segments ko **1's Complement Arithmetic** ke jariye aapas me add (sum) kiya jata hai. Agar sum me carry-over bit (extra bit) aaye, toh use sum ke right-most bit me wapas add (wrap) kar diya jata.
  3. Final sum ka **Complement (1's complement)** liya jata hai (0s ko 1s aur 1s ko 0s me flip kiya jata hai). Yahi inverted sum humara **Checksum** hota hai.
  4. Sender is Checksum value ko packet header me append (chipka) kar data ke sath network par send kar deta hai.
* **At Receiver Side:**
  1. Receiver pure data blocks plus received checksum value ko 1's complement arithmetic ke jariye aapas me add karta hai.
  2. Final sum ka complement (invert) kiya jata hai:
     - *If result is all 0s (sum is all 1s):* Data bilkul safe hai (Accept).
     - *If result is non-zero (non-all 1s):* Data transit me corrupt ho chuka hai (Reject/Discard).

### ➕ Advantages (Fayde)
* **Highly Lightweight:** Cryptographic hash algorithms (MD5, SHA-256) ya high-end cyclic redundancy checks (CRC) ke comparison me Checksum computation kafi simple aur fast hota hai, jisse CPU overhead bahut kam padta hai.
* **Easy Implementation:** Hardware aur software levels dono par minimal logic gates design or coding arrays se implemented ho jata hai.
* **Effective for simple noise errors:** Transmission wires noise se hone wale single-bit ya simple multiple-bit errors ko easily catch kar leta hai.

### ➖ Disadvantages (Nuksan)
* **Vulnerable to Undetectable Error Patterns (Cancellation Errors):** Agar data transmission ke dauran multiple bits ek sath swap ho jayein (jaise ek segment me 0 switch to 1 ho aur doosre me same position par 1 switch to 0 ho), toh total addition sum value same rahegi. Aise cases me Checksum error check fail ho jata hai aur corrupt data accept ho jata hai.
* **No Error Correction:** Checksum sirf error **Detect (pechaan)** kar sakta hai, use **Correct (theek)** nahi kar sakta. Error milne par packet ko drop karke retransmission request karni padti hai.

### 📊 Diagram
Ye layout Sender side Checksum generation aur Receiver side Validation steps sequence mapping ko show karta hai:

```
[ Sender Side ]
  Data Blocks: Block 1 + Block 2 + Block 3 
                     |
                 [ Sum blocks ]
                     |  <-- Wrap carry bits if any
             [ Invert Sum (1's Complement) ] ===> This is Checksum!
                     |
         [ Transmit: Data Blocks + Checksum ]
                     |
                     v
[ Receiver Side ]
  Received: Data Blocks + Checksum
                     |
            [ Add All Together ]
                     |  <-- Wrap carry bits if any
           [ Invert Final Sum ]
                     |
         { Is final result 0000? }
          /                    \
     (Yes)                      (No)
      /                            \
[Data is Safe: Accept]        [Data Corrupt: Discard]
```

### 💡 Real-world Example (Udaharan)
* **Bus Passenger Count Metaphor:**
  - **Sender (Conductor A):** Bus trip start hone se pehle conductor ne passengers count kiye: total **42** passengers hain. Conductor sheet par likhta hai: "42" (Checksum).
  - **Transit:** Bus highway cross karti hai.
  - **Receiver (Conductor B at destination):** Bus stop par pahunchne par Conductor B ne count kiya: total **41** passengers hain. Wo sheet ke value check count (42) se match karta hai. 41 is not equal to 42. Conductor B instantly samajh jata hai ki beech me koi passenger (Data bit) drop ho gaya hai, aur trip corrupted drop register check ho jati hai.
* **Cashier Bill Total:** Jab aap market se 3 products buy karte hain. Cashier bill receipt par individual items amount (Segments) add karke final total write karta hai. Aap bill check karte waqt items ko manually add karke compare karte hain agar total correct match hai.

### 🚀 Application (Kahan use hota hai?)
* **IP Protocol Headers:** IPv4 headers checking.
* **Reliable Transport Layer:** TCP segment headers and UDP packet checksum configurations checking.
* **ICMP ping packets:** Network check validation query integrity tests.

---