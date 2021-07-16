const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const board = input.map(line => line.split(' ').map(x => +x));

const count = (row, col) => {
  let r = row,
    c = col;
  const team = board[r][c];
  let cnt = 0;

  // 아래
  while (board[r][c] === team) {
    ++cnt;
    r++;
  }

  if (cnt >= 5) {
    if (cnt === 5) return true;
    return false;
  }

  // 오른쪽
  r = row;
  c = col;
  cnt = 0;
  while (board[r][c] === team) {
    ++cnt;
    c++;
  }

  if (cnt >= 5) {
    if (cnt === 5) return true;
    return false;
  }

  // 대각 1
  cnt = 0;
  r = row;
  c = col;
  while (board[r][c] === team) {
    ++cnt;
    r++;
    c++;
  }
  if (cnt >= 5) {
    if (cnt === 5) return true;
    return false;
  }

  // 대각 2
  cnt = 0;
  r = row;
  c = col;
  while (board[r][c] === team) {
    ++cnt;
    r--;
    c++;
  }
  if (cnt >= 5) {
    if (cnt === 5) return true;
    return false;
  }
};
for (let i = 0; i < board.length; i++) {
  for (let j = 0; j < board.length; j++) {
    if (board[i][j]) {
      count(i, j);
    }
  }
}
