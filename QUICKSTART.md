# 🚀 INICIO RÁPIDO

## Ejecutar Localmente

### Opción 1: Script Automático
```bash
./start.sh
```

### Opción 2: Manual
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

### Opción 3: Pruebas primero
```bash
# Ejecutar pruebas del sistema
python3 test_system.py

# Si todo pasa, ejecutar aplicación
python app.py
```

## Acceder a la Aplicación

Abre tu navegador en: **http://localhost:5000**

## Deploy en Render

### Paso 1: Subir a GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/TU-USUARIO/tumor-detector-mri.git
git push -u origin main
```

### Paso 2: Conectar en Render
1. Ve a [render.com](https://render.com)
2. New + → Web Service
3. Conecta tu repositorio
4. Configuración:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Click "Create Web Service"

**Guía completa**: Ver `DEPLOYMENT.md`

## 📁 Estructura del Proyecto

```
tumor-detector/
├── app.py                  # ⭐ Aplicación Flask principal
├── data_processor.py       # 🔧 Procesamiento de datos
├── test_system.py          # 🧪 Pruebas del sistema
├── start.sh                # 🚀 Script de inicio
├── requirements.txt        # 📦 Dependencias
├── Brain_MRI/             # 📊 Dataset
│   └── data_mask.csv
├── templates/             # 🎨 HTML
│   └── index.html
└── static/                # 💅 CSS y JS
    ├── css/style.css
    └── js/main.js
```

## 🔍 Endpoints Disponibles

- `/` - Página principal
- `/api/statistics` - Estadísticas en JSON
- `/api/refresh` - Nuevas muestras aleatorias
- `/health` - Health check

## 🎨 Características

✅ Estadísticas del dataset (3929 imágenes)
✅ Gráfico de distribución de tumores
✅ Visualización de 12 casos con tumor
✅ MRI original, máscara y overlay
✅ Diseño responsivo
✅ Actualización dinámica

## ⚡ Comandos Útiles

```bash
# Probar sistema
python3 test_system.py

# Iniciar aplicación
python app.py

# Ver estructura
tree -L 2

# Verificar dependencias
pip list

# Actualizar requirements
pip freeze > requirements.txt
```

## 📞 Troubleshooting

### Error: ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Error: Port already in use
```bash
# Cambiar puerto en app.py o usar:
PORT=8000 python app.py
```

### Error: Dataset no encontrado
```bash
# Verificar que existe:
ls Brain_MRI/data_mask.csv
```

## 🌟 Próximos Pasos

1. ✅ Probar localmente con `python app.py`
2. ✅ Verificar funcionamiento en http://localhost:5000
3. 📤 Subir a GitHub
4. 🚀 Deployar en Render
5. 🎉 Compartir tu proyecto

---

**¿Problemas?** Revisa `DEPLOYMENT.md` o abre un issue en GitHub.
