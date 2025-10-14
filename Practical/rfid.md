## 7. Study of RFID System

**Program:**

```c
char aniket[12];
void setup() {
    serial.begin(9600);
}
void loop() {
    int i = 0;
    if (serial.available()) {
        while (i < 12) {
            aniket[i] = serial.read();
            i = i+1;
            delay(10);
        }
        for (i=0, i<12, i++) {
            serial.print(aniket[i]);
        }
    serial.print("/n");
    }
}
```
