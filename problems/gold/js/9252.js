const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const word1 = input.shift();
const word2 = input.shift();

const dp = Array.from({ length: word2.length + 1 }, () =>
  Array.from({ length: word1.length + 1 }, () => 0)
);

const nMap = {};

for (let i = 1; i < word2.length + 1; i++) {
  for (let j = 1; j < word1.length + 1; j++) {
    if (word2[i - 1] === word1[j - 1]) {
      dp[i][j] = dp[i - 1][j - 1] + 1;
      nMap[dp[i][j]] = [i - 1, j - 1];
    } else {
      dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
    }
  }
}

const cnt = dp[word2.length][word1.length];
console.log(cnt);

if (cnt) {
  let str = '';
  let r = word2.length;
  let c = word1.length;

  while (str.length < cnt) {
    if (dp[r][c] !== dp[r - 1][c] && dp[r][c] !== dp[r][c - 1]) {
      str = word2[r - 1] + str;
      r--;
      c--;
      continue;
    }

    if (dp[r][c] === dp[r - 1][c]) r--;
    else if (dp[r][c] === dp[r][c - 1]) c--;
  }

  console.log(str);
}
