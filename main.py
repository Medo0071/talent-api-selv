from fastapi import FastAPI, HTTPException

from data import DOCUMENTS, TALENT, TALENT_ID
from models import Document, Talent

app = FastAPI()

@app.get("/talent", response_model=list[Talent])
def hent_talenter():
    return [TALENT]


@app.get("/talent/{id}", response_model=Talent)
def hent_talent(id: str):
    if id != TALENT_ID:
        raise HTTPException(status_code=404, detail="Talent not found")
    return TALENT


@app.get("/talent/{id}/documents", response_model=list[Document])
def hent_dokumenter(id: str):
    if id != TALENT_ID:
            raise HTTPException(status_code=404, detail="Talent not found")
    return DOCUMENTS

@app.get("/talent/{id}/documents/{documentId}", response_model=Document)
def hent_dokument(id: str, documentId: str):
    if id != TALENT_ID:
            raise HTTPException(status_code=404, detail="Talent not found")

    for dokument in DOCUMENTS:
        if str(dokument.id) == documentId:
            return dokument

    raise HTTPException(status_code=404, detail="Document not found")



