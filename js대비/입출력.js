// Run by Node.js
const readline = require("readline");

const d = [(-1, 0), (1, 0), (0, -1), (0, 1)];

const bfs = (x, y, checked) => {
  q = [];
  q.push((x, y));
  checked[x][y] = 1;
  while (q) {
    x, (y = q.shift());
    for (i of d) {
      console.log(i);
    }
    break;
  }
};

const solution = (N, data) => {
  console.log(N);
  let checked = Array.from({ length: N }, () => new Array(N).fill(0));
  console.log(checked);
  for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[0].length; j++) {
      if ((checked[i][j] === 0) & (data[i][j] === 1)) {
        console.log(i, j);
        bfs(i, j, checked);
      }
    }
  }
};

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let N = null;
  let data = [];
  let count = 0;
  for await (const line of rl) {
    if (!N) {
      N = +line;
    } else {
      data.push(line.split(" ").map((el) => parseInt(el, 10)));
      count += 1;
    }
    if (count === N) {
      rl.close();
    }
  }

  solution(N, data);
  process.exit();
})();
