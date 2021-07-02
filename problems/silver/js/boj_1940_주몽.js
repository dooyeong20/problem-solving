const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = +input.shift();
const M = +input.shift();
const nums = input
  .shift()
  .split(' ')
  .map(x => +x)
  .sort((a, b) => a - b);

const solve = nums => {
  let l = 0;
  let r = N - 1;
  let cnt = 0;

  while (l < r) {
    if (nums[l] + nums[r] === M) {
      cnt++;
      l++;
      r--;
    } else if (nums[l] + nums[r] < M) l++;
    else r--;
  }

  return cnt;
};

console.log(solve(nums));
