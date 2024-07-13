# Definición de las rutas de la API


from fastapi import APIRouter

router = APIRouter()

# Rutas para AtenciónProveedores
@router.post("/proveedores/cargar-requerimientos")
async def cargar_requerimientos(data: dict):
    return {"status": "Requerimientos cargados", "data": data}

@router.post("/proveedores/registrar-compra")
async def registrar_compra(data: dict):
    return {"status": "Compra registrada", "data": data}

# Rutas para Compras/Ventas
@router.post("/compras/registrar-venta")
async def registrar_venta(data: dict):
    return {"status": "Venta registrada", "data": data}

@router.post("/compras/generar-factura")
async def generar_factura(data: dict):
    return {"status": "Factura generada", "data": data}

# Rutas para Contabilidad
@router.post("/contabilidad/actualizar-inventario")
async def actualizar_inventario(data: dict):
    return {"status": "Inventario actualizado", "data": data}

# Rutas para Tienda
@router.post("/tienda/cargar-productos")
async def cargar_productos(data: dict):
    return {"status": "Productos cargados", "data": data}

@router.post("/tienda/ordenar-transporte")
async def ordenar_transporte(data: dict):
    return {"status": "Transporte ordenado", "data": data}
