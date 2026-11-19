# Importamos el control central.
from control_central import ControlCentral

# Importamos las clases necesarias.
from clientes import Cliente
from servicios import (
    ReservaSalas,
    AlquilerEquipos,
    AsesoriaEspecializada
)

# Importamos las excepciones personalizadas.
from excepciones import ErrorSistema


print("\n========== PRUEBA DEL CONTROL CENTRAL ==========")

# --------------------------------------------------
# 1. Crear el control central
# --------------------------------------------------

sistema = ControlCentral()

print("\nControl central inicializado correctamente.")


# --------------------------------------------------
# 2. Registrar un cliente
# --------------------------------------------------

cliente1 = Cliente(
    "CLI-101",
    "Laura Martinez",
    "1234567891",
    "laura@gmail.com",
    "3001234568"
)

print(sistema.registrar_cliente(cliente1))


# --------------------------------------------------
# 3. Registrar servicios
# --------------------------------------------------

sala = ReservaSalas(
    "SER-101",
    "Sala de conferencias",
    50000,
    25
)

equipo = AlquilerEquipos(
    "SER-102",
    "Computador portátil",
    25000,
    "Computador"
)

asesoria = AsesoriaEspecializada(
    "SER-103",
    "Asesoría ambiental",
    80000,
    "Gestión ambiental"
)

print(sistema.registrar_servicio(sala))
print(sistema.registrar_servicio(equipo))
print(sistema.registrar_servicio(asesoria))


# --------------------------------------------------
# 4. Buscar un cliente y un servicio
# --------------------------------------------------

print("\n========== BÚSQUEDAS ==========")

cliente_encontrado = sistema.buscar_cliente("CLI-101")
print("Cliente encontrado:", cliente_encontrado.nombre)

servicio_encontrado = sistema.buscar_servicio("SER-101")
print("Servicio encontrado:", servicio_encontrado.nombre)


# --------------------------------------------------
# 5. Crear una reserva
# --------------------------------------------------

print("\n========== CREACIÓN DE RESERVA ==========")

reserva1 = sistema.crear_reserva(
    "RES-101",
    "CLI-101",
    "SER-101",
    3
)

print(reserva1.mostrar_informacion())


# --------------------------------------------------
# 6. Confirmar la reserva
# --------------------------------------------------

print("\n========== CONFIRMAR RESERVA ==========")

print(sistema.confirmar_reserva("RES-101"))


# --------------------------------------------------
# 7. Crear y cancelar otra reserva
# --------------------------------------------------

print("\n========== CANCELAR RESERVA ==========")

reserva2 = sistema.crear_reserva(
    "RES-102",
    "CLI-101",
    "SER-102",
    2
)

print(sistema.cancelar_reserva("RES-102"))


# --------------------------------------------------
# 8. Probar el control de errores
# --------------------------------------------------

print("\n========== PRUEBA DE ERRORES ==========")

try:

    # Intentamos buscar un cliente inexistente.
    sistema.buscar_cliente("CLI-999")

except ErrorSistema as error:

    print("Error controlado:", error)


# --------------------------------------------------
# 9. Mostrar las listas registradas
# --------------------------------------------------

print("\n========== ELEMENTOS REGISTRADOS ==========")

print("Clientes:", len(sistema.listar_clientes()))
print("Servicios:", len(sistema.listar_servicios()))
print("Reservas:", len(sistema.listar_reservas()))


# --------------------------------------------------
# 10. Consultar el estado general
# --------------------------------------------------

print(sistema.mostrar_estado_general())


print("\n========== FIN DE LAS PRUEBAS ==========")
