## Traffic Light Controller Using 8051 Microcontroller



🔹 Set A – Slip TL1

Title:
Traffic Light Controller Using 8051 Microcontroller



1️⃣ Objective
To simulate a traffic light sequence using 8051 microcontroller and LEDs.



2️⃣ Apparatus / Components

Component	Description

8051 Microcontroller	Main controller
LEDs (Red, Yellow, Green)	Represent traffic lights
Resistors (220 Ω – 330 Ω)	Current limiting
Breadboard & Wires	Circuit assembly
Power Supply (5V)	Operates microcontroller




3️⃣ Theory
Traffic lights control vehicular traffic at intersections.

Sequence: Red → Green → Yellow → Red

8051 microcontroller is programmed to turn ON/OFF LEDs with time delays simulating real traffic light timing.




4️⃣ Algorithm / Steps

1. Start.


2. Initialize 8051 output ports connected to LEDs.


3. Turn Red LED ON, others OFF → delay.


4. Turn Green LED ON, others OFF → delay.


5. Turn Yellow LED ON, others OFF → delay.


6. Repeat the sequence infinitely.





5️⃣ Flowchart
```
┌─────────────┐
│   Start     │
└─────┬───────┘
      │
Initialize LED Ports
      │
Red ON → Delay
      │
Green ON → Delay
      │
Yellow ON → Delay
      │
Loop back to Red
```


6️⃣ Program (8051 Embedded C)
```c
#include <reg51.h>

sbit RED = P1^0;
sbit YELLOW = P1^1;
sbit GREEN = P1^2;

void delay_ms(unsigned int ms) {
    unsigned int i, j;
    for(i=0;i<ms;i++)
        for(j=0;j<1275;j++);
}

void main(void) {
    while(1) {
        RED = 0; YELLOW = 1; GREEN = 1;  // Red ON
        delay_ms(1000);
        RED = 1; YELLOW = 1; GREEN = 0;  // Green ON
        delay_ms(1000);
        RED = 1; YELLOW = 0; GREEN = 1;  // Yellow ON
        delay_ms(500);
    }
}
```
💡 Note: LED ON is logic 0 if active low.



7️⃣ Observation Table

Step	LED Status	Delay

1	Red ON	1 s
2	Green ON	1 s
3	Yellow ON	0.5 s




8️⃣ Result
Traffic light sequence simulated successfully using 8051 and LEDs.



9️⃣ Conclusion
Microcontroller can control timed sequences of outputs. Traffic light simulation demonstrates digital output control and delays.



🔟 Viva Questions

Q	Answer

1. Why use delays?	To make LED changes visible.
2. Ports used?	Any 8051 output port, here P1.
3. LED active high or low?	Depends on wiring; can adjust program logic.
4. Applications?	Traffic light systems, sequence controllers.
