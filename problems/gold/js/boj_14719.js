const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const [H, W] = input[0].split(" ").map((x) => +x);
const blocks = input[1].split(" ").map((x) => +x);

const solution = (h, w, blocks) => {
  let board = Array.from(Array(h), () => new Array(w).fill(0));
  let ans = 0;

  for (let i = 0; i < w; ++i) {
    for (let j = 0; j < blocks[i]; ++j) {
      board[h - 1 - j][i] = 1;
    }
  }

  board.forEach((row) => {
    let cnt = 0;
    let left = false;

    row.forEach((el) => {
      if (el) {
        if (left) {
          ans += cnt;
        } else {
          left = true;
        }

        cnt = 0;
        return;
      }

      ++cnt;
    });
  });

  /*
    for (let i = 0; i < h; ++i) {
      let cnt = 0;
      let left = false;

      for (let j = 0; j < w; ++j) {
        if (board[i][j]) {
          if (left) {
            ans += cnt;
          } else {
            left = true;
          }

          cnt = 0;
          continue;
        }

        ++cnt;
      }
    }
*/

  return ans;
};

console.log(solution(H, W, blocks));
