
# -*- coding: utf-8 -*-

from time import sleep
from TwitterAPI import TwitterAPI #pip install TwitterAPI
from serial import Serial #pip install pyserial


from auth_xxxx import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

microbitPort = '/dev/tty.usbmodem40122' # USB port address for the micro:bit /dev/ttyACM0 or /dev/tty.usbmodem40132 or similar
microbitBaud = '115200' # Baud for serial communication
microbitWaitTime = 0.001 # The length of time Python wait before attemping to issue commands to the micro:bit
stringToTrack = "#happy" # Change this to the search term you wish to track from Twitter
tweet_number = 0 #count Twitter in stream

ser = Serial(microbitPort, microbitBaud, timeout=3)
api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

print 'Twitter ready!'

r = api.request('statuses/filter', {'track':stringToTrack})
for item in r.get_iterator():
    if 'text' in item:
        tweet = item['text'].encode('utf-8').strip(stringToTrack) #making Tweet from stringToTrack
        ser.write("\n") #sending new line to micro:bit over Serial
        tweet_number = tweet_number + 1
        print tweet_number
        print tweet
        print('-------------------')
        print('')
        sleep(microbitWaitTime)
