// case 1
// 10

const solution = (n) => {
  console.log(n);
  console.log(typeof n);
};

const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let data;

  for await (const line of rl) {
    data = +line; // +를 붙이면 문자열이 아닌 숫자로 넘어감
    rl.close();
  }
  solution(data);

  process.exit();
})();
