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
            'total': 3929,
            'with_tumor': 1373,
            'without_tumor': 2556,
            'with_tumor_percent': 34.95,
            'without_tumor_percent': 65.05
        }
        
        # IDs de pacientes reales del dataset (casos reales usados)
        self.patient_ids = [
            'TCGA_DU_7300_19910814', 'TCGA_DU_7306_19930512', 'TCGA_DU_6405_19851005',
            'TCGA_FG_6690_20020226', 'TCGA_DU_A5TU_19980312', 'TCGA_EZ_7264_20010816',
            'TCGA_DU_A5TP_19970614', 'TCGA_DU_7298_19910324', 'TCGA_HT_7879_19981009',
            'TCGA_DU_7309_19960831', 'TCGA_HT_A5RC_19990831', 'TCGA_HT_7602_19951103'
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
