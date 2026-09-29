from datetime import date, time
from pydantic import BaseModel, EmailStr, Field


class EventoEntrada(BaseModel):
    titulo: str = Field(..., min_length=1)
    descricao: str = Field(..., min_length=1)
    data: date
    horario: time
    local: str = Field(..., min_length=1)
    capacidade: int = Field(..., gt=0)
    categoria: str = Field(..., min_length=1)


class Evento(EventoEntrada):
    id: int


class ParticipanteEntrada(BaseModel):
    nome: str = Field(..., min_length=1)
    email: EmailStr
    curso: str = Field(..., min_length=1)


class Participante(ParticipanteEntrada):
    id: int


class Inscricao(BaseModel):
    evento_id: int
    participante_id: int
