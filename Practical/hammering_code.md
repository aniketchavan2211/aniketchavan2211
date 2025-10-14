## Hammering code

Title:
Study of Error Detection and Correction Using Hamming Code Technique


---

1️⃣ Objective
To study Hamming Code for detecting and correcting single-bit errors in digital data transmission.


---

2️⃣ Apparatus / Components

Component	Description

Logic Gates / ICs	AND, OR, XOR gates
Binary Data Source	Manual input switches or microcontroller
LEDs	Visualize transmitted and received bits
Breadboard & Wires	Circuit assembly
Power Supply (5V)	Circuit operation



---

3️⃣ Theory
Hamming Code is an error-detecting and correcting code used in digital communication.

Adds parity bits to original data bits to detect and correct errors.

Single-bit errors can be detected and corrected automatically.

Positions of parity bits: powers of 2 → 1, 2, 4, 8…

Example: For 4-bit data 1011, parity bits added → p1 p2 d1 p4 d2 d3 d4 → transmitted.

Receiver recalculates parity → identifies error → flips erroneous bit → corrects data.



---

4️⃣ Algorithm / Steps

1. Start.


2. Take original data bits (e.g., 4-bit data 1011).


3. Calculate parity bits using even parity.


4. Place parity bits at positions 1, 2, 4, etc. → create Hamming code word.


5. Transmit code word.


6. Introduce single-bit error manually or simulate error.


7. Recalculate parity bits at receiver → detect error position.


8. Correct the erroneous bit.


9. Observe corrected data.




---

5️⃣ Flowchart

┌─────────────┐
│   Start     │
└─────┬───────┘
      │
Input data bits (e.g., 1011)
      │
Calculate parity bits
      │
Transmit Hamming code
      │
Introduce single-bit error
      │
Receiver recalculates parity
      │
Detect error position
      │
Correct erroneous bit
      │
Observe corrected data
      │
──────┘ End


---

6️⃣ Example

Original 4-bit data: 1011

Parity bits (even parity) added → 7-bit Hamming code: p1 p2 d1 p4 d2 d3 d4 = 0111011

Introduce error at bit 5 → received: 0111111

Recalculate parity → error detected at bit 5 → correct it → 0111011


Observation: Single-bit error successfully detected and corrected.


---

7️⃣ Observation Table

Step	Data / Hamming Code	Observation

1	1011	Original data
2	0111011	Hamming code generated
3	0111111	Error introduced at bit 5
4	0111011	Error detected and corrected



---

8️⃣ Result
Hamming Code technique successfully used to detect and correct single-bit errors in transmitted data.


---

9️⃣ Conclusion
Hamming Code is an effective method for error detection and correction, improving reliability in digital communication systems.


---

🔟 Viva / Oral Questions

Q	Answer

1. What is Hamming Code?	Error-detecting and correcting code for single-bit errors.
2. How are parity bits positioned?	At positions that are powers of 2 → 1, 2, 4, 8…
3. What types of errors can it correct?	Single-bit errors.
4. Difference between parity and Hamming Code?	Parity detects only errors; Hamming can detect and correct single-bit errors.
5. Use of Hamming Code?	Reliable digital communication, memory systems, network data transfer.



---

✅ Slip HAM1 Completed


---

Now you have TDM, FSK, and Hamming Code slips ready in full journal format for your Sem 1 practicals.

If you want, I can also make a slip for “Event Counter using Opto-Coupler / Seven Segment Display”, which is another easy and common practical for Sem 1.

Do you want me to do that next?

