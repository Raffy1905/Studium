# PHY-Schicht

Schnittstelle zur HW -> Senden und Empfangen von Daten  


## Konstanten und Variablen

**Datenbank:** PHY-PAN Information Base (PHY-PIB)  
Konstanten beginnen alle mit einem *a*, Variablen mit *phy*  

### Konstanten
Konstante | Beschreibung | Wert
-|-|-
aMaxPHYPachetSize | Maximale Größe an Nutzdaten eines PHY-Frame | 127 (Bytes)
aTurnaroundTime | Maximale Zeit, welche benötigt wird, um von RX in TX zu wechseln und umgekehrt | 12 (Symboldauer)

### Variablen
Variable | Beschreibung | Wertebereich
-|-|-
phyCurrentChannel | Der für den Datenverkehr benutzte Funkkanal | 0-26
phyChannelsSupported | - | -
phyTXPower | Sendeleistung des Funkmoduls in dbm | Signed Integer
phyTXPowerTolerance | Toleranz der Sendeleistung | 1/3/6 db
pyhCCAMode | CCA-Mode | 1-6
phyCurrentpage | Zusammen mit phyCurrentChanel erigbt sich die benutzte Frquenz und Modulation | 0-31 
phyMaxframeDuration | Maximale Anzahl von Symbolen in einem Frame | Integer
...

## Servicedienste und zugehörige Primitive

Zwei unterschiedliche Kategorien: PHY Dada (PD) beinhält Dienst für Datenübertragung und Physical Layer Management Entity (PLME) beinhält Dientste für Managementaufgaben

### PHY Data Service
Austausch von Daten mit der darüberliegender (MAC-) Schicht  
**SUCCESS** erfolgreiche Datenübertragung  
**RX_ON** Failed: Receiver aktivert  
**TRX_OFF** Failed: Transmitter deaktiviert  
**BUSY_TX** Failed: andere Datenübertragung findet statt  

### PLME GET / PLME SET
Zugriff auf Variablen der PHY-Schicht  
**SUCCESS** Erfolgreich - PIBAttributeValue gefüllt  
**UNSUPPORTED_ATTRIBUTE** Failed: Variable existiert nicht

**SUCCESS** Erfolgreich  
**UNSUPPORTED_ATTRIBUTE** Variable existiert nicht  
**INVALID_PARAMETER** Failed: ungültiger Wert
**READ_ONLY** Failed: Zugriff auf Read-only Variable

### PLME ED
Energieerkennung auf einem Funkkanal, um Kanälen mit viel Funkverkehr ausweichen zu können.  
**SUCCESS** Energielevel von 0x00 bis 0xFF  
**TX_ON** Failed: Transmitter sendet gerade  
**TRX_OFF** Failed: Receiver deaktiviert  



## PHY Frame
### Synchronisationsheader (SHR)
Kennzeichnung des Anfangs des Frames  
**Präambelsequenz** Wiederholende Sequenz von gleichen Zeichen und leitet ein Frame ein  
**Framestartbegrenzer** Ende der Präambelsequenz und Beginn der eigentlichen Framestruktur  

### PHY Header (PHR)
Framelänge (7 bit - Wert bis 127)
