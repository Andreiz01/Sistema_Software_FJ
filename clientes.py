# Importamos la clase Entidad para utilizar la herencia.
from entidades import Entidad

# Importamos re para validar el correo electrónico.
import re

# Importamos las funciones para registrar eventos y errores.
from registro import registrar_evento, registrar_error

# Importamos la excepción personalizada para clientes.
from excepciones import ClienteInvalidoError


# ==========================================================
# CLASE CLIENTE
# ==========================================================

# Cliente hereda de la clase abstracta Entidad.
class Cliente(Entidad):

    # ------------------------------------------------------
    # CONSTRUCTOR
    # ------------------------------------------------------

    def __init__(
        self,
        identificador,
        nombre,
        documento,
        correo,
        telefono
    ):

        # Inicializamos los atributos heredados.
        super().__init__(identificador)

        # Asignamos los datos mediante sus propiedades.
        # Las propiedades ejecutan las validaciones correspondientes.
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

        # Registramos la creación exitosa del cliente.
        registrar_evento(
            f"Cliente registrado correctamente: {self.identificador}"
        )

    # ======================================================
    # MÉTODOS DE VALIDACIÓN
    # ======================================================

    # ------------------------------------------------------
    # VALIDAR NOMBRE
    # ------------------------------------------------------

    @staticmethod
    def validar_nombre(nombre):

        # Comprobamos que sea una cadena y no esté vacía.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        # Evitamos que el nombre contenga números.
        if any(caracter.isdigit() for caracter in nombre):
            raise ValueError(
                "El nombre no debe contener números."
            )

        return nombre.strip()

    # ------------------------------------------------------
    # VALIDAR DOCUMENTO
    # ------------------------------------------------------

    @staticmethod
    def validar_documento(documento):

        # Convertimos el documento a texto.
        documento = str(documento).strip()

        # Comprobamos que contenga solamente números.
        if not documento.isdigit():
            raise ValueError(
                "El documento debe contener solamente números."
            )

        # Comprobamos que tenga entre 5 y 15 dígitos.
        if not 5 <= len(documento) <= 15:
            raise ValueError(
                "El documento debe tener entre 5 y 15 dígitos."
            )

        return documento

    # ------------------------------------------------------
    # VALIDAR CORREO ELECTRÓNICO
    # ------------------------------------------------------

    @staticmethod
    def validar_correo(correo):

        # Comprobamos que el correo sea una cadena de texto.
        if not isinstance(correo, str) or not correo.strip():
            raise ValueError(
                "El correo electrónico no puede estar vacío."
            )

        # Expresión regular para validar el formato del correo.
        # Exige un usuario, el símbolo @, un dominio y una extensión.
        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        # Comprobamos que el correo cumpla con el formato establecido.
        if not re.fullmatch(patron, correo.strip()):
            raise ValueError(
                "El correo electrónico no tiene un formato válido."
            )

        # Retornamos el correo sin espacios y en minúsculas.
        return correo.strip().lower()

    # ------------------------------------------------------
    # VALIDAR TELÉFONO
    # ------------------------------------------------------

    @staticmethod
    def validar_telefono(telefono):

        # Convertimos el teléfono a texto.
        telefono = str(telefono).strip()

        # Comprobamos que contenga solamente números.
        if not telefono.isdigit():
            raise ValueError(
                "El teléfono debe contener solamente números."
            )

        # Comprobamos que tenga entre 7 y 15 dígitos.
        if not 7 <= len(telefono) <= 15:
            raise ValueError(
                "El teléfono debe tener entre 7 y 15 dígitos."
            )

        return telefono

    # ======================================================
    # PROPIEDADES Y ENCAPSULAMIENTO
    # ======================================================

    # ------------------------------------------------------
    # PROPIEDAD NOMBRE
    # ------------------------------------------------------

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        try:
            self.__nombre = self.validar_nombre(valor)

        except ValueError as error:

            # Registramos el error detectado.
            registrar_error(
                f"Error al validar el nombre del cliente: {error}"
            )

            # Generamos la excepción personalizada.
            raise ClienteInvalidoError(
                f"Nombre del cliente inválido: {error}"
            ) from error

    # ------------------------------------------------------
    # PROPIEDAD DOCUMENTO
    # ------------------------------------------------------

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):

        try:
            self.__documento = self.validar_documento(valor)

        except ValueError as error:

            # Registramos el error detectado.
            registrar_error(
                f"Error al validar el documento del cliente: {error}"
            )

            # Generamos la excepción personalizada.
            raise ClienteInvalidoError(
                f"Documento del cliente inválido: {error}"
            ) from error

    # ------------------------------------------------------
    # PROPIEDAD CORREO
    # ------------------------------------------------------

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        try:
            self.__correo = self.validar_correo(valor)

        except ValueError as error:

            # Registramos el error detectado.
            registrar_error(
                f"Error al validar el correo del cliente: {error}"
            )

            # Generamos la excepción personalizada.
            raise ClienteInvalidoError(
                f"Correo del cliente inválido: {error}"
            ) from error

    # ------------------------------------------------------
    # PROPIEDAD TELÉFONO
    # ------------------------------------------------------

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        try:
            self.__telefono = self.validar_telefono(valor)

        except ValueError as error:

            # Registramos el error detectado.
            registrar_error(
                f"Error al validar el teléfono del cliente: {error}"
            )

            # Generamos la excepción personalizada.
            raise ClienteInvalidoError(
                f"Teléfono del cliente inválido: {error}"
            ) from error

    # ======================================================
    # MÉTODO HEREDADO DE ENTIDAD
    # ======================================================

    # Implementamos el método abstracto de la clase Entidad.
    def mostrar_informacion(self):

        return (
            f"Identificador: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )
