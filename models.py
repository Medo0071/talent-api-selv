from uuid import UUID

from pydantic import BaseModel

class Document(BaseModel):
    id: UUID
    name: str
    content: str

class Talent(BaseModel):
    id: UUID
    name:str
    title: str
    profile_text: str
    email: str
    phone: str
    city: str
    country: str
    github: str | None = None
    linkedin: str | None = None




    