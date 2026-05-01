# CODECRAFT_CS_05
---

# Python Network Packet Analyzer

A simple, lightweight network packet sniffer written in Python used in linux  This tool captures live network traffic and displays the source/destination IP addresses, protocols, and raw payload data.

### 📋 Overview


This script is designed for educational purposes to demonstrate how data moves across a network and how network interfaces can be used to inspect traffic.

### 🚀 Features
* **Real-time Capture:** Monitors live packets on your chosen network interface.
* **IP Extraction:** Clearly displays Source and Destination IP addresses.
* **Protocol Identification:** Identifies common network protocols (TCP, UDP, etc.).
* **Payload Inspection:** Extracts and displays the first 50 bytes of raw data.

### 🛠 Prerequisites
* **Python 3.x**
* **Root/Admin Privileges:** Capturing network traffic requires elevated permissions (`sudo` on Linux).

### 💻 Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/8lso-M/CODECRAFT_CS_05.git
    cd CODECRAFT_CS_05
    ```

2.  **Run the script:**
    ```bash
    sudo python3 sniffer.py
    ```

3.  **Stop:**
    Press `Ctrl+C` to terminate the capture.

### ⚠️ Ethical Warning
**Educational Use Only.** This tool is intended for learning network fundamentals. Do not use this tool to monitor, intercept, or analyze traffic on networks you do not own or do not have explicit, written permission to test. Unauthorized packet sniffing is illegal in many jurisdictions.

### 🛡️ Troubleshooting
* **No output?** Ensure you are running with `sudo`. If you have multiple network interfaces, you may need to specify the correct one (e.g., `eth0`, `wlan0`) in the script.
* **Encrypted Traffic:** Note that modern HTTPS traffic is encrypted; the payload will appear as scrambled, unreadable text
