// case 2
// 2 3

const solution = (data) => {
  console.log(data);
  console.log(typeof data);
  let [a, b] = data;
  console.log(a, b);
};

const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let data = [];

  for await (const line of rl) {
    data = line.split(" ").map((e) => +e);
    rl.close();
  }
  solution(data);

  process.exit();
})();
