# Topic 01 - Metasploit Framework & Database Setup

Metasploit is one of the most powerful and widely used penetration testing frameworks in the cybersecurity industry. It is designed to find, exploit, and validate security vulnerabilities.

---

## 1. Core Modules of Metasploit (The 6 Pillars)

Metasploit's functionality is divided into distinct modules located in the `/usr/share/metasploit-framework/modules/` directory in Kali Linux.

1. **Exploits**
   * **Purpose:** Code that takes advantage of a specific vulnerability in a target system to grant access.
   * **Real-world Analogy:** Finding a broken lock on a window to gain entry into a house.

2. **Payloads**
   * **Purpose:** The actual code that runs on the target system *after* successful exploitation (e.g., spawning a command shell, opening a Meterpreter session).
   * **Real-world Analogy:** The action of stealing money from a vault or setting up a hidden camera once inside the house.
   * **Meterpreter:** The most advanced payload that runs entirely in memory (hard for antivirus to detect) and allows complete control of the system.

3. **Auxiliary**
   * **Purpose:** Scanning, sniffing, fuzzing, or brute-forcing tools. They do not exploit target systems (do not run payloads) but are crucial for information gathering and vulnerability analysis.
   * **Real-world Analogy:** Testing all the door handles to see which ones are unlocked without actually going inside.

4. **Post**
   * **Purpose:** Modules executed after gaining access (Post-Exploitation). Used for gathering credentials, escalating privileges, and looting target systems.

5. **Encoders**
   * **Purpose:** Modifying/obfuscating payload code to bypass security filters like Antivirus (AV) or Intrusion Detection Systems (IDS).
   * **Example:** `shikata_ga_nai` (polymorphic XOR additive feedback encoder).

6. **Evasion**
   * **Purpose:** Modern modules designed specifically to generate payloads that bypass newer OS-level protections (like Windows Defender) without needing manual encoding.

---

## 2. Why Do We Need a Database in Metasploit?

By default, Metasploit can be run without a database. However, connecting it to a **PostgreSQL** database offers major advantages:
1. **Data Persistence:** Automatically saves host IPs, open ports, OS information, gathered credentials, and detected vulnerabilities.
2. **Speed & Efficiency:** Allows quick searching and querying of scan results across multiple targets.
3. **Collaboration:** Multiple team members can share and view the same target data.

---

## 3. Practical: Initializing and Starting Metasploit with Database Support

Follow these step-by-step commands in your Kali Linux terminal to set up and verify the database connection.

### Step 1: Start the PostgreSQL Service
PostgreSQL must be running in the background for Metasploit to connect to it.
```bash
sudo systemctl start postgresql
```
> [!TIP]
> To make PostgreSQL start automatically every time you boot Kali Linux, run:
> `sudo systemctl enable postgresql`

### Step 2: Initialize the Metasploit Database (First-time setup only)
Create the database schema, configuration, and default users:
```bash
sudo msfdb init
```

### Step 3: Launch Msfconsole in Quiet Mode
Start the Metasploit interactive console. The `-q` flag starts it quietly by hiding the large ASCII art banners, which speeds up load time:
```bash
msfconsole -q
```

### Step 4: Verify the Database Connection
Inside the `msfconsole` shell, run the following command to verify status:
```text
msf6 > db_status
```
*Expected Output:*
```text
[*] Connected to msf. Connection type: postgresql.
```

---

## 4. Advanced: Integrating Nmap with Metasploit Database (`db_nmap`)

Instead of running Nmap in a separate terminal and copy-pasting IPs, you can run Nmap directly inside Metasploit using the `db_nmap` command. This automatically saves all results into the connected database.

### Syntax:
```text
msf6 > db_nmap -sV -O <Target-IP/Range>
```

### Querying the Database:
After the scan completes, you can retrieve the saved results using database commands:

* **List all discovered hosts:**
  ```text
  msf6 > hosts
  ```
* **List all open services and port versions:**
  ```text
  msf6 > services
  ```
* **Filter services by port number:**
  ```text
  msf6 > services -p 445
  ```
