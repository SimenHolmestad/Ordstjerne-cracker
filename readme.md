# Ordstjerne-cracker
Ordstjerne-cracker er et python-script for å kunne løse VGs ordstjerne: <https://www.vg.no/spill/ordstjernen>

Scriptet går gjennom en ordbok-fil, finner alle ordene som tilfredsstiller Ordstjernen og skriver ett og ett ord inn på nettsiden ved hjelp av [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/).

Det skal sies at Ordstjerne-crackeren ødelegger litt av moroa med Ordstjernen, men jeg hadde det i hvert fall mer morsomt mens jeg skrev dette scriptet enn da jeg faktisk prøvde å løse ordstjernene.

## Installering
Hvis du har python installert kan du installere avhengighetene ved å kjøre:

``` sh
pip install -r requirements.txt
```

## Ordbok
Per nå er scriptet satt opp til å bruke Norsk Scrabbleforbund sin ordbok. Last denne ned her: <http://www2.scrabbleforbundet.no/?p=4609>. Denne ordbok-filen må ligge i samme folder som python-filen for at scriptet skal fungere.

*OBS:* Norsk Scrabbleforbund sin ordbok er ikke helt lik den som Ordstjernen bruker, så det er mulig at scriptet finner noen overflødige ord og at ikke alle ordene blir funnet. I så fall kan du bruke hint og prøve deg frem på de siste ordene.

## Hvordan bruke scriptet
Etter at avhengighetene er lastet ned og du har puttet ordbok-tekstfilen på riktig plass (se over) er det følgende instruks som gjelder:

1. Gå inn på en ordstjerne: <https://www.vg.no/spill/ordstjernen>
2. Kjør scriptet med `python crack.py <7-ordstjerne-bokstaver> <hoved-bokstav>`
3. Trykk på innskrivningsfeltet i ordstjernen
4. Profitt?

## Eksempel på løsningskommando
Dersom for eksempel Ordstjernen har bokstavene æ, t, r, s, k, u og v, og hovedbokstaven er r blir kommandoen:
``` sh
python crack.py ætrskuv r
```

Rekkefølgen på de 7 ordstjerne-bokstavene har ingenting å si.
