# ==========================================================
# EXCEPCIONES PERSONALIZADAS DEL SISTEMA SOFTWARE FJ
# ==========================================================

class ErrorSistema(ValueError):
    """
    Excepción general para los errores controlados
    que pueden presentarse en el sistema Software FJ.
    """
    pass


# ==========================================================
# ERROR RELACIONADO CON LOS CLIENTES
# ==========================================================

class ClienteInvalidoError(ErrorSistema):
    """
    Se genera cuando los datos de un cliente
    no cumplen las condiciones establecidas.
    """
    pass


# ==========================================================
# ERROR RELACIONADO CON LOS SERVICIOS
# ==========================================================

class ServicioNoDisponibleError(ErrorSistema):
    """
    Se genera cuando se intenta utilizar
    un servicio que no está disponible.
    """
    pass


# ==========================================================
# ERROR RELACIONADO CON LAS RESERVAS
# ==========================================================

class ReservaNoValidaError(ErrorSistema):
    """
    Se genera cuando una reserva contiene
    información incorrecta o condiciones inválidas.
    """
    pass


# ==========================================================
# ERROR RELACIONADO CON EL ESTADO DE UNA RESERVA
# ==========================================================

class EstadoReservaError(ErrorSistema):
    """
    Se genera cuando se intenta realizar
    una operación que no corresponde al estado
    actual de una reserva.
    """
    pass
