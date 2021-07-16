const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const board = input.map(line => line.split(''));

function solution(board) {
  const ROW = 12;
  const COL = 6;
  let cnt = 0;
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, 1, -1];

  const popPuyo = board => {
    const visited = Array.from({ length: ROW }, () =>
      Array.from({ length: COL }, () => 0)
    );
    let poped = false;
    const bfs = (r, c, k) => {
      const q = [[r, c]];
      const puyos = [[r, c]];
      let cnt = 1;
      visited[r][c] = 1;

      while (q.length) {
        const [cr, cc] = q.shift();
        for (let i = 0; i < 4; i++) {
          const [nr, nc] = [cr + dr[i], cc + dc[i]];

          if (board[nr] && board[nr][nc] === k && !visited[nr][nc]) {
            q.push([nr, nc]);
            puyos.push([nr, nc]);
            cnt++;
            visited[nr][nc] = 1;
          }
        }
      }

      return puyos;
    };

    for (let i = 0; i < ROW; i++) {
      for (let j = 0; j < COL; j++) {
        if (board[i][j] === '.' || visited[i][j]) continue;

        const puyos = bfs(i, j, board[i][j]);
        if (puyos.length < 4) continue;
        poped = true;
        for (let i = 0; i < puyos.length; i++) {
          const [r, c] = puyos[i];
          board[r][c] = '.';
        }
      }
    }

    return poped;
  };

  const downPuyo = board => {
    for (let row = ROW - 2; row >= 0; row--) {
      for (let col = 0; col < COL; col++) {
        if (board[row][col] === '.') continue;
        const key = board[row][col];
        board[row][col] = '.';
        let r = row;
        let c = col;
        while (r < 11 && board[r + 1][c] === '.') {
          r++;
        }
        board[r][c] = key;
      }
    }
  };

  while (1) {
    const poped = popPuyo(board);
    if (!poped) return cnt;
    cnt++;
    downPuyo(board);
  }
}

console.log(solution(board));
