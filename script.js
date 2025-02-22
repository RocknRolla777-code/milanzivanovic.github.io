// Smooth scrolling for internal links
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', event => {
        const targetId = event.target.getAttribute('href').slice(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            event.preventDefault();
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});


// Add more JavaScript functionality as needed
// Existing smooth scroll code...

// Form submission
document.querySelector('.contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    // Add your form submission logic here
});

// Add animation on scroll
const observerOptions = {
    threshold: 0.1
};

// Scroll animation for sections
const observer = new IntersectionObserver(
    (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = `fadeIn 0.8s ease forwards`;
                observer.unobserve(entry.target); // Stop observing once animated
            }
        });
    },
    { threshold: 0.1 }
);

document.querySelectorAll('.projects-hero, .projects-showcase, .project-card').forEach(section => {
    observer.observe(section);
});

