const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = +input.shift();
const dices = input.map(line => line.split(' ').map(x => +x));
const oppo = {
  0: 5,
  1: 3,
  2: 4,
  3: 1,
  4: 2,
  5: 0,
};

const getMaxSide = (dIdx, idx) => {
  let tmpMax = -1;

  for (let i = 0; i < 6; i++) {
    if (i === idx || i === oppo[idx]) continue;
    if (dices[dIdx][i] > tmpMax) tmpMax = dices[dIdx][i];
  }

  return tmpMax;
};

const getUpDiceDownIdxByNum = (j, lastUpNum) => {
  for (let i = 0; i < 6; i++) {
    if (dices[j][i] === lastUpNum) {
      return i;
    }
  }
};

let ans = 6;

for (let i = 1; i <= 6; i++) {
  let tSum = 0;
  let lastUpNum = i;

  for (let j = 0; j < N; j++) {
    let downIdx = getUpDiceDownIdxByNum(j, lastUpNum);
    tSum += getMaxSide(j, downIdx);
    lastUpNum = dices[j][oppo[downIdx]];
  }

  ans = Math.max(ans, tSum);
}

console.log(ans);
