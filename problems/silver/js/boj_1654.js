const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [K, N] = input.shift().split(' ');
const lans = input.map((x) => +x);

const binS = (N) => {
  let st = 0;
  let en = Math.max(...lans);

  while (st <= en) {
    const mid = Math.floor((st + en) / 2);
    const count = lans.reduce((p, c) => (p += Math.floor(c / mid)), 0);
    if (count < N) {
      en = mid - 1;
    } else {
      st = mid + 1;
    }
  }

  return st - 1;
};

console.log(binS(N));
