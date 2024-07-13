# Archivo principal para iniciar la aplicación

from fastapi import FastAPI
from middleware.orquestador import OrquestadorMiddleware
from api.routes import router

app = FastAPI()

# Agregar el middleware orquestador
app.add_middleware(OrquestadorMiddleware)

# Incluir las rutas definidas anteriormente
app.include_router(router)

# Punto de entrada para FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)

