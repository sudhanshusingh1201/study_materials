# nslookup

**nslookup** (which stands for **Name Server Lookup**) is a command-line tool used to query the **Domain Name System (DNS)**. 

DNS is the system that translates human-readable website names (like `google.com`) into computer-readable IP addresses (like `142.250.190.46`). `nslookup` lets you ask the DNS system: *"What is the IP address for this domain?"* or vice-versa.

---

### 1. The Real-World Analogy: The Phonebook Directory
Computers communicate using numbers (IP addresses), but humans prefer names. 
* **The Analogy:** Imagine you want to call a restaurant named "Pizza Palace," but you don't know their phone number. You open a **phonebook** (DNS) to look up "Pizza Palace" and get their number: `555-0199` (IP address).
* **Using nslookup:** Running `nslookup` is like calling directory assistance and asking: *"Can you give me the phone number registered for 'Pizza Palace'?"* or asking *"Whose name is registered to the phone number '555-0199'?"*

---

### 2. Cybersecurity Example: Spotting a Phishing Website
Phishing attacks often use domains that look almost identical to real ones (e.g., `paypa1.com` instead of `paypal.com`). Security analysts use `nslookup` to investigate suspicious links.

1. **The Setup:** A user receives an email saying their bank account is locked, directing them to login at `secure-verify-bank.com`.
2. **The Investigation:** A cybersecurity analyst runs:
   ```bash
   nslookup secure-verify-bank.com
   ```
3. **The Result:** `nslookup` returns an IP address like `203.0.113.50`. 
4. **The Discovery:** The analyst looks up that IP address and finds it is hosted on a cheap server in a country where the bank has no operations, and the domain name servers (the computers hosting the record) are completely unverified. 
5. **The Action:** The analyst blocks this IP address on the company’s firewall, preventing any employees from accidentally visiting the phishing site.
