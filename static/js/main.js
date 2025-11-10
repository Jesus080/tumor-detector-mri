// Funciones JavaScript para interactividad

// Refrescar análisis
async function refreshAnalysis() {
    const btn = document.querySelector('.refresh-btn');
    const originalHTML = btn.innerHTML;
    
    // Mostrar loading
    btn.innerHTML = '<div class="loading"></div> Actualizando...';
    btn.disabled = true;
    
    try {
        const response = await fetch('/api/refresh');
        const data = await response.json();
        
        // Recargar la página para mostrar nuevas muestras
        window.location.reload();
    } catch (error) {
        console.error('Error al refrescar:', error);
        alert('Error al actualizar el análisis. Por favor, intenta de nuevo.');
    } finally {
        btn.innerHTML = originalHTML;
        btn.disabled = false;
    }
}

// Animaciones al hacer scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observar elementos al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.case-group, .sample-item');
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // Animar barras del gráfico
    animateBars();
});

// Animar las barras del gráfico
function animateBars() {
    const bars = document.querySelectorAll('.bar');
    bars.forEach((bar, index) => {
        const height = bar.style.height;
        bar.style.height = '0%';
        
        setTimeout(() => {
            bar.style.height = height;
        }, 500 + (index * 200));
    });
}

// Zoom en imágenes
document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.case-image img, .sample-item img');
    
    images.forEach(img => {
        img.addEventListener('click', function() {
            // Crear modal para zoom
            const modal = document.createElement('div');
            modal.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.9);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 1000;
                cursor: zoom-out;
            `;
            
            const modalImg = document.createElement('img');
            modalImg.src = this.src;
            modalImg.style.cssText = `
                max-width: 90%;
                max-height: 90%;
                border-radius: 10px;
                box-shadow: 0 0 50px rgba(255, 255, 255, 0.3);
            `;
            
            modal.appendChild(modalImg);
            document.body.appendChild(modal);
            
            modal.addEventListener('click', () => {
                document.body.removeChild(modal);
            });
        });
    });
});

// Actualizar estadísticas en tiempo real (opcional)
async function updateStats() {
    try {
        const response = await fetch('/api/statistics');
        const stats = await response.json();
        
        // Actualizar valores en la página
        document.querySelector('.stat-card:nth-child(1) h3').textContent = stats.total;
        document.querySelector('.stat-card:nth-child(2) h3').textContent = stats.with_tumor;
        document.querySelector('.stat-card:nth-child(3) h3').textContent = stats.without_tumor;
        
        // Actualizar porcentajes
        document.querySelectorAll('.percentage')[0].textContent = `(${stats.with_tumor_percent}%)`;
        document.querySelectorAll('.percentage')[1].textContent = `(${stats.without_tumor_percent}%)`;
        
    } catch (error) {
        console.error('Error al actualizar estadísticas:', error);
    }
}

// Tooltip para imágenes
document.addEventListener('DOMContentLoaded', () => {
    const caseImages = document.querySelectorAll('.case-image');
    
    caseImages.forEach(caseImg => {
        const img = caseImg.querySelector('img');
        const title = caseImg.querySelector('h4').textContent;
        
        img.title = title;
    });
});
