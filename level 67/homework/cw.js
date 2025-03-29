function sumArray(numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}

let numbers = [10, 20, 30, 40, 50];
console.log( sumArray(numbers));


function findMinMax(numbers1) {
    let min = Math.min(...numbers1);
    let max = Math.max(...numbers1);
    
    return { min, max };
}

let numbers1 = [15, 3, 9, 27, 42, 8];
let result = findMinMax(numbers1);

console.log( result.min); 
console.log( result.max); 






function generateRandomArray(N) {
    let array = [];
    for (let i = 0; i < N; i++) {
        array.push(Math.floor(Math.random() * 100) + 1);
    }
    return array;
}

let randomNumbers = generateRandomArray(5);
console.log(randomNumbers);







function squareArray(numbers2) {
    return numbers2.map(num1 => num1 ** 2);
}

let numbers2 = [2, 4, 6, 8];
let squaredNumbers = squareArray(numbers2);

console.log(squaredNumbers);

