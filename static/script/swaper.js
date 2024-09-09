const swiper = new Swiper('.slider-wrapper', {
    loop: true,
    grabCursor: true,
    spaceBetween: 30,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      ckickable: true,
      dynamicBullets: true,
  
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    breakpoints: {
        0: {
            slidesPerView: 1
        },
        1000: {
            slidesPerView: 2
        },
  
        1200: {
            slidesPerView: 3
        }
    }
  
  });