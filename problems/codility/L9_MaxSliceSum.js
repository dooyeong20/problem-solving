function solution(A) {
  const dp = Array.from({ length: A.length }, () => 0);

  dp[0] = A[0];

  for (let i = 1; i < A.length; i++) {
    dp[i] = Math.max(dp[i - 1] + A[i], A[i]);
  }

  return Math.max(...dp);
}
