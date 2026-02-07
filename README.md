# English IA 🤖

Asistente inteligente de traducción y análisis de inglés impulsado por múltiples modelos de IA. Utiliza una arquitectura de agentes que alterna entre diferentes proveedores de inteligencia artificial (Groq, Cerebras y Google Gemini) para proporcionar respuestas de alta calidad.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Agentes Disponibles](#agentes-disponibles)
- [Desarrollo](#desarrollo)
- [Licencia](#licencia)

## ✨ Características

- **Múltiples Agentes IA**: Alterna automáticamente entre Groq, Cerebras y Google Gemini
- **Interfaz CLI Moderna**: Usa Rich para una presentación visual atractiva
- **Streaming de Respuestas**: Visualización en tiempo real del contenido generado
- **Gestión de Estado**: Guarda el agente actual para usar en próximas consultas
- **Sistema de Prompts Personalizable**: Prompts del sistema configurables para cada consulta
- **Integración con Portapapeles**: Copia automática de resultados con pyperclip

## 🔧 Requisitos

- **Python**: >= 3.10
- **Sistema Operativo**: Windows, macOS, Linux
- **Conexión a Internet**: Requerida para acceder a las APIs de IA

### Dependencias Principales

- `cerebras_cloud_sdk`: SDK para API de Cerebras
- `groq`: Cliente para API de Groq
- `google-genai`: Cliente para Google Gemini
- `python-dotenv`: Gestión de variables de entorno
- `rich`: Visualización de terminal mejorada
- `pyperclip`: Gestión de portapapeles

## 📥 Instalación

### Opción 1: Instalación desde el repositorio (Recomendado)

```bash
# Clonar el repositorio
git clone <URL-del-repositorio>
cd english_ia

# Crear un entorno virtual (opcional pero recomendado)
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt

# Instalar el paquete en modo editable
pip install -e .
```

### Opción 2: Instalación directa

```bash
pip install -r requirements.txt
pip install -e .
```

## ⚙️ Configuración

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con tus claves de API:

```env
# Groq API
GROQ_API_KEY=tu_clave_de_groq_aqui

# Cerebras API
CEREBRAS_API_KEY=tu_clave_de_cerebras_aqui

# Google Gemini API
GOOGLE_API_KEY=tu_clave_de_google_aqui
```

### Obtener Claves de API

- **Groq**: [console.groq.com](https://console.groq.com)
- **Cerebras**: [cerebras.ai](https://cerebras.ai)
- **Google Gemini**: [ai.google.dev](https://ai.google.dev)

### Archivo de Datos (data.json)

El archivo `src/english_ia/data/data.json` almacena el índice del agente actual:

```json
{
    "current_agent": 0
}
```

### Sistema de Prompts (system.txt)

Modifica `src/english_ia/data/system.txt` para personalizar el comportamiento del asistente:

```
Eres un experto en inglés ayudando a usuarios a mejorar sus habilidades...
```

## 📁 Estructura del Proyecto

```
english_ia/
├── README.md                          # Este archivo
├── pyproject.toml                     # Configuración del proyecto Python
├── requirements.txt                   # Dependencias del proyecto
└── src/
    └── english_ia/
        ├── main.py                    # Punto de entrada principal
        ├── utilities.py               # Funciones utilitarias
        ├── __init__.py               # Inicializador del paquete
        ├── agents/                   # Módulo de agentes IA
        │   ├── __init__.py           # Exporta los agentes
        │   ├── groq_client.py        # Cliente y agente de Groq
        │   ├── cerebras_client.py    # Cliente y agente de Cerebras
        │   └── gemini_client.py      # Cliente y agente de Google Gemini
        └── data/                     # Archivos de configuración
            ├── data.json             # Estado del agente actual
            └── system.txt            # Prompt del sistema personalizado
```

### Descripción de Componentes

| Archivo/Carpeta | Descripción |
|---|---|
| `main.py` | Lógica principal de la CLI, manejo de comandos y orquestación de agentes |
| `utilities.py` | Funciones para cargar/guardar data, sistema de prompts y estado |
| `agents/` | Implementación de clientes para los diferentes proveedores de IA |
| `data/` | Archivos de configuración y estado de la aplicación |

## 🚀 Uso

### Comando Básico

```bash
ing "Tu pregunta o texto en inglés aquí"
```

### Ejemplos

```bash
# Traducir texto
ing translate "Hello, how are you?"

# Analizar gramática
ing analyze "She go to school"

# Generar contenido
ing generate "Write a short story about adventure"

# Mejorar redacción
ing improve "i want to go to the store"
```

### Comportamiento de Agentes

La aplicación alterna automáticamente entre los tres agentes:

1. **Primera llamada**: Usa Groq (agente 0)
2. **Segunda llamada**: Usa Cerebras (agente 1)
3. **Tercera llamada**: Usa Google Gemini (agente 2)
4. **Cuarta llamada**: Vuelve a Groq

Esta rotación se guarda en `data.json` para mantener continuidad entre sesiones.

### Opciones Avanzadas

```bash
# Ver agentes disponibles
ing --agents

# Línea de ayuda
ing --help
```

## 🤖 Agentes Disponibles

### Groq
- **Proveedor**: Groq (groq.com)
- **Ventaja**: Rápido y económico
- **Caso de Uso**: Consultas rápidas y análisis básicos

### Cerebras
- **Proveedor**: Cerebras AI
- **Ventaja**: Potente y eficiente
- **Caso de Uso**: Análisis profundos y tareas complejas

### Google Gemini
- **Proveedor**: Google AI Studio
- **Ventaja**: Modelo avanzado con buen contexto
- **Caso de Uso**: Respuestas detalladas y creativas

## 💻 Desarrollo

### Configurar Entorno de Desarrollo

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependencias de desarrollo
pip install -r requirements.txt
pip install -e .
```

### Estructura de un Agente

Cada agente debe implementar la interfaz `generate(question, system)`:

```python
def generate(question: str, system: str):
    """
    Genera una respuesta en chunks
    
    Args:
        question: Pregunta/prompt del usuario
        system: Prompt del sistema
        
    Yields:
        str: Chunks de texto de la respuesta
    """
```

### Agregar un Nuevo Agente

1. Crea un nuevo archivo en `src/english_ia/agents/` (ej: `new_agent.py`)
2. Implementa la función `generate(question, system)`
3. Actualiza `src/english_ia/agents/__init__.py`
4. Agrega el nuevo agente a la lista `agents` en `main.py`

```python
# src/english_ia/agents/new_agent.py
def generate(question: str, system: str):
    # Tu implementación aquí
    yield "Respuesta del nuevo agente"
```

### Ejecutar Código Localmente

```bash
# Desde la raíz del proyecto
python -m english_ia.main "Tu pregunta"

# O directamente
ing "Tu pregunta"
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-feature`)
3. Commit tus cambios (`git commit -m 'Agrega nueva feature'`)
4. Push a la rama (`git push origin feature/nueva-feature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está disponible bajo licencia MIT. Ver archivo `LICENSE` para más detalles.

## 📞 Soporte

Para reportar bugs o solicitar features, abre un issue en el repositorio.

---

**Última actualización**: Febrero 2026
**Versión**: 0.1.0
