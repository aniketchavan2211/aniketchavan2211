## 2. Program Raspberry Pi to get feedback from switch connected to GPIO pins

**Aim: To program Raspberry Pi to read status of switch and control LED accordingly.**

**Algorithm:**

1. Import GPIO library.
2. Import time library.
3. set the numbering scheme to be used.
4. set the pins / channels connected to LEDs as Output.
5. set the pins / channels connnected to push button switches connected
as active low as input.
6. Read the positions of switch 1 and switch 2.
7. Send logic state to output to make LED1 ON or OFF depending on state of switch 1.
8. Send logic state to output to make LED2 ON or OFF depending on state of switch 2.
9. wait for some time.
10. Go to step 6.
11. Free up the resources and return the channels to default of being inputs.

**Programs:**
**Q.1 One Switch and one LED**
```python3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
switch1 = 17
led1 = 4

GPIO.setup(switch1, GPIO.In, pull_ip_down = GPIO.PUD_UP)
GPIO.setup(led1, GPIO.OUT)

while (True):
    my_input = GPIO.input(switch1)
    if my_input == False:
        GPIO.output(led1, 0)
    else:
        GPIO.output(led1, 1)

GPIO.cleanup()
```

**Q. Two Switch and Two LEDs:**
```python3
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

switch1 = 23
switch2 = 18

led1 = 5
led2 = 19

GPIO.setup(switch1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(switch2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

while(True):

    my_input = GPIO.input(switch1)

    if my_input == False:
        GPIO.output(led1, 0)
    else:
        GPIO.output(led1, 1)

    my_input = GPIO.input(switch2)

    if my_input == False:
        GPIO.output(led2, 0)
    else:
        GPIO.output(led2, 1)

GPIO.cleanup()
```
