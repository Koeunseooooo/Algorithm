// Run by Node.js
const readline = require("readline");

const d = [(-1, 0), (1, 0), (0, -1), (0, 1)];

let dy = [-1, 0, 1, 0];
let dx = [0, 1, 0, -1];

const bfs = (x, y, checked, N, data) => {
  q = [];
  q.push([x, y]);
  checked[x][y] = 1;
  let cnt = 1;
  while (q.length) {
    let [x, y] = q.shift();
    for (let i = 0; i < 4; i++) {
      let X = x + dx[i];
      let Y = y + dy[i];
      if (
        0 <= X &&
        X < N &&
        0 <= Y &&
        Y < N &&
        data[X][Y] === 1 &&
        checked[X][Y] == 0
      ) {
        q.push([X, Y]);
        checked[X][Y] = 1;
        cnt += 1;
      }
    }
  }
  return cnt;
};

const solution = (N, data) => {
  let checked = Array.from({ length: N }, () => Array(N).fill(0));
  let answer = [];
  for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[0].length; j++) {
      if ((checked[i][j] === 0) & (data[i][j] === 1)) {
        answer.push(bfs(i, j, checked, N, data));
      }
    }
  }
  answer.sort((a, b) => a - b);
  console.log(answer.length);
  console.log(answer.join(" "));
};

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let N = null;
  let data = [];
  let count = 0;
  for await (const line of rl) {
    if (!N) {
      N = +line; // +는 형변환을 바로 해주기 위함임
    } else {
      data.push(Array.from(line).map((el) => parseInt(el, 10)));
      count += 1;
    }
    if (count === N) {
      rl.close();
    }
  }

  solution(N, data);
  process.exit();
})();
