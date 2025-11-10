"""
Procesador de datos para producción - usa imágenes pre-generadas
"""
import os
import random

class StaticMRIDataProcessor:
    """
    Procesador optimizado para producción que usa imágenes estáticas
    """
    
    def __init__(self):
        """Inicializa el procesador con datos pre-calculados"""
        self.stats = {
            'total': 3064,
            'with_tumor': 1373,
            'without_tumor': 1691,
            'with_tumor_percent': 44.81,
            'without_tumor_percent': 55.19
        }
        
        # IDs de pacientes reales del dataset
        self.patient_ids = [
            'TCGA_CS_4941', 'TCGA_DU_6404', 'TCGA_CS_5395', 'TCGA_DU_7008',
            'TCGA_DU_5872', 'TCGA_CS_6290', 'TCGA_DU_6407', 'TCGA_CS_4942',
            'TCGA_DU_7018', 'TCGA_CS_6188', 'TCGA_DU_5855', 'TCGA_DU_7299'
        ]
    
    def get_statistics(self):
        """
        Retorna estadísticas del dataset
        """
        return self.stats
    
    def get_tumor_samples(self, n_samples=12):
        """
        Retorna rutas a imágenes pre-generadas de tumores
        
        Args:
            n_samples: Número de muestras (siempre retorna 12)
        """
        samples = []
        
        # Usar las 12 imágenes pre-generadas
        for i in range(min(n_samples, 12)):
            samples.append({
                'patient_id': self.patient_ids[i],
                'mri_image': f'/static/images/samples/tumor_mri_{i}.png',
                'mask_image': f'/static/images/samples/tumor_mask_{i}.png',
                'overlay_image': f'/static/images/samples/tumor_overlay_{i}.png',
                'has_tumor': True
            })
        
        return samples
    
    def get_mixed_samples(self, n_samples=3):
        """
        Retorna muestras mixtas pre-generadas
        
        Args:
            n_samples: Número de muestras (máximo 6)
        """
        samples = []
        
        # Primeras 3 imágenes - con tumor
        for i in range(min(n_samples, 3)):
            has_tumor = i < 2  # Primeras 2 con tumor, última sin tumor
            tumor_tag = 'tumor' if has_tumor else 'notumor'
            
            samples.append({
                'patient_id': self.patient_ids[i],
                'mri_image': f'/static/images/samples/mixed_mri_{i}_{tumor_tag}.png',
                'mask_image': f'/static/images/samples/mixed_mask_{i}_{tumor_tag}.png',
                'has_tumor': has_tumor
            })
        
        return samples
    
    def process_samples_for_web(self, samples):
        """
        Procesa muestras para visualización web
        Las imágenes ya están en formato correcto
        
        Args:
            samples: Lista de muestras
        """
        return samples
    
    def refresh_samples(self):
        """
        Simula actualización aleatoria cambiando el orden
        """
        # Reordenar aleatoriamente los IDs de pacientes
        random.shuffle(self.patient_ids)
        return self.get_tumor_samples(12)
