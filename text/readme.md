# sending text to micro:bit

<img src="https://github.com/udirbetalab/microbit/blob/master/text/text_from_python.png"><br>
https://makecode.microbit.org/_E3pdgUJkh8AH

```
#micro:bit code https://makecode.microbit.org/_E3pdgUJkh8AH


from serial import Serial
import time

microbitPort = '/dev/tty.usbmodem40122' #change port 
microbitBaud = '115200'
ser = Serial(microbitPort, microbitBaud, timeout=3)

while True:
    text = input("Write to micro:bit: ") + '\n'
    print("Sending: " + text)
    ser.write(text.encode())
    time.sleep(1)
```
