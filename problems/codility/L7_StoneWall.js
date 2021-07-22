function solution(H) {
  const st = [];
  let cnt = 0;

  for (let i = 0; i < H.length; i++) {
    const h = H[i];

    if (!st.length) {
      st.push(h);
      continue;
    }

    while (st.length && st[st.length - 1] > h) {
      st.pop();
      cnt++;
    }

    if (st[st.length - 1] !== h) {
      st.push(h);
    }
  }

  return cnt + st.length;
}
