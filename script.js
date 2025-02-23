// Smooth scrolling for navigation links
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', (event) => {
        const targetId = event.target.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            event.preventDefault();
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Mobile menu toggle for navigation
function toggleMenu() {
    const navContainer = document.querySelector('.nav');
    navContainer.classList.toggle('menu-active');
}

// Hero text dynamic animation
const changingText = document.querySelector('[data-text]');
const texts = [
    "Transforming data into insights",
    "Pretvaranje podataka u uvid",
    "Omvandla data till insikter"
];
let currentIndex = 0;

function changeText() {
    changingText.textContent = texts[currentIndex];
    currentIndex = (currentIndex + 1) % texts.length;
}

setInterval(changeText, 3000);

// Smooth reveal for sections
const observerOptions = { threshold: 0.1 };

const revealSection = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = `fadeIn 0.8s ease forwards`;
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.about, .contact, .projects-hero, .project-card').forEach(section => {
    revealSection.observe(section);
});
