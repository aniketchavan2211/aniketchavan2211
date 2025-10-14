## 4. Progarmming Raspberry Pi for image detection using Pi camera.

**Q. Program: To capture image**
```python3
import RPi.GPIO as GPIO
import time
import picamera

switch = 14
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_UP)
picture = picamera.picamera()
picture.rotation = 90
picture.brightness = 40
picture.resolution = (720, 480)
picture.sharpness = 80
time.sleep(2)
while(1):
    if (GPIO.input(switch) == 0):
        picture.start_preview()
        time.sleep(5)
        picture.capture("aniket.jpg")
        picture.stop_preview()
GPIO.cleanup()

```

**Q. To record video:**
```python3
import RPi.GPIO as GPIO
import time
import picamera
switch = 14
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_UP)
camera = picamera.picamera()
camera.rotation = 180
camera.brightness = 65
time.sleep(2)
while(1):
    if (GPIO.input(switch) == 0):
        camera.start_preview()
        camera.start_recording("aniket.h264")
        time.sleep(5)
        camera.stop_recording()
        camera.stop_preview()
GPIO.cleanup()

```
