## 6. Temperature and Humidity sensing using Arduino
**Program:**
```c
#include <DHT11.h>
DHT11 aniket(8);
void setup() {
    serial.begin(9600);
}

void loop() {
    int var1, var2;
    var1 = aniket.readTemperature();
    var2 = aniket.readHumidity();
    serial.print("temperature: ");
    serial.print("var1");
    serial.print("humidity: ");
    serial.print("var2");
    serial.print("/n");
    delay(1000);
}
```
