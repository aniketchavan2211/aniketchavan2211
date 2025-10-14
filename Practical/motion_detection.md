## 3. Program Raspberry Pi for motion detection using PIR Sensor

**Aim: To study and understand programming of Raspberry Pi for motion detection using PIR sensor.**

**Program:**
```python3
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 23
BUZZ = 6
PIR = 18

GPIO.setup(PIR, GPIO.IN)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZ, GPIO.OUT)

while(1):

    my_input = GPIO.input(PIR)

    if my_input == True:

        GPIO.output(LED, 0)
        GPIO.output(BUZZ, 1)

        print("Motion is detected")

    else:
        GPIO.output(BUZZ, 0)
        GPIO.output(LED, 1)

        print("motion is not detected")

        time.sleep(1)

GPIO.cleanup()

```
