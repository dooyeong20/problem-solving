const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [N, M] = input[0].split(" ").map((x) => +x);
const trees = input[1].split(" ").map((x) => +x);
const check = (trees, height, size) => {
  let take = 0;

  for (let i = 0; i < trees.length; ++i) {
    take += trees[i] > height ? trees[i] - height : 0;
    if (take > size) break;
  }

  return take;
};
const solution = (N, M, trees) => {
  let left = 0,
    right = 2000000000,
    take;

  while (left <= right) {
    let mid = parseInt((left + right) / 2);
    check(trees, mid, M) > M ? (left = mid + 1) : (right = mid - 1);
  }

  take = check(trees, ++right, M);

  return take < M ? right - 1 : right;
};

console.log(solution(N, M, trees));
