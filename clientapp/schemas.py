from pydantic import BaseModel


class ClientsBase(BaseModel):
    email: str


class ClientsCreate(ClientsBase):
    password: str


class Clients(ClientsBase):
    id: int
    surname: str
    name: str

    class Config:
        orm_mode = True
