## FSK

Title:
Build and Test Frequency Shift Keying (FSK) Circuit


---

1️⃣ Objective
To study Frequency Shift Keying (FSK) and generate digital signals transmitted using two distinct frequencies representing logic ‘0’ and logic ‘1’.


---

2️⃣ Apparatus / Components

Component	Description

Function Generator / Microcontroller	Generate input digital signal (binary data)
XR-2206 IC / 555 Timer / FSK Modulator Circuit	Generate FSK signals
Oscilloscope	Observe output waveform and frequency shifts
Power Supply (5V)	Circuit operation
Breadboard & Connecting Wires	Circuit assembly



---

3️⃣ Theory
Frequency Shift Keying (FSK) is a digital modulation technique in which binary data is transmitted by changing the frequency of a carrier signal:

Logic 1 → Frequency f1

Logic 0 → Frequency f0


FSK is robust against noise and widely used in modems, telemetry, and radio communication.

Example:

Binary data: 1010

Assign f1 = 2 kHz for logic 1, f0 = 1 kHz for logic 0

Transmitted signal switches between 2 kHz and 1 kHz according to the data sequence.



---

4️⃣ Algorithm / Steps

1. Start.


2. Generate digital input data stream (e.g., 1010).


3. Assign frequencies for logic 0 and 1 (f0 = 1 kHz, f1 = 2 kHz).


4. Use FSK modulator IC/circuit to shift the carrier frequency based on input.


5. Observe the modulated signal on an oscilloscope.


6. Verify that frequency changes correspond correctly to logic 0 and 1.


7. Record observations.




---

5️⃣ Flowchart

┌─────────────┐
│   Start     │
└─────┬───────┘
      │
Generate digital input (binary data)
      │
Assign f0 for 0, f1 for 1
      │
FSK Modulation → switch carrier frequency
      │
Transmit modulated signal
      │
Observe waveform on oscilloscope
      │
Check frequency shift matches input data
      │
──────┘ Loop / End


---

6️⃣ Circuit Diagram / Example Setup

Input data: 1010 (digital square wave)

Logic 1: 2 kHz output frequency

Logic 0: 1 kHz output frequency


Observation on Oscilloscope:

Time → 
Logic: 1 0 1 0
Freq : f1 f0 f1 f0
Waveform shows alternating frequencies corresponding to the binary input.

Components:

XR-2206 IC: Monolithic function generator for FSK

Input digital data → modulates output frequency between f0 and f1

Output observed on oscilloscope



---

7️⃣ Observation Table

Time Slot	Input Data	Output Frequency	Observation

t1	1	2 kHz	Logic 1 → higher frequency
t2	0	1 kHz	Logic 0 → lower frequency
t3	1	2 kHz	Logic 1 → higher frequency
t4	0	1 kHz	Logic 0 → lower frequency


Observed Result: Frequency of carrier correctly switches according to input digital data.


---

8️⃣ Result
FSK modulation successfully demonstrated. The transmitted digital data was represented accurately using two different carrier frequencies.


---

9️⃣ Conclusion
Frequency Shift Keying (FSK) allows digital signals to be transmitted over an analog channel using two distinct frequencies. The experiment demonstrates digital-to-analog modulation and how binary data is converted into frequency variations.


---

🔟 Viva / Oral Questions

Q	Answer

1. What is FSK?	Digital modulation technique using two distinct frequencies for 0 and 1.
2. Example of FSK use?	Modems, telemetry, radio communication.
3. Difference between ASK and FSK?	ASK → amplitude changes; FSK → frequency changes.
4. How do you generate FSK?	Using function generator, 555 timer, or XR-2206 IC modulator.
5. What is the advantage of FSK?	Robust against noise, reliable digital data transmission.



---

✅ Slip FSK1 Completed


---

If you want, I can next make a detailed journal slip for Hamming Code (Error Detection & Correction) in the same format so your Sem 1 practicals journal is ready.

Do you want me to do that?

