document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.carousel-track');
    const slides = Array.from(track.children);
    const slideWidth = slides[0].getBoundingClientRect().width;

    let currentIndex = 0;

    const moveToSlide = (track, currentIndex) => {
        track.style.transform = 'translateX(-' + slideWidth * currentIndex + 'px)';
    };

    const autoSlide = () => {
        if (currentIndex < slides.length - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        moveToSlide(track, currentIndex);
    };

    setInterval(autoSlide, 3000); // Change slide every 3 seconds
});
