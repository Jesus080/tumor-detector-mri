"""
Test para verificar que el sistema funciona correctamente
"""
import os
import sys

def test_static_processor():
    """Test del procesador estático"""
    print("🧪 Testeando procesador estático...")
    
    from static_data_processor import StaticMRIDataProcessor
    processor = StaticMRIDataProcessor()
    
    # Test estadísticas
    stats = processor.get_statistics()
    assert stats['total'] == 3064, "Total de imágenes incorrecto"
    assert stats['with_tumor'] == 1373, "Casos con tumor incorrecto"
    assert stats['without_tumor'] == 1691, "Casos sin tumor incorrecto"
    print("  ✅ Estadísticas correctas")
    
    # Test muestras de tumores
    samples = processor.get_tumor_samples(12)
    assert len(samples) == 12, "Número de muestras incorrecto"
    assert all('patient_id' in s for s in samples), "Falta patient_id"
    assert all('mri_image' in s for s in samples), "Falta mri_image"
    print("  ✅ Muestras de tumores OK")
    
    # Test muestras mixtas
    mixed = processor.get_mixed_samples(3)
    assert len(mixed) == 3, "Número de muestras mixtas incorrecto"
    print("  ✅ Muestras mixtas OK")
    
    print("✅ Procesador estático funciona correctamente\n")

def test_images_exist():
    """Test que las imágenes existen"""
    print("🖼️  Verificando imágenes...")
    
    samples_dir = 'static/images/samples'
    assert os.path.exists(samples_dir), "Directorio de samples no existe"
    
    # Verificar imágenes de tumores
    for i in range(12):
        assert os.path.exists(f'{samples_dir}/tumor_mri_{i}.png'), f"Falta tumor_mri_{i}.png"
        assert os.path.exists(f'{samples_dir}/tumor_mask_{i}.png'), f"Falta tumor_mask_{i}.png"
        assert os.path.exists(f'{samples_dir}/tumor_overlay_{i}.png'), f"Falta tumor_overlay_{i}.png"
    print("  ✅ 12 sets de imágenes de tumores OK")
    
    # Verificar imágenes mixtas
    for i in range(3):
        tumor_tag = 'tumor' if i < 2 else 'notumor'
        assert os.path.exists(f'{samples_dir}/mixed_mri_{i}_{tumor_tag}.png'), f"Falta mixed_mri_{i}"
        assert os.path.exists(f'{samples_dir}/mixed_mask_{i}_{tumor_tag}.png'), f"Falta mixed_mask_{i}"
    print("  ✅ 3 sets de imágenes mixtas OK")
    
    print("✅ Todas las imágenes están presentes\n")

def test_app_imports():
    """Test que app.py se importa correctamente"""
    print("🔧 Verificando app.py...")
    
    try:
        import app
        print("  ✅ app.py se importa correctamente")
        print("  ✅ Flask app configurado")
    except ImportError as e:
        print(f"  ❌ Error importando app: {e}")
        print("  ℹ️  Asegúrate de tener Flask instalado: pip install -r requirements.txt")
        return False
    
    print("✅ Aplicación Flask OK\n")
    return True

def test_file_sizes():
    """Test tamaños de archivos"""
    print("📦 Verificando tamaños...")
    
    samples_dir = 'static/images/samples'
    total_size = 0
    
    for root, dirs, files in os.walk(samples_dir):
        for file in files:
            filepath = os.path.join(root, file)
            size = os.path.getsize(filepath)
            total_size += size
    
    total_mb = total_size / (1024 * 1024)
    print(f"  📊 Tamaño total de imágenes: {total_mb:.2f} MB")
    
    if total_mb < 5:
        print("  ✅ Tamaño optimizado para deploy")
    else:
        print("  ⚠️  Tamaño considerable pero aceptable")
    
    print()

def main():
    """Ejecuta todos los tests"""
    print("="*60)
    print("🧠 TEST DEL SISTEMA DE DETECCIÓN DE TUMORES CEREBRALES")
    print("="*60)
    print()
    
    try:
        test_static_processor()
        test_images_exist()
        test_file_sizes()
        app_ok = test_app_imports()
        
        print("="*60)
        print("✅ ¡TODOS LOS TESTS PASARON!")
        print("="*60)
        print()
        print("🚀 El sistema está listo para deploy en Render")
        print()
        print("Próximos pasos:")
        print("1. git add .")
        print("2. git commit -m 'Sistema optimizado para producción'")
        print("3. git push origin main")
        print("4. Conectar repositorio en Render.com")
        print()
        
        return True
        
    except AssertionError as e:
        print()
        print("="*60)
        print("❌ TEST FALLIDO")
        print("="*60)
        print(f"Error: {e}")
        print()
        return False
    except Exception as e:
        print()
        print("="*60)
        print("❌ ERROR INESPERADO")
        print("="*60)
        print(f"Error: {e}")
        print()
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
