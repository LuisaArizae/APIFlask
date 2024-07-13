 # Middleware que agrega un encabezado personalizado
 
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class OrquestadorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Aplica reglas de negocio, como autenticación
        if not request.headers.get("Authorization"):
            return Response("Unauthorized", status_code=401)

        # Llama al siguiente middleware o controlador
        response = await call_next(request)

        # Otras reglas de negocio, como validación
        return response
