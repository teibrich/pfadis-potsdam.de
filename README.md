[![Netlify Status](https://api.netlify.com/api/v1/badges/ef3bf18f-d569-4beb-b19d-24c5038d95ec/deploy-status)](https://app.netlify.com/sites/pensive-yonath-253aac/deploys)

# README

Dieses git repository enthält die original Dateien für unsere Homepage: http://www.pfadis-potsdam.de/
Alle Änderungen werden mittels https://www.netlify.com/ direct gebaut und veröffentlicht.

## Download / Checkout

Dieses Project verwendet git submodules, die du mit auschecken musst:

    git clone --recurse-submodules git@github.com:teibrich/pfadis-potsdam.de.git
    cd pfadis-potsdam.de

## Bearbeitung

Die meisten Markdown-Datein können direkt in Github bearbeitet werden. Um die Website lokal zu testen benötigst du `python3.7`.

Zur Vorbeitung installiert zunächst alle Abhängigkeiten:

    python3.7 -m venv pelican-env
    source pelican-env/bin/activate
    pip install -r requirements.txt

Danach kannst du die Website bauen und testen (http://localhost:8000/):

    cd pelican
    make devserver

Veränderungen lösen zumeinst automatisch einen Neubau aus. Veränderungen innerhalb von `pelican/custom-theme` müssen manuell neu mit dem original Theme gemerged werden:

    make theme
