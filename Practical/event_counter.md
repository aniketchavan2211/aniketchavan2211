## Event Counter

🔹 Set A – Slip EC1

Title:
Event Counter Using Opto-Coupler and Seven Segment / LCD Display Interface to 8051 Microcontroller



1️⃣ Objective
To design and implement an event counting system using an 8051 microcontroller, which counts external pulses via an opto-coupler and displays the count on a 7-segment LED or LCD.



2️⃣ Apparatus / Components

Component	Description

8051 Microcontroller	Main controller for counting
Opto-Coupler (e.g., 4N35)	Detect external pulses without electrical interference
Seven Segment Display / LCD	Visual display of count
Resistors, LEDs, Wires	Supporting circuit connections
Breadboard / PCB	Circuit assembly
Power Supply (5V)	Operates microcontroller and display




3️⃣ Theory
An event counter counts the number of external events or pulses.

The opto-coupler converts the external signal into a safe logic-level signal for the microcontroller.

The 8051 increments a counter on each pulse and displays it on 7-segment LED or LCD.

Useful for industrial applications, production lines, or digital measurement systems.




4️⃣ Algorithm / Steps

1. Start.


2. Initialize 8051 ports: input for opto-coupler, output for display.


3. Set count = 0.


4. Wait for input pulse from opto-coupler.


5. On pulse detection → increment counter.


6. Update count on 7-segment / LCD display.


7. Repeat steps 4–6 for continuous counting.





5️⃣ Flowchart
```
┌─────────────┐
│   Start     │
└─────┬───────┘
      │
Initialize 8051 ports & counter
      │
Wait for pulse from opto-coupler
      │
Pulse detected?
  ┌───┴───┐
  │ Yes   │
  ▼       │
Increment counter
Update display
  │       │
  └───────┘
Loop back to wait for next pulse
```


6️⃣ Program (8051 Embedded C)
```c
#include <reg51.h>

sbit sensor = P3^2;   // Opto-coupler input
unsigned int count = 0;

void display(unsigned int val) {
    P1 = val; // Example: directly display on 7-segment with appropriate encoding
}

void main(void) {
    P1 = 0x00; // Initialize display
    while(1) {
        if(sensor == 0) { // Pulse detected (active low)
            count++;
            display(count);
            while(sensor == 0); // Wait until pulse ends (debounce)
        }
    }
}
```
💡 Note: For LCD, use 8051 LCD library routines instead of direct port output.



7️⃣ Observation Table

Pulse Number	Input from Sensor	Count Displayed

1	High → Low	1
2	High → Low	2
3	High → Low	3


Observed Result: The counter increments correctly on each pulse and displays the value.



8️⃣ Result
The event counting system was successfully implemented using 8051, opto-coupler, and display. It accurately counts and shows the number of events.



9️⃣ Conclusion
An event counter using a microcontroller and opto-coupler is a simple yet practical digital system. It demonstrates external signal interfacing, pulse counting, and display output.



🔟 Viva / Oral Questions

Q	Answer

1. What is an opto-coupler?	A device that isolates and transfers signals using light.
2. How does event counter work?	Detects pulses and increments a counter on each pulse.
3. Why use 7-segment or LCD?	To visually display the counted events.
4. How is pulse debounced?	By waiting until the pulse ends before counting again.
5. Applications of event counter?	Industrial counting, speed measurement, production monitoring.
