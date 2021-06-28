const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = input.shift();
const meetings = input.map((line) => line.split(' ').map((x) => +x));
let answer = 0;
let last = -Infinity;

meetings.sort((m1, m2) => {
  if (m1[1] < m2[1]) {
    return -1;
  }
  if (m1[1] === m2[1] && m1[0] < m2[0]) {
    return -1;
  }
  return 1;
});

meetings.forEach(([st, en]) => {
  if (st >= last) {
    answer++;
    last = en;
  }
});

console.log(answer);
