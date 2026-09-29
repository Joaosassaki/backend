from fastapi import APIRouter, status

import services
from models import Evento, EventoEntrada, Participante, ParticipanteEntrada, Inscricao

router = APIRouter()


@router.post("/eventos", response_model=Evento, status_code=status.HTTP_201_CREATED, tags=["Eventos"])
def cadastrar_evento(evento: EventoEntrada):
    return services.cadastrar_evento(evento)


@router.get("/eventos", response_model=list[Evento], tags=["Eventos"])
def listar_eventos():
    return services.listar_eventos()


@router.get("/eventos/{evento_id}", response_model=Evento, tags=["Eventos"])
def consultar_evento(evento_id: int):
    return services.buscar_evento(evento_id)


@router.put("/eventos/{evento_id}", response_model=Evento, tags=["Eventos"])
def atualizar_evento(evento_id: int, evento: EventoEntrada):
    return services.atualizar_evento(evento_id, evento)


@router.delete("/eventos/{evento_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Eventos"])
def excluir_evento(evento_id: int):
    services.remover_evento(evento_id)


@router.post(
    "/eventos/{evento_id}/inscricoes/{participante_id}",
    response_model=Inscricao,
    status_code=status.HTTP_201_CREATED,
    tags=["Eventos"],
)
def inscrever(evento_id: int, participante_id: int):
    return services.inscrever_participante(evento_id, participante_id)


@router.get("/eventos/{evento_id}/inscricoes", response_model=list[Participante], tags=["Eventos"])
def listar_inscritos(evento_id: int):
    return services.listar_inscritos(evento_id)


@router.post("/participantes", response_model=Participante, status_code=status.HTTP_201_CREATED, tags=["Participantes"])
def cadastrar_participante(participante: ParticipanteEntrada):
    return services.cadastrar_participante(participante)


@router.get("/participantes", response_model=list[Participante], tags=["Participantes"])
def listar_participantes():
    return services.listar_participantes()


@router.get("/participantes/{participante_id}", response_model=Participante, tags=["Participantes"])
def consultar_participante(participante_id: int):
    return services.buscar_participante(participante_id)


@router.put("/participantes/{participante_id}", response_model=Participante, tags=["Participantes"])
def atualizar_participante(participante_id: int, participante: ParticipanteEntrada):
    return services.atualizar_participante(participante_id, participante)


@router.delete("/participantes/{participante_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Participantes"])
def excluir_participante(participante_id: int):
    services.remover_participante(participante_id)
