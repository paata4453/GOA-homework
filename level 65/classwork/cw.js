const person = {
    name: "giorgi",
    age: 30,
    greet: function() {
        return `hello my name is ${this.name}`;
    }
};

console.log(person.greet());  

function Person(name, age, city) {
    this.name = "giorgi";
    this.age = "30";
    this.city = "tbilisi";
    this.greet = function() {
        return "hello my name is ${this.name} and i live in ${this.city}";
    };
}

function Car(brand, model, year, color, horsePower) {
    this.brand = "BMW";
    this.model = "X6";
    this.year = "2020";
    this.color = "black";
    this.horsePower = "300";

    this.boostHorsePower = function() {
        this.horsePower += 100;
        return "${this.brand} ${this.model} now has ${this.horsePower} donkey power dd";
    };
}

