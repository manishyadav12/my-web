// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Animate hamburger bars
            const bars = hamburger.querySelectorAll('.bar');
            if (navMenu.classList.contains('active')) {
                bars[0].style.transform = 'rotate(-45deg) translate(-5px, 6px)';
                bars[1].style.opacity = '0';
                bars[2].style.transform = 'rotate(45deg) translate(-5px, -6px)';
            } else {
                bars[0].style.transform = 'none';
                bars[1].style.opacity = '1';
                bars[2].style.transform = 'none';
            }
        });
        
        // Close menu when clicking on a link
        const navLinks = navMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                const bars = hamburger.querySelectorAll('.bar');
                bars[0].style.transform = 'none';
                bars[1].style.opacity = '1';
                bars[2].style.transform = 'none';
            });
        });
    }
    
    // Flash Message Dismissal
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        const closeBtn = message.querySelector('.flash-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                message.style.animation = 'slideOut 0.3s ease forwards';
                setTimeout(() => {
                    message.remove();
                }, 300);
            });
        }
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (message.parentNode) {
                message.style.animation = 'slideOut 0.3s ease forwards';
                setTimeout(() => {
                    if (message.parentNode) {
                        message.remove();
                    }
                }, 300);
            }
        }, 5000);
    });
    
    // Smooth Scrolling for Anchor Links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const navbar = document.querySelector('.navbar');
                    const navHeight = navbar ? navbar.offsetHeight : 70;
                    // Add extra buffer to prevent section titles from being cut off
                    const extraBuffer = 20; // Additional 20px buffer
                    const targetPosition = target.offsetTop - navHeight - extraBuffer;
                    
                    window.scrollTo({
                        top: Math.max(0, targetPosition), // Ensure we don't scroll to negative position
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu if open
                    if (navMenu && navMenu.classList.contains('active')) {
                        navMenu.classList.remove('active');
                        const bars = hamburger.querySelectorAll('.bar');
                        bars[0].style.transform = 'none';
                        bars[1].style.opacity = '1';
                        bars[2].style.transform = 'none';
                    }
                }
            }
        });
    });
    
    // Active navigation highlighting
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('.nav-link');
    
    function updateActiveNavigation() {
        const navbar = document.querySelector('.navbar');
        const navHeight = navbar ? navbar.offsetHeight : 70;
        const scrollPosition = window.scrollY + navHeight + 30; // Add buffer for better detection
        
        sections.forEach((section, index) => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => link.classList.remove('active'));
                const correspondingLink = document.querySelector(`a[href="#${section.id}"]`);
                if (correspondingLink) {
                    correspondingLink.classList.add('active');
                }
            }
        });
    }
    
    window.addEventListener('scroll', updateActiveNavigation);
    
    // Simple Name Animation - Reliable version
    const homeSection = document.getElementById('home');
    const nameText = document.getElementById('nameText');
    const heroTitle = document.getElementById('heroTitle');
    
    if (homeSection && nameText && heroTitle) {
        // Simple wave animation trigger
        function triggerWaveEmoji() {
            heroTitle.classList.add('wave-emoji');
            setTimeout(() => {
                heroTitle.classList.remove('wave-emoji');
            }, 2000);
        }
        
        // Intersection observer for scroll-triggered animation
        const nameAnimationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Just trigger the wave emoji
                    triggerWaveEmoji();
                }
            });
        }, {
            threshold: 0.3,
            rootMargin: '0px'
        });
        
        nameAnimationObserver.observe(homeSection);
        
        // Initial wave on page load
        setTimeout(() => {
            triggerWaveEmoji();
        }, 1500);
        
        // Click to trigger wave
        nameText.addEventListener('click', () => {
            triggerWaveEmoji();
        });
    }
    
    // Form Validation Enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = 'var(--accent-error)';
                    field.addEventListener('input', function() {
                        this.style.borderColor = 'var(--border-color)';
                    }, { once: true });
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showFlashMessage('Please fill in all required fields', 'error');
            }
        });
    });
    
    // Add Loading State to Forms
    const submitButtons = document.querySelectorAll('form button[type="submit"]');
    submitButtons.forEach(button => {
        button.addEventListener('click', function() {
            const form = this.closest('form');
            if (form.checkValidity()) {
                this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
                this.disabled = true;
            }
        });
    });
    
    // Navbar Scroll Effect - Keep navbar always visible
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Always keep navbar visible
        navbar.style.transform = 'translateY(0)';
        
        // Add stronger background on scroll
        if (scrollTop > 50) {
            navbar.style.background = 'rgba(10, 10, 15, 0.98)';
            navbar.style.backdropFilter = 'blur(20px)';
            navbar.style.borderBottom = '1px solid var(--border-color)';
        } else {
            navbar.style.background = 'rgba(10, 10, 15, 0.95)';
            navbar.style.backdropFilter = 'blur(20px)';
            navbar.style.borderBottom = '1px solid var(--border-light)';
        }
    });
    
    // Intersection Observer for Animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.highlight-card, .project-card, .post-card, .timeline-item');
    if (animateElements.length > 0) {
        animateElements.forEach(el => {
            try {
                el.style.opacity = '0';
                el.style.transform = 'translateY(20px)';
                observer.observe(el);
            } catch (e) {
                // Fallback: make element visible if animation fails
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }
        });
    }
    
    // Typing Effect for Hero Title (if present)
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle && heroTitle.textContent.includes('Manish Yadav')) {
        const text = heroTitle.innerHTML;
        heroTitle.innerHTML = text.replace('Manish Yadav', '<span class="typed-text">Manish Yadav</span>');
        
        const typedElement = heroTitle.querySelector('.typed-text');
        if (typedElement) {
            const originalText = typedElement.textContent;
            typedElement.textContent = '';
            
            let i = 0;
            const typeWriter = function() {
                if (i < originalText.length) {
                    typedElement.textContent += originalText.charAt(i);
                    i++;
                    setTimeout(typeWriter, 100);
                }
            };
            
            // Start typing after a short delay
            setTimeout(typeWriter, 1000);
        }
    }
});

// Utility function to show flash messages
function showFlashMessage(message, type = 'success') {
    const flashDiv = document.createElement('div');
    flashDiv.className = `flash-message flash-${type}`;
    flashDiv.innerHTML = `
        ${message}
        <button class="flash-close">&times;</button>
    `;
    
    document.body.appendChild(flashDiv);
    
    const closeBtn = flashDiv.querySelector('.flash-close');
    closeBtn.addEventListener('click', () => {
        flashDiv.style.animation = 'slideOut 0.3s ease forwards';
        setTimeout(() => {
            flashDiv.remove();
        }, 300);
    });
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (flashDiv.parentNode) {
            flashDiv.style.animation = 'slideOut 0.3s ease forwards';
            setTimeout(() => {
                if (flashDiv.parentNode) {
                    flashDiv.remove();
                }
            }, 300);
        }
    }, 5000);
}

// Add CSS animations dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .typed-text {
        border-right: 2px solid var(--accent-primary);
        animation: blink 0.7s infinite;
    }
    
    @keyframes blink {
        0%, 50% { border-right-color: var(--accent-primary); }
        51%, 100% { border-right-color: transparent; }
    }
`;
document.head.appendChild(style);