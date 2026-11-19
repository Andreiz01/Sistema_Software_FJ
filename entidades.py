# Importamos ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod


# Creamos la clase abstracta Entidad.
# Esta clase servirá como plantilla para otras clases del sistema.
class Entidad(ABC):

    # Constructor de la clase.
    def __init__(self, identificador):

        # Validamos que el identificador no esté vacío.
        if not str(identificador).strip():
            raise ValueError("El identificador no puede estar vacío.")

        # Guardamos el identificador como atributo protegido.
        self._identificador = str(identificador).strip()

    # Creamos una propiedad para consultar el identificador.
    @property
    def identificador(self):
        return self._identificador

    # Definimos un método abstracto.
    # Las clases hijas deberán implementar este método.
    @abstractmethod
    def mostrar_informacion(self):
        pass
