const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const tc = +input.shift();
const sentences = input.map(line => line.trim());

function solution(tc, sentences) {
  let ans = [];
  const isAlphabet = ch =>
    'a'.charCodeAt() <= ch.charCodeAt() && ch.charCodeAt() <= 'z'.charCodeAt();

  for (let c = 0; c < tc; c++) {
    const alphaArr = Array.from({ length: 26 }, () => 0);
    const counter = [0, 0, 0];
    let lev = 0;
    for (let j = 0; j < sentences[c].length; j++) {
      const ch = sentences[c][j].toLowerCase();
      if (!isAlphabet(ch)) continue;
      const idx = ch.charCodeAt() - 'a'.charCodeAt();
      alphaArr[idx]++;
      counter[alphaArr[idx] - 1]++;
    }

    for (let i = 2; i >= 0; i--) {
      if (counter[i] === 26) {
        lev = i + 1;
        break;
      }
    }

    if (lev < 1) ans.push(`Case ${c + 1}: Not a pangram`);
    else if (lev < 2) ans.push(`Case ${c + 1}: Pangram!`);
    else if (lev < 3) ans.push(`Case ${c + 1}: Double pangram!!`);
    else ans.push(`Case ${c + 1}: Triple pangram!!!`);
  }

  return ans.join('\n');
}

console.log(solution(tc, sentences));
