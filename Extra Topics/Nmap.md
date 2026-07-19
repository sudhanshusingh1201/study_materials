# Nmap

**Nmap** (short for **Network Mapper**) is a free command-line tool used by cybersecurity professionals to discover devices on a network and find out what services and ports are open on them. 

In simple terms, it helps you map out a network and find potential entry points.

---

### 1. The Real-World Analogy: The Security Guard Check
Imagine you are a security guard hired to audit the safety of a large office building at night:
* **Scanning the Building:** You walk around the building to count how many doors and windows there are. (In Nmap, this is discovering **IP addresses** on a network).
* **Checking the Doors:** You pull on each door handle to see if it is **open, locked, or unlocked**. (In Nmap, this is checking **ports** like Port 80, Port 22, etc.).
* **Identifying What's Inside:** Through an open window, you look inside to see if it's an office, a server room, or a storage closet. (In Nmap, this is **OS/Service detection**—identifying if the target is running Windows, Linux, or a specific version of web software).

---

### 2. Cybersecurity Example: Finding an Open Backdoor
Suppose an ethical hacker (penetration tester) is hired to test a company's security. They run Nmap against the company's servers:

1. **The Scan:** They type a command like `nmap -sV targetcompany.com` (which tells Nmap to scan the target and detect service versions).
2. **The Discovery:** Nmap reports back that **Port 21 (FTP - File Transfer Protocol)** is open and running an outdated version of file-sharing software from 2018.
3. **The Risk:** Because the service version is outdated, the hacker knows there is a publicly known exploit (vulnerability) for it. 
4. **The Fix:** The security team uses this report to close the open port or upgrade the software before a malicious hacker can exploit it.
