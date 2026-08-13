import yaml
from pathlib import Path

from fastapi.testclient import TestClient


from data import DOCUMENTS, TALENT_ID
from main import app


client = TestClient(app)
DOK_ID =str(DOCUMENTS[0].id)


def test_liste_giver_200():
    svar = client.get("/talent")
    assert svar.status_code == 200
    assert len(svar.json()) == 1

def test_talent_giver_200():
    svar = client.get(f"/talent/{TALENT_ID}")
    assert svar.status_code == 200
    assert svar.json()["id"] == TALENT_ID


def test_ukendt_talent_giver_404():
    assert client.get("/talent/forkert").status_code == 404


def test_dokumenter_giver_200():
    svar = client.get(f"/talent/{TALENT_ID}/documents")
    assert svar.status_code == 200
    assert len(svar.json()) == len(DOCUMENTS)


def test_enkelt_dokument_giver_200():
    svar = client.get(f"/talent/{TALENT_ID}/documents/{DOK_ID}")
    assert svar.status_code == 200


def test_ukendt_dokument_giver_404():
    svar = client.get(f"/talent/{TALENT_ID}/documents/forkert")
    assert svar.status_code == 404

SPEC = yaml.safe_load(Path("swagger.yaml").read_text())


def test_felter_matcher_specen():
    forventet = set(SPEC["components"]["schemas"]["Talent"]["properties"])
    faktisk = set(client.get(f"/talent/{TALENT_ID}").json())
    assert faktisk == forventet
