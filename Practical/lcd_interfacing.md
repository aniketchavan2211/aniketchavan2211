## LCD Interfacing to 8051 Microcontroller



🔹 Set A – Slip LCD1

Title:
Interfacing 16x2 LCD with 8051 Microcontroller



1️⃣ Objective
To interface a 16x2 LCD module with 8051 microcontroller and display alphanumeric characters.



2️⃣ Apparatus / Components

Component	Description

8051 Microcontroller	Main controller
16x2 LCD Module	Display output (16 characters × 2 lines)
Resistors (220 Ω – 330 Ω)	Current limiting for backlight
Potentiometer (10kΩ)	Adjust LCD contrast
Breadboard & Connecting Wires	Circuit assembly
Power Supply (5V)	Operates microcontroller and LCD




3️⃣ Theory
LCD (Liquid Crystal Display) modules display characters, numbers, and symbols.

16x2 LCD has 16 columns and 2 rows.

Operates in 4-bit or 8-bit mode.

8051 sends command or data through data lines and control signals (RS, RW, EN).

Common tasks: Initialize LCD, clear display, write data/characters.




4️⃣ Algorithm / Steps

1. Start.


2. Initialize 8051 ports connected to LCD data and control pins.


3. Initialize LCD (function set, display ON, clear display).


4. Send data/characters to display.


5. Repeat as needed for multiple messages or scrolling text.





5️⃣ Flowchart
```
┌─────────────┐
│   Start     │
└─────┬───────┘
      │
Initialize 8051 ports
      │
Initialize LCD (Function set, Display ON, Clear)
      │
Send character/data to LCD
      │
Wait for EN pulse
      │
Display characters
      │
Loop/Next message

```

6️⃣ Program (8051 Embedded C, 8-bit mode)
```c
#include <reg51.h>

sbit RS = P3^0;
sbit RW = P3^1;
sbit EN = P3^2;

#define LCD P2 // Data lines D0-D7 connected to P2

void delay_ms(unsigned int ms) {
    unsigned int i,j;
    for(i=0;i<ms;i++)
        for(j=0;j<1275;j++);
}

void lcd_cmd(unsigned char cmd) {
    LCD = cmd;
    RS = 0; RW = 0; EN = 1;
    delay_ms(2);
    EN = 0;
}

void lcd_data(unsigned char dat) {
    LCD = dat;
    RS = 1; RW = 0; EN = 1;
    delay_ms(2);
    EN = 0;
}

void lcd_init() {
    lcd_cmd(0x38); // 8-bit, 2 lines, 5x7 font
    lcd_cmd(0x0C); // Display ON, cursor OFF
    lcd_cmd(0x01); // Clear display
    delay_ms(2);
}

void lcd_string(unsigned char *str) {
    while(*str) {
        lcd_data(*str++);
    }
}

void main(void) {
    lcd_init();
    lcd_string("SPPU Practical");
    while(1);
}
```
💡 Note: Adjust pin mapping and delays according to your LCD and clock frequency.



7️⃣ Observation Table

Step	Command/Data Sent	LCD Display

1	0x38	LCD initialized
2	0x0C	Display ON, Cursor OFF
3	0x01	Display cleared
4	"SPPU Practical"	Characters displayed on first line


Observed Result: LCD displays the string correctly.



8️⃣ Result
16x2 LCD successfully interfaced with 8051. Characters and messages can be displayed as per program.



9️⃣ Conclusion
This practical demonstrates LCD initialization, command/data communication, and alphanumeric display using a microcontroller.



🔟 Viva / Oral Questions

Q	Answer

1. What is 16x2 LCD?	LCD with 16 characters per line and 2 lines.
2. What are control pins?	RS, RW, EN for selecting command/data, read/write, and enabling data transfer.
3. Difference between command and data?	Command → configure LCD; Data → display characters.
4. Which modes are used?	4-bit or 8-bit mode.
5. Applications?	Digital displays, counters, microcontroller projects.
