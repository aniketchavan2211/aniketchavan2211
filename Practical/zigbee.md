## 8. Study Zig-bee communication for one application.

**Program:**

**Transmitter:**
```c
void setup() {
    serial.begin(9600);
}
void loop() {
    float x1 = analogRead(A0);
    float x2 = analogRead(A1);
    x1 = x1 * 5 / 1023 * 100;
    serial.print(x1);
    serialprint("/n");
    x2 = x2 * 5 / 1023 *1;
    serial.print(x2);
    serial.print("/n");
    delay(3000);
}
```

**Receiver:**

```c
char xyz[10];
void setup() {
    serial.begin(9600)
}
void loop() {
    int i = 0;
    if (serial.available(1>0)) {
        i = 0;
        while (i < 10) {
            xyz[i] = char(serial.read());
            i = i+1;
            delay(100);
        }
        for (i=0, i<10, i++) {
            serial.print(xyz[i]);
        }
    delay(1000);
    }
}

```
