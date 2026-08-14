# Talent API

Min løsning på Tech Chapters praktikant-udfordring. Et REST API bygget
efter deres Swagger-spec, skrevet i Python med FastAPI og pakket i en
container.

API'et returnerer data om mig: Elmedin Babajic, IT-teknolog og
bachelorstuderende i IT-sikkerhed fra Aarhus.

Jeg søger praktikpladsen inden for Cloud Native.

---

## Kør det

```bash
docker run --rm -p 8080:8080 ghcr.io/medo0071/talent-api-selv:latest
```

Så ligger den på:

- <http://localhost:8080/talent> - data om mig
- <http://localhost:8080/docs> - Swagger UI
- <http://localhost:8080/redoc> - ReDoc

## Kør den lokalt uden Docker

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

## Tests

```bash
python -m pytest tests/ -v
```

---

## Endpoints

| Metode | Sti | Returnerer |
|---|---|---|
| GET | `/talent` | Liste af talenter |
| GET | `/talent/{id}` | Ét talent, eller 404 |
| GET | `/talent/{id}/documents` | Alle dokumenter, eller 404 |
| GET | `/talent/{id}/documents/{documentId}` | Ét dokument, eller 404 |

Dokumenterne er mit CV, delt op i uddannelse, erhvervserfaring,
projekter og kompetencer.

---

## Filerne

| Fil | Hvad den gør |
|---|---|
| `main.py` | Endpoints og fejlhåndtering |
| `models.py` | Pydantic-modeller, der matcher specen |
| `data.py` | Mine data |
| `tests/test_api.py` | Tests |
| `Dockerfile` | Bygger imaget |
| `.github/workflows/ci.yml` | Kører tests og udgiver imaget |

---

## Hvorfor jeg gjorde som jeg gjorde

**Python og FastAPI.** Opgaven siger, man må vælge sprog selv, og Python
er det, jeg er stærkest i. FastAPI havde jeg ikke prøvet før, men det
viste sig at passe godt til opgaven: Swagger-dokumentationen bliver
genereret ud fra de samme modeller, der validerer svarene, så de to ting
ikke kan komme til at sige noget forskelligt.

Jeg kan ikke .NET C# eller React, som I bruger. Det er en del af det,
jeg gerne vil lære i en praktik.

**Data i sin egen fil.** `data.py` er adskilt fra `main.py`. Kom dataene
en dag fra en database, skulle jeg kun ændre det ene sted.

**404 i stedet for at returnere mig selv.** Den første version af mit API
returnerede mine data, uanset hvad der stod i URL'en. `/talent/abc` gav
det samme som `/talent/{mit-id}`. Det opdagede jeg, da jeg testede med et
tilfældigt id, og det er nok den fejl, jeg lærte mest af. Nu giver et
ukendt id 404, så den, der bruger API'et, kan se forskel på "findes ikke"
og "findes, men er tom".

**Tests der læser specen.** En af mine tests henter feltnavnene fra
`swagger.yaml` og sammenligner dem med det, mit API faktisk sender. Jeg
testede den ved at fjerne et felt fra min model. Testen fejlede, som den
skulle. Det er bedre end at skrive forventningerne i hånden, for så
opdager jeg det selv, hvis jeg kommer til at afvige fra specen.

**Ikke-root i containeren.** Imaget opretter en bruger og skifter til
den, i stedet for at køre som root. Slipper nogen ud af applikationen, er
de så ikke root inde i containeren.

**Pipelinen bygger kun, hvis testene er grønne.** `needs: test` i
workflow-filen betyder, at imaget ikke bliver bygget eller pushet, hvis
noget fejler.

---

## Hvad jeg lærte

Jeg havde ikke bygget et API før. Jeg startede med fire linjer, der
returnerede `{"navn": "test"}`, og byggede derfra.

Det, der overraskede mig mest, var 404-fejlen. Mit API så rigtigt ud, når
jeg testede med de rigtige id'er, og var forkert hele tiden. Jeg fandt
det kun, fordi jeg tastede forkert og fik mine egne data tilbage
alligevel.

Jeg blev også overrasket over, at Swagger-siden bare dukkede op, uden at
jeg havde skrevet et ord dokumentation. Den bliver lavet ud fra typerne i
koden.

---

## Kontakt

- elmedinbabajic@gmail.com
- +45 42 65 52 75
- <https://github.com/Medo0071>
- <https://www.linkedin.com/in/elmedin-babajic-48417b347/>
- <https://cyberbuddy.dk>
