const box = document.querySelector('.box');

let x = 0;
let y = 0;

// 1
const moveRight = setInterval(() => {
    x += 1; 
    box.style.top = `${x}px`;
    if (x == 450){
       clearInterval(moveRight);
       const moveDown = setInterval(() => {
          y += 1; 
          box.style.left = `${y}px`;
          if (y == 450){
             clearInterval(moveDown);
             const moveLeft = setInterval(() => {
                x -= 1; 
                box.style.top = `${x}px`;
                if (x == 0){
                   clearInterval(moveLeft);
                   const moveUp = setInterval(() => {
                      y -= 1; 
                      box.style.left = `${y}px`;
                      if (y == 0){
                         clearInterval(moveUp);
                      }
                   }, 5)
                }
             }, 5)
          }
       }, 5)
    }
 }, 5)