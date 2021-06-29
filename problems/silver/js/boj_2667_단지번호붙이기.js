const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = +input.shift();
const board = input.map((line) => line.split('').map((x) => +x));
const answer = [];

const bfs = (r, c) => {
  const dirs = [
    [1, 0],
    [0, 1],
    [0, -1],
    [-1, 0],
  ];
  const q = [[r, c]];
  let count = 0;
  board[r][c] = 0;

  while (q.length) {
    const [r, c] = q.pop();
    count++;

    dirs.forEach(([dr, dc]) => {
      const [nr, nc] = [r + dr, c + dc];

      if (board[nr] && board[nr][nc] === 1) {
        q.push([nr, nc]);
        board[nr][nc] = 0;
      }
    });
  }

  return count;
};

const solution = () => {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (board[i][j] === 1) {
        answer.push(bfs(i, j));
      }
    }
  }
  return answer.sort((a, b) => a - b).reduce((p, c) => p + '\n' + c, answer.length);
};

console.log(solution());
