---
title: "Day 60 - REST APIs"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🤖 Day 60: REST APIs (Web-Based Device Management)

Welcome to the notes for **Day 60: REST APIs** of Jeremy's IT Lab CCNA Complete Course! Network controllers aur modern switches programmatically communicate karne ke liye HTTP protocols par rely karte hain. Aaj hum **REST (Representational State Transfer) API** ke fundamentals, client-server stateless properties, HTTP verbs (GET, POST, PUT, PATCH, DELETE) aur unki dynamic CRUD mappings, API request structures (Headers, URI, Body), aur HTTP response status codes (2xx, 4xx, 5xx families) ko tables aur code blocks ke sath detail mein cover karenge. Ye notes Hinglish language aur English/Latin script mein hain.

---

## 🚦 1. What is an API?

*   **API (Application Programming Interface):** 
    *   Ye ek software bridge hai jo do programs ya systems ko aapas mein communicate aur data share karne ki facility deta hai.
    *   *Analogy:* Jab aap restaurant mein jaate hain, toh waiter (API) aapka order (Request) kitchen (Server) tak lekar jata hai aur wahan se food prepare hone par aapki table (Response) tak bhejta hai.

---

## 🏛️ 2. REST Architecture Constraints

**REST (Representational State Transfer)** koi software ya protocol nahi hai. Ye web-based APIs design karne ka ek **architectural design style** hai jo standard HTTP connections use karta hai. REST APIs satisfy karne ke liye niche diye points are critical:

1.  **Client-Server Architecture:**
    *   Client (Automation script ya application) requests bhejta hai aur Server (SDN Controller ya Router) response return karta hai. Dono aapas mein independent hote hain.
2.  **Statelessness (Sabse Important Rule):**
    *   Server client ka koi session history memory mein save nahi rakhta. **Har request completely independent hoti hai** aur client ko har request ke sath authentication tokens aur metadata bejhna padta hai.
3.  **Cacheability:**
    *   Server responses indicate kar sakte hain ki unhe cache (temp save) kiya ja sakta hai ya nahi, jisse web efficiency improve ho sake.

---

## 🧭 3. HTTP Verbs and CRUD Operations

REST APIs networks database par **CRUD (Create, Read, Update, Delete)** actions perform karne ke liye standard HTTP request methods use karte hain:

| CRUD Operation | HTTP Request Method | Description / Network Use Case |
| :--- | :--- | :--- |
| **Create** | **`POST`** | Network par new configurations add/create karna (e.g. creating a new VLAN 100). |
| **Read** | **`GET`** | Target configurations details read/retrieve karna (e.g. fetching interface counters database). |
| **Update** | **`PUT`** / **`PATCH`** | Existing configuration modify karna. **PUT** poori configuration replace karta hai; **PATCH** sirf particular field change karta hai. |
| **Delete** | **`DELETE`** | Configuration ya resource remove karna (e.g. deleting an interface IP address). |

---

## 🕸️ 4. HTTP Request & Response Structure

Ek automation client server ko HTTP request bhejte waqt niche diye variables build karta hai:

### A. HTTP Request Components:
1.  **URI / Endpoint (URL):**
    *   Resource ka physical link address.
    *   *Example:* `https://192.168.1.1/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1`
2.  **Headers (Metadata):**
    *   *Content-Type:* Bata raha hai ki request body mein data kis format mein hai (e.g. `application/json` ya `application/xml`).
    *   *Accept:* Server ko bata raha hai ki client ko response kis format mein chahiye.
    *   *Authorization:* Security tokens (credentials, Basic auth base64 strings ya Bearer API keys).
3.  **Request Body (Payload):**
    *   JSON ya XML format mein actual configuration data jo client push karna chahta hai (not required for GET and DELETE).

---

### B. HTTP Response Status Codes (CCNA Exam Core):
Server reply ke sath ek numeric status code bhejta hai jo request ka result status batata hai:

*   **2xx (Success Codes):**
    *   **`200 OK`:** Request verify successfully completed (e.g. GET returned values).
    *   **`201 Created`:** New configuration successfully added (usually returned for POST).
*   **3xx (Redirection):**
    *   Client request ko doosre link par redirect kiya gaya.
*   **4xx (Client Errors - User's Fault):**
    *   **`400 Bad Request`:** Request ke payload/syntax syntax mein error hai (galat JSON template).
    *   **`401 Unauthorized`:** Credentials galat hain ya authentication credentials missing hain.
    *   **`403 Forbidden`:** Login toh valid hai par us user ko resource access karne ki access permissions (authorization) nahi hai.
    *   **`404 Not Found`:** requested URI link or resource target server par exist nahi karta.
*   **5xx (Server Errors - Device's Fault):**
    *   **`500 Internal Server Error`:** Server software crash ho gaya ya general server crash bug.
    *   **`503 Service Unavailable`:** Server over-loaded hai ya offline maintenance par hai.

---

## 📝 5. CCNA Day 60 Practice Questions

1. **Q1: REST API design systems ke context mein 'Statelessness' property kya indicate karti hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Server client ke past requests ka koi session data ya history save nahi rakhta. Har ek request self-contained hoti hai jisme authorization aur target variables data point check mandatory hote hain.
   </details>

2. **Q2: Database database actions system 'CRUD' ka full form kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Create, Read, Update, Delete**.
   </details>

3. **Q3: Router par dynamic interface status counters check variables fetch karne ke liye hum kis HTTP request method use karenge?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **`GET`** request method (Read action).
   </details>

4. **Q4: REST API calls parameters me, 'PUT' aur 'PATCH' request methods ke beech main difference kya hota hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **PUT** method pure resource object ko replacement update parameters se overwrite kar deta hai, jabki **PATCH** method object ke selective fields (partial updates) ko hi modify karta hai.
   </details>

5. **Q5: API requests headers check mein, 'Content-Type' aur 'Accept' fields kis information variables ko convey karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Content-Type** batata hai ki client request body me kis format (JSON/XML) ka payload bhej raha hai, aur **Accept** field batata hai ki client ko server se response kis specific format (JSON/XML) mein read/receive karna pasand hai.
   </details>

6. **Q6: HTTP response status code `201` kya represent karta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Created** (Request success ho gayi hai aur backend database par resource/configuration successfully add/create ho gaya hai).
   </details>

7. **Q7: Python scripts REST calls run ke dauran incorrect API tokens keys use karne par kis numeric error code series return hogi?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **`401 Unauthorized`** error.
   </details>

8. **Q8: User credentials valid hone par bhi agar user ko specific configuration parameters change karne ki access permissions block mile, toh kya HTTP code milega?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **`403 Forbidden`** error.
   </details>

9. **Q9: Router REST interface configuration push karte waqt JSON array braces errors (galat code syntax) hone par server kya output code generate karega?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **`400 Bad Request`** error.
   </details>

10. **Q10: Target web server system application crashes or script execution failures hone par kis status code range ko receive kiya jata hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **`500 Internal Server Error`** code.
    </details>
