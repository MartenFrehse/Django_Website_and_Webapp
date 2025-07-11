// document.addEventListener("DOMContentLoaded", function() {
//     let slideIndex = 1;
//     showSlides(slideIndex);
    
//     // Next / previous controls 
//     document.querySelector('.prev').addEventListener('click', function() {
//       plusSlides(-1);
//     });
  
//     document.querySelector('.next').addEventListener('click', function() {
//       plusSlides(1);
//     });
    
//     // Thumbnail image controls 
//     let thumbnails = document.querySelectorAll('.demo');
//     thumbnails.forEach(function(thumbnail, index) {
//       thumbnail.addEventListener('click', function() {
//         currentSlide(index + 1);
//       });
//     });
    
//     function plusSlides(n) {
//       showSlides(slideIndex += n);
//     }
    
//     function currentSlide(n) {
//       showSlides(slideIndex = n);
//     }
    
//     function showSlides(n) {
//       let i;
//       let slides = document.getElementsByClassName("imageSlide");
//       let dots = document.getElementsByClassName("demo");
//       let captionText = document.getElementById("caption");
//       if (n > slides.length) {slideIndex = 1}
//       if (n < 1) {slideIndex = slides.length}
//       for (i = 0; i < slides.length; i++) {
//         slides[i].style.display = "none";
//       }
//       for (i = 0; i < dots.length; i++) {
//         dots[i].className = dots[i].className.replace(" active", "");
//       }
//       slides[slideIndex-1].style.display = "block";
//       dots[slideIndex-1].className += " active";
//       captionText.innerHTML = dots[slideIndex-1].alt;
//     }
//   });
  
document.addEventListener("DOMContentLoaded", function() {
  initializeSlideshows();
});

function initializeSlideshows() {
  const containers = document.querySelectorAll('.imageContainer');
  containers.forEach((container) => {
      let containerId = container.id;
      showSlides(1, containerId);
  });
}

let slideIndex = {};

function plusSlides(n, containerId) {
  showSlides(slideIndex[containerId] += n, containerId);
}

function currentSlide(n, containerId) {
  showSlides(slideIndex[containerId] = n, containerId);
}

function showSlides(n, containerId) {
  let i;
  let container = document.getElementById(containerId);
  let slides = container.getElementsByClassName("imageSlide");
  let dots = container.getElementsByClassName("demo");
  let captionText = container.getElementsByClassName("caption-container")[0].getElementsByTagName("p")[0];

  if (!slideIndex[containerId]) {
      slideIndex[containerId] = 1;
  }

  if (n > slides.length) { slideIndex[containerId] = 1 }
  if (n < 1) { slideIndex[containerId] = slides.length }
  
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }

  slides[slideIndex[containerId] - 1].style.display = "block";
  dots[slideIndex[containerId] - 1].className += " active";
  captionText.innerHTML = dots[slideIndex[containerId] - 1].alt;
}