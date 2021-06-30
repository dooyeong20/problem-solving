const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = +input.shift();
const meetings = input.map(line => line.split(' ').map(x => +x));

let tmpMeetings = [];
let cnt = 0;
let ans = 0;

for (let i = 0; i < N; i++) {
  tmpMeetings.push([meetings[i][0], 1]);
  tmpMeetings.push([meetings[i][1], -1]);
}

tmpMeetings.sort((a, b) => a[0] - b[0]);

for (let i = 0; i < tmpMeetings.length; i++) {
  cnt += tmpMeetings[i][1];
  if (tmpMeetings[i + 1] && tmpMeetings[i][0] === tmpMeetings[i + 1][0])
    continue;
  if (ans < cnt) ans = cnt;
}

console.log(ans);
