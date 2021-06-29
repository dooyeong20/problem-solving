const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input
  .shift()
  .split(' ')
  .map((x) => +x);
let [r, c, d] = input
  .shift()
  .split(' ')
  .map((x) => +x);
const board = input.map((line) => line.split(' ').map((x) => +x));

const startCleaning = (cr, cc, cd) => {
  const turnLeft = (d) => {
    return d === 0 ? 3 : --d;
  };
  const checkDirtyLeft = (x, y, d) => {
    switch (d) {
      case 0:
        y--;
        break;
      case 1:
        x--;
        break;
      case 2:
        y++;
        break;
      case 3:
        x++;
        break;
    }

    return board[x] && board[x][y] === 0 ? true : false;
  };
  const goForward = (x, y, d) => {
    if (d === 0) x--;
    else if (d === 1) y++;
    else if (d === 2) x++;
    else y--;

    return [x, y];
  };
  const canGoBackward = (x, y, d) => {
    if (d === 0) x++;
    else if (d === 1) y--;
    else if (d === 2) x--;
    else y++;

    return board[x] && board[x][y] != 1 ? true : false;
  };
  const goBackward = (x, y, d) => {
    if (d === 0) x++;
    else if (d === 1) y--;
    else if (d === 2) x--;
    else y++;

    return [x, y];
  };
  let [x, y, d] = [cr, cc, cd];
  let count = 0;

  while (1) {
    let cleaned = false;
    if (board[x][y] !== 2) count++;
    board[x][y] = 2;

    for (let i = 0; i < 4; i++) {
      if (checkDirtyLeft(x, y, d)) {
        cleaned = true;
        d = turnLeft(d);
        [x, y] = goForward(x, y, d);
        break;
      }
      d = turnLeft(d);
    }

    if (!cleaned) {
      if (!canGoBackward(x, y, d)) break;
      [x, y] = goBackward(x, y, d);
    }
  }

  return count;
};

console.log(startCleaning(r, c, d));
