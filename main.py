from fastapi import FastAPI

from routers import router

app = FastAPI(title="API de Eventos Acadêmicos", version="1.0.0")
app.include_router(router)


@app.get("/")
def raiz():
    return {"mensagem": "API de Eventos Acadêmicos no ar. Acesse /docs para o Swagger."}
