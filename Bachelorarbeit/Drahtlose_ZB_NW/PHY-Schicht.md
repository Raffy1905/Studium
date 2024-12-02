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


