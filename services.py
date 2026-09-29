from fastapi import HTTPException, status

from models import Evento, EventoEntrada, Participante, ParticipanteEntrada, Inscricao

eventos = []
participantes = []
inscricoes = []

proximo_id_evento = 1
proximo_id_participante = 1


def cadastrar_evento(dados: EventoEntrada):
    global proximo_id_evento
    evento = Evento(id=proximo_id_evento, **dados.model_dump())
    eventos.append(evento)
    proximo_id_evento += 1
    return evento


def listar_eventos():
    return eventos


def buscar_evento(evento_id: int):
    for evento in eventos:
        if evento.id == evento_id:
            return evento
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Evento não encontrado.")


def atualizar_evento(evento_id: int, dados: EventoEntrada):
    evento_atual = buscar_evento(evento_id)
    posicao = eventos.index(evento_atual)
    evento_novo = Evento(id=evento_id, **dados.model_dump())
    eventos[posicao] = evento_novo
    return evento_novo


def remover_evento(evento_id: int):
    evento = buscar_evento(evento_id)
    eventos.remove(evento)


def cadastrar_participante(dados: ParticipanteEntrada):
    global proximo_id_participante
    participante = Participante(id=proximo_id_participante, **dados.model_dump())
    participantes.append(participante)
    proximo_id_participante += 1
    return participante


def listar_participantes():
    return participantes


def buscar_participante(participante_id: int):
    for participante in participantes:
        if participante.id == participante_id:
            return participante
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Participante não encontrado.")


def atualizar_participante(participante_id: int, dados: ParticipanteEntrada):
    participante_atual = buscar_participante(participante_id)
    posicao = participantes.index(participante_atual)
    participante_novo = Participante(id=participante_id, **dados.model_dump())
    participantes[posicao] = participante_novo
    return participante_novo


def remover_participante(participante_id: int):
    participante = buscar_participante(participante_id)
    participantes.remove(participante)


def inscrever_participante(evento_id: int, participante_id: int):
    evento = buscar_evento(evento_id)
    buscar_participante(participante_id)

    for inscricao in inscricoes:
        if inscricao.evento_id == evento_id and inscricao.participante_id == participante_id:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Participante já está inscrito neste evento.")

    vagas_ocupadas = 0
    for inscricao in inscricoes:
        if inscricao.evento_id == evento_id:
            vagas_ocupadas += 1

    if vagas_ocupadas >= evento.capacidade:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Não existem vagas disponíveis para este evento.")

    nova_inscricao = Inscricao(evento_id=evento_id, participante_id=participante_id)
    inscricoes.append(nova_inscricao)
    return nova_inscricao


def listar_inscritos(evento_id: int):
    buscar_evento(evento_id)
    lista = []
    for inscricao in inscricoes:
        if inscricao.evento_id == evento_id:
            for participante in participantes:
                if participante.id == inscricao.participante_id:
                    lista.append(participante)
    return lista
