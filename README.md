# Python Port Scanner

Et letvægts terminal-værktøj skrevet i Python, der lader brugeren indtaste en IP-adresse eller et domæne for at scanne efter almindelige åbne porte (f.eks. HTTP, HTTPS, SSH, FTP).

## Om projektet
Som kommende IT-Teknolog har jeg en stor interesse for netværk og infrastruktur. Jeg byggede dette script for at få en dybere forståelse af netværks-sockets i Python og hvordan man opdager åbne TCP-forbindelser.

## Teknologier brugt
* **Python 3**
* `socket` biblioteket til netværkskommunikation.
* `sys` og `datetime` til terminal-output og tidsstempling.
* Fejlhåndtering (`try/except`) for at sikre at ugyldige hostnames ikke får scriptet til at crashe.

## Sådan kører du det
1. Sørg for at have Python installeret på din computer.
2. Kør scriptet fra din terminal:
   ```bash
   python port_scanner.py
