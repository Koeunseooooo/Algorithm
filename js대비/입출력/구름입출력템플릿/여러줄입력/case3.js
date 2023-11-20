// case 3 (테케T 가 있는 경우)
// 2 <- T
// 3
// 1 2 3
// 4 5 6
// 7 8 9
// 2
// 2 1
// 5 4

const solution = (N, data) => {
  console.log(N);
  console.log(data);
  console.log("1cycle");
};
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let T = null;
  let N = null;
  let countN = 0;
  let countT = 0;
  let data = [];
  for await (const line of rl) {
    if (!T) {
      T = +line;
    } else if (!N) {
      N = +line;
    } else {
      data.push(line.split(" ").map((e) => +e));
      countN += 1;
    }
    if (countN === N) {
      solution(N, data);
      N = null;
      countN = 0;
      data = [];

      countT += 1;
    }
    if (countT === T) {
      rl.close();
    }
  }
  process.exit();
})();
