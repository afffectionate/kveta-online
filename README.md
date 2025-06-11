# KVĚTA Online

## 1) Uživatelská dokumentace

### Kdo je Květa

KVĚTA Online je webová aplikace pro analýzu textů vzniknuvší po vzoru programu QUITA Online. Po nahrání .txt souboru se uživateli zobrazí jednoduchý přehled kvantitativně-lingvistických statistik.

⚠ POZOR: Určité komponenty aplikace fungují pouze pro texty v anglickém jazyce.

### Instalace a spuštění
- Vyžaduje Python 3.8+
- Knihovny nainstalujete příkazem `pip install sanic regex plotly`.
- Server spustíte přes `python server.py`.
- Nástroj bude dostupný na adrese `http://localhost:8000`.

⚠ *V budoucnu přejde nástroj na Docker, aktuální řešení je dočasné.*

### Jak nástroj používat

- Nahrajte textový soubor přes tlačítko „Vybrat soubor“.
- Klikněte na „Spustit analýzu“.
- Po chvíli se zobrazí výsledky analýzy.


## 2) Programátorská dokumentace

### Dependencies
- Sanic — backendový webový framework
- Regex — tokenizace textu
- Plotly — generování grafů na frontend

### Instalace a spuštění

Viz výše.

### Architektura

**Backend**  
Server je napsaný v Pythonu se Sanicem. Poskytuje statické soubory (CSS, JS, HTML).

Má dvě hlavní routy:

- `/` — zobrazuje hlavní stránku (index.html).

- `/process` — přijímá POST požadavek s textovým souborem, analyzuje text a vrací JSON s výsledky pro zobrazení na frontendu.

**Frontend**  
Statická HTML stránka se základním designem v CSS. JavaScript zajišťuje nahrávání souboru a posílání na backend přes fetch API. Po obdržení JSONu dynamicky generuje a zobrazí výsledky.

Plánuje se integrace Plotly pro zobrazení grafů.
