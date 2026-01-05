# 🌿 NaturIA Chile

Aplicación web educativa que identifica la biodiversidad chilena usando Inteligencia Artificial (Google Gemini).

**🌐 Acceso en Vivo: [https://naturia.duckdns.org](https://naturia.duckdns.org)**

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-orange.svg)
![PWA](https://img.shields.io/badge/PWA-Ready-success.svg)
![SSL](https://img.shields.io/badge/SSL-Encrypted-brightgreen.svg)

## 🎯 Características

- 🐛 **Identificación Multiespecie**: Reconoce insectos, plantas, aves y animales silvestres nativos de Chile.
- 👤 **Perfiles de Usuario**: Crea tu cuenta para guardar progresos y personalizar tu experiencia.
- 📔 **Mi Naturadex**: Colección personal de todos los descubrimientos realizados.
- 🔊 **Canto y Sonidos**: Escucha los sonidos de aves e insectos (Integración con Xeno-Canto y Wikimedia).
- 🗺️ **Mapa de Distribución**: Visualiza en qué regiones de Chile habita cada especie.
- 🎤 **Búsqueda por Voz**: Usa el micrófono para buscar especies rápidamente.
- 🎮 **Sistema de Puntos Premium**: Gana puntos y sube de rango (desde Novato hasta Maestro).
- 🌙 **Modo Oscuro**: Diseño adaptable para una mejor visualización.
- 📱 **PWA (Progressive Web App)**: Instálala en tu móvil para un acceso rápido y uso optimizado.
- ⚠️ **Indicador de Peligrosidad**: Información clara sobre si la especie representa un riesgo.

## 🚀 Instalación

### Requisitos Previos

- Python 3.9 o superior
- Una API Key de Google Gemini ([obtener aquí](https://aistudio.google.com/app/apikey))

### Pasos

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/j-alexander-acosta/NaturIA-Chile.git
   cd NaturIA-Chile
   ```

2. **Crea el entorno virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la API Key**
   ```bash
   cp .env.example .env
   # Edita .env y agrega tu GOOGLE_API_KEY
   ```

5. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

6. **Abre en el navegador**
   ```
   http://127.0.0.1:5001
   ```

## 📁 Estructura del Proyecto

```
NaturIA-Chile/
├── static/
│   ├── css/
│   │   └── styles.css          # Diseño moderno, animaciones y modo oscuro
│   └── js/
│       └── app.js              # Lógica principal, PWA, Mapa y Sonidos
├── templates/
│   └── index.html              # Interfaz de usuario (Jinja2)
├── utils/
│   ├── gemini_client.py        # Integración con Google Gemini AI
│   ├── sound_search.py         # Búsqueda de sonidos (Xeno-Canto/Wikimedia)
│   └── image_search.py         # Cliente para imágenes de Wikipedia
├── .env.example                # Plantilla de variables de entorno
├── app.py                      # Servidor Flask y API Endpoints
└── requirements.txt            # Dependencias del sistema
```

## 🔧 Tecnologías

- **IA**: Google Gemini 1.5 Flash / 2.0 Flash
- **Backend**: Flask (Python)
- **APIs**: Xeno-Canto (Sonidos), Wikimedia Commons (Imágenes/Audio)
- **Frontend**: CSS Grid/Flexbox, Vanilla JS, Web Speech API
- **Almacenamiento**: LocalStorage para historial y puntos

## 🤝 Contribuir

Las contribuciones son bienvenidas:
1. Haz fork del repositorio
2. Crea una rama (`git checkout -b feature/nueva-mejora`)
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-mejora`)
5. Abre un Pull Request

## 📄 Licencia

© 2026 NaturIA Chile. Todos los derechos reservados. Desarrollado por **J. Alexander Acosta Z.**

---
*Desarrollado con 🌿 para los exploradores del mañana.*
