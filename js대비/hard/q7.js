// 5 -2
// 강미나 김도연 김세정 김소혜 김청하
// 유연정 임나영 전소미 정채연 주결경
// 최유정 강시라 기희현 김나영 김소희
// 박소연 윤채경 이해인 전소연 정은우
// 한혜리 강예빈 권은빈 김다니 김서경

// 김세정 김소혜 김청하 주결경 김소희
// 김도연 윤채경 강시라 임나영 정은우
// 강미나 이해인 기희현 전소미 김서경
// 유연정 전소연 김나영 정채연 김다니
// 최유정 박소연 한혜리 강예빈 권은빈

// w의 부호 : 가장 바깥 테두리의 회전 방향 결정
// w가 양수 : 시계 방향, 음수 : 반시계 방향
const solution = (info, data) => {
  let [l, w] = info; // 배열 총 길이, 회전 방향
  let n = parseInt(l / 2, 10);
  console.log(l, n, 3, 4 * (l - 1));
  let r_flag = 1;
  if (w < 0) {
    r_flag = 0;
  }
  w = Math.abs(w);
  for (let i = 0; i < n; i++) {
    w = w % (4 * (l - 1));
    console.log(w);
  }
};
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let info = null;
  let count = 0;
  let data = [];
  for await (const line of rl) {
    if (!info) {
      info = line.split(" ").map((e) => +e);
      console.log(info);
    } else {
      data.push(line.split(" ").map((e) => e));
      count += 1;
    }
    if (count === info[0]) {
      rl.close();
    }
  }
  solution(info, data);
  process.exit();
})();
