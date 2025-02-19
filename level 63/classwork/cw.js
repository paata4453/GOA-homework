const scoreInput = prompt("enter your score: ");
console.log(scoreInput)
if(100 <= scoreInput < 90 ){
    alert("Grade A");
} else if(89 <= scoreInput < 80 ){
    alert("Grade B");
} else if(70 <= scoreInput < 79 ){
    alert("Grade C");
} else {
    alert("Grade F");
}



const ageInput = prompt("enter your age: ")
console.log(ageInput)

if (ageInput < 13){
    alert("You are a kid.");
} else if(ageInput < 18 && ageInput > 13){
    alert("You are not an adult yet.");
} else if(ageInput > 18){
    alert("You are an adult.");
}
