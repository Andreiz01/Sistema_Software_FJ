# Importamos logging para registrar eventos y errores.
import logging

# Importamos os para trabajar con las rutas del sistema.
import os


# =====================================================
# CONFIGURACIÓN DEL REGISTRO
# =====================================================

# Obtenemos la carpeta donde se encuentra este archivo.
CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))

# Construimos la ruta de la carpeta logs.
CARPETA_LOGS = os.path.join(CARPETA_PROYECTO, "logs")

# Creamos la carpeta logs si todavía no existe.
os.makedirs(CARPETA_LOGS, exist_ok=True)

# Definimos el nombre y la ubicación del archivo de registro.
ARCHIVO_LOG = os.path.join(CARPETA_LOGS, "sistema.log")


# Configuramos el sistema de registro.
logging.basicConfig(
    filename=ARCHIVO_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8"
)

# Creamos un registrador para utilizarlo en otros archivos.
logger = logging.getLogger("SoftwareFJ")


# =====================================================
# FUNCIONES PARA REGISTRAR EVENTOS
# =====================================================

def registrar_evento(mensaje):
    """Registra una operación importante del sistema."""
    logger.info(mensaje)


def registrar_error(mensaje):
    """Registra un error ocurrido durante una operación."""
    logger.error(mensaje)


def registrar_excepcion(mensaje):
    """Registra un error junto con sus detalles técnicos."""
    logger.exception(mensaje)
