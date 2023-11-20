// case 2 (테케T 가 없는 경우)
// 4
// 2 3
// 1 0 0 1
// 1 1 1 1
// 0 1 0 1
// 0 1 1 1

const solution = (N, info, data) => {
  console.log(N);
  console.log(info);
  console.log(data);
};
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let N = null;
  let count = 0;
  let info = null; // 빈배열은 null이 아니므로 초기에 null로 초기화해줘야 분기 처리 잘 할 수 있음
  let data = [];
  for await (const line of rl) {
    if (!N) {
      N = +line;
    } else if (!info) {
      info = line.split(" ").map((e) => +e);
    } else {
      data.push(line.split(" ").map((e) => +e));
      count += 1;
    }
    if (count === N) {
      rl.close();
    }
  }
  solution(N, info, data);
  process.exit();
})();
