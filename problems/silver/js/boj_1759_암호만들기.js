const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [L, C] = input
  .shift()
  .split(' ')
  .map(x => +x);
const characters = input[0].split(' ').sort();
const aeiou = new Set(['a', 'e', 'i', 'o', 'u']);
const ans = [];

const dfs = (cnt, st, key, aeiouCnt) => {
  if (cnt === L) {
    if (aeiouCnt < 1 || aeiouCnt > L - 2) return;
    ans.push(key);
    return;
  }

  for (let i = st; i < characters.length; i++) {
    const c = characters[i];
    dfs(cnt + 1, i + 1, key + [c], aeiouCnt + (aeiou.has(c) ? 1 : 0));
  }
};

dfs(0, 0, [], 0);
console.log(ans.sort().join('\n'));
