"""
Script de prueba para verificar que todo funciona correctamente
"""
import os
import sys

def test_imports():
    """Verifica que todas las librerías necesarias estén instaladas"""
    print("🔍 Verificando imports...")
    try:
        import pandas
        print("✅ pandas")
        import numpy
        print("✅ numpy")
        import cv2
        print("✅ opencv")
        import flask
        print("✅ flask")
        from skimage import io
        print("✅ scikit-image")
        from PIL import Image
        print("✅ Pillow")
        return True
    except ImportError as e:
        print(f"❌ Error: {e}")
        return False

def test_files():
    """Verifica que los archivos necesarios existan"""
    print("\n📁 Verificando archivos y carpetas...")
    files = [
        'app.py',
        'data_processor.py',
        'requirements.txt',
        'Brain_MRI/data_mask.csv',
        'templates/index.html',
        'static/css/style.css',
        'static/js/main.js'
    ]
    
    all_exist = True
    for file in files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - NO ENCONTRADO")
            all_exist = False
    
    return all_exist

def test_data():
    """Verifica que los datos se puedan cargar"""
    print("\n📊 Verificando datos...")
    try:
        import pandas as pd
        df = pd.read_csv('Brain_MRI/data_mask.csv')
        print(f"✅ CSV cargado: {len(df)} registros")
        print(f"✅ Con tumor: {df[df['mask'] == 1].shape[0]}")
        print(f"✅ Sin tumor: {df[df['mask'] == 0].shape[0]}")
        return True
    except Exception as e:
        print(f"❌ Error cargando datos: {e}")
        return False

def test_processor():
    """Verifica que el procesador de datos funcione"""
    print("\n🔧 Verificando procesador de datos...")
    try:
        from data_processor import MRIDataProcessor
        processor = MRIDataProcessor('Brain_MRI/data_mask.csv', 'Brain_MRI')
        
        stats = processor.get_statistics()
        print(f"✅ Estadísticas obtenidas:")
        print(f"   - Total: {stats['total']}")
        print(f"   - Con tumor: {stats['with_tumor']} ({stats['with_tumor_percent']}%)")
        print(f"   - Sin tumor: {stats['without_tumor']} ({stats['without_tumor_percent']}%)")
        
        return True
    except Exception as e:
        print(f"❌ Error en procesador: {e}")
        return False

def main():
    """Ejecuta todas las pruebas"""
    print("=" * 60)
    print("🧪 PRUEBAS DEL SISTEMA DE DETECCIÓN DE TUMORES")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Archivos", test_files),
        ("Datos", test_data),
        ("Procesador", test_processor)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Error en prueba {name}: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 60)
    print("📋 RESUMEN DE PRUEBAS")
    print("=" * 60)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    all_passed = all(result for _, result in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ¡TODAS LAS PRUEBAS PASARON!")
        print("✅ El sistema está listo para ejecutarse")
        print("\nPuedes iniciar la aplicación con:")
        print("  python app.py")
        print("o")
        print("  ./start.sh")
    else:
        print("⚠️  ALGUNAS PRUEBAS FALLARON")
        print("❌ Revisa los errores antes de continuar")
        sys.exit(1)
    print("=" * 60)

if __name__ == '__main__':
    main()
