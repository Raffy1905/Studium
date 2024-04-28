placebic explanations have a similar level of trust as real explanations => unjustified trust
Dual Process Theory -> Menschen verlassen sich auf Heuristiken und kognitive Verzerrungen, um Entscheidungen zu treffen
=> "systematic error in judgement and decisionmaking common to all human beings which can be due to cognitive limitations, motivational factors, and/or adaptations to natural environment." - Amos Tversky, Daniel Kahneman 
Kognitive Verzerrungen verändern die Interpretation von AI Modellen

## Explanatory heuristics affecting XAI Design

Erklärungen:
1. Wahrscheinliche Gründe finden (Abductive reasoning)
2. Relevantesten dieser Gründe auswählen (verschiedene fokusponte je nach Person) (heuristics)

Menschen tendieren dazu, inhärente/innewohnende Merkmale gegenüber Extrinsischen für Erklärungen zu bevorzugen.
Menschen müssen Unsicherheit bewerten können, um Entscheidungen zu treffen. -> Unsicherheit muss in AI explizit genannt werden, da weitere Hinweise, wie Stimmlage oder Körpersprache nicht zur Verfügung stehen

Verschiedene Arten von Erklärungen: einfach, weitgefasst, komplex
einfache erklärungen sind leichter verständlich, man erwartet aber bei komplexen Modellen auch komplexere Erklärungen
Umfassende Erklärungen hefen dabei das Verständnis der Nutzer zu verbessern, können aber auch zu blindem Vertrauen führen
 -> Schlüssig und weitfassend  VS.  einfach und weitfassend

Erklärungen sind sowohl ein sozialer als auch kognitiver Prozess
Sozial:
 - Wissensunterschied identifizieren
 - Vokabular anpassen
 - Folgefragen beantworten
Maschinen werden immer mehr menschliche Eingenschaften zugeschrieben (homunculus fallacy) -> menschliche Kommunikation wird erwartet =>  interaktive Erklärungen ==> overreliance?


## Cognitive Biases arising in user-based evaluations of explainaility techniques

Man sollte keine Beispielaufgaben nehmen, um die Performance von Erklärungen zu bewerten. Die subjektiven Preferencen haben keine Aussage darüber, wie sich die Leistung bei der Entscheidung mithilfe der Erklärungen verbessern würde.

Bei Bilderkennung wurde bemerkt, dass Personen eher auf Falschnegative achten als auf Falschpositive.
Gleiche Erklärungen werden je nach Aufmachung unterschiedlich bewertet.
**Change Blindness**: Teilnehmer bei Teststudien fallen nie alle Änderungen auf, die vorgenommen wurden. Daher sollten diese hervorgehoben werden. 

## Cognitive biases in AI-aided descitions that are mitigated thanks to explainability

Mitigated Trust | Explanation method used to mitigate bias | Task/user
-|-|-
Misattributed trust | Uncertainty extimates | Medical diagnosis / domain expert
Representativeness bias | Prototype cases of decision outcomes | Medical dignosis / domain expert
Tendency to believe persuasive claims unsupported by evidence | Natural language explanations | Fake news detection / lay users
Pre-use algorithmic optimism | local feature importance (word highlighting) | Emotional analysis / lay users

XAI gibt die Möglichkeit, kognitive Verzerrungen der Nutzer zu vermindern. HIerfür wird vor allem Wert auf große Transparenz gesetzt

**Example:** Pre-use algorithmic optimism  
*Pre-use algorithmic optimism:* Positive Erwartungen an ein transparentes System vor der Nutzung  
Das System wird schnell Überschätzt. Um dem zu entgehen werden Erklärungen nur schrittweise oder auf Nachfrage gezeigt, um die Nutzer davon abzuhalten Vertrauen zu verlieren, wenn das System nicht ihren Erwartungen entspricht.


## Cognitive biases in AI-aided descisions that are exacerbated by explainability

Der Nutzer hat die Wahl zwischen, AI zu vertrauen oder große Erklärungen zu lesen -> Entwickeln von Heuristiken wann und ob man die Erklärungen liest - wird durch XAI verstärkt  
Erklärungen können zudem falsch sein, was eine weitere Fehlerquelle zu AI hinzufügt -> Entdecken und Verhindern von Fehlern wird immer anpruchsvoller (Menschen sind schlecht darin, Falsche Informationen Wahrzunehmen)  


