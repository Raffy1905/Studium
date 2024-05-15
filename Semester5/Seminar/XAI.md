[1] https://www.kobold.ai/explainable-ai/ (07.05.2024)  
[2] https://www.computerweekly.com/de/feature/Wie-wird-Regression-beim-maschinellen-Lernen-angewendet (07.05.2024)  
[3] https://medium.com/@akshanshmishra/interpolation-and-its-application-in-machine-learning-a0a5b5df653f (07.05.2024)  
[4] https://www.techtarget.com/whatis/definition/extrapolation-and-interpolation (07.05.2024)   
[5] https://towardsdatascience.com/real-artificial-intelligence-understanding-extrapolation-vs-generalization-b8e8dcf5fd4b (07.05.2024)

[6] https://www.ibm.com/de-de/topics/decision-trees (09.05.2024)  

[7] https://www.ibm.com/de-de/topics/random-forest (09.05.2024)  
[8] https://www.bigdata-insider.de/was-ist-random-forest-a-913937/ (09.05.2024)  
[9] https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf

[10] https://christophm.github.io/interpretable-ml-book/


# Ante-hoc

## erklärbare klassische modelle

### Regressionen [1]
Methode zur Erfassung von Zusammenhängen zwischen zwei Variablen. Es werden Algorithmen trainiert,
um Muster zu erkennen, Datenpunkte zu cahrakterisieren und so Vorhersagen zu treffen. [2]

**lineare Regression:**[2]  
Alle Datenpunkte entlang einer gerade Linie anzupassen.  
Wird vor Allem zur Beantwortung quantitaiver Fragen genutzt [2]  


**logistische Regression:**[2]  
Bestimmen, ob ein Datenpunkt oberhalb oder unterhalb einer Linie liegt [2]

Interpolation / Generalization | Extrapolation
-|-
Lesen von Werten zwischen zwei Punkten des Datensatzes | Schätzen von Werten außerhalb des Datensatzes
Hauptsächlich zum Identifizieren von fehlenden Vergangenheitswerte | Große Rolle beim Vorhersagen
Geschätzer wert ist wahrscheinlicher korrekt | Geschätzte Werte sind nur Wahrscheinlichkeiten, sind also weniger wahrscheinlich korrekt
[4]


**Interpolation/Generalization:**[2]  
Werte innerhalb von verfügbaren Datenpunkten schätzen. [2]  
Schätzen von fehlenden Werten innerhalb eines Datensatzes, Vorhersagen von neuen Datenpunkten auf Grundlage von bekannten Daten oder in Klassifizierungsproblemen, um die Wahrscheinlichkeit für jede Klasse zu schätzen
Es gibt *lineare Interpolation*, *Polynominterpolation*, *Spline Interpolation* und *Radial Basis Function Interpolation*. [3]  
Interpolation wird meist in ML angewendet. Bei Interpolation bzw Generalisierung wird ein Problem antrainert, um ähnliche Probeleme lösen zu können. [5]



**Extrapolation:**[2]  
Auf Grundlage vorhandener Regressionsbeziehungen Werte jenseits der Grenzen der vorhandenen Daten vorherzusagen. [2]  
Es gibt *lineare Extrapolation*, *Polynome Extrapolation* und *Konische Extrapolation* [4]


### Entscheidungsbäume [1] 
Bei Entscheidungsbäumen handlt es sich um einen supervised Algorithmus für Klassifizierungs- und Regressionsaufgaben.
Es wird eine hiererchische Struktur an Entscheidungsregeln erzeugt, durch welche Neue Datensätze vorausgesagt werdeb können. [6]

### Random Forests [1]
Beim Random Forest werden die Ergebnisse verschiedener Entscheidungsbäume zu einem Ergebnis zusammengefasst. [7]

**Bagging (Bootstrap-Aggregation):**  
Eine Zufallsstichprobe wird aus dem Datensatz genommen und wieder zurück gelegt. -> Mehrfachauswahl möglich  
Im Anschluss werden die Bäume mit ihren jeweiligen Datensätzen trainert. Das Ergebnis liefert am Ende die Mehrzahl bei Klassifizierungen bzw der Durchschnitt bei Regressionen[7]

Random Forest liefert verschiedene Regeln, mit denen mehrere Bäume generiert und im Anschluss kombiniert werden können [8]  
Durch das Trainieren und Kombinieren verschiedener Bäume entsteht ein "Wald", mit denen final die Entscheidungen getroffen werden.


## Generative Additive Modelle (GAMs)

https://www.cs.cmu.edu/~epxing/papers/2011/Eisenstein_Ahmed_Xing_ICML11.pdf


## Hybride Modelle

https://www.sciencedirect.com/science/article/pii/S1877050919304247


# Post-Hoc

## LIME

*Local Interpretable Model-Agnostic Explanations*  
*Lokale, interpretierbare, modell-agnostische Erklärungen*  
versuchen alle Modelle erklärbar zu machen, ohne Wissen über das spezifische Modell.  
Beispiel: Linear Classifier auf die Ergebnisse des neuronalen Netzes geschaltet. Senkt die genauigkeit des Modells, erlaubt aber eine Erklärung. [1]

## Kontrafaktische Modelle

*Counterfactual Method*  
Hierbei werden die Imput daten geändert, bis sich der Output des Modells andert. Mit mehrfacher Wiederholung kann man systematisch erarbeiten, welche Features des Inputs welche Auswirkungen auf den Output haben

## Layer-wise Relevance Propagation (LRP)

Nutzt *Backpropagation*, um zu identifizieren, welche Teile des Inputs den meisten Einfluss haben. Hierbei werden von den Knoten des Outputs die Kanten auf dir gewichteten Knoten zurückverfolgt bsihin zu den Inputknoten. [1]

## Partial Dependen Plot (PDP)

2001 von J.H. Friedmann  
Ein oder zwei Input Variablen werden jeweils in einen Graph geplottet. Dadurch lässt sich einfach erkläten, welche Input Features welche Abhängigkeiten haben und ob das Verhältnis zwischen Target und Feature linear, monoton oder komplex ist. [1]

## Rationalization

Hierbei wird eine weiter Rechenschicht hinzugefügt, weshalb eine Handlung ausgelöst wurde oder eine Entscheidung getroffen wurde. Dadurch können Maschinen wie beispielsweise Roboter ihre Entscheidungen selbst erklären. [1]

## Weitere:
*Individual Conditional Explanation (ICE)*  
*Accumulated Local effects (ALE)*  
*Permutation Feature Importance*  
*Global Surrogates*  
*Scoped Rules*  
*Shapley Values*  
*Shapley Additive exPlanaions(SHARP)*  
...



