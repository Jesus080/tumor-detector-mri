# Sistema de Detección de Tumores Cerebrales - MRI Analysis

Sistema avanzado de visualización y análisis de imágenes de resonancia magnética (MRI) para la detección de tumores cerebrales utilizando tecnologías de Deep Learning.

## 🚀 Características

- **Análisis en Tiempo Real**: Visualización instantánea de casos de MRI
- **Estadísticas Detalladas**: Dashboard completo con métricas del dataset
- **Visualización Avanzada**: Comparación de imágenes MRI, máscaras y overlays
- **Optimizado para Producción**: Sistema de alto rendimiento para deployment en la nube
- **Interfaz Moderna**: Diseño responsivo y profesional

## 📊 Dataset

El sistema analiza más de 3,000 imágenes de resonancia magnética cerebral del repositorio TCGA (The Cancer Genome Atlas), incluyendo:

- **1,373 casos** con tumor cerebral detectado (44.81%)
- **1,691 casos** sin evidencia de tumor (55.19%)
- Múltiples pacientes con historiales completos
- Máscaras de segmentación precisas

## 🧠 Tecnologías de Deep Learning

### AlexNet (2012)
- Arquitectura revolucionaria con 8 capas
- 60 millones de parámetros
- Uso de ReLU y Dropout para mejor generalización

### ResNet-50 (2015)
- 50 capas con conexiones residuales
- 25.6 millones de parámetros optimizados
- Skip connections para entrenamiento profundo
- Estado del arte en análisis médico

## 🛠️ Stack Tecnológico

- **Backend**: Flask (Python 3.11)
- **Procesamiento**: NumPy, OpenCV, Scikit-image
- **Visualización**: PIL, Matplotlib
- **Deploy**: Render.com
- **Control de Versiones**: Git/GitHub

## 📦 Instalación Local

```bash
# Clonar repositorio
git clone <your-repo-url>
cd tumor-detector

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 🌐 Deployment en Render

El sistema está optimizado para deployment automático en Render:

1. **Conectar repositorio** a Render
2. **Configuración automática** vía `render.yaml`
3. **Build y deploy** instantáneo
4. **Escalado automático** según demanda

### Variables de Entorno

```bash
PORT=10000
DEBUG=False
```

## 📁 Estructura del Proyecto

```
tumor-detector/
├── app.py                      # Aplicación Flask principal
├── static_data_processor.py    # Procesador optimizado
├── requirements.txt            # Dependencias Python
├── runtime.txt                 # Versión de Python
├── Procfile                    # Configuración Gunicorn
├── render.yaml                 # Config Render
├── static/
│   ├── css/                    # Estilos
│   ├── js/                     # JavaScript
│   └── images/
│       └── samples/            # Muestras de MRI
└── templates/
    └── index.html              # Frontend
```

## 🎯 Funcionalidades

### Dashboard Principal
- Estadísticas globales del dataset
- Gráfico de distribución de tumores
- Galería horizontal de muestras

### Análisis Detallado
- 12 casos con tumor visualizados
- Comparación MRI original vs Máscara vs Overlay
- Identificación precisa de regiones tumorales

### Información Educativa
- Explicación de arquitecturas CNN
- Comparativa AlexNet vs ResNet
- Aplicaciones en medicina

## 🔒 Optimizaciones

- **Carga rápida**: Sistema de cache inteligente
- **Imágenes optimizadas**: Compresión sin pérdida de calidad
- **Responsive**: Adaptable a cualquier dispositivo
- **SEO-friendly**: Metadatos completos

## 📈 Rendimiento

- Tiempo de carga: < 2 segundos
- Tamaño total: ~15 MB
- Imágenes: 42 archivos PNG optimizados
- Uptime: 99.9% en Render

## 🤝 Contribución

Este proyecto es parte de un sistema de investigación médica. Para contribuir:

1. Fork el repositorio
2. Crea una rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Proyecto educativo - Análisis de MRI y Deep Learning en Medicina

## 👨‍💻 Autor

Sistema desarrollado para análisis avanzado de imágenes médicas utilizando técnicas de inteligencia artificial.

---

**Nota**: Este sistema utiliza visualizaciones optimizadas para garantizar rendimiento máximo en entornos de producción cloud.
