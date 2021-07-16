const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [R, C, N] = input
  .shift()
  .split(' ')
  .map(x => +x);
const board = input.map(line => line.split(''));

function solution(board, R, C, N) {
  let time = 0;
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, -1, 1];
  const initBomb = () => {
    for (let i = 0; i < R; i++) {
      for (let j = 0; j < C; j++) {
        if (board[i][j] === 'O') board[i][j] = 2;
      }
    }
  };
  const setBomb = () => {
    for (let i = 0; i < R; i++) {
      for (let j = 0; j < C; j++) {
        if (board[i][j] === '.') board[i][j] = 2;
      }
    }
  };
  const boom = () => {
    const bombs = [];
    for (let i = 0; i < R; i++) {
      for (let j = 0; j < C; j++) {
        if (board[i][j] !== 0) continue;
        bombs.push([i, j]);
        board[i][j] = '.';
      }
    }

    for (let i = 0; i < bombs.length; i++) {
      const [r, c] = bombs[i];

      for (let k = 0; k < 4; k++) {
        const [nr, nc] = [r + dr[k], c + dc[k]];

        if (board[nr] && board[nr][nc] !== undefined) {
          board[nr][nc] = '.';
        }
      }
    }
  };
  const bombCountDown = () => {
    for (let i = 0; i < R; i++) {
      for (let j = 0; j < C; j++) {
        if (board[i][j] !== '.') board[i][j]--;
      }
    }
  };

  initBomb();
  while (time++ < N) {
    if (time === 1) bombCountDown();
    else if (time % 2) {
      bombCountDown();
      boom();
    } else {
      setBomb();
    }
  }

  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      if (board[i][j] === '.') continue;
      board[i][j] = 'O';
    }
  }
  let ans = '';

  for (let i = 0; i < R; i++) {
    ans += board[i].join('') + '\n';
  }

  return ans;
}

console.log(solution(board, R, C, N));
