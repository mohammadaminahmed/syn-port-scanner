# TCP SYN Port Scanner using Python & Scapy

## 📌 Project Overview

This project is a TCP SYN Port Scanner developed using **Python** and **Scapy** as part of my cybersecurity and network programming studies.

The purpose of this project is to understand how TCP connections work at the packet level by creating and analyzing TCP SYN packets and interpreting the responses from target systems.

The scanner identifies the state of ports based on TCP responses:

* **SYN-ACK response** → Port is Open
* **RST response** → Port is Closed
* **No Response** → Port may be Filtered by a Firewall

> This project was developed and tested only in a personal lab environment and on systems where authorization was available.

---

## 🎯 Learning Objectives

Through this project, I explored:

* TCP Three-Way Handshake
* TCP Flags (SYN, ACK, RST)
* Packet crafting using Scapy
* Raw packet analysis
* Network reconnaissance concepts
* Python network programming

---

## ⚙️ How It Works

The scanner sends a TCP SYN packet to a selected target port.

Example:

```
Kali Linux                  Target System

     SYN  -------------------->

     <-------------------- SYN-ACK

Port Status: OPEN
```

If the target responds with:

```
RST
```

the port is considered closed.

If there is no response:

```
No Reply
```

the port may be filtered by a firewall.

---

## 🛠 Requirements

* Python 3
* Scapy
* Linux environment (tested on Kali Linux)

Install Scapy:

```bash
sudo apt install python3-scapy
```

or:

```bash
pip install scapy
```

---

## 🚀 Usage

Clone the repository:

```bash
git clone https://github.com/mohammadaminahmed/syn-port-scanner.git
```

Enter the project directory:

```bash
cd syn-port-scanner
```

Run the scanner:

```bash
sudo python3 syn_scanner.py
```

---

## 📄 Example Output

```
Starting SYN Scan...

Target: 192.168.100.102

Port 22    -> OPEN
Port 80    -> CLOSED
Port 443   -> CLOSED
Port 3389  -> FILTERED

Scan completed successfully.
Report saved.
```

---

## 📂 Project Structure

```
syn-port-scanner/

│
├── syn_scanner.py
├── targets.txt
├── reports/
├── README.md
└── screenshots/
```

---

## 🔬 Technologies Used

* Python
* Scapy
* TCP/IP
* Linux
* Git & GitHub

---

## ⚠️ Disclaimer

This tool is created for educational purposes only.

Do not scan systems or networks without proper authorization.

The author is not responsible for misuse of this project.

---

## 👨‍💻 Author

Mohammad Amin Ahmed

Cybersecurity Student

GitHub:
https://github.com/mohammadaminahmed
