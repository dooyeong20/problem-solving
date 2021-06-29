const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = +input.shift();
const numbers = input[0].split(' ').map((x) => +x);
const dp = new Array(N + 1).fill(1);

for (let i = 1; i < numbers.length; i++) {
  for (let j = 0; j < i; j++) {
    if (numbers[j] < numbers[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
  }
}

console.log(Math.max(...dp));
