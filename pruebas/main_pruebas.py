from clientes import Cliente

# Importamos la clase abstracta.
from entidades import Entidad

from servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada

# Creamos una clase de prueba que hereda de Entidad.
class EntidadPrueba(Entidad):

    # Implementamos el método abstracto obligatorio.
    def mostrar_informacion(self):
        return f"Identificador: {self.identificador}"


# Creamos un objeto de prueba.
objeto = EntidadPrueba("ENT-001")

# Mostramos la información del objeto.
print(objeto.mostrar_informacion())


# Intentamos crear directamente una entidad abstracta.
try:
    entidad = Entidad("ENT-002")
except TypeError as error:
    print("Error controlado:", error)


# ==========================================
# PRUEBAS DE LA CLASE CLIENTE
# ==========================================

print("\n========== PRUEBA DE CLIENTE ==========")

# Creamos un cliente con datos válidos.
cliente1 = Cliente(
    "CLI-001",
    "Carlos Rodriguez",
    "1234567890",
    "carlos@gmail.com",
    "3001234567"
)

# Mostramos la información del cliente.
print(cliente1.mostrar_informacion())


# Probamos la validación del correo electrónico.
print("\n========== PRUEBA DE VALIDACION ==========")

try:
    cliente1.correo = "correo_incorrecto"
except ValueError as error:
    print("Error controlado:", error)


# Comprobamos que el cliente conserva su correo anterior.
print("\nCorreo actual:", cliente1.correo)


# Probamos la validación del documento.
try:
    cliente1.documento = "ABC123"
except ValueError as error:
    print("Error controlado:", error)


# ==========================================
# PRUEBAS DE LOS SERVICIOS
# ==========================================

print("\n========== PRUEBAS DE SERVICIOS ==========")

# Creamos un servicio de reserva de salas.
sala = ReservaSalas(
    "SER-001",
    "Sala de reuniones",
    50000,
    20
)

# Creamos un servicio de alquiler de equipos.
equipo = AlquilerEquipos(
    "SER-002",
    "Computador portátil",
    25000,
    "Computador"
)

# Creamos un servicio de asesoría especializada.
asesoria = AsesoriaEspecializada(
    "SER-003",
    "Asesoría informática",
    80000,
    "Tecnología"
)


# Guardamos los servicios en una lista.
lista_servicios = [sala, equipo, asesoria]


# Recorremos los servicios utilizando polimorfismo.
for servicio in lista_servicios:

    print("\n----------------------------------")

    # Mostramos la descripción del servicio.
    print(servicio.describir_servicio())

    # Calculamos el costo de dos horas.
    costo = servicio.calcular_costo(2, 19, 10)

    print(f"Costo de dos horas: ${costo:,.2f}")


# ==========================================
# PRUEBAS DE VALIDACIONES DE SERVICIOS
# ==========================================

print("\n========== PRUEBAS DE VALIDACION ==========")

# Intentamos reservar una sala durante 15 horas.
try:
    sala.calcular_costo(15)

except ValueError as error:
    print("Error controlado:", error)


# Intentamos utilizar un servicio no disponible.
try:

    servicio_no_disponible = ReservaSalas(
        "SER-004",
        "Sala ocupada",
        50000,
        15,
        False
    )

    servicio_no_disponible.calcular_costo(2)

except ValueError as error:
    print("Error controlado:", error)


# Importamos la clase Reserva.
from reservas import Reserva

print("\n========== PRUEBAS DE RESERVAS ==========")

# Creamos una reserva para el cliente Carlos.
reserva1 = Reserva(
    "RES-001",
    cliente1,
    sala,
    3
)

# Mostramos la información inicial.
print("\nINFORMACIÓN INICIAL:")
print(reserva1.mostrar_informacion())

# Calculamos el costo con impuesto y descuento.
print("\nCOSTO CON IMPUESTO Y DESCUENTO:")
print(f"${reserva1.calcular_total(19, 10):,.2f}")

# Confirmamos la reserva.
print("\nCONFIRMACIÓN:")
print(reserva1.confirmar())

# Mostramos el estado actualizado.
print("Estado actual:", reserva1.estado)

# Creamos una segunda reserva para probar la cancelación.
reserva2 = Reserva(
    "RES-002",
    cliente1,
    equipo,
    2
)

print("\nCANCELACIÓN:")
print(reserva2.cancelar())
print("Estado actual:", reserva2.estado)

# Intentamos calcular el costo de una reserva cancelada.
print("\nPRUEBA DE ERROR:")

try:
    reserva2.calcular_total()
except ValueError as error:
    print("Error controlado:", error)

# Intentamos crear una reserva con duración inválida.
try:
    reserva_invalida = Reserva(
        "RES-003",
        cliente1,
        sala,
        15
    )
except ValueError as error:
    print("Error controlado:", error)


# Importamos las excepciones personalizadas.
from excepciones import (
    ErrorSistema,
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaNoValidaError,
    EstadoReservaError
)

print("\n========== PRUEBAS DE EXCEPCIONES PERSONALIZADAS ==========")

# Probamos cada excepción de manera individual.

try:
    raise ClienteInvalidoError("El correo del cliente es incorrecto.")

except ClienteInvalidoError as error:
    print("Error de cliente controlado:", error)


try:
    raise ServicioNoDisponibleError("El servicio no está disponible.")

except ServicioNoDisponibleError as error:
    print("Error de servicio controlado:", error)


try:
    raise ReservaNoValidaError("La duración de la reserva no es válida.")

except ReservaNoValidaError as error:
    print("Error de reserva controlado:", error)


try:
    raise EstadoReservaError("La reserva ya fue cancelada.")

except EstadoReservaError as error:
    print("Error de estado controlado:", error)


# Comprobamos que la clase general puede capturar
# cualquiera de las excepciones personalizadas.
try:
    raise ClienteInvalidoError("Prueba de la excepción general.")

except ErrorSistema as error:
    print("Excepción general controlada:", error)


# =====================================================
# PRUEBAS DEL SISTEMA DE REGISTRO
# =====================================================

# Importamos las funciones del archivo registro.py.
from registro import (
    registrar_evento,
    registrar_error,
    registrar_excepcion
)

print("\n========== PRUEBAS DE REGISTRO ==========")

# PRUEBA 1: Registrar un evento normal.
registrar_evento(
    "Sistema Software FJ iniciado correctamente."
)

# PRUEBA 2: Registrar un error.
registrar_error(
    "Prueba de registro de un error controlado."
)

# PRUEBA 3: Registrar una excepción.
try:
    # Intentamos dividir un número entre cero.
    resultado = 10 / 0

except ZeroDivisionError:
    # Registramos la excepción y sus detalles técnicos.
    registrar_excepcion(
        "Se produjo una división entre cero."
    )

# Mostramos un mensaje de confirmación en pantalla.
print("Eventos y errores registrados correctamente.")