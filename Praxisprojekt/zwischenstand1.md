# Thermostate

## Homematic IP
Keine Anmeldung erforderlich. Kopplung durch Scannen eines Codes.
Inklusive Fenster-offen Erkennung. Die Erkennung kann mit Fenstersensoren genauer werden.  
Für den Betrieb der Sensoren kann die HomematicIP App genutzt werden, jedoch kann mit der HomematicIP Rest API wahrscheinlich auch eine Software geschrieben werden, über die im Anschluss die Heizverläufe, Temperaturen etc eingestellt werden können.

## sonstige
Optionaler Vergleich mit Sperrthermostaten. 

# Energiemessung

Messung der Temperatur am Heizkörper und im Raum. Mit der Temperaturdifferenz kann im Anschluss die verbrauchte Energie angeschätzt werden.

## Aufbau

2 Wärmesensoren (DS18B30 je ca 5 €) mit einem ESP32-c6-DevKitM (ca 15 €) 
Mosquito MQTT - Telegraf - InfluxDB - Grafana  
über Docker auf internem Server installiert.  
Für die Stromversorgung wird eine LiFePo 18650 Batterien mit 3,2V genutzt. Die LiFePo haben weniger Risiko als herkömmliche Lithium-Ionen Batterien.  (~ 10 €) plus eine Halterung für die Batterie (~ 1 €). Zudem wird ein Ladegerät für die Batterien benötigt (~ 40 €)

**Gesamtaufbau pro Raum:**   
$$
LiFePo + Sensoren + ESP32 + Halterung \\
= 10 € + 15 € + 10 € + 1 € = 36 €
$$
Für Wetterdaten wird Free Weather API genutzt, welches für non-commercial use kostenlos ist bei weniger als 10'000 API-calls am Tag.

## Berechnung
Für die Berechnung gibt es unterschiedliche Möglichkeiten. Die Schwierigkeit ist, Genauigkeit und Aufwand abzuwiegen.  
Ansatz:
$$
\dot{Q} = \alpha \cdot A \cdot (T_{Heizkörper} - T_{Raum})
$$
Alpha ist abhängig von dem Heizkörper und umgebungsbedingten Faktoren. Dadurch muss der Wert entweder gemessen oder geschätzt werden. Da die Messung und Berechnung des Wertes relativ umständlich ist, schätze ich den Wert ab. Die genauere Weise wäre es, den Wert zu berechnen.  
Da die gesamte Messung selbst aber bereits nur annäherungsweise Ergebnisse liefert, da genaue Messungen sehr viel umständlicher und teurer sind und es lediglich um des Vergleich geht, ist die Abweichung nicht so relevant.  
Lediglich die Amortisationsdauer lässt sich dadurch nicht wirklich gut abschätzen.




# Kosten

### HomematicIP Evo / KOMPAKT
Produkt | Minimum | Fenster | Sperr | Sperr + Fenster
-|-|-|-|-
smart Thermostat | 80 | 80 | 80 | 80
Access Point | 50 | 50 | 50 | 50
Fenstersensoren | - | 100 | - | 100
Sperrthermostat | - | - | 20 | 20
Sensoraufbau | 72 | 72 | 108 | 108
Ladegerät | 40 | 40 | 40 | 40
Ersatzbatterien | 20 | 20 | 30 | 30
-|-|-|-|-
**Gesamt** | 262 | 362 | 328 | 428

### HomematicIP Basic
Produkt | Minimum | Fenster | Sperr | Sperr + Fenster
-|-|-|-|-
smart Thermostat | 30 | 30 | 30 | 30
Access Point $^1$ | - | 20 | - | 20
Fenstersensoren | - | 100 | - | 100
Sperrthermostat | - | - | 20 | 20
Sensoraufbau | 72 | 72 | 108 | 108
Ladegerät | 40 | 40 | 40 | 40
Ersatzbatterien | 20 | 20 | 30 | 30
-|-|-|-|-
**Gesamt** | 162 | 312 | 228 | 378
$^1$ Smart Home starter Pack für 50 mit Access Point and Thermostat

# Links

Open Weather API: https://open-meteo.com/  
Thermostats: [Amazon.de](https://www.amazon.de/Homematic-IP-Smart-Home-Heizk%C3%B6rperthermostat/dp/B08YDVCBY9?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=A29K75SSZ258MM&th=1)  
Sperrthermostat: [bauhaus.info](https://www.bauhaus.info/thermostatkoepfe/heimeier-heizkoerper-thermostat/p/25716072)  
Fensterkontakte: [Amazon.de](https://www.amazon.de/-/en/Homematic-Window-Contacts-Optical-Battery/dp/B082LQSTBJ/ref=sr_1_2?crid=ZQN33QYVSTS2&dib=eyJ2IjoiMSJ9.rvtcpIcTk_iTqbwhpeiJt0K5oBNW5yPaNR0iwA4BOGpa7PPBjAFjgAw0i6Wd4ScKA8eeHJ5gIjz084sWqRRC4mDQB1-pr3Kw0-lIExCPsrM94kJ5FxCEA1w3KUY64sVURGyLAs0PE1CsZSb7GSr_XUuQxg6aqtJrL3kNB2FUSmhcEl8504KwrknrtfhyyTUsrt7GQE2EuWCd_1CdKBfeRgtntI8S1kMnfvpk0Kh-Nh7lVQa1GBp_yVKYR2_e1Xc_lJ6aQT5HG5XVo82kZIu5Hp97RH0Wt2GPTJ_IgLXH0E4.t1Kfs9fILMWzOt7GRYllw50j5iBFvLK57772L4RGWGs&dib_tag=se&keywords=homematic%2Bip%2Bfensterkontakt&qid=1726736927&sprefix=hom%2Caps%2C118&sr=8-2&th=1)  
WLAN Access Point: [elv.com](https://de.elv.com/p/homematic-ip-wlan-access-point-hmip-wlan-hap-b-P160954/)  
Access Point: [Otto.de](https://www.otto.de/p/homematic-ip-access-point-140887a0-smart-home-station-C1418976266/#ech=28779158&variationId=S0J5I053RC6I); [Klarna.com](https://www.klarna.com/de/shopping/pl/cl272/5308045/Access-Points-Bridges-Repeater/Homematic-IP-HMIP-HAP/?utm_source=google&utm_medium=cssx&ref-site=google-css)  
Batterie: [Akkuteile.de](https://www.akkuteile.de/lifepo-akkus/26650/ifr26650-3-2v-3-3v-3000mah-lifepo4-lithium-eisenphosphat-akku_100725_2407)  
Batteriehalter: [Amazon.de](https://www.amazon.de/-/en/Battery-Storage-Box-Wire-Cable-standard/dp/B07FKPL7NS/ref=sr_1_9?crid=T2HPSZCSU9A1&dib=eyJ2IjoiMSJ9.6Cq7dlcI0L5iuij9HpGf0Jrf5PSKYlcwvIZXE-mB0IIfM9ocb7mnoi8K9k9ubg1j1IHGI3fR8P1DHAKWqmSrIgASrZhBzNgoBgRm-iS2GrB63Mtc4YRyXE2wrRryzTgiOQYTXEKLUwDYikW5cyn4evTl6EqsdtrljNvGEWtgPnV_-VWY6-_jLwxDFHIpkXhyjQHlI3BPMCQjaLblOLW9fB5BU60jPvyYFxySVN1jYb8.CJq3u8Bdd7RCr5vODptpjmTwlS01H4C9ybhaopGjnhs&dib_tag=se&keywords=18650+lifepo4+battery+holder&qid=1726744105&sprefix=18650+lifepo4+battery+holder%2Caps%2C91&sr=8-9)  
Ladegerät: [Amazon.de](https://www.amazon.de/VX4-Sichtbarer-Batteriekapazit%C3%A4tspr%C3%BCfer-Kapazit%C3%A4tspr%C3%BCfer-Lithium-Batterien/dp/B0D8PY21FN?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A2OUX3508FD2K2); [Otto.de](https://www.otto.de/p/aplic-batterie-ladegeraet-2000-ma-akku-ladegeraet-fuer-li-ion-ni-mh-ni-cd-lifepo4-akkus-mit-display-S0X2207Q/#ech=28779159&variationId=S0X2207QT8Z2)  
Microcontroller: [Botland.de](https://botland.de/wifi-und-bt-module-esp32/24607-esp32-c6-devkitm-1-n4-wifi-bluetooth-zigbee-thread-entwicklungsboard-mit-esp32-c6-mini-1-chip.html)  
Temperature Sensor: [Amazon.de](https://www.amazon.de/SHELLY-Temperatursensor-DS18B20-2-St%C3%BCck/dp/B0CVKZHRB9?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A2OLLM5U3LXOGB); [Plonke-shop.de](https://plonke-shop.de//temperatur-sensor-dallas-ds18b20-fuer-z.b.-shelly-plus-sensor-addon-kabellaenge-1-meter)  




