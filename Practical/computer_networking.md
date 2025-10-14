## 4️⃣  Computer Networking Practical – LAN Setup & Configuration


---

🔹 Set A – Slip CN1

Title:
Study of Computer Network Components, LAN Setup, and IP/MAC Configuration


---

1️⃣ Objective
To study network components, their interconnections, and configure a Local Area Network (LAN) with IP and MAC addressing.


---

2️⃣ Apparatus / Components

Component	Description

Computers / PCs	Network nodes for LAN
Ethernet Cables (Cat5/6)	Connect devices
Switch / Hub / Router	Network interconnection devices
NIC (Network Interface Card)	Each computer’s network card
Command Prompt / Terminal	For IP/MAC configuration
LAN Simulator (Optional)	Cisco Packet Tracer, Packet Tracer, or real hardware



---

3️⃣ Theory

A computer network connects multiple devices to share data and resources.

LAN (Local Area Network) is a network limited to a small area (office, lab).

Components of LAN:

1. NIC – provides unique MAC address for each device.


2. Switch / Hub – connects devices and forwards data.


3. Router – connects LAN to other networks or internet.


4. Cables / Connectors – Ethernet cables (RJ-45) for wired connections.



IP Addressing: Logical address assigned to each device to identify it in the network.

MAC Address: Unique hardware identifier of NIC.



---

4️⃣ Algorithm / Steps

1. Start.


2. Connect devices via switch/hub using Ethernet cables.


3. Assign IP addresses to each device (static or DHCP).


4. Note MAC addresses using ipconfig /all (Windows) or ifconfig (Linux).


5. Test connectivity using ping between devices.


6. Observe communication and note any errors.


7. Optionally, configure router to simulate internet access.




---

5️⃣ Flowchart

┌─────────────┐
│   Start     │
└─────┬───────┘
      │
Connect PCs via switch/hub
      │
Assign IP addresses (Static/DHCP)
      │
Note MAC addresses of NICs
      │
Ping other devices to check connectivity
      │
Verify LAN operation
      │
──────┘ End


---

6️⃣ Procedure / Commands Example

Windows:

Check IP: ipconfig

Check MAC: ipconfig /all

Test connectivity: ping 192.168.1.2


Linux:

Check IP/MAC: ifconfig or ip addr

Test connectivity: ping 192.168.1.2


Static IP Assignment Example (Windows 10):

1. Control Panel → Network & Sharing → Change Adapter Settings


2. Right-click NIC → Properties → Internet Protocol Version 4 (TCP/IPv4)


3. Set IP: 192.168.1.2, Subnet: 255.255.255.0, Gateway: 192.168.1.1





---

7️⃣ Observation Table

Device	IP Address	MAC Address	Ping Result

PC1	192.168.1.2	00-1A-2B-3C-4D-5E	Success
PC2	192.168.1.3	00-1A-2B-3C-4D-5F	Success
PC3	192.168.1.4	00-1A-2B-3C-4D-60	Success


Observed Result: All PCs successfully communicate over the LAN; IP and MAC addresses verified.


---

8️⃣ Result
Local Area Network successfully set up. IP addresses assigned and MAC addresses verified. Devices can communicate via ping.


---

9️⃣ Conclusion
Practical demonstrates LAN setup, IP/MAC addressing, and basic network testing. Understanding of switches, routers, NICs, and Ethernet cabling is reinforced.


---

🔟 Viva / Oral Questions

Q	Answer

1. What is LAN?	Local Area Network connecting devices in a small area.
2. Difference between IP and MAC address?	IP → logical address; MAC → hardware address.
3. Use of switch?	Connect multiple devices, forward data packets.
4. How to test connectivity?	Using ping command between devices.
5. Difference between router and switch?	Router → connects networks; Switch → connects devices within a LAN.



---

✅ Slip CN1 Completed


---

This completes your easy Sem 1 practicals and the computer networking practical.

If you want, I can also prepare the remaining “moderate/hard” Sem 1 practicals like TDM, FSK, Hamming Code in one go, so your full Sem 1 journal is ready.

Do you want me to do that next?

