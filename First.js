let num = parseInt(prompt("Enter a number:"));
let persistence = 0;

while (num >= 10) {
    let sum = 0;
    while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
    }
    num = sum;
    persistence++;
}

console.log(persistence);
