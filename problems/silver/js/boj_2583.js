const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [M, N, K] = input
  .shift()
  .split(' ')
  .map((x) => +x);
const squares = input.map((line) => line.split(' ').map((x) => +x));
const board = Array.from(new Array(M), () => new Array(N).fill(0));
const visited = Array.from(new Array(M), () => new Array(N).fill(0));

const ansArr = [];
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

squares.forEach(([x1, y1, x2, y2]) => {
  for (let j = M - y2; j < M - y1; j++) {
    for (let i = x1; i < x2; i++) {
      board[j][i] = 1;
    }
  }
});

for (let i = 0; i < board.length; i++) {
  for (let j = 0; j < board[i].length; j++) {
    if (board[i][j] || visited[i][j]) continue;

    const q = [[i, j]];
    let count = 1;
    visited[i][j] = 1;

    while (q.length) {
      const [cr, cc] = q.shift();

      for (let k = 0; k < 4; k++) {
        const [nr, nc] = [cr + dx[k], cc + dy[k]];
        if (board[nr] && board[nr][nc] === 0 && !visited[nr][nc]) {
          q.push([nr, nc]);
          visited[nr][nc] = 1;
          count++;
        }
      }
    }

    ansArr.push(count);
  }
}

console.log(ansArr.length);
console.log(ansArr.sort((a, b) => a - b).join(' '));
