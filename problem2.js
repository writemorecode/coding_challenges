/*
Project Euler - Problem 2
Find the sum of all even Fibonacci numbers that are not larger than 4 million.
*/

function fib(n) {
    if (n <= 1) {
        return n;
    }

    return fib(n - 1) + fib(n - 2);
}

var sum = 0, i = 0;

do {
    var f = fib(i);

    if (f % 2 == 0) {
        sum += f;
    }

    i++;

} while (f < 4000000);

console.log(sum);
