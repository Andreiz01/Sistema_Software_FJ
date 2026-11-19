# Importamos herramientas para validar números.
import math

# Importamos la clase abstracta Entidad.
from entidades import Entidad

# Importamos herramientas para crear métodos abstractos.
from abc import abstractmethod

# Importamos las funciones para registrar eventos y errores.
from registro import registrar_evento, registrar_error

# Importamos las excepciones personalizadas.
from excepciones import (
    ServicioNoDisponibleError,
    ReservaNoValidaError
)


# ==========================================================
# CLASE ABSTRACTA SERVICIO
# ==========================================================

class Servicio(Entidad):
    """
    Clase abstracta que representa un servicio ofrecido
    por la empresa Software FJ.
    """

    def __init__(
        self,
        identificador,
        nombre,
        precio_unitario,
        disponible=True
    ):

        # Inicializamos el identificador heredado de Entidad.
        super().__init__(identificador)

        # Validamos que el nombre sea correcto.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError(
                "El nombre del servicio no puede estar vacío."
            )

        # Validamos que el precio sea numérico.
        # También evitamos aceptar valores booleanos.
        if (
            isinstance(precio_unitario, bool)
            or not isinstance(precio_unitario, (int, float))
        ):
            raise ValueError(
                "El precio del servicio debe ser numérico."
            )

        # Comprobamos que el precio sea positivo y finito.
        if (
            not math.isfinite(precio_unitario)
            or precio_unitario <= 0
        ):
            raise ValueError(
                "El precio del servicio debe ser mayor que cero "
                "y representar un número finito."
            )

        # Validamos que la disponibilidad sea verdadera o falsa.
        if not isinstance(disponible, bool):
            raise ValueError(
                "La disponibilidad debe ser True o False."
            )

        # Atributos protegidos del servicio.
        self._nombre = nombre.strip()
        self._precio_unitario = float(precio_unitario)
        self._disponible = disponible

    # ------------------------------------------------------
    # REGISTRO DE CREACIÓN DEL SERVICIO
    # ------------------------------------------------------

    def _registrar_creacion(self):

        registrar_evento(
            f"Servicio creado: {self.identificador} - {self.nombre}"
        )

    # ------------------------------------------------------
    # PROPIEDADES PARA ACCEDER A LOS ATRIBUTOS
    # ------------------------------------------------------

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_unitario(self):
        return self._precio_unitario

    @property
    def disponible(self):
        return self._disponible

    # ------------------------------------------------------
    # VALIDACIÓN DE DURACIÓN
    # ------------------------------------------------------

    def _validar_duracion(self, duracion, limite, mensaje):

        try:

            # Comprobamos que la duración sea numérica.
            if (
                isinstance(duracion, bool)
                or not isinstance(duracion, (int, float))
            ):
                raise ValueError(
                    "La duración debe ser numérica."
                )

            # Comprobamos que la duración sea finita y positiva.
            if (
                not math.isfinite(duracion)
                or duracion <= 0
            ):
                raise ValueError(
                    "La duración debe ser un número finito "
                    "mayor que cero."
                )

            # Comprobamos el límite permitido para cada servicio.
            if duracion > limite:
                raise ValueError(mensaje)

        except ValueError as error:

            # Registramos el error.
            registrar_error(
                f"Error al validar la duración del servicio "
                f"{self.identificador}: {error}"
            )

            # Generamos una excepción personalizada
            # y conservamos el error original.
            raise ReservaNoValidaError(
                str(error)
            ) from error

        return True

    # ------------------------------------------------------
    # VALIDACIÓN DE DISPONIBILIDAD
    # ------------------------------------------------------

    def _validar_disponibilidad(self):

        # Comprobamos si el servicio está disponible.
        if not self.disponible:

            mensaje = (
                "El servicio seleccionado no está disponible."
            )

            # Registramos el error.
            registrar_error(
                f"Servicio no disponible: {self.identificador}"
            )

            # Generamos la excepción personalizada.
            raise ServicioNoDisponibleError(mensaje)

        return True

    # ------------------------------------------------------
    # MÉTODO PARA CALCULAR EL COSTO
    # CON IMPUESTOS Y DESCUENTOS
    # ------------------------------------------------------

    def _calcular_total(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo total del servicio.

        Permite utilizar diferentes combinaciones:

        1. Solamente duración.
        2. Duración e impuesto.
        3. Duración, impuesto y descuento.
        """

        try:

            # Validamos que la duración sea numérica,
            # finita y positiva.
            if (
                isinstance(duracion, bool)
                or not isinstance(duracion, (int, float))
                or not math.isfinite(duracion)
                or duracion <= 0
            ):
                raise ValueError(
                    "La duración debe ser un número finito positivo."
                )

            # Validamos los porcentajes del impuesto y descuento.
            for porcentaje, nombre in [
                (impuesto, "impuesto"),
                (descuento, "descuento")
            ]:

                # Comprobamos que el porcentaje sea numérico.
                if (
                    isinstance(porcentaje, bool)
                    or not isinstance(porcentaje, (int, float))
                ):
                    raise ValueError(
                        f"El {nombre} debe ser numérico."
                    )

                # Comprobamos que esté entre 0 y 100.
                # Esta condición también rechaza NaN e infinito.
                if not 0 <= porcentaje <= 100:
                    raise ValueError(
                        f"El {nombre} debe estar entre 0 y 100 "
                        "y ser un número finito."
                    )

        except ValueError as error:

            # Registramos el error en el archivo de registro.
            registrar_error(
                f"Error al calcular el costo del servicio "
                f"{self.identificador}: {error}"
            )

            # Generamos una excepción personalizada.
            # El uso de 'from error' conserva la causa original.
            raise ReservaNoValidaError(
                str(error)
            ) from error

        # Calculamos el subtotal según la duración.
        subtotal = self._precio_unitario * duracion

        # Aplicamos el descuento.
        subtotal = subtotal - (
            subtotal * descuento / 100
        )

        # Aplicamos el impuesto.
        total = subtotal + (
            subtotal * impuesto / 100
        )

        # Comprobamos que el resultado sea finito.
        if not math.isfinite(total):

            error = ValueError(
                "El resultado del cálculo no es un número finito."
            )

            registrar_error(
                f"Error al calcular el costo del servicio "
                f"{self.identificador}: {error}"
            )

            raise ReservaNoValidaError(
                str(error)
            ) from error

        # Retornamos el resultado con dos decimales.
        return round(total, 2)

    # ------------------------------------------------------
    # MÉTODOS ABSTRACTOS
    # ------------------------------------------------------

    @abstractmethod
    def calcular_costo(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    # ------------------------------------------------------
    # MOSTRAR INFORMACIÓN GENERAL
    # ------------------------------------------------------

    def mostrar_informacion(self):

        return (
            f"Identificador: {self.identificador}\n"
            f"Servicio: {self.nombre}\n"
            f"Precio por unidad: ${self.precio_unitario:,.2f}\n"
            f"Disponible: {'Sí' if self.disponible else 'No'}\n"
            f"Descripción: {self.describir_servicio()}"
        )


# ==========================================================
# CLASE RESERVA DE SALAS
# ==========================================================

class ReservaSalas(Servicio):
    """
    Servicio de alquiler de salas para reuniones y eventos.
    """

    def __init__(
        self,
        identificador,
        nombre,
        precio_unitario,
        capacidad,
        disponible=True
    ):

        # Inicializamos los atributos heredados.
        super().__init__(
            identificador,
            nombre,
            precio_unitario,
            disponible
        )

        # Validamos que la capacidad sea un entero positivo.
        if (
            isinstance(capacidad, bool)
            or not isinstance(capacidad, int)
            or capacidad <= 0
        ):
            raise ValueError(
                "La capacidad debe ser un número entero positivo."
            )

        # Guardamos la capacidad de la sala.
        self._capacidad = capacidad

        # Registramos el servicio después de validar sus atributos.
        self._registrar_creacion()

    def calcular_costo(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):

        # Validamos los parámetros antes de calcular.
        self.validar_parametros(duracion)

        return self._calcular_total(
            duracion,
            impuesto,
            descuento
        )

    def describir_servicio(self):

        return (
            f"Alquiler de sala con capacidad para "
            f"{self._capacidad} personas."
        )

    def validar_parametros(self, duracion):

        # Validamos la duración máxima de 12 horas.
        self._validar_duracion(
            duracion,
            12,
            "La reserva de salas no puede superar 12 horas."
        )

        # Comprobamos que la sala esté disponible.
        self._validar_disponibilidad()

        return True


# ==========================================================
# CLASE ALQUILER DE EQUIPOS
# ==========================================================

class AlquilerEquipos(Servicio):
    """
    Servicio de alquiler de equipos tecnológicos.
    """

    def __init__(
        self,
        identificador,
        nombre,
        precio_unitario,
        tipo_equipo,
        disponible=True
    ):

        # Inicializamos los atributos heredados.
        super().__init__(
            identificador,
            nombre,
            precio_unitario,
            disponible
        )

        # Validamos el tipo de equipo.
        if (
            not isinstance(tipo_equipo, str)
            or not tipo_equipo.strip()
        ):
            raise ValueError(
                "Debe especificar el tipo de equipo."
            )

        # Guardamos el tipo de equipo.
        self._tipo_equipo = tipo_equipo.strip()

        # Registramos el servicio después de validar sus atributos.
        self._registrar_creacion()

    def calcular_costo(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):

        # Validamos los parámetros antes de calcular.
        self.validar_parametros(duracion)

        return self._calcular_total(
            duracion,
            impuesto,
            descuento
        )

    def describir_servicio(self):

        return (
            f"Alquiler de equipo tecnológico: "
            f"{self._tipo_equipo}."
        )

    def validar_parametros(self, duracion):

        # Validamos la duración máxima de 24 horas.
        self._validar_duracion(
            duracion,
            24,
            "El alquiler de equipos no puede superar 24 horas."
        )

        # Comprobamos que el equipo esté disponible.
        self._validar_disponibilidad()

        return True


# ==========================================================
# CLASE ASESORÍA ESPECIALIZADA
# ==========================================================

class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesoría profesional especializada.
    """

    def __init__(
        self,
        identificador,
        nombre,
        precio_unitario,
        especialidad,
        disponible=True
    ):

        # Inicializamos los atributos heredados.
        super().__init__(
            identificador,
            nombre,
            precio_unitario,
            disponible
        )

        # Validamos la especialidad de la asesoría.
        if (
            not isinstance(especialidad, str)
            or not especialidad.strip()
        ):
            raise ValueError(
                "Debe especificar la especialidad de la asesoría."
            )

        # Guardamos la especialidad.
        self._especialidad = especialidad.strip()

        # Registramos el servicio después de validar sus atributos.
        self._registrar_creacion()

    def calcular_costo(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):

        # Validamos los parámetros antes de calcular.
        self.validar_parametros(duracion)

        return self._calcular_total(
            duracion,
            impuesto,
            descuento
        )

    def describir_servicio(self):

        return (
            f"Asesoría profesional en el área de "
            f"{self._especialidad}."
        )

    def validar_parametros(self, duracion):

        # Validamos la duración máxima de 8 horas.
        self._validar_duracion(
            duracion,
            8,
            "La asesoría no puede superar 8 horas."
        )

        # Comprobamos que la asesoría esté disponible.
        self._validar_disponibilidad()

        return True
