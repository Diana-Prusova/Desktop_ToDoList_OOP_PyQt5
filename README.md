
# Desktopová aplikace To do list (OOP, PyQt5)

Jedná se o kód jednoduché aplikace pro zapisování a odškrtávání úkolů. Aplikaci je možné také stáhnout jako klasickou desktopovou aplikaci a to zde: 

    ...bude doplněno...

Cílem při psaní tohoto kódu bylo získat větší znalost knihovny PyQt5 a naučit se vytvořit z kódu funkční aplikaci, který si může kdokoliv stáhnout a používat ji.

Ačkoliv je aplikace především studijní materiál, snažila jsem se, aby měla všechny potřebné funkcionality. Jde například o ukládání seznamu úkolů, kontrola uložení při zavření či snadnější ovládání (potvrení ENTEREM, snazší zavření vyskakovacích oken). Jako drobný bonus jsem přidala i motivnační složku v podobě gratulací při splnění určitých podmínek.


## Instalace knihoven

Ke spuštění programu je potřeba stáhnout knihovny třetích stran. Jejich seznam je uložený v souboru requirements.txt. Knihovny můžete naistalovat pomocí příkazu: 

    pip install -r requirements.txt
## Spuštění aplikace

Aplikace se spouští pomocí hlavního souboru main.py. Z příkazového řádku jej můžete spustit pomocí příkazu: 

    python main.py #je nutné být ve složce aplikace

případně

    python3 main.py #je nutné být ve složce aplikace
## Seznam souborů

1. main.py: Hlavní soubor aplikace. Spouští ji a obsahuje kód hlavního okna aplikace.

2. neni_ulozeno.py: Vyskakovací okno, které uživatele upozorní, pokud se snaží zavřít neuložený seznam úkolů.

3. okno_upozorneni.py: Vyskakovací okno, ve kterém se zobrazuje gratulace podle toho, jaké podmínky při odškrtávání úkolů byly splněny.

4. ulozene_ukoly.json: Soubor sloužící k ukládání zadaného seznamu úkolů.

5. requiremen.txt: Soubor se seznamem knihoven, které tento projekt používá.

6. README.md: Soubor se základními informacemi o kódu.

7. __pycache_: Složka vytvořená pythonem pro rychlejší běh programu. Lze vymazat.