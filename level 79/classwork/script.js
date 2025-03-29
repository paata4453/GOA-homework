
const cars = ["BMW", "Volvo", "Mini", "Mercedes"];
for (let i of cars) {
    console.log(i);
}


const numbers = [45, 4, 9, 16, 25];

let text = "";
for (let i in numbers) {
  text += numbers[i];
  console.log(text)
}

const sum = (a, b) => a * b;
console.log(sum(10, 5));

const obj1 = {
    name: "hamdula",
    lastname: "pubgishvili",
    age: 16,
};

const obj2 = {
    name: "xvicha",
    lastname: "kvaratsxelia"
};

console.log(Object.assign({}, obj1, obj2))

