# KVĚTA Online

## 1) Uživatelská dokumentace

### Kdo je Květa

KVĚTA Online je webová aplikace pro analýzu textů vzniknuvší po vzoru programu QUITA Online. Po nahrání .txt souboru se uživateli zobrazí jednoduchý přehled kvantitativně-lingvistických statistik.

⚠ POZOR: Určité komponenty aplikace (POS tagging) fungují pouze pro texty v anglickém jazyce.

### Funkce:
- Počet tokenů, typů, TTR
- Word cloud nejčastějších slov
- Grafy délek slov a vět
- Graf zastoupení slovních druhů

### Jak nástroj používat

- Nahrajte textový soubor přes tlačítko „Vybrat soubor“.
- Klikněte na „Spustit analýzu“.
- Po chvíli se zobrazí výsledky analýzy.

### Instalace



```bash
python3 -m venv venv && source venv/bin/activate
pip install sanic spacy
python -m spacy download en_core_web_sm
python server.py
```

Aplikace poběží na [http://localhost:8000](http://localhost:8000).

## 2) Programátorská dokumentace

### Dependencies
Aplikace vyžaduje knihovny `Sanic` (asynchronní web server) a `spaCy` (NLP knihovna pro zpracování textu).

### Instalace a spuštění

Viz výše.

### Architektura

**Backend**  
Server je napsaný v Pythonu se Sanicem. Poskytuje statické soubory (CSS, JS, HTML).

Má dvě hlavní routy:

- `/` — zobrazuje hlavní stránku (index.html).

- `/process` — přijímá POST požadavek s textovým souborem, analyzuje text a vrací JSON s výsledky pro zobrazení na frontendu.

**Frontend**  
Statická HTML stránka se základním designem v CSS. JavaScript zajišťuje nahrávání souboru a posílání na backend přes fetch API. Po obdržení JSONu dynamicky generuje a zobrazí výsledky pomocí knihoven Plotly a D3js.
