// case 1
// 5
// 1
// 2
// 3
// 4
// 5

const solution = (N, data) => {
  console.log(N);
  console.log(data);
};
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let N = null;
  let count = 0;
  let data = [];
  for await (const line of rl) {
    if (!N) {
      N = +line;
    } else {
      data.push(+line);
      count += 1;
    }
    if (count === N) {
      rl.close();
    }
  }
  solution(N, data);
  process.exit();
})();

// case 1+
// 5
// 1 2 3 4 5

// const solution = (N, data) => {
//   console.log(N);
//   console.log(data);
// };
// const readline = require("readline");

// (async () => {
//   let rl = readline.createInterface({ input: process.stdin });
//   let N = null;
//   let data = [];
//   for await (const line of rl) {
//     if (!N) {
//       N = +line;
//     } else {
//       data = line.split(" ").map((e) => +e);
//       rl.close();
//     }
//   }
//   solution(N, data);
//   process.exit();
// })();
