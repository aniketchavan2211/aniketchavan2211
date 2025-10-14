## TDM

Title:
Build and Test Time Division Multiplexing (TDM) Circuit



1️⃣ Objective
To study and demonstrate Time Division Multiplexing (TDM) and separate multiple digital signals using time slots.



2️⃣ Apparatus / Components

Component	Description

Logic Gates / ICs	AND, OR, NOT, Flip-Flops (for timing)
Function Generator	Generate input digital signals
Oscilloscope	Observe multiplexed output
Power Supply (5V)	Circuit operation
Connecting Wires & Breadboard	Circuit assembly


3️⃣ Theory
Time Division Multiplexing (TDM) allows multiple signals to share a single channel by allocating unique time slots to each signal. Signals are transmitted sequentially; the receiver demultiplexes them by sampling at the correct time slot.

Use: Telecommunication, digital data transmission.



4️⃣ Algorithm / Steps

1. Start.


2. Generate two or more digital input signals (e.g., A and B).


3. Assign time slots to each signal.


4. Use logic gates/flip-flops to multiplex signals sequentially.


5. Transmit through single channel.


6. At receiver, sample signals according to time slots → demultiplex.


7. Observe output on oscilloscope or LEDs.





5️⃣ Flowchart
```
┌─────────────┐
│   Start     │
└─────┬───────┘
      │
Generate digital input signals
      │
Assign time slots to each signal
      │
Multiplex signals sequentially
      │
Transmit over single channel
      │
Demultiplex at receiver based on time slots
      │
Observe outputs
      │
──────┘ Loop / End
```


6️⃣ Observation & Output

Step	Input Signals	Output (Multiplexed)

1	A = 1010	A + B interleaved
2	B = 1100	Signals separated by time slots


Observed Result: Multiple digital signals successfully transmitted over a single channel and separated at receiver using time slots.



7️⃣ Result
TDM circuit successfully built and tested; signals transmitted sequentially and correctly demultiplexed at the receiver.



8️⃣ Conclusion
TDM is an efficient method to transmit multiple signals over a single channel by assigning unique time slots. The experiment demonstrates signal multiplexing and demultiplexing.



9️⃣ Viva / Oral Questions

Q	Answer

1. What is TDM?	Technique to share one channel among multiple signals using time slots.
2. How are signals separated at receiver?	By sampling each signal in its allocated time slot.
3. Use of TDM?	Telecommunication and digital data transmission.
4. Difference between TDM and FDM?	TDM → time slots; FDM → different frequencies.
5. Hardware used for TDM?	Flip-flops, logic gates, function generator.
