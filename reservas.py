# Importamos la clase abstracta Entidad.
from entidades import Entidad

# Importamos las clases necesarias para validar los objetos.
from clientes import Cliente
from servicios import Servicio

# Importamos las funciones para registrar eventos y errores.
from registro import registrar_evento, registrar_error

# Importamos las excepciones personalizadas.
from excepciones import (
    ReservaNoValidaError,
    EstadoReservaError
)


# ==========================================================
# CLASE RESERVA
# ==========================================================

class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente
    para utilizar uno de los servicios de Software FJ.
    """

    def __init__(self, identificador, cliente, servicio, duracion):

        try:

            # Inicializamos el identificador heredado de Entidad.
            # Se incluye dentro del try para registrar también
            # los errores relacionados con identificadores inválidos.
            super().__init__(identificador)

            # Validamos que el cliente sea un objeto Cliente.
            if not isinstance(cliente, Cliente):
                raise TypeError(
                    "La reserva debe tener un cliente válido."
                )

            # Validamos que el servicio sea un objeto Servicio.
            if not isinstance(servicio, Servicio):
                raise TypeError(
                    "La reserva debe tener un servicio válido."
                )

            # Validamos la duración según el tipo de servicio.
            servicio.validar_parametros(duracion)

            # Guardamos los datos de la reserva.
            self._cliente = cliente
            self._servicio = servicio
            self._duracion = duracion

            # Toda reserva nueva comienza pendiente.
            self._estado = "PENDIENTE"

        except (TypeError, ValueError) as error:

            # Registramos el error producido al crear la reserva.
            registrar_error(
                f"Error al crear la reserva {identificador}: {error}"
            )

            # Generamos una excepción personalizada,
            # conservando el error original.
            raise ReservaNoValidaError(
                f"No fue posible crear la reserva: {error}"
            ) from error

        else:

            # Registramos la reserva únicamente si fue creada correctamente.
            registrar_evento(
                f"Reserva creada: {self.identificador} | "
                f"Cliente: {self._cliente.nombre} | "
                f"Servicio: {self._servicio.nombre}"
            )

    # ------------------------------------------------------
    # PROPIEDADES PARA ACCEDER A LOS ATRIBUTOS
    # ------------------------------------------------------

    # Permite consultar el cliente asociado a la reserva.
    @property
    def cliente(self):
        return self._cliente

    # Permite consultar el servicio asociado a la reserva.
    @property
    def servicio(self):
        return self._servicio

    # Permite consultar la duración de la reserva.
    @property
    def duracion(self):
        return self._duracion

    # Permite consultar el estado actual de la reserva.
    @property
    def estado(self):
        return self._estado

    # ------------------------------------------------------
    # CALCULAR EL COSTO DE LA RESERVA
    # ------------------------------------------------------

    def calcular_total(self, impuesto=0, descuento=0):
        """
        Calcula el costo de la reserva.

        Permite aplicar impuestos y descuentos opcionales.
        """

        try:

            # No se permite calcular el costo de una reserva cancelada.
            if self._estado == "CANCELADA":
                raise EstadoReservaError(
                    "No se puede calcular una reserva cancelada."
                )

            # Delegamos el cálculo al servicio correspondiente.
            # El servicio aplica sus propias validaciones y tarifas.
            return self._servicio.calcular_costo(
                self._duracion,
                impuesto,
                descuento
            )

        except (TypeError, ValueError) as error:

            # Registramos el error producido durante el cálculo.
            registrar_error(
                f"Error al calcular la reserva "
                f"{self.identificador}: {error}"
            )

            # Propagamos el error para controlarlo desde main.py.
            raise

    # ------------------------------------------------------
    # CONFIRMAR RESERVA
    # ------------------------------------------------------

    def confirmar(self):
        """
        Cambia el estado de una reserva pendiente a confirmada.
        """

        try:

            # Solamente se pueden confirmar reservas pendientes.
            if self._estado != "PENDIENTE":
                raise EstadoReservaError(
                    "Solamente se pueden confirmar reservas pendientes."
                )

            # Actualizamos el estado de la reserva.
            self._estado = "CONFIRMADA"

        except EstadoReservaError as error:

            # Registramos el intento de confirmación no válido.
            registrar_error(
                f"Error al confirmar la reserva "
                f"{self.identificador}: {error}"
            )

            raise

        else:

            # Registramos la confirmación exitosa.
            registrar_evento(
                f"Reserva confirmada: {self.identificador}"
            )

            return (
                f"Reserva {self.identificador} "
                "confirmada correctamente."
            )

    # ------------------------------------------------------
    # CANCELAR RESERVA
    # ------------------------------------------------------

    def cancelar(self):
        """
        Cambia el estado de una reserva a cancelada.
        """

        try:

            # No se permite cancelar una reserva que ya está cancelada.
            if self._estado == "CANCELADA":
                raise EstadoReservaError(
                    "La reserva ya se encuentra cancelada."
                )

            # Actualizamos el estado de la reserva.
            self._estado = "CANCELADA"

        except EstadoReservaError as error:

            # Registramos el intento de cancelación no válido.
            registrar_error(
                f"Error al cancelar la reserva "
                f"{self.identificador}: {error}"
            )

            raise

        else:

            # Registramos la cancelación exitosa.
            registrar_evento(
                f"Reserva cancelada: {self.identificador}"
            )

            return (
                f"Reserva {self.identificador} "
                "cancelada correctamente."
            )

    # ------------------------------------------------------
    # MOSTRAR INFORMACIÓN DE LA RESERVA
    # ------------------------------------------------------

    def mostrar_informacion(self):
        """
        Retorna los datos principales de la reserva.
        """

        # Si la reserva está cancelada, no calculamos su costo.
        if self._estado == "CANCELADA":

            costo = "No disponible (reserva cancelada)"

        else:

            # Calculamos el costo normal de la reserva.
            costo = f"${self.calcular_total():,.2f}"

        return (
            f"Identificador de reserva: {self.identificador}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion} horas\n"
            f"Costo: {costo}\n"
            f"Estado: {self.estado}"
        )
