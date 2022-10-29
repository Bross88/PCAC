document.addEventListener("DOMContentLoaded", () =>{
   const elementoscarousel= document.querySelectorAll('.carousel');
   M.Carousel.init(elementoscarousel,{
    duration:150,
    dist: -80,
    shift: 5,
    padding: 5,
    numVisible: 3,
    indicators: true,
    
   });
});