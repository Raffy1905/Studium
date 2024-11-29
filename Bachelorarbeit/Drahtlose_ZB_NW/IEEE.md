# IEEE 802.15.4

**Übertragungsraten:** 20 kb/s, 40 kb/s, 100 kb/s, 250 kb/s  
**Netzwerktypen:** Stern, Peer-to-Peer  
**Adressierung:** 16-bit oder 64-bit  
**Netzwerktyp:** CSMA-CA (Carrier sense multiple access with collision avoidance)  
**GTS:** *guaranteed time slots*; Zeitintervale für Zeitkritische Anwendungen  
Geringer Energieverbrauch  
**ED:** *Energy Detection* Energieerkennung auf unterstützten Funkkanälen  
**LQI:** *Link Quality indication* Bestimmung der Qualität der Verbinung  
**Frequenzbänder:** 2400-2483.5 MHz (weltweit), 868-868.6 MHz (Europa), 902-928 MHz (USA), 950-956 MHz (Japan), 314-316 MHz, 340-343 MHz, 779-787 MHz (China)


## Komponenten und Topologie:

2 oder mehr Funkmodule mit einem von 2 Gerätetypen:  
- **Full Function Device** (*FFD*)  
- **Reduced Function Device** (*RFD*)  

RFDs können nur mit FFDs kommunizieren. FFDs können mit anderen FFDs als auch RFDs kommunizieren. Beim Senden von Daten zwischen 2 RFDs wird ein FFD als Vermittler benötigt.  
IEEE 802.15.4 ist ein *Personal Area Network* (PAN). Ein FFD wird als PAN-Koordinator ausgewählt und verwaltet das PAN. Er ermöglicht den Beitritt in das PAN und weist jedem Gerät eine PAN-ID zu. (16-bit Adresse)

In der Sterntopologie verläuft jedlicher Datenaustauch über den PAN-Koordinator. Bei P2P können alle Funkmodulen mit allem Funkmodulen in Reichweite kommunizieren, vorrausgesetzt mind. eines davon ist ein FFD.



## Grundstruktur

2 Schichten:
- Physical Layer / PHY-Schicht (PHY-Schicht bei OSI)
- Media Access Control / MAC-Schicht (Bitübertragungsschicht bei OSI)

### Physical Layer
hardwarespezifische Implementierung  
Zusändig für:
- Übertragung der Signale über Hardware. 
- aktivieren und deaktivieren Transceiver 
- Senden und Empfangen über Transceiver.
- Überprüfen der Funkkanäle auf Aktivität
- Bestimmung der Qualität einer Verbindung
- Auswahl des günstigsten Funkkanals
- Bestimmung, ob ein Kanal frei oder belegt ist

### MAC-Schicht
Sorgt für zuverlässige Kommunikation in dem Netzwerk  
Bildung und Verwaltung des PANs, sowie zuverlässige Datenübertragung zwischen Funkmodulen  

Zuständig für:
- Senden und empfangen von sog Beacons zur Übermittlung von Verwaltungsinformationen und Synchronisierung
- Zugriffskontrolle auf den Funkkanal
- Validierung von Frames mittels CRC Prüfsumme
- Senden von Empfangsbestätigung (ack)
- Verbindung und Trennung von Funkmpdulen zum PAN
- Möglichkeit zur Nutzung von Sicherheitsmechanismen


### Aufbau der Schichten

Jede Schicht hat eine Datenbank (Information Base /IB) für Einstellungen. (variablen sowie konstanten)  
Jede Schicht hat einen Daten- und einen Managementdienst.  
**Datendients** -> Verarbeitung der empf. und zu sendenden Daten und Weiterleitung über *Service Access Points* (SAP) in andere Schichten.  
**Managementdienst** -> Verwaltungsaufgaben der Schicht, Verwaltet Zugriff auf Variablen und Kosntanten der IB


Dienst | Abkürzung | Schicht | Art
-|-|-|-
PHY Data | PD | PHY | Datendienst
MAC Common Part Sublayer | MCPS | MAC | Datendienst
Physical Layer Management Entity | PLME | PHY | Managementdienst
MAC Layer Management Entity | MLME | MAC | Managementdienst


### Primitive

Kommunikation der Schichten über Primitive.

***request:*** an unterliegende Schichten gesendet, um Service von unterer Schicht zu erhalten  
***confirm:*** Antwort auf eine zuvor erhaltene Request an nächsthöhere Schicht  
***indication:*** an nächsthöhere Schicht als Hinweis auf eingetretenes Event  
***response:*** Antwort auf eine Indication an untere Schicht. Nicht jedes indication Primitive erfordert eine Response  


