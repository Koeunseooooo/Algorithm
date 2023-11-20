// case 3
// abcd

const solution = (data) => {
  console.log(data);
  console.log(typeof data);
};

const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let data = [];

  for await (const line of rl) {
    data = line.split("").map((e) => e);
    rl.close();
  }
  solution(data);

  process.exit();
})();
