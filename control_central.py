# Importamos la clase Cliente para validar los clientes registrados.
from clientes import Cliente

# Importamos la clase abstracta Servicio.
# Esto permite recibir cualquiera de sus clases especializadas.
from servicios import Servicio

# Importamos la clase Reserva para gestionar las reservas.
from reservas import Reserva

# Importamos las excepciones personalizadas.
from excepciones import (
    ErrorSistema,
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaNoValidaError
)

# Importamos las funciones para registrar eventos y errores.
from registro import registrar_evento, registrar_error


# ==========================================================
# CLASE CONTROL CENTRAL
# ==========================================================

class ControlCentral:
    """
    Clase encargada de administrar los clientes,
    servicios y reservas de la empresa Software FJ.
    """

    def __init__(self):

        # Listas que almacenan los objetos en memoria.
        # No se utiliza una base de datos.
        self._clientes = []
        self._servicios = []
        self._reservas = []

        # Registramos el inicio del control central.
        registrar_evento(
            "Control central del sistema inicializado correctamente."
        )

    # ======================================================
    # REGISTRAR CLIENTES
    # ======================================================

    def registrar_cliente(self, cliente):
        """
        Recibe un objeto Cliente y lo almacena en la lista.
        """

        try:

            # Comprobamos que el objeto sea de tipo Cliente.
            if not isinstance(cliente, Cliente):
                raise ClienteInvalidoError(
                    "El objeto proporcionado no es un cliente válido."
                )

            # Evitamos registrar dos clientes con el mismo identificador.
            if self.buscar_cliente(cliente.identificador, mostrar_error=False):
                raise ClienteInvalidoError(
                    "Ya existe un cliente con ese identificador."
                )

            # Guardamos el cliente en la lista.
            self._clientes.append(cliente)

            # Registramos la operación exitosa.
            registrar_evento(
                f"Cliente agregado al control central: "
                f"{cliente.identificador}"
            )

            return (
                f"Cliente {cliente.nombre} registrado "
                "en el control central correctamente."
            )

        except (TypeError, ValueError) as error:

            # Registramos el error y lo propagamos.
            registrar_error(
                f"Error en el registro central de clientes: {error}"
            )
            raise

    # ======================================================
    # REGISTRAR SERVICIOS
    # ======================================================

    def registrar_servicio(self, servicio):
        """
        Recibe un objeto de alguna clase especializada de Servicio
        y lo almacena en la lista correspondiente.
        """

        try:

            # Comprobamos que el objeto pertenezca a Servicio
            # o a una de sus clases derivadas.
            if not isinstance(servicio, Servicio):
                raise ServicioNoDisponibleError(
                    "El objeto proporcionado no es un servicio válido."
                )

            # Comprobamos que no exista el mismo identificador.
            if self.buscar_servicio(servicio.identificador, mostrar_error=False):
                raise ErrorSistema(
                    "Ya existe un servicio con ese identificador."
                )

            # Almacenamos el servicio.
            self._servicios.append(servicio)

            # Registramos el evento.
            registrar_evento(
                f"Servicio agregado al control central: "
                f"{servicio.identificador}"
            )

            return (
                f"Servicio {servicio.nombre} registrado "
                "en el control central correctamente."
            )

        except (TypeError, ValueError) as error:

            registrar_error(
                f"Error en el registro central de servicios: {error}"
            )
            raise

    # ======================================================
    # BUSCAR CLIENTES
    # ======================================================

    def buscar_cliente(self, identificador, mostrar_error=True):
        """
        Busca un cliente utilizando su identificador.

        Si mostrar_error es False, retorna None cuando no existe.
        Esto permite comprobar duplicados sin generar un error.
        """

        for cliente in self._clientes:

            if cliente.identificador == identificador:
                return cliente

        # Si no encontramos el cliente, controlamos la situación.
        if mostrar_error:

            mensaje = (
                f"No se encontró el cliente con identificador "
                f"{identificador}."
            )

            registrar_error(mensaje)

            raise ClienteInvalidoError(mensaje)

        return None

    # ======================================================
    # BUSCAR SERVICIOS
    # ======================================================

    def buscar_servicio(self, identificador, mostrar_error=True):
        """
        Busca un servicio utilizando su identificador.
        """

        for servicio in self._servicios:

            if servicio.identificador == identificador:
                return servicio

        if mostrar_error:

            mensaje = (
                f"No se encontró el servicio con identificador "
                f"{identificador}."
            )

            registrar_error(mensaje)

            raise ServicioNoDisponibleError(mensaje)

        return None

    # ======================================================
    # CREAR RESERVAS
    # ======================================================

    def crear_reserva(
        self,
        identificador,
        id_cliente,
        id_servicio,
        duracion
    ):
        """
        Crea una reserva utilizando los identificadores
        del cliente y del servicio.
        """

        try:

            # Comprobamos que no exista una reserva con ese código.
            if self.buscar_reserva(identificador, mostrar_error=False):
                raise ReservaNoValidaError(
                    "Ya existe una reserva con ese identificador."
                )

            # Buscamos el cliente que realizará la reserva.
            cliente = self.buscar_cliente(id_cliente)

            # Buscamos el servicio que utilizará el cliente.
            servicio = self.buscar_servicio(id_servicio)

            # Creamos el objeto Reserva.
            nueva_reserva = Reserva(
                identificador,
                cliente,
                servicio,
                duracion
            )

            # Almacenamos la reserva creada.
            self._reservas.append(nueva_reserva)

            # Registramos la operación.
            registrar_evento(
                f"Reserva agregada al control central: {identificador}"
            )

            return nueva_reserva

        except (TypeError, ValueError) as error:

            registrar_error(
                f"Error al crear una reserva desde el control central: "
                f"{error}"
            )

            raise

    # ======================================================
    # BUSCAR RESERVAS
    # ======================================================

    def buscar_reserva(self, identificador, mostrar_error=True):
        """
        Busca una reserva utilizando su identificador.
        """

        for reserva in self._reservas:

            if reserva.identificador == identificador:
                return reserva

        if mostrar_error:

            mensaje = (
                f"No se encontró la reserva con identificador "
                f"{identificador}."
            )

            registrar_error(mensaje)

            raise ReservaNoValidaError(mensaje)

        return None

    # ======================================================
    # CONFIRMAR RESERVAS
    # ======================================================

    def confirmar_reserva(self, identificador):
        """
        Busca una reserva y solicita su confirmación.
        """

        try:

            reserva = self.buscar_reserva(identificador)

            resultado = reserva.confirmar()

            registrar_evento(
                f"Confirmación gestionada por control central: "
                f"{identificador}"
            )

            return resultado

        except (TypeError, ValueError) as error:

            registrar_error(
                f"Error al confirmar desde el control central: {error}"
            )
            raise

    # ======================================================
    # CANCELAR RESERVAS
    # ======================================================

    def cancelar_reserva(self, identificador):
        """
        Busca una reserva y solicita su cancelación.
        """

        try:

            reserva = self.buscar_reserva(identificador)

            resultado = reserva.cancelar()

            registrar_evento(
                f"Cancelación gestionada por control central: "
                f"{identificador}"
            )

            return resultado

        except (TypeError, ValueError) as error:

            registrar_error(
                f"Error al cancelar desde el control central: {error}"
            )
            raise

    # ======================================================
    # CONSULTAR CLIENTES, SERVICIOS Y RESERVAS
    # ======================================================

    def listar_clientes(self):
        """Retorna una copia de la lista de clientes."""
        return list(self._clientes)

    def listar_servicios(self):
        """Retorna una copia de la lista de servicios."""
        return list(self._servicios)

    def listar_reservas(self):
        """Retorna una copia de la lista de reservas."""
        return list(self._reservas)

    # ======================================================
    # MOSTRAR INFORMACIÓN GENERAL DEL SISTEMA
    # ======================================================

    def mostrar_estado_general(self):
        """
        Genera un resumen de los elementos almacenados
        en el control central.
        """

        # Contamos las reservas según su estado.
        pendientes = sum(
            1 for reserva in self._reservas
            if reserva.estado == "PENDIENTE"
        )

        confirmadas = sum(
            1 for reserva in self._reservas
            if reserva.estado == "CONFIRMADA"
        )

        canceladas = sum(
            1 for reserva in self._reservas
            if reserva.estado == "CANCELADA"
        )

        # Construimos el resumen general.
        return (
            "\n========== ESTADO GENERAL DEL SISTEMA ==========\n"
            f"Total de clientes registrados: {len(self._clientes)}\n"
            f"Total de servicios registrados: {len(self._servicios)}\n"
            f"Total de reservas registradas: {len(self._reservas)}\n"
            "\nESTADO DE LAS RESERVAS:\n"
            f"Pendientes: {pendientes}\n"
            f"Confirmadas: {confirmadas}\n"
            f"Canceladas: {canceladas}\n"
            "================================================"
        )
    