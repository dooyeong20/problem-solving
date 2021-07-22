function solution(A, B) {
  const dp = (function () {
    const dp = [0, 1, 2];

    for (let i = 3; i < 50001; i++) {
      dp.push((dp[i - 2] + dp[i - 1]) % 2 ** 30); // 너무 커지니까 2^30 모듈러로 초기화
    }

    return dp;
  })();

  const ans = [];

  for (let i = 0; i < A.length; i++) {
    ans.push(dp[A[i]] % 2 ** B[i]);
  }

  return ans;
}
