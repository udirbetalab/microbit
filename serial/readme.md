# Hvordan lese data fra micro:bit på din PC eller MAC.

I dette eksemplet tar vi utgangspunkt i den innebygde lyssensoren til micro:bit, men du kan fint bruke de andre sensorene om du ønkser det. <br>
<br>
<img src="https://github.com/udirbetalab/microbit/blob/master/serial/filer/serial_write.png" width="500"><br>
micro:bit kode: https://github.com/udirbetalab/microbit/blob/master/serial/filer/serial_write.png<br>
<br>
# Windows PC
For å lese data fra seriellport på din Windows PC er det enklest å bruke programmet <b>Putty</b> - https://www.putty.org/<br>
Last ned og installer programmet på din PC.<br>
<br>
Når en micro:bit er tilkoblet din PC har den fått tilordnet en COM port. Raskeste måte å finne COM porten til micro:bit er ved hjelp av Ledetekst som du får opp ved hjelp av CMD i søkefeltet fra startknappen.<br>
I Ledetekst vinduet skriver du komandoen <b>mode</b><br>
<img src="https://github.com/udirbetalab/microbit/blob/master/serial/filer/01.PNG"><br>
Her ser dere ett eksemple uten micro:bit tilkoblet.<br>
<br>
<img src="https://github.com/udirbetalab/microbit/blob/master/serial/filer/02.PNG"><br>
Her ser dere ett eksempel der micro:bit er tilkoblet og har COM port COM3<br>
<br>
Når du vet hvilken port micro:bit bruker kan du nå koble deg opp mot micro:bit ved hjelp av Putty med COM3 og 115200 som er kommunikasjonshastigheten til micro:bit<br>
<img src="https://github.com/udirbetalab/microbit/blob/master/serial/filer/06.png"><br>
<br>
<img src="https://github.com/udirbetalab/microbit/blob/master/serial/filer/07.PNG"><img src="https://github.com/udirbetalab/microbit/blob/master/serial/filer/08.PNG"><br>
Over ser dere eksempler på verdier sendt fra micro:bit. Til venstre er det kontorplass lysstyrke og til høyre er det tildekt micro:bit.<br>
# MAC

På MAC er det litt enklere å få tilgang til seriell data fra micro:bit. Du trenger ikke eget programm som Putty, men du bruker terminalvinduet som er innebygd i operativsystemet.<br>
Åpne terminalvinduet og skriv inn kommandoen <b>ls -l /dev/tty.usb*</b> for å liste opp alle USB som er koblet til den MAC.<br>
<img src="https://github.com/udirbetalab/microbit/blob/master/serial/filer/09.PNG"><br>
Som dere ser over er micro:bit koblet til på <b>/dev/tty.usbmodem40122</br>
For å koble til terminalvinduet til micro:bit og lese ut verdier, bruker dere komandoen <b>screen /dev/tty.usbmodem40122 115200</b> der tallet etter <i>usbmodem</i> må byttes ut med dine verdier. Tallet 115200 er kommunikasjonshastigheten til micro:bit.<br>
<img src="https://github.com/udirbetalab/microbit/blob/master/serial/filer/10.PNG"><br>
Over ser dere verdiene som kommer fra micro:bit<br>

# hva kan dette brukes til?


Skal du kommunisere med micro:bit fra din datamaskin er det vitig å kjenne til hvilken port (COM eller tty.usbmodemXXXX eller tilsvarende) micro:bit har. 

