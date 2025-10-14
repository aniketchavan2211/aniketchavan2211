## 1. Program of Raspberry Pi to control LEDs attached to GPIO pins

**Q. Blinking LED using raspberry pi GPIO:**

```python3
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED1=4

GPIO.setup(LED1, GPIO.OUT)

while(1):

    GPIO.output(LED1, 1)
    time.sleep(1)

    GPIO.output(LED1, 0)
    time.sleep(1)

GPIO.cleanup()
```

**Q. Blinking of four LEDs interfacing with Raspberry Pi GPIO pins:**

```python3
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.semode(GPIO.BCM)

LED1 = 4
LED2 = 14
LED3 = 17
LED4 = 16

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

while(1):
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 1)

    time.sleep(1)

    GPIO.output(LED1, 0)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 0)

    time.sleep(1)

GPIO.cleanup()
```


**Q. Ring Counter with 4 LEDs:**
```python3
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED1 = 4
LED2 = 17
LED3 = 18
LED4 = 27

Arrled = [LED1, LED2, LED3 , LED4]

GPIO.setup(Arrled, GPIO.OUT)

while(1):
    GPIO.output(Arrled, [0, 1, 1, 1])
    time.sleep(1)

    GPIO.output(Arrled, [1, 0, 1, 1])
    time.sleep(1)

    GPIO.output(Arrled, [1, 1, 0, 1])
    time.sleep(1)

    GPIO.output(Arrled, [1, 1, 1, 0])
    time.sleep(1)

GPIO.cleanup()

```


