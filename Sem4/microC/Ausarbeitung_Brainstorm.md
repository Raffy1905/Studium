### Allgemeine Informationen
**Drehzahlbereich:** 800 U/min - 6.000U/min
**Geberad:** 36 Zähne - Lücke von 2 Zähnen

### Bestimmung der Drehzahl
36 Zähne auf 360° -> 10° pro Zahn
Timer bei Steigender Flanke auf 0 setzen und zählen lassen.
 - Timer-Frequenz deutlich kleiner als 0,278 ms
 - Timer maximum groß genug für 800 U/min

### Berechnungen
Mit der Drehzahl n, kann man sich die Anzahl der Zähne pro Minute berechnen.

$$n_{min}={800 {{U} \over min}} = {800 * 36{{Zähne} \over min}}$$
$$n_{max}={6.000 {{U} \over min}} = {6.000 * 36{{Zähne} \over min}}$$

Minuten in Sekunden:

$$n_{min}={800 * 36{{Zähne} \over min}} = {800 * 36{{Zähne} \over 60 s}} = {80 * 6{{Zähne} \over s}}$$
$$n_{max}={6.000 * 36{{Zähne} \over min}} = {6.000 * 36{{Zähne} \over 60 s}} = {100 * 36{{Zähne} \over s}}$$

Zeit für einen Zahn:

$$t_{max}={1 \over {80 * 6{{Zähne} \over s}}} = {{1 \over 480} s}$$
$$t_{min}={1 \over {100 * 36{{Zähne} \over s}}} = {{1 \over 3.600} s}$$

in Millisekunden:

$$t={{1 \over 480} * 1000 ms} = {{100 \over 48} * ms} \approx 2,083 ms$$
$$t={{1 \over 3.600} * 1000 ms} = {{1 \over 3,6} * ms} \approx 0,278 ms$$



