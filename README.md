# Trabajo Práctico Integrador – Organización Empresarial

# Chatbot para Gestión de Solicitudes de Vacaciones

## Universidad Tecnológica Nacional

### Tecnicatura Universitaria en Programación

**Materia:** Organización Empresarial

**Alumno:** Nayla Benitez

---

# Descripción del Proyecto

Este proyecto fue desarrollado como Trabajo Práctico Integrador para la materia Organización Empresarial.

La solución consiste en un chatbot desarrollado en Python que permite automatizar el proceso de solicitud de vacaciones dentro de una organización.

El sistema consulta una base de datos simulada almacenada en un archivo CSV, valida reglas de negocio previamente definidas y determina automáticamente si una solicitud debe ser aprobada o rechazada.

Además, el proceso fue modelado utilizando BPMN 2.0 para representar gráficamente el flujo de trabajo y las interacciones entre el usuario y el sistema.

---

# Objetivos Académicos

Mediante este proyecto se aplicaron los siguientes conceptos:

- Análisis de procesos organizacionales.
- Modelado BPMN 2.0.
- Automatización de procesos administrativos.
- Definición de reglas de negocio.
- Diseño de flujos conversacionales.
- Gestión mediante máquina de estados.
- Lectura de archivos CSV.
- Manejo de excepciones.
- Validación de datos.
- Documentación técnica y funcional.
- Uso de herramientas de control de versiones.

---

# Proceso Analizado

## Situación Actual (AS-IS)

El empleado solicita vacaciones de manera manual.

El área de Recursos Humanos debe:

- Recibir la solicitud.
- Verificar disponibilidad.
- Analizar la información.
- Comunicar la aprobación o rechazo.

Este proceso genera demoras y aumenta la carga administrativa.

---

## Situación Propuesta (TO-BE)

El chatbot:

1. Solicita el legajo del empleado.
2. Consulta la información almacenada.
3. Solicita la cantidad de días requeridos.
4. Valida las reglas de negocio.
5. Aprueba o rechaza la solicitud.
6. Informa el resultado al usuario.

---

# Reglas de Negocio Implementadas

- El legajo debe existir.
- La cantidad de días solicitados debe ser mayor a cero.
- La cantidad de días solicitados no puede superar el saldo disponible.
- Si todas las validaciones son correctas, la solicitud es aprobada.
- Si alguna validación falla, la solicitud es rechazada.

---

# Funcionalidades Implementadas

## Gestión de Solicitudes

- Consulta de empleados mediante legajo.
- Visualización de días disponibles.
- Solicitud de vacaciones.
- Validación automática.

## Validaciones

- Legajo inexistente.
- Ingreso de valores no numéricos.
- Solicitud de días negativos.
- Solicitud de días iguales a cero.
- Solicitud superior al saldo disponible.

## Automatización

- Aprobación automática.
- Rechazo automático.
- Respuesta inmediata al usuario.

---

# Persistencia de Datos

La información de los empleados se almacena en un archivo CSV.

Campos utilizados:

```csv
Legajo
Nombre
Dias_Disponibles
Email
```

El archivo se utiliza como fuente de datos para las pruebas realizadas durante la simulación.

---

# Máquina de Estados

La conversación fue implementada mediante una máquina de estados simple:

```text
ESPERANDO_LEGAJO
        ↓
ESPERANDO_DIAS
        ↓
APROBADO / RECHAZADO
        ↓
FIN
```

Esta estructura permite controlar el flujo de la conversación y garantizar la ejecución correcta de las validaciones.

---

# Tecnologías Utilizadas

- Python 3
- Módulo csv
- BPMN 2.0
- Draw.io
- Git
- GitHub
- Visual Studio Code

---

# Organización del Proyecto

```text
TPI---Trabajo-Integrador-Chatbot-Organizacion-Empresarial---Benitez-Nayla
│
├── datos
│   ├── empleados.csv
│   └── DIAGRAMA BPMN Benitez Nayla.png
│
├── evidencias
│   └── casos_de_prueba_E2E.xlsx
│
├── src
│   └── chatbot_vacaciones.py
│
└── README.md
```

---

# Casos de Prueba Realizados

Se verificaron los siguientes escenarios:

- Solicitud aprobada.
- Solicitud rechazada por falta de saldo.
- Legajo inexistente.
- Ingreso de texto en lugar de números.
- Solicitud con días negativos.
- Solicitud con días iguales a cero.
- Solicitud utilizando el saldo exacto disponible.

Todos los casos obtuvieron los resultados esperados.

---

# Instrucciones de Ejecución

## Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

## Acceder al proyecto

```bash
cd TPI---Trabajo-Integrador-Chatbot-Organizacion-Empresarial---Benitez-Nayla
```

## Ejecutar el programa

```bash
python src/chatbot_vacaciones.py
```

---

# Aspectos Técnicos Destacados

- Lectura de datos desde archivo CSV.
- Uso de diccionarios para almacenar información.
- Implementación de máquina de estados.
- Validación de entradas mediante try/except.
- Separación entre lógica de negocio y persistencia.
- Aplicación de reglas de negocio definidas durante el análisis del proceso.
- Representación gráfica mediante BPMN 2.0.

---

# Evidencias Incluidas

- Diagrama BPMN.
- Código fuente del chatbot.
- Archivo CSV utilizado como base de datos.
- Casos de prueba E2E.
- Documentación académica del proyecto.

---

# Bibliografía

- BPMN 2.0 Specification.
- Python Software Foundation. Python Documentation.
- Git Documentation.
- GitHub Documentation.
- Material de cátedra de Organización Empresarial.

---

Proyecto desarrollado para la materia Organización Empresarial – Tecnicatura Universitaria en Programación – Universidad Tecnológica Nacional.
