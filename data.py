from models import Document, Talent

TALENT_ID = "540af9a2-b63a-4cd0-a333-270c2b592394"

TALENT = Talent(
    id=TALENT_ID,
    name="Elmedin Babajic",
    title="IT-sikkerhedsstuderende · DevSecOps og automatisering",
    profile_text=(
    "IT-teknolog med speciale i netværk, cloud og IT-sikkerhed, nu i gang "
    "med professionsbachelor i IT-sikkerhed. Jeg bygger automatiseringer i "
    "Python og pakker dem i containere, og jeg tænker sikkerhed ind fra "
    "start i stedet for at lænke det på til sidst. To år i IT-support hos "
    "Jyske Bank-koncernen har lært mig, hvordan systemer fejler i praksis. "
    "Jeg søger praktik inden for Cloud Native og DevSecOps."
    ),
    email="elmedinbabajic@gmail.com",
    phone="+4542655275",
    city="Aarhus",
    country="Denmark",
    github="https://github.com/Medo0071",
    linkedin="https://www.linkedin.com/in/elmedin-babajic-48417b347/",
)



DOCUMENTS = [
    Document(
        id="4d405887-48b6-4f9c-a7cc-c85e9a5e50ae",
        name="Uddannelse",
        content=(
            "Professionsbachelor i IT-sikkerhed, Erhvervsakademi Aarhus "
            "(2026 - nu). Webapplikationssikkerhed, sårbarhedsanalyse, "
            "sikker drift, risikostyring og trusselsvurdering."
            "IT-teknolog, Erhvervsakademi Aarhus (2024 - 2026). Speciale i "
            "netværk, cloud og IT-sikkerhed. Linux- og "
            "Windows-administration, netværksdesign, virtualisering og "
            "infrastruktur."
            "Afsluttende projekt: penetrationstest i Kali Linux mod et "
            "miljø, jeg selv havde sat op med Linux-servere og "
            "virtualisering i VMware. At bygge miljøet først og angribe det "
            "bagefter gjorde det tydeligt, hvilke af mine egne "
            "opsætningsvalg der var fejl."
        ),
    ),
    Document(
        id="c334accd-cd3b-41e2-b109-3881e18c619b",
        name="Erhvervserfaring",
        content=(
            "IT-support, studentermedhjælper - Jyske Bank-koncernen, "
            "Silkeborg (jan. 2024 - nov. 2025). 1. level support til over "
            "4.000 medarbejdere i et enterprise-miljø med strenge krav til "
            "compliance og datasikkerhed. Fejlfinding på tværs af hardware, "
            "software og systemer, og præcis dokumentation af hver sag. Jeg "
            "lærte at prioritere mange parallelle opgaver og at dokumentere "
            "ordentligt, så andre kan overtage."
            "IT-praktikant - Airteam (aug. - okt. 2025). Installation og "
            "vedligeholdelse af IT-infrastruktur samt implementering af "
            "sikkerhedsforanstaltninger."
            "Tidligere: produktionsmedarbejder hos Bang & Olufsen (2023), "
            "poder på Testcenter Holstebro (2020-2022) og medarbejder hos "
            "Løvbjerg (2018-2020)."
        ),
    ),
    Document(
        id="b129f05d-620c-4981-9901-7a08e790233b",
        name="Projekter",
        content=(
            "Cyberbuddy (cyberbuddy.dk) - eget udviklingsprojekt. Jeg "
            "bygger automatiserings- og integrationsløsninger til mindre "
            "virksomheder."
            "Kontaktformularen validerer alt på serveren og har "
            "CSRF-token, honeypot-felt mod bots, hastighedsbegrænsning per "
            "IP og beskyttelse mod header injection. Gennemgået mod OWASP "
            "Top 10."
            "Cowrie honeypot på Raspberry Pi. Python-baseret SSH-honeypot "
            "eksponeret mod internettet. Den indsamlede reelle "
            "angrebsforsøg: kilde-IP'er, loginforsøg, kørte kommandoer og "
            "forsøg på malware-download. Det interessante var ikke, at der "
            "kom trafik, men hvor forudsigelig den var - de samme "
            "brugernavne og de samme første kommandoer gik igen."
            "MQTT til PostgreSQL. Python-service der abonnerer på "
            "MQTT-emner fra IoT-sensorer og skriver hver måling til "
            "databasen med tidsstempel. Samme grundform som enhver "
            "integration: hent fra ekstern kilde, omsæt, gem."
            "Autonom robotbil. Bygget på Raspberry Pi Pico med infrarøde "
            "sensorer. Kører vægfølgning, forhindringsundvigelse, sumo-mode "
            "og manuel fjernstyring. Programmeret i MicroPython direkte mod "
            "hardwaren."
            "Simon Says. Embedded spil på to Raspberry Pi Pico'er og en "
            "Raspberry Pi med LCD-skærm og højttaler. To spillere med hver "
            "sit knappanel. Tre enheder, der skal være enige om, hvis tur "
            "det er."
        ),
    ),
    Document(
        id="6821ca65-79ae-41a9-bf1b-8ba177bfc612",
        name="Kompetencer",
        content=(
            "Bruger dagligt: Python, Linux, SQL og relationelle databaser, "
            "REST API-integration, Git og webapplikationssikkerhed (OWASP "
            "Top 10)."
            "Har bygget med: Docker og docker-compose, FastAPI, Flask, "
            "GitHub Actions, MicroPython og embedded, netværk og "
            "infrastruktur, VMware og bash-scripting."
            "Under opbygning: Azure, Kubernetes, Terraform, JavaScript og "
            "TypeScript. Jeg kan ikke .NET C# eller React i dag, men det er "
            "en del af det, jeg gerne vil lære i praktikken."
            "Praktisk sikkerhed: PortSwigger Web Security Academy og "
            "HackTheBox. SQL injection, XSS, adgangskontrol og "
            "autentificeringsfejl udnyttet i praksis, ikke kun læst om. "
            "Kali Linux og sårbarhedsanalyse."
            "Sprog: dansk (modersmål) og engelsk (flydende). Kørekort "
            "kategori B."
        ),
    ),
]