# sending text to micro:bit from Python

<img src="https://github.com/udirbetalab/microbit/blob/master/text/text_from_python.png"><br>
https://makecode.microbit.org/_E3pdgUJkh8AH

Python code:
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
https://github.com/udirbetalab/microbit/blob/master/text/text_to_microbit.py
