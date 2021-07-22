const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
let T = +input.shift();

class Deque {
  constructor() {
    this.front = null;
    this.back = null;
    this.size = 0;
  }

  push(x) {
    const node = { val: x, left: this.back, right: null };

    if (this.isEmpty()) {
      this.front = node;
    } else {
      this.back.right = node;
    }

    this.back = node;
    this.size++;
  }

  unshift(x) {
    const node = { val: x, left: null, right: this.front };

    if (this.isEmpty()) {
      this.back = node;
    } else {
      this.front.left = node;
    }

    this.front = node;
    this.size++;
  }

  pop() {
    if (this.isEmpty()) return null;
    const key = this.back.val;

    this.back = this.back.left;
    this.size--;

    return key;
  }

  shift() {
    if (this.isEmpty()) return null;
    const key = this.front.val;

    this.front = this.front.right;
    this.size--;

    return key;
  }

  isEmpty() {
    return this.size === 0;
  }
}

let ans = '';

while (T--) {
  let right = true;
  const cmd = input.shift();
  const N = +input.shift();
  let nums = input.shift();
  nums = nums.slice(1, nums.length - 1);
  if (nums.length) nums = nums.split(',');

  const q = new Deque();

  for (let i = 0; i < nums.length; i++) {
    q.push(nums[i]);
  }

  let flag = true;

  for (let i = 0; i < cmd.length; i++) {
    if (cmd[i] === 'R') {
      right = !right;
      continue;
    }

    if (cmd[i] === 'D') {
      let tmp;

      tmp = right ? q.shift() : q.pop();

      if (!tmp) {
        ans += 'error' + (T === 0 ? '' : '\n');
        flag = false;
        break;
      }
    }
  }
  if (!flag) continue;

  let tmp = '';

  if (right) {
    while (1) {
      const t = q.shift();
      if (!t) break;
      tmp += t + ',';
    }
  } else {
    while (1) {
      const t = q.pop();
      if (!t) break;
      tmp += t + ',';
    }
  }
  tmp = '[' + tmp.slice(0, tmp.length - 1) + ']';
  ans += tmp + (T === 0 ? '' : '\n');
}

console.log(ans);
