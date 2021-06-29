const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, C] = input
  .shift()
  .split(' ')
  .map((x) => +x);
const numbers = input[0].split(' ').map((x) => +x);
const used = new Set();
const counter = numbers.reduce((p, c) => {
  if (used.has(c)) {
    p[c]++;
  } else {
    used.add(c);
    p[c] = 1;
  }
  return p;
}, {});
const nums = [...used].sort((a, b) => counter[b] - counter[a]);

console.log(...nums.map((n) => Array.from(new Array(counter[n]), () => n)).flat());
