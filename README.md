# 🧠 Sistema de Detección de Tumores Cerebrales con MRI

Aplicación web desarrollada con Flask para la visualización y análisis de imágenes de resonancia magnética (MRI) cerebral, enfocada en la detección de tumores.

## 🌟 Características

- **Análisis Estadístico**: Visualización de estadísticas del dataset (total de imágenes, con/sin tumor)
- **Gráficos Interactivos**: Distribución visual de casos mediante gráficos de barras
- **Galería de Muestras**: Visualización de imágenes MRI, máscaras y superposiciones
- **Análisis Detallado**: Casos específicos con visualización de MRI original, máscara y tumor identificado
- **Diseño Responsivo**: Interfaz moderna y adaptable a diferentes dispositivos
- **Actualización Dinámica**: Botón para refrescar el análisis con nuevas muestras aleatorias

## 🚀 Tecnologías

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Procesamiento de Imágenes**: OpenCV, scikit-image, Pillow
- **Análisis de Datos**: Pandas, NumPy
- **Deployment**: Render

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🛠️ Instalación Local

1. **Clonar el repositorio**:
```bash
git clone https://github.com/tu-usuario/tumor-detector.git
cd tumor-detector
```

2. **Crear entorno virtual**:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

4. **Verificar estructura de datos**:
Asegúrate de tener el archivo `Brain_MRI/data_mask.csv` y las imágenes en la carpeta correspondiente.

5. **Ejecutar la aplicación**:
```bash
python app.py
```

6. **Abrir en el navegador**:
```
http://localhost:5000
```

## 📁 Estructura del Proyecto

```
tumor-detector/
├── app.py                      # Aplicación Flask principal
├── data_processor.py           # Procesamiento de datos e imágenes
├── requirements.txt            # Dependencias del proyecto
├── .gitignore                 # Archivos a ignorar en Git
├── README.md                  # Documentación
├── Brain_MRI/                 # Dataset de imágenes
│   ├── data_mask.csv         # Metadata del dataset
│   └── TCGA_*/               # Carpetas con imágenes MRI
├── templates/                 # Plantillas HTML
│   └── index.html            # Página principal
└── static/                    # Archivos estáticos
    ├── css/
    │   └── style.css         # Estilos CSS
    └── js/
        └── main.js           # JavaScript para interactividad

```

## 🌐 Deployment en Render

### Opción 1: Deployment Automático desde GitHub

1. **Subir el proyecto a GitHub**:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/tu-usuario/tumor-detector.git
git push -u origin main
```

2. **Conectar con Render**:
   - Ve a [Render.com](https://render.com)
   - Crea una cuenta o inicia sesión
   - Click en "New +" → "Web Service"
   - Conecta tu repositorio de GitHub
   - Selecciona el repositorio `tumor-detector`

3. **Configurar el servicio**:
   - **Name**: `tumor-detector-mri`
   - **Region**: Elige la más cercana
   - **Branch**: `main`
   - **Root Directory**: (dejar vacío)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free`

4. **Variables de entorno** (si es necesario):
   - Añade variables en la sección "Environment Variables"

5. **Deploy**:
   - Click en "Create Web Service"
   - Espera a que se complete el deployment (5-10 minutos)

### Opción 2: Deployment Manual

Crea un archivo `render.yaml` en la raíz del proyecto y sube el código.

## 🎨 Características de la Interfaz

- **Header**: Título de la aplicación con botón de actualización
- **Estadísticas**: Tarjetas con métricas clave del dataset
- **Gráfico de Barras**: Visualización de distribución de tumores
- **Galería de Muestras**: Grid con ejemplos del dataset
- **Análisis Detallado**: 12 casos con MRI, máscara y overlay
- **Footer**: Información del proyecto

## 🔧 Configuración

### Modificar el número de muestras

En `app.py`, puedes ajustar el número de muestras:

```python
tumor_samples = processor.get_tumor_samples(n_samples=12)  # Cambiar 12 por el número deseado
mixed_samples = processor.get_mixed_samples(n_samples=3)   # Cambiar 3 por el número deseado
```

### Personalizar estilos

Edita `static/css/style.css` para modificar colores, fuentes y diseño.

## 📊 Dataset

El proyecto utiliza el dataset TCGA de imágenes MRI cerebrales:
- **Total de imágenes**: 3929
- **Con tumor**: 1373 (34.95%)
- **Sin tumor**: 2556 (65.05%)

## 🤝 Contribuir

Las contribuciones son bienvenidas:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 👨‍💻 Autor

Desarrollado como proyecto de Healthcare AI y Deep Learning.

## 🙏 Agradecimientos

- Dataset TCGA (The Cancer Genome Atlas)
- Comunidad de Machine Learning y Healthcare AI

## 📞 Contacto

Para preguntas o sugerencias, abre un issue en el repositorio.

---

⭐ Si te gusta este proyecto, dale una estrella en GitHub!
