
window.addEventListener('load', function() {
    let header = document.querySelector('header');
  
    if (window.pageYOffset > 0) {
      header.style.backgroundColor = 'rgb(69, 69, 221)';
    } else {
      header.style.backgroundColor = 'transparent';
    }
});
  
  
window.addEventListener('scroll', function() {
    let header = document.querySelector('header');
  
    if (window.pageYOffset > 0) {
      header.style.backgroundColor = 'rgb(69, 69, 221)';
    } else {
      header.style.backgroundColor = 'transparent';
    }
});


let menu = document.querySelector('.menu');
menu.addEventListener('onmouseover', function() {
    document.querySelector('header').style.backgroundColor = 'rgb(69, 69, 221)';
});

