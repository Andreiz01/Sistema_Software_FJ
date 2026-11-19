# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

## 1. Descripción del proyecto

El presente proyecto consiste en el desarrollo de un sistema de software para la empresa ficticia Software FJ, orientado a la gestión integral de clientes, servicios y reservas.

La aplicación está desarrollada utilizando el lenguaje de programación Python y el paradigma de programación orientada a objetos (POO), aplicando conceptos fundamentales como abstracción, herencia, polimorfismo y encapsulamiento.

El sistema permite registrar y validar clientes, administrar diferentes tipos de servicios, gestionar reservas, calcular costos, confirmar y cancelar operaciones. Además, incorpora un sistema de manejo de excepciones personalizadas y un mecanismo de registro de eventos y errores mediante archivos de log.

La información de clientes, servicios y reservas se administra mediante listas internas de Python, sin utilizar bases de datos externas. Los archivos se emplean exclusivamente para almacenar los registros de eventos y errores generados durante la ejecución del sistema.

## 2. Objetivo del proyecto

Desarrollar una aplicación funcional que permita gestionar clientes, servicios y reservas mediante programación orientada a objetos, implementando mecanismos de validación, control de errores, excepciones personalizadas y registro de eventos, con el propósito de garantizar un funcionamiento organizado y confiable.

## 3. Tecnologías utilizadas

- **Lenguaje de programación:** Python 3.13.
- **Entorno de desarrollo:** Visual Studio Code.
- **Paradigma:** Programación orientada a objetos (POO).
- **Control de versiones:** Git.
- **Repositorio remoto:** GitHub.
- **Registro de eventos y errores:** Módulo `logging` de Python.
- **Almacenamiento de información:** Listas internas de Python.
- **Sistema operativo de desarrollo:** Windows.

## 4. Estructura y descripción de los módulos

El proyecto está organizado en diferentes módulos, cada uno con responsabilidades específicas:

### entidades.py

Contiene la clase abstracta `Entidad`, que funciona como clase base para las demás entidades del sistema. Define el identificador y el método abstracto `mostrar_informacion()`, estableciendo una estructura común para las clases derivadas.

### clientes.py

Contiene la clase `Cliente`, encargada de registrar y administrar la información de los clientes. Implementa validaciones para nombres, documentos, correos electrónicos y teléfonos, utilizando atributos privados y propiedades para proteger los datos.

También incorpora mecanismos de control de errores y registro de eventos relacionados con la creación y modificación de la información de los clientes.

### servicios.py

Contiene la clase abstracta `Servicio` y sus tres clases derivadas:

- `ReservaSalas`: administra los servicios de alquiler de salas.
- `AlquilerEquipos`: gestiona el alquiler de equipos tecnológicos.
- `AsesoriaEspecializada`: administra los servicios de asesoría especializada.

Cada clase implementa sus propios métodos para calcular costos, describir el servicio y validar parámetros.

También se incluyen validaciones de precios, disponibilidad, duración, impuestos y descuentos.

### reservas.py

Contiene la clase `Reserva`, encargada de gestionar las reservas realizadas por los clientes. Permite calcular costos, confirmar y cancelar reservas, controlando los diferentes estados de cada operación.

Además, verifica la validez de los clientes, servicios y duración de las reservas, registrando los errores que se presentan durante el proceso.

### excepciones.py

Define las excepciones personalizadas utilizadas para controlar los errores relacionados con clientes, servicios, reservas y estados de las operaciones.

Entre las excepciones implementadas se encuentran:

- `ErrorSistema`.
- `ClienteInvalidoError`.
- `ServicioNoDisponibleError`.
- `ReservaNoValidaError`.
- `EstadoReservaError`.

Estas excepciones permiten identificar y controlar situaciones específicas del sistema.

### registro.py

Implementa el sistema de registro mediante el módulo `logging` de Python. Permite almacenar eventos, errores y excepciones en el archivo `sistema.log`, ubicado dentro de la carpeta `logs`.

El registro utiliza diferentes niveles de información, principalmente `INFO` y `ERROR`, facilitando el seguimiento de las operaciones y la identificación de problemas.

### control_central.py

Contiene la clase `ControlCentral`, encargada de centralizar la administración de clientes, servicios y reservas mediante listas internas.

Permite registrar, buscar, consultar y gestionar las diferentes operaciones, además de controlar registros duplicados y verificar la existencia de los elementos antes de realizar determinadas acciones.

### main.py

Es el archivo principal del proyecto. Ejecuta las demostraciones y pruebas del sistema, incluyendo la abstracción, validación de datos, herencia, polimorfismo, gestión de reservas y manejo de excepciones.

También contiene escenarios de prueba para comprobar el funcionamiento de las operaciones exitosas y los errores controlados.

## 5. Estructura del proyecto

La organización de los archivos y carpetas es la siguiente:

```text
Sistema_Software_FJ/
│
├── main.py
├── entidades.py
├── clientes.py
├── servicios.py
├── reservas.py
├── excepciones.py
├── registro.py
├── control_central.py
├── README.md
├── .gitignore
│
├── pruebas/
│   ├── main_pruebas.py
│   └── prueba_control.py
│
└── logs/
    └── sistema.log
```

**Nota:** La carpeta `logs` y el archivo `sistema.log` se generan y actualizan durante la ejecución del programa. Estos archivos están excluidos del repositorio mediante `.gitignore`, ya que se utilizan para almacenar registros locales.

## 6. Conceptos de programación orientada a objetos implementados

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos:

- **Abstracción:** se implementó mediante las clases abstractas `Entidad` y `Servicio`, estableciendo estructuras y métodos que deben implementar las clases derivadas.

- **Herencia:** las clases `Cliente` y `Servicio` heredan de `Entidad`, mientras que los diferentes tipos de servicios heredan de `Servicio`.

- **Polimorfismo:** se implementa mediante la sobrescritura de métodos en las clases de servicios, permitiendo que cada una tenga su propio comportamiento para calcular costos, describir servicios y validar parámetros.

- **Encapsulamiento:** se utiliza para proteger los atributos de las clases, especialmente en `Cliente`, mediante atributos privados y propiedades que permiten controlar el acceso y la modificación de los datos.

- **Sobrecarga de métodos:** se simula mediante el uso de parámetros opcionales y valores predeterminados, permitiendo utilizar un mismo método con diferentes cantidades de argumentos, de acuerdo con las características de Python.

## 7. Manejo de excepciones y registro de eventos

El sistema incorpora mecanismos para controlar los errores que pueden presentarse durante la ejecución de las operaciones.

Se implementan los siguientes recursos:

- Excepciones personalizadas para clientes, servicios y reservas.
- Bloques `try` y `except` para capturar y controlar errores.
- Bloques `else` para ejecutar instrucciones cuando no se presentan excepciones.
- Bloques `finally` para garantizar la ejecución de instrucciones finales.
- Encadenamiento de excepciones mediante `raise ... from error`, conservando el origen de los errores.
- Registro de eventos y errores mediante el módulo `logging`.

Los registros se almacenan automáticamente en el archivo:

```text
logs/sistema.log
```

Esto permite realizar un seguimiento de las operaciones ejecutadas, identificar errores y conservar información sobre el comportamiento del sistema.

## 8. Pruebas y validaciones realizadas

El sistema incluye pruebas de funcionamiento que permiten comprobar las diferentes operaciones y mecanismos de control implementados.

Entre las principales pruebas realizadas se encuentran:

- Intento de instanciar una clase abstracta.
- Registro de clientes con información válida.
- Validación de correos electrónicos incorrectos.
- Detección de documentos y datos no válidos.
- Control de registros duplicados.
- Creación de diferentes tipos de servicios.
- Validación de precios y parámetros de los servicios.
- Cálculo de costos mediante polimorfismo.
- Búsqueda de clientes y servicios registrados.
- Creación de reservas exitosas.
- Validación de duración y disponibilidad de servicios.
- Confirmación y cancelación de reservas.
- Control de estados de las reservas.
- Manejo de excepciones personalizadas.
- Captura de errores generales mediante bloques `try`, `except`, `else` y `finally`.
- Registro de eventos y errores en el archivo de log.

Las pruebas ejecutadas en el archivo principal permiten demostrar más de diez operaciones simuladas, incluyendo escenarios exitosos y situaciones de error.

Adicionalmente, el proyecto cuenta con archivos de pruebas independientes dentro de la carpeta `pruebas`, utilizados para verificar el funcionamiento de los módulos y del control central.

## 9. Instrucciones para ejecutar el proyecto

Para ejecutar la aplicación se deben seguir los siguientes pasos:

1. Tener instalado Python 3.13 o una versión compatible.
2. Abrir la carpeta `Sistema_Software_FJ` en Visual Studio Code.
3. Abrir una terminal de PowerShell desde el entorno de desarrollo.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

También es posible ejecutar el proyecto utilizando la ruta completa del intérprete de Python instalado en el equipo:

```powershell
& C:\Users\jams2\AppData\Local\Programs\Python\Python313\python.exe d:/perfil/Documents/Sistema_Software_FJ/main.py
```

Al ejecutar el programa, se mostrarán en la terminal las diferentes demostraciones y pruebas del sistema.

Los eventos y errores detectados durante la ejecución se almacenarán automáticamente en:

```text
logs/sistema.log
```

## 10. Control de versiones y archivos excluidos

El proyecto incorpora el archivo `.gitignore`, cuya función es evitar que determinados archivos y carpetas locales sean incluidos en el repositorio de GitHub.

Entre los elementos excluidos se encuentran:

- Archivos temporales de Python, como `__pycache__/`.
- Archivos compilados con extensiones `.pyc` y similares.
- Entornos virtuales como `venv/` y `.venv/`.
- Archivos de registro generados en `logs/*.log`.

De esta manera, el repositorio conserva los archivos fuente, la documentación y las pruebas del proyecto, evitando incluir archivos temporales o registros locales.

## 11. Consideraciones finales

El proyecto Software FJ permite demostrar la aplicación práctica de los principios de programación orientada a objetos en el desarrollo de una solución de gestión de clientes, servicios y reservas.

La separación del código en módulos facilita su organización, mantenimiento y comprensión. Asimismo, la implementación de validaciones, excepciones personalizadas y registros de eventos contribuye a mejorar el control de las operaciones y la identificación de posibles errores.

La utilización de listas internas permite administrar la información sin depender de una base de datos externa, mientras que el sistema de registro facilita el seguimiento de las operaciones y el control de las situaciones inesperadas.

Finalmente, el desarrollo de esta aplicación fortalece los conocimientos sobre programación en Python, diseño de clases, relaciones de herencia, polimorfismo, encapsulamiento y manejo de excepciones, integrando estos conceptos en un proyecto funcional.
