# 🚀 Guía de Deployment en Render

Esta guía te ayudará a deployar tu aplicación de detección de tumores cerebrales en Render.

## 📋 Pre-requisitos

1. Cuenta en [GitHub](https://github.com)
2. Cuenta en [Render](https://render.com) (puedes usar tu cuenta de GitHub)
3. Proyecto listo con todos los archivos necesarios

## 🔧 Paso 1: Preparar el Proyecto

Asegúrate de tener estos archivos en tu proyecto:

- ✅ `app.py` - Aplicación Flask
- ✅ `data_processor.py` - Procesador de datos
- ✅ `requirements.txt` - Dependencias
- ✅ `Procfile` - Comando de inicio
- ✅ `runtime.txt` - Versión de Python
- ✅ `render.yaml` - Configuración de Render
- ✅ `.gitignore` - Archivos a ignorar
- ✅ `README.md` - Documentación
- ✅ Carpetas: `templates/`, `static/`, `Brain_MRI/`

## 📤 Paso 2: Subir a GitHub

### 2.1 Inicializar Git (si no lo has hecho)

```bash
cd /home/jesus/Documentos/plf/Graficacion/MRI/tumor-detector
git init
```

### 2.2 Configurar Git (primera vez)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
```

### 2.3 Crear repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Click en "+" (arriba derecha) → "New repository"
3. Nombre: `tumor-detector-mri`
4. Descripción: "Sistema de Detección de Tumores Cerebrales con MRI"
5. Público o Privado (tu elección)
6. **NO** marques "Initialize with README" (ya tienes uno)
7. Click en "Create repository"

### 2.4 Subir el código

```bash
# Agregar todos los archivos
git add .

# Hacer commit
git commit -m "Initial commit: MRI Tumor Detection System"

# Conectar con GitHub (reemplaza TU-USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU-USUARIO/tumor-detector-mri.git

# Cambiar a rama main
git branch -M main

# Subir el código
git push -u origin main
```

Si te pide autenticación, usa un **Personal Access Token**:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → Marca "repo" → Generate
3. Copia el token y úsalo como contraseña

## 🌐 Paso 3: Deployar en Render

### 3.1 Crear cuenta en Render

1. Ve a [render.com](https://render.com)
2. Click en "Get Started"
3. Elige "Sign up with GitHub"
4. Autoriza Render para acceder a tus repositorios

### 3.2 Crear Web Service

1. En el dashboard de Render, click en "New +" → "Web Service"
2. Conecta tu repositorio:
   - Click en "Connect account" si es necesario
   - Busca `tumor-detector-mri`
   - Click en "Connect"

### 3.3 Configurar el servicio

Render detectará automáticamente el `render.yaml`, pero verifica:

- **Name**: `tumor-detector-mri` (o el que prefieras)
- **Region**: Elige la más cercana (Oregon, Frankfurt, Singapore)
- **Branch**: `main`
- **Root Directory**: (dejar vacío)
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Instance Type**: `Free`

### 3.4 Variables de Entorno (Opcional)

Si necesitas configurar variables:
- Click en "Advanced"
- Add Environment Variable
- Ejemplo: `FLASK_ENV=production`

### 3.5 Deploy

1. Click en "Create Web Service"
2. Render comenzará a:
   - Clonar tu repositorio
   - Instalar dependencias
   - Iniciar la aplicación
3. **Espera 5-10 minutos** (primera vez es más lento)

### 3.6 Ver tu aplicación

Una vez completado:
- Verás "Live" en verde
- Tu URL será: `https://tumor-detector-mri.onrender.com`
- Click en la URL para ver tu aplicación

## ✅ Verificación

Prueba estas rutas:
- `https://tu-app.onrender.com/` - Página principal
- `https://tu-app.onrender.com/health` - Health check
- `https://tu-app.onrender.com/api/statistics` - API de estadísticas

## 🔄 Actualizaciones Futuras

Cada vez que hagas cambios:

```bash
# Hacer cambios en tu código
# ...

# Guardar cambios
git add .
git commit -m "Descripción de los cambios"
git push

# Render detectará automáticamente y re-deployará
```

## ⚠️ Consideraciones Importantes

### Free Tier de Render

- ✅ **Gratis** para siempre
- ⚠️ Se apaga después de **15 minutos de inactividad**
- ⏱️ Tarda **30-60 segundos** en despertar
- 💾 **512MB RAM**
- 🌐 **750 horas/mes** de uso

### Limitaciones del Dataset

Si tu carpeta `Brain_MRI/` es muy grande (>500MB):

**Opción 1**: Reducir el dataset
```bash
# Mantén solo una muestra representativa
# Por ejemplo, 100 imágenes con tumor y 100 sin tumor
```

**Opción 2**: Usar almacenamiento externo
- Subir imágenes a **AWS S3**, **Google Cloud Storage**, o **Cloudinary**
- Modificar `data_processor.py` para cargar desde URL

**Opción 3**: Upgrade a plan de pago
- Render Starter: $7/mes
- Más RAM y almacenamiento

## 🐛 Troubleshooting

### Error: "Build failed"

Verifica `requirements.txt`:
```bash
# Probar localmente
pip install -r requirements.txt
```

### Error: "Application failed to respond"

Verifica que `app.py` tenga:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

### Error: "Module not found"

Asegúrate de que todas las dependencias estén en `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### La aplicación es lenta

- Reduce el número de muestras en `app.py`
- Optimiza el tamaño de las imágenes
- Considera usar caché

## 📊 Monitoreo

En Render puedes ver:
- **Logs**: Click en "Logs" para ver errores
- **Metrics**: CPU, RAM, requests
- **Events**: Historial de deployments

## 🔒 Seguridad

Para producción:
- No expongas rutas sensibles
- Usa HTTPS (Render lo proporciona automáticamente)
- Considera autenticación si es necesario

## 💡 Optimizaciones

### Caché de imágenes
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_cached_samples():
    return processor.get_tumor_samples(n_samples=12)
```

### Compresión
```python
from flask_compress import Compress
Compress(app)
```

### Variables de entorno
```python
import os
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

## 🎉 ¡Listo!

Tu aplicación está en línea y accesible desde cualquier lugar del mundo.

### Siguiente paso:
- Comparte tu URL con amigos, profesores o en tu portafolio
- Agrega el link a tu README en GitHub
- Considera añadir más features: autenticación, base de datos, etc.

## 📞 Soporte

- **Documentación de Render**: https://render.com/docs
- **Documentación de Flask**: https://flask.palletsprojects.com/
- **GitHub Issues**: Si encuentras problemas con el código

---

**¡Felicidades por tu deployment!** 🎊
