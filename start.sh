#!/bin/bash

echo "🧠 Iniciando Sistema de Detección de Tumores Cerebrales..."
echo "=================================================="
echo ""

# Verificar Python
echo "📌 Verificando Python..."
python3 --version

# Verificar pip
echo ""
echo "📌 Verificando pip..."
pip3 --version

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo ""
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo ""
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# Verificar estructura de archivos
echo ""
echo "📁 Verificando estructura del proyecto..."

# Verificar si hay dataset completo (modo desarrollo) o imágenes estáticas (modo producción)
if [ -f "Brain_MRI/data_mask.csv" ]; then
    echo "✅ Dataset completo encontrado (modo desarrollo)"
elif [ -d "static/images/samples" ]; then
    echo "✅ Imágenes optimizadas encontradas (modo producción)"
else
    echo "❌ ERROR: No se encontraron datos de MRI"
    exit 1
fi

if [ -d "templates" ]; then
    echo "✅ Carpeta templates encontrada"
else
    echo "❌ ERROR: No se encontró la carpeta templates"
    exit 1
fi

if [ -d "static" ]; then
    echo "✅ Carpeta static encontrada"
else
    echo "❌ ERROR: No se encontró la carpeta static"
    exit 1
fi

echo ""
echo "=================================================="
echo "✅ ¡Todo listo! Iniciando servidor Flask..."
echo "=================================================="
echo ""
echo "🌐 Accede a la aplicación en: http://localhost:5000"
echo "⏹️  Para detener: Ctrl+C"
echo ""

# Iniciar aplicación
python app.py
