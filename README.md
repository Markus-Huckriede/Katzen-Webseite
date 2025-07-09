🐱 Lustige Katzen-Webseite mit Flask 🐱
Dieses kleine Projekt zeigt zufällige Katzenbilder. Die Bilder stammen von TheCatAPI.com, und die Seite ist mit Python + Flask gebaut.

Funktionen
----------

Zufälliges Katzenbild beim Laden der Seite

„Mehr Katzen!“-Button lädt neue Bilder

Leicht erweiterbar mit GIFs, Memes oder Sprüchen

Installation & Ausführen
------------------------

Repository klonen:
git clone https://github.com/dein-benutzername/KatzenWebseite.git
cd KatzenWebseite

Virtuelle Umgebung erstellen (optional, empfohlen):
python -m venv .venv
source .venv/bin/activate (Windows: .venv\Scripts\activate)

Abhängigkeiten installieren:
----------------------------

pip install -r requirements.txt

App starten:
------------

python app.py

Dann im Browser öffnen:
-----------------------

http://127.0.0.1:5000

Projektstruktur
---------------

KatzenWebseite/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── fallback-cat.jpg (optional)

Voraussetzungen
---------------

Python 3.7 oder höher

Flask & requests (siehe requirements.txt)
