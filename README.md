# KVĚTA Online

## 1) Uživatelská dokumentace

### Kdo je Květa?

KVĚTA Online je webová aplikace pro základní kvantitativní analýzu textů inspirovaná nástrojem QUITA Online. Po nahrání .txt souboru se uživateli zobrazí přehled základních statistických údajů o textu, jako je počet slov, délka vět, nebo nejčastější slova.

⚠ **POZOR:** Gramatická analýza (např. rozpoznávání slovních druhů) funguje pouze pro texty v angličtině. Pro jiné jazyky budou výsledky neúplné nebo nepřesné.

### Funkce
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

### Plánované features:
- Zpracování českých textů pomocí `udpipe`
- Vizualizace hapaxů
- Analýza sentimentu
- Export grafů
- Víc obrázků tuleňů

## 2) Programátorská dokumentace

### Dependencies
Aplikace vyžaduje knihovny `Sanic` (asynchronní web server) a `spaCy` (NLP knihovna pro zpracování textu).

### Instalace a spuštění

Viz výše.

### Architektura

**Frontend**  
Statická HTML stránka se základním designem v CSS. JavaScript zajišťuje nahrávání souboru a posílání na backend přes fetch API. Po obdržení JSONu dynamicky generuje a zobrazí výsledky pomocí knihoven Plotly a D3js.

**Backend**  
Server je napsaný v Pythonu se Sanicem. Poskytuje statické soubory (CSS, JS, HTML).

Má dvě hlavní routy:

- `/` — zobrazuje hlavní stránku (index.html).

- `/process` — přijímá POST požadavek s textovým souborem, analyzuje text a vrací JSON s výsledky pro zobrazení na frontendu.

Vrací response ve formátu:
```json
{
  "tokens": 1500,
  "types": 700,
  "ttr": 0.47,
  "wordLengths": [4, 5, 6, 3, 7],
  "sentenceLengths": [12, 15, 9],
  "hapaxLegomena": ["coalescence", "stochastic"],
  "wordCloudData": {
    "data": 120,
    "model": 95,
    "language": 30
  },
  "posFrequencies": {
    "NOUN": 300,
    "VERB": 200,
    "ADJ": 100
  }
}
``
