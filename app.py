"""
Aplicación Flask para visualización de análisis de MRI de tumores cerebrales
"""
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Inicializar procesador de datos
# Usar procesador estático para producción (optimizado para Render)
try:
    # Intentar usar datos reales si están disponibles (desarrollo local)
    if os.path.exists('Brain_MRI/data_mask.csv'):
        from data_processor import MRIDataProcessor
        processor = MRIDataProcessor('Brain_MRI/data_mask.csv', 'Brain_MRI')
        print("✓ Usando dataset completo (modo desarrollo)")
    else:
        raise FileNotFoundError("Dataset no disponible")
except:
    # Usar datos pre-generados para producción
    from static_data_processor import StaticMRIDataProcessor
    processor = StaticMRIDataProcessor()
    print("✓ Usando visualizaciones optimizadas (modo producción)")

@app.route('/')
def index():
    """
    Página principal con visualización completa
    """
    # Obtener estadísticas
    stats = processor.get_statistics()
    
    # Obtener muestras de tumores
    tumor_samples = processor.get_tumor_samples(n_samples=12)
    processed_samples = processor.process_samples_for_web(tumor_samples)
    
    # Obtener muestras mixtas para galería adicional
    mixed_samples = processor.get_mixed_samples(n_samples=3)
    processed_mixed = processor.process_samples_for_web(mixed_samples)
    
    return render_template('index.html', 
                         stats=stats, 
                         samples=processed_samples,
                         mixed_samples=processed_mixed)

@app.route('/api/statistics')
def get_statistics():
    """
    Endpoint para obtener estadísticas en formato JSON
    """
    stats = processor.get_statistics()
    return jsonify(stats)

@app.route('/api/refresh')
def refresh_samples():
    """
    Endpoint para obtener nuevas muestras aleatorias
    """
    tumor_samples = processor.get_tumor_samples(n_samples=12)
    processed_samples = processor.process_samples_for_web(tumor_samples)
    
    return jsonify({
        'samples': processed_samples
    })

@app.route('/health')
def health():
    """
    Health check para Render
    """
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    # Para desarrollo local y producción
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False') == 'True'
    app.run(debug=debug, host='0.0.0.0', port=port)
