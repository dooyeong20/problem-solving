const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input
  .shift()
  .split(' ')
  .map(x => +x);
const board = input.map(line => line.split(' ').map(x => +x));

function solution(n, m, board) {
  const virusPos = [];
  let emptySize = 0;
  const getCombi = (a, b) => {
    const res = [];
    const key = Array.from({ length: b }, () => 0);

    const dfs = (l, idx) => {
      if (l === b) {
        res.push([...key]);
        return;
      }
      for (let i = idx; i < a; i++) {
        key[l] = i;
        dfs(l + 1, i + 1);
      }
    };

    dfs(0, 0);
    return res;
  };

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] !== 1) emptySize++;
      if (board[i][j] === 2) virusPos.push([i, j]);
    }
  }
  const virusCombi = getCombi(virusPos.length, m);
  const dr = [-1, 1, 0, 0];
  const dc = [0, 0, -1, 1];

  const myBoard = Array.from({ length: n }, () =>
    Array.from({ length: n }, () => 0)
  );

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 1) myBoard[i][j] = 1;
    }
  }

  const bfs = (myBoard, loc) => {
    const q = loc;
    let maxVal = 1;
    const visited = Array.from({ length: n }, () =>
      Array.from({ length: n }, () => 0)
    );
    let visitedCnt = 0;

    for (const [r, c] of q) {
      visited[r][c] = 1;
      visitedCnt++;
    }

    while (q.length) {
      const [cr, cc] = q.shift();

      for (let i = 0; i < 4; i++) {
        const nr = cr + dr[i];
        const nc = cc + dc[i];

        if (myBoard[nr] && myBoard[nr][nc] === 0 && !visited[nr][nc]) {
          q.push([nr, nc]);
          visited[nr][nc] = visited[cr][cc] + 1;
          if (visited[nr][nc] > maxVal) maxVal = visited[nr][nc];
          visitedCnt++;
        }
      }
    }

    if (emptySize !== visitedCnt) return -5;
    return maxVal;
  };

  let ans = Infinity;

  for (let cc = 0; cc < virusCombi.length; cc++) {
    const loc = [];
    for (let i = 0; i < virusCombi[cc].length; i++) {
      const idx = virusCombi[cc][i];
      const [r, c] = virusPos[idx];
      myBoard[r][c] = 2;
      loc.push([r, c]);
    }

    const res = bfs(myBoard, loc);
    if (res !== -5) ans = Math.min(ans, res);

    for (let i = 0; i < virusCombi[cc].length; i++) {
      const idx = virusCombi[cc][i];
      const [r, c] = virusPos[idx];
      myBoard[r][c] = 0;
    }
  }

  return !isFinite(ans) ? -1 : ans - 1;
}

console.log(solution(N, M, board));
