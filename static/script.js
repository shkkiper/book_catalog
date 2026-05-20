document.querySelectorAll('.btn-delete').forEach(button => {
    button.addEventListener('click', function(e) {
        if (!confirm('Вы уверены, что хотите удалить эту книгу?')) {
            e.preventDefault();
        }
    });
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

const currentLocation = location.pathname;
document.querySelectorAll('.nav-links a').forEach(link => {
    if (link.getAttribute('href') === currentLocation) {
        link.style.color = '#667eea';
        link.style.fontWeight = 'bold';
    }
});