const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const word = input.shift();
const explosive = input.shift();

function solution(word, bomb) {
  const s = [];
  let tmpStr = '';

  for (let i = 0; i < word.length; i++) {
    s.push(word[i]);
    if (tmpStr.length < bomb.length) {
      tmpStr += word[i];
    } else {
      tmpStr = tmpStr.slice(1) + word[i];
    }
    if (tmpStr !== bomb) continue;

    for (let j = 0; j < bomb.length; j++) s.pop();
    let idx = s.length - 1;
    tmpStr = '';
    while (idx >= 0 && tmpStr.length < bomb.length) {
      tmpStr = s[idx--] + tmpStr;
    }
  }

  return s.join('') || 'FRULA';
}

console.log(solution(word, explosive));
