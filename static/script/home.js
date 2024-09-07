const toggleButton = document.getElementById('toggle-btn')
const sidebar = document.getElementById('sidebar')

function toggleSidebar(){
  sidebar.classList.toggle('close')
  toggleButton.classList.toggle('rotate')

  closeAllSubMenus()
}

function toggleSubMenu(button){

  if(!button.nextElementSibling.classList.contains('show')){
    closeAllSubMenus()
  }

  button.nextElementSibling.classList.toggle('show')
  button.classList.toggle('rotate')

  if(sidebar.classList.contains('close')){
    sidebar.classList.toggle('close')
    toggleButton.classList.toggle('rotate')
  }
}

function closeAllSubMenus(){
  Array.from(sidebar.getElementsByClassName('show')).forEach(ul => {
    ul.classList.remove('show')
    ul.previousElementSibling.classList.remove('rotate')
  })
}



// swaper added by ayush
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
