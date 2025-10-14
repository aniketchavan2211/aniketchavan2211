
## Thumbwheel & Seven Segment Display Interface Using 8051


---

🔹 Set A – Slip TS1

Title:
Thumbwheel & Seven Segment Display Interface to 8051 Microcontroller


---

1️⃣ Objective
To interface a thumbwheel switch with 8051 microcontroller and display the selected number on a 7-segment LED display.


---

2️⃣ Apparatus / Components

Component	Description

8051 Microcontroller	Main controller
Thumbwheel Switch	Input device for selecting digits
Seven Segment Display	Display the selected digit
Resistors (220 Ω – 330 Ω)	Current limiting for LEDs
Breadboard & Wires	Circuit assembly
Power Supply (5V)	Operates microcontroller



---

3️⃣ Theory
A thumbwheel switch provides a binary-coded decimal (BCD) output corresponding to the selected number.

8051 reads the BCD value from the thumbwheel.

7-segment display is updated to show the corresponding decimal digit.

Used in digital panels, counters, and input devices.



---

4️⃣ Algorithm / Steps

1. Start.


2. Initialize 8051 input port (for thumbwheel) and output port (for 7-segment).


3. Read BCD value from thumbwheel switch.


4. Convert BCD to 7-segment code using lookup table.


5. Output code to 7-segment display.


6. Repeat steps 3–5 continuously.




---

5️⃣ Flowchart

┌─────────────┐
│   Start     │
└─────┬───────┘
      │
Initialize ports
      │
Read BCD from thumbwheel
      │
Convert BCD to 7-segment code
      │
Output to 7-segment display
      │
Loop back


---

6️⃣ Program (8051 Embedded C)

#include <reg51.h>

unsigned char seg_code[10] = {0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F};
// 0-9 Seven segment common cathode codes

sbit THUMB = P2; // Example: P2 input for thumbwheel (4 bits)
#define DISPLAY P1 // Seven segment display connected to P1

void main(void) {
    unsigned char val;
    while(1) {
        val = P2 & 0x0F; // Read lower 4 bits (BCD)
        DISPLAY = seg_code[val]; // Display corresponding number
    }
}

💡 Note: Adjust BCD reading according to thumbwheel wiring.


---

7️⃣ Observation Table

Thumbwheel Setting	BCD Output	7-Segment Display

0	0000	0
1	0001	1
2	0010	2
…	…	…
9	1001	9


Observed Result: Number selected on thumbwheel correctly displayed on 7-segment LED.


---

8️⃣ Result
Thumbwheel switch successfully interfaced to 8051. The selected digit is correctly displayed on 7-segment LED.


---

9️⃣ Conclusion
This practical demonstrates input device interfacing, BCD-to-7-segment conversion, and digital output control using 8051 microcontroller.


---

🔟 Viva Questions

Q	Answer

1. What is a thumbwheel switch?	A rotary switch that outputs a BCD value.
2. How is BCD converted to 7-segment code?	Using a lookup table in microcontroller memory.
3. Ports used?	Input port for thumbwheel, output port for display.
4. Applications?	Digital panels, counters, numerical input devices.
5. What is the common cathode code for 0?	0x3F



---

✅ Slip TS1 Completed


---

Next, we can do the Event Counter using Opto-Coupler and 7-Segment / LCD, which is also very easy.

Do you want me to proceed with that one now?

