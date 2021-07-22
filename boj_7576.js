const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input
  .shift()
  .split(' ')
  .map(x => +x);
const board = input.map(line => line.split(' ').map(x => +x));

function solution(COL, ROW, board) {
  const dr = [-1, 1, 0, 0];
  const dc = [0, 0, -1, 1];
  const tomatos = (function () {
    const tomatos = [];
    let front = 0;

    for (let i = 0; i < ROW; i++) {
      for (let j = 0; j < COL; j++) {
        if (board[i][j] !== 1) continue;
        tomatos.push([i, j]);
      }
    }

    tomatos.popleft = () => {
      if (front === tomatos.length) {
        return null;
      }

      return tomatos[front++];
    };

    return tomatos;
  })();
  const inRange = (r, c) => r >= 0 && r < ROW && c >= 0 && c < COL;

  return (() => {
    let ans = 0;

    while (tomatos.length) {
      const pop = tomatos.popleft();
      if (!pop) break;
      const [r, c] = pop;

      for (let i = 0; i < 4; i++) {
        const nr = r + dr[i];
        const nc = c + dc[i];

        if (inRange(nr, nc) && board[nr][nc] === 0) {
          tomatos.push([nr, nc]);
          board[nr][nc] = board[r][c] + 1;
          if (board[nr][nc] - 1 > ans) ans = board[nr][nc] - 1;
        }
      }
    }

    for (let i = 0; i < ROW; i++) {
      for (let j = 0; j < COL; j++) {
        if (board[i][j] === 0) return -1;
      }
    }

    return ans;
  })();
}

console.log(solution(N, M, board));
