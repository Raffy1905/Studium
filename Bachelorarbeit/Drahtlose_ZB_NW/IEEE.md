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

