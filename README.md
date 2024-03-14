# Popis programu
Program extrahuje data z vybraného okrsku voleb do Poslanecké sněmovny z roku 2017. Odkaz: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

# Jak nainstalovat potřebné knihovny
Potřebné knihovny, které program využívá, jsou uloženy v přiloženém dokumentu requirements.txt. Pro instalaci je vhodné použít nové virtuální prostředí a následně spustit pomocí příkazu:

$pip -- version                         #ověření verze manažeru
$pip install -r requirements.txt       #nainstaluje knihovny

# Jak spustit program
ke spuštění programu je potřeba zadat 2 povinné argumenty.
1. URL adresu na hlavní stránku vybraného okrsku
2. název souboru CSV, který bude vytvořen jako výstup (název musí být ukončen ".csv")

vstupní příkaz
python election_scraper.py "<URL adresa vybraného okrsku>" "<název výsledného soboru>"

# Praktická ukázka
## Příklad využití programu
Chceme posbírat data z Okresu: Olomouc (zadávat hlavní stránku Okresů, ne Krajů) a vypsat ji do souboru s názvem CSV_Olomouc

vstupní argumenty budou vypadat takto:
1. argument URL adresa - "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7102"
2. argument název CSV - "CSV_Olomouc.csv"

celkový příkaz zadaný do konzole pak bude následující:
python election_scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'CSV_Olomouc.csv'

## Průběh programu:
Downloading data at the selected URL:https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
I am creating a CSV file named: CSV_Olomouc.csv

## Část výstupu programu:
Code,Location,Registred,Envelopes,Valid,Občanská demokratická strana,...

506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0

589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1

589276,Bílovice-Lutotín,431,279,275,0,0,32,0,8,40,1,0,4,0,0,30,0,3,83,0,0,22,0,0,0,1,38,0

...
