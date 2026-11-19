# ------------------------------------------------------------
# IMPORTACIÓN DE CLASES Y FUNCIONES
# ------------------------------------------------------------

from entidades import Entidad

from clientes import Cliente

from servicios import (
    ReservaSalas,
    AlquilerEquipos,
    AsesoriaEspecializada
)

from control_central import ControlCentral

from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaNoValidaError,
    EstadoReservaError
)

from registro import (
    registrar_evento,
    registrar_error,
    registrar_excepcion
)


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def ejecutar_sistema():

    print("\n==============================================")
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print("==============================================")

    registrar_evento(
        "Sistema Software FJ iniciado correctamente."
    )

    # --------------------------------------------------------
    # 1. DEMOSTRACIÓN DE ABSTRACCIÓN
    # --------------------------------------------------------

    print("\n========== 1. DEMOSTRACIÓN DE ABSTRACCIÓN ==========")

    try:

        # Creamos un cliente concreto para demostrar
        # que una clase derivada de Entidad sí funciona.

        cliente_demo = Cliente(
            "CLI-DEMO",
            "Usuario Demostracion",
            "12345678",
            "demo@gmail.com",
            "3001234567"
        )

        print(
            "Identificador:",
            cliente_demo.identificador
        )

        # Intentamos instanciar directamente la clase abstracta.
        entidad_demo = Entidad("ENT-001")

    except TypeError as error:

        print("Abstracción comprobada:", error)

        registrar_error(
            f"Prueba de abstracción: {error}"
        )

    except (ValueError, ClienteInvalidoError) as error:

        print("Error en la demostración:", error)

        registrar_error(
            f"Error en la demostración de abstracción: {error}"
        )

    # --------------------------------------------------------
    # 2. INICIALIZACIÓN DEL SISTEMA
    # --------------------------------------------------------

    print("\n========== 2. INICIALIZACIÓN DEL SISTEMA ==========")

    control = ControlCentral()

    print("Control central inicializado correctamente.")

    registrar_evento(
        "Control central inicializado correctamente."
    )

    # --------------------------------------------------------
    # 3. REGISTRO DE CLIENTES
    # --------------------------------------------------------

    print("\n========== 3. REGISTRO DE CLIENTES ==========")

    # OPERACIÓN 1: Registro de un cliente válido.

    try:

        cliente1 = Cliente(
            "CLI-001",
            "Carlos Rodriguez",
            "12345678",
            "carlos@gmail.com",
            "3001234567"
        )

        print(control.registrar_cliente(cliente1))

    except (ClienteInvalidoError, ValueError, TypeError) as error:

        print("Error al registrar cliente:", error)

        registrar_error(
            f"Registro de cliente CLI-001: {error}"
        )

    # OPERACIÓN 2: Registro de un segundo cliente válido.

    try:

        cliente2 = Cliente(
            "CLI-002",
            "Laura Martinez",
            "87654321",
            "laura@gmail.com",
            "3109876543"
        )

        print(control.registrar_cliente(cliente2))

    except (ClienteInvalidoError, ValueError, TypeError) as error:

        print("Error al registrar cliente:", error)

        registrar_error(
            f"Registro de cliente CLI-002: {error}"
        )

    # OPERACIÓN 3: Intento de registro de un cliente duplicado.

    try:

        cliente_duplicado = Cliente(
            "CLI-001",
            "Pedro Ramirez",
            "11223344",
            "pedro@gmail.com",
            "3201234567"
        )

        print(control.registrar_cliente(cliente_duplicado))

    except (ClienteInvalidoError, ValueError, TypeError) as error:

        print("Error controlado:", error)

        registrar_error(
            f"Prueba de cliente duplicado: {error}"
        )

    # OPERACIÓN 4: Intento de creación de un cliente inválido.

    try:

        cliente_invalido = Cliente(
            "CLI-003",
            "Pedro Ramirez",
            "12345",
            "correo_incorrecto",
            "3001234567"
        )

        print(control.registrar_cliente(cliente_invalido))

    except (ClienteInvalidoError, ValueError, TypeError) as error:

        print("Registro de cliente inválido:", error)

        registrar_error(
            f"Prueba de registro de cliente inválido: {error}"
        )

    # OPERACIÓN 5: Intento de modificar el correo de Carlos
    # utilizando un formato incorrecto.

    try:

        cliente1.correo = "correo_incorrecto"

    except (ClienteInvalidoError, ValueError) as error:

        print("Validación de correo:", error)

        print(
            "Correo conservado:",
            cliente1.correo
        )

        registrar_error(
            f"Intento de modificar correo del cliente: {error}"
        )

    # --------------------------------------------------------
    # 4. REGISTRO DE SERVICIOS
    # --------------------------------------------------------

    print("\n========== 4. REGISTRO DE SERVICIOS ==========")

    # OPERACIÓN 6: Creación de un servicio de salas.

    try:

        sala = ReservaSalas(
            "SER-001",
            "Sala de reuniones",
            50000,
            20
        )

        print(control.registrar_servicio(sala))

    except (ValueError, TypeError) as error:

        print("Error al crear sala:", error)

        registrar_error(
            f"Creación de sala: {error}"
        )

    # OPERACIÓN 7: Creación de un servicio de equipos.

    try:

        equipo = AlquilerEquipos(
            "SER-002",
            "Computador portátil",
            25000,
            "Computador"
        )

        print(control.registrar_servicio(equipo))

    except (ValueError, TypeError) as error:

        print("Error al crear equipo:", error)

        registrar_error(
            f"Creación de equipo: {error}"
        )

    # OPERACIÓN 8: Creación de un servicio de asesoría.

    try:

        asesoria = AsesoriaEspecializada(
            "SER-003",
            "Asesoría informática",
            80000,
            "Tecnología"
        )

        print(control.registrar_servicio(asesoria))

    except (ValueError, TypeError) as error:

        print("Error al crear asesoría:", error)

        registrar_error(
            f"Creación de asesoría: {error}"
        )

    # OPERACIÓN 9: Intento de creación de un servicio inválido.

    try:

        servicio_invalido = ReservaSalas(
            "SER-005",
            "Sala inválida",
            -10000,
            10
        )

        print(control.registrar_servicio(servicio_invalido))

    except (ValueError, TypeError) as error:

        print("Creación de servicio inválido:", error)

        registrar_error(
            f"Prueba de creación de servicio inválido: {error}"
        )

    # --------------------------------------------------------
    # 5. DEMOSTRACIÓN DE POLIMORFISMO
    # --------------------------------------------------------

    print("\n========== 5. DEMOSTRACIÓN DE POLIMORFISMO ==========")

    servicios = [
        sala,
        equipo,
        asesoria
    ]

    for servicio in servicios:

        print("\n----------------------------------------")

        print(servicio.describir_servicio())

        print(
            f"Costo de dos horas: "
            f"${servicio.calcular_costo(2):,.2f}"
        )

    # --------------------------------------------------------
    # 6. BÚSQUEDAS
    # --------------------------------------------------------

    print("\n========== 6. BÚSQUEDAS ==========")

    try:

        cliente_encontrado = control.buscar_cliente("CLI-001")

        print(
            "Cliente encontrado:",
            cliente_encontrado.nombre
        )

    except ClienteInvalidoError as error:

        print("Búsqueda de cliente:", error)

        registrar_error(
            f"Búsqueda de cliente: {error}"
        )

    try:

        servicio_encontrado = control.buscar_servicio("SER-001")

        print(
            "Servicio encontrado:",
            servicio_encontrado.nombre
        )

    except ServicioNoDisponibleError as error:

        print("Búsqueda de servicio:", error)

        registrar_error(
            f"Búsqueda de servicio: {error}"
        )

    try:

        control.buscar_cliente("CLI-999")

    except ClienteInvalidoError as error:

        print("Búsqueda controlada:", error)

        registrar_error(
            f"Cliente inexistente: {error}"
        )

    # --------------------------------------------------------
    # 7. CREACIÓN DE RESERVAS
    # --------------------------------------------------------

    print("\n========== 7. CREACIÓN DE RESERVAS ==========")

    # OPERACIÓN 10: Creación de una reserva exitosa.

    try:

        reserva1 = control.crear_reserva(
            "RES-001",
            "CLI-001",
            "SER-001",
            3
        )

        print(reserva1.mostrar_informacion())

        print("\nCosto con impuesto y descuento:")

        total = reserva1.calcular_total(
            impuesto=19,
            descuento=10
        )

        print(f"Total: ${total:,.2f}")

    except (ReservaNoValidaError, ValueError, TypeError) as error:

        print("Error al crear reserva:", error)

        registrar_error(
            f"Creación de reserva RES-001: {error}"
        )

    # OPERACIÓN 11: Creación de una segunda reserva exitosa.

    try:

        reserva2 = control.crear_reserva(
            "RES-002",
            "CLI-002",
            "SER-002",
            2
        )

        print("\nSegunda reserva creada correctamente.")

    except (ReservaNoValidaError, ValueError, TypeError) as error:

        print("Error al crear segunda reserva:", error)

        registrar_error(
            f"Creación de reserva RES-002: {error}"
        )

    # --------------------------------------------------------
    # 8. GESTIÓN DE RESERVAS
    # --------------------------------------------------------

    print("\n========== 8. GESTIÓN DE RESERVAS ==========")

    # OPERACIÓN 12: Confirmación de reserva.

    try:

        control.confirmar_reserva("RES-001")

        print("Reserva RES-001 confirmada correctamente.")

    except (ReservaNoValidaError, EstadoReservaError, ValueError) as error:

        print("Error al confirmar reserva:", error)

        registrar_error(
            f"Confirmación de reserva: {error}"
        )

    # OPERACIÓN 13: Cancelación de reserva.

    try:

        control.cancelar_reserva("RES-002")

        print("Reserva RES-002 cancelada correctamente.")

    except (ReservaNoValidaError, EstadoReservaError, ValueError) as error:

        print("Error al cancelar reserva:", error)

        registrar_error(
            f"Cancelación de reserva: {error}"
        )

    # --------------------------------------------------------
    # 9. PRUEBAS DE VALIDACIÓN
    # --------------------------------------------------------

    print("\n========== 9. PRUEBAS DE VALIDACIÓN ==========")

    # OPERACIÓN 14: Intento de reserva con duración excesiva.

    try:

        control.crear_reserva(
            "RES-003",
            "CLI-001",
            "SER-001",
            15
        )

    except (ReservaNoValidaError, ValueError, TypeError) as error:

        print("Duración no válida:", error)

        registrar_error(
            f"Prueba de duración no válida: {error}"
        )

    # OPERACIÓN 15: Intento de reserva con servicio no disponible.

    try:

        servicio_ocupado = ReservaSalas(
            "SER-004",
            "Sala ocupada",
            50000,
            10,
            disponible=False
        )

        print(control.registrar_servicio(servicio_ocupado))

        control.crear_reserva(
            "RES-004",
            "CLI-001",
            "SER-004",
            2
        )

    except (
        ServicioNoDisponibleError,
        ReservaNoValidaError,
        ValueError,
        TypeError
    ) as error:

        print("Disponibilidad controlada:", error)

        registrar_error(
            f"Prueba de servicio no disponible: {error}"
        )

    # --------------------------------------------------------
    # 10. EXCEPCIONES PERSONALIZADAS
    # --------------------------------------------------------

    print("\n========== 10. EXCEPCIONES PERSONALIZADAS ==========")

    try:

        raise ClienteInvalidoError(
            "El correo del cliente es incorrecto."
        )

    except ClienteInvalidoError as error:

        print("Error de cliente:", error)

        registrar_error(
            f"Excepción de cliente: {error}"
        )

    try:

        raise ServicioNoDisponibleError(
            "El servicio no está disponible."
        )

    except ServicioNoDisponibleError as error:

        print("Error de servicio:", error)

        registrar_error(
            f"Excepción de servicio: {error}"
        )

    try:

        raise ReservaNoValidaError(
            "La duración de la reserva no es válida."
        )

    except ReservaNoValidaError as error:

        print("Error de reserva:", error)

        registrar_error(
            f"Excepción de reserva: {error}"
        )

    try:

        raise EstadoReservaError(
            "La reserva ya fue cancelada."
        )

    except EstadoReservaError as error:

        print("Error de estado:", error)

        registrar_error(
            f"Excepción de estado: {error}"
        )

    # --------------------------------------------------------
    # 11. REGISTRO DE EVENTOS Y MANEJO DE ERRORES
    # --------------------------------------------------------

    print("\n========== 11. REGISTRO DE EVENTOS ==========")

    try:

        print("Simulación de una operación matemática.")

        # Generamos intencionalmente un error matemático.
        resultado = 10 / 0

    except ZeroDivisionError as error:

        print("Excepción controlada:", error)

        registrar_excepcion(
            "Error matemático controlado durante la ejecución."
        )

    else:

        print("Operación realizada correctamente.")

    finally:

        print("Bloque finally ejecutado correctamente.")

        registrar_evento(
            "Bloque finally ejecutado correctamente."
        )

    # --------------------------------------------------------
    # 12. ESTADO GENERAL DEL SISTEMA
    # --------------------------------------------------------

    print("\n========== 12. ESTADO GENERAL ==========")

    # El método devuelve un texto, por eso utilizamos print().
    print(control.mostrar_estado_general())

    registrar_evento(
        "Ejecución de las pruebas del sistema finalizada."
    )

    print("\n==============================================")
    print("       EJECUCIÓN FINALIZADA CORRECTAMENTE")
    print("==============================================")


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

if __name__ == "__main__":

    try:

        ejecutar_sistema()

    except Exception as error:

        print("\nERROR GENERAL CONTROLADO:", error)

        registrar_excepcion(
            "Se presentó un error general durante la ejecución."
        )

        print(
            "El error fue registrado en el archivo de logs."
        )
