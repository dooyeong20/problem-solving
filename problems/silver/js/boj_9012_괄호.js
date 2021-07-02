const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const T = +input.shift();
const brackets = input;

const checkBracket = line => {
  const stack = [];

  for (let i = 0; i < line.length; i++) {
    const ch = line[i];

    if (ch === '(') {
      stack.push(ch);
      continue;
    }
    if (stack.length < 1) return false;
    stack.pop();
  }
  return !stack.length;
};

brackets.forEach(line => {
  console.log(checkBracket(line) ? 'YES' : 'NO');
});
