function solution(A) {
  const counter = new Map();
  const cntArr = Array.from({ length: A.length }, () => 0);
  let leader = 'no';
  let ans = 0;

  for (let i = 0; i < A.length; i++) {
    counter.set(A[i], (counter.get(A[i]) || 0) + 1);

    if (counter.get(A[i]) > Math.floor(A.length / 2)) {
      leader = A[i];
      break;
    }
  }

  if (leader === 'no') return 0;

  for (let i = 0; i < A.length; i++) {
    if (A[i] === leader) {
      cntArr[i] = i < 1 ? 1 : cntArr[i - 1] + 1;
      continue;
    }
    cntArr[i] = i < 1 ? 0 : cntArr[i - 1];
  }

  for (let i = 0; i < A.length - 1; i++) {
    const leftTotal = i + 1;
    const leftLeaderCnt = cntArr[i];
    const rightLeaderCnt = cntArr[cntArr.length - 1] - cntArr[i];

    if (
      leftLeaderCnt > Math.floor(leftTotal / 2) &&
      rightLeaderCnt > Math.floor((A.length - leftTotal) / 2)
    ) {
      ans++;
    }
  }

  return ans;
}
