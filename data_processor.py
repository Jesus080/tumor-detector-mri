"""
Script para procesar y analizar datos de MRI de tumores cerebrales
"""
import pandas as pd
import numpy as np
import cv2
from skimage import io
import os
import random
import base64
from io import BytesIO
from PIL import Image

class MRIDataProcessor:
    def __init__(self, csv_path, base_path='Brain_MRI'):
        """
        Inicializa el procesador de datos de MRI
        
        Args:
            csv_path: Ruta al archivo CSV con los datos
            base_path: Ruta base donde están las imágenes
        """
        self.base_path = base_path
        self.df = pd.read_csv(csv_path)
        
    def get_statistics(self):
        """
        Obtiene estadísticas del dataset
        
        Returns:
            dict con estadísticas
        """
        total_images = len(self.df)
        with_tumor = self.df[self.df['mask'] == 1].shape[0]
        without_tumor = self.df[self.df['mask'] == 0].shape[0]
        
        return {
            'total': total_images,
            'with_tumor': with_tumor,
            'without_tumor': without_tumor,
            'with_tumor_percent': round((with_tumor / total_images) * 100, 2),
            'without_tumor_percent': round((without_tumor / total_images) * 100, 2)
        }
    
    def get_tumor_samples(self, n_samples=12):
        """
        Obtiene muestras aleatorias de imágenes con tumor
        
        Args:
            n_samples: Número de muestras a obtener
            
        Returns:
            list de diccionarios con información de las muestras
        """
        tumor_df = self.df[self.df['mask'] == 1]
        samples = []
        
        # Obtener índices aleatorios
        if len(tumor_df) < n_samples:
            n_samples = len(tumor_df)
        
        random_indices = random.sample(range(len(tumor_df)), n_samples)
        
        for idx in random_indices:
            row = tumor_df.iloc[idx]
            
            # Construir rutas completas
            image_path = os.path.join(self.base_path, row['image_path'])
            mask_path = os.path.join(self.base_path, row['mask_path'])
            
            if os.path.exists(image_path) and os.path.exists(mask_path):
                samples.append({
                    'patient_id': row['patient_id'],
                    'image_path': image_path,
                    'mask_path': mask_path,
                    'has_tumor': row['mask'] == 1
                })
        
        return samples
    
    def get_mixed_samples(self, n_samples=6):
        """
        Obtiene muestras mezcladas (con y sin tumor)
        
        Args:
            n_samples: Número de muestras de cada tipo
            
        Returns:
            list de diccionarios con información de las muestras
        """
        tumor_df = self.df[self.df['mask'] == 1]
        no_tumor_df = self.df[self.df['mask'] == 0]
        
        samples = []
        
        # Obtener muestras con tumor
        if len(tumor_df) >= n_samples:
            tumor_indices = random.sample(range(len(tumor_df)), n_samples)
            for idx in tumor_indices:
                row = tumor_df.iloc[idx]
                image_path = os.path.join(self.base_path, row['image_path'])
                mask_path = os.path.join(self.base_path, row['mask_path'])
                
                if os.path.exists(image_path) and os.path.exists(mask_path):
                    samples.append({
                        'patient_id': row['patient_id'],
                        'image_path': image_path,
                        'mask_path': mask_path,
                        'has_tumor': True
                    })
        
        # Obtener muestras sin tumor
        if len(no_tumor_df) >= n_samples:
            no_tumor_indices = random.sample(range(len(no_tumor_df)), n_samples)
            for idx in no_tumor_indices:
                row = no_tumor_df.iloc[idx]
                image_path = os.path.join(self.base_path, row['image_path'])
                mask_path = os.path.join(self.base_path, row['mask_path'])
                
                if os.path.exists(image_path) and os.path.exists(mask_path):
                    samples.append({
                        'patient_id': row['patient_id'],
                        'image_path': image_path,
                        'mask_path': mask_path,
                        'has_tumor': False
                    })
        
        return samples
    
    def image_to_base64(self, image_path):
        """
        Convierte una imagen a base64 para mostrarla en HTML
        
        Args:
            image_path: Ruta de la imagen
            
        Returns:
            String base64 de la imagen
        """
        try:
            img = cv2.imread(image_path)
            if img is None:
                return None
            
            # Convertir de BGR a RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Convertir a PIL Image
            pil_img = Image.fromarray(img)
            
            # Guardar en buffer
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            
            # Convertir a base64
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return f"data:image/png;base64,{img_str}"
        except Exception as e:
            print(f"Error convirtiendo imagen {image_path}: {e}")
            return None
    
    def create_overlay_image(self, image_path, mask_path):
        """
        Crea una imagen con la máscara superpuesta en rojo
        
        Args:
            image_path: Ruta de la imagen MRI
            mask_path: Ruta de la máscara
            
        Returns:
            String base64 de la imagen con overlay
        """
        try:
            img = io.imread(image_path)
            mask = io.imread(mask_path)
            
            # Crear copia de la imagen
            overlay = img.copy()
            
            # Aplicar máscara en rojo
            overlay[mask == 255] = (255, 0, 0)
            
            # Convertir a PIL Image
            pil_img = Image.fromarray(overlay.astype('uint8'))
            
            # Guardar en buffer
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            
            # Convertir a base64
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return f"data:image/png;base64,{img_str}"
        except Exception as e:
            print(f"Error creando overlay: {e}")
            return None
    
    def process_samples_for_web(self, samples):
        """
        Procesa muestras para visualización web
        
        Args:
            samples: Lista de muestras
            
        Returns:
            Lista de diccionarios con imágenes en base64
        """
        processed_samples = []
        
        for sample in samples:
            mri_img = self.image_to_base64(sample['image_path'])
            mask_img = self.image_to_base64(sample['mask_path'])
            overlay_img = self.create_overlay_image(sample['image_path'], sample['mask_path'])
            
            if mri_img and mask_img and overlay_img:
                processed_samples.append({
                    'patient_id': sample['patient_id'],
                    'mri_image': mri_img,
                    'mask_image': mask_img,
                    'overlay_image': overlay_img,
                    'has_tumor': sample['has_tumor']
                })
        
        return processed_samples
