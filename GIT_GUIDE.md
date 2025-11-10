# 📤 Guía de Git y GitHub

## 🚀 Comandos para Subir tu Proyecto a GitHub

### Paso 1: Inicializar Git (si no lo has hecho)

```bash
cd /home/jesus/Documentos/plf/Graficacion/MRI/tumor-detector
git init
```

### Paso 2: Configurar Git (primera vez)

```bash
# Configurar tu nombre
git config --global user.name "Tu Nombre"

# Configurar tu email
git config --global user.email "tu-email@example.com"

# Verificar configuración
git config --list
```

### Paso 3: Agregar Archivos

```bash
# Agregar todos los archivos
git add .

# Ver qué archivos se agregarán
git status
```

### Paso 4: Hacer Commit

```bash
git commit -m "Initial commit: Sistema de Detección de Tumores Cerebrales con MRI"
```

### Paso 5: Crear Repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Inicia sesión
3. Click en el botón "+" (arriba derecha)
4. Selecciona "New repository"
5. Configuración:
   - **Repository name**: `tumor-detector-mri`
   - **Description**: `Sistema web de detección de tumores cerebrales mediante análisis de imágenes MRI con Flask y Deep Learning`
   - **Public** o **Private** (tu elección)
   - **NO** marques "Add a README file" (ya tienes uno)
   - **NO** marques "Add .gitignore" (ya tienes uno)
6. Click en "Create repository"

### Paso 6: Conectar con GitHub

Copia el URL de tu repositorio (ejemplo: `https://github.com/tu-usuario/tumor-detector-mri.git`)

```bash
# Agregar remote (reemplaza TU-USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU-USUARIO/tumor-detector-mri.git

# Verificar remote
git remote -v

# Cambiar a rama main
git branch -M main
```

### Paso 7: Subir el Código

```bash
# Primera vez
git push -u origin main
```

**Nota**: GitHub te pedirá autenticación. Debes usar un **Personal Access Token** en lugar de tu contraseña.

## 🔑 Crear Personal Access Token

### Método 1: Clásico (Recomendado)

1. GitHub → Settings (tu perfil)
2. Developer settings (al final del menú izquierdo)
3. Personal access tokens → Tokens (classic)
4. "Generate new token" → "Generate new token (classic)"
5. Configuración:
   - **Note**: `Tumor Detector MRI`
   - **Expiration**: 90 days (o el que prefieras)
   - **Scopes**: Marca `repo` (completo)
6. Click "Generate token"
7. **¡IMPORTANTE!** Copia el token (no lo volverás a ver)

### Usar el Token

Cuando Git te pida contraseña:
- **Username**: tu usuario de GitHub
- **Password**: pega el Personal Access Token

### Guardar Credenciales (Opcional)

```bash
# Para no escribir el token cada vez
git config --global credential.helper store

# Primera vez que hagas push, ingresa el token
# Se guardará para futuros comandos
```

## 📝 Comandos de Git Comunes

### Ver Estado

```bash
# Ver archivos modificados
git status

# Ver diferencias
git diff

# Ver historial de commits
git log --oneline
```

### Hacer Cambios

```bash
# Después de editar archivos
git add .
git commit -m "Descripción del cambio"
git push
```

### Actualizar desde GitHub

```bash
# Traer cambios desde GitHub
git pull
```

### Ver Ramas

```bash
# Ver ramas locales
git branch

# Crear nueva rama
git checkout -b feature/nueva-funcionalidad

# Cambiar de rama
git checkout main
```

## 🔄 Flujo de Trabajo Típico

```bash
# 1. Hacer cambios en tu código
# (editar archivos)

# 2. Ver qué cambió
git status

# 3. Agregar cambios
git add .

# 4. Hacer commit
git commit -m "Descripción clara del cambio"

# 5. Subir a GitHub
git push
```

## 🎯 Ejemplos de Mensajes de Commit

Buenos mensajes:
```bash
git commit -m "Add: Sistema de caché para imágenes"
git commit -m "Fix: Error en procesamiento de máscaras"
git commit -m "Update: Mejorar diseño responsivo en móviles"
git commit -m "Refactor: Optimizar carga de imágenes"
git commit -m "Docs: Actualizar README con nuevas features"
```

Convenciones:
- **Add**: Nueva funcionalidad
- **Fix**: Corrección de errores
- **Update**: Mejora de funcionalidad existente
- **Refactor**: Cambios en código sin cambiar funcionalidad
- **Docs**: Cambios en documentación
- **Style**: Cambios de formato (CSS, indentación, etc.)

## 🚫 Archivos a NO Subir

El archivo `.gitignore` ya está configurado para ignorar:

```
# Entornos virtuales
venv/
env/

# Cache de Python
__pycache__/
*.pyc

# Archivos del sistema
.DS_Store

# IDEs
.vscode/
.idea/

# Variables de entorno
.env

# Jupyter Notebooks (opcional)
*.ipynb
```

## 📊 Verificar Subida

Después de `git push`, ve a tu repositorio en GitHub:
```
https://github.com/TU-USUARIO/tumor-detector-mri
```

Deberías ver:
- ✅ Todos tus archivos
- ✅ README.md renderizado
- ✅ Commit history

## 🔧 Troubleshooting

### Error: "Permission denied"

Usa Personal Access Token en lugar de contraseña.

### Error: "Repository not found"

Verifica que el remote esté bien configurado:
```bash
git remote -v
git remote remove origin
git remote add origin https://github.com/TU-USUARIO/tumor-detector-mri.git
```

### Error: "Updates were rejected"

Primero haz pull:
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

### Deshacer Último Commit (sin perder cambios)

```bash
git reset --soft HEAD~1
```

### Ver Archivos que se Subirán

```bash
git status
git ls-files
```

## 🌐 Después de Subir a GitHub

1. ✅ Verifica que todo esté en GitHub
2. 🚀 Procede con el deployment en Render
3. 📝 Actualiza el README con la URL de producción
4. 🎉 Comparte tu proyecto

## 📱 GitHub Desktop (Alternativa)

Si prefieres una interfaz gráfica:

1. Descarga [GitHub Desktop](https://desktop.github.com/)
2. Instala y abre
3. File → Add local repository
4. Selecciona la carpeta del proyecto
5. Usa la interfaz para commit y push

## 🎓 Recursos Adicionales

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Docs](https://docs.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

## ✅ Checklist Final

Antes de hacer push, verifica:

- [ ] ✅ `.gitignore` incluido
- [ ] ✅ README.md completo
- [ ] ✅ `requirements.txt` actualizado
- [ ] ✅ No hay archivos sensibles (contraseñas, tokens)
- [ ] ✅ No hay carpeta `venv/` o `__pycache__/`
- [ ] ✅ Código probado localmente
- [ ] ✅ Todos los archivos necesarios incluidos

---

**¡Listo para subir tu proyecto!** 🚀
