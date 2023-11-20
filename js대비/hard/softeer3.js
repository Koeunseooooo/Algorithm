//
// 13;
// 8;
// 0000000000000;
// 0110001111000;
// 0110001001000;
// 0000001001000;
// 0000111011000;
// 0000101001000;
// 0000111111000;
// 0000000000000;

// 30;
// 0.7;
// 0.1;
// 4;

// 30;
// 12;
// 000000000000000000000000000000;
// 011111111111111011111111110110;
// 010000000000001010000100010110;
// 010111111100001010000100010110;
// 010100011100001010000100010110;
// 010101011100001010000100010110;
// 010101011100001010000100010110;
// 010100011100001010000100010110;
// 010111111100001010000100010110;
// 010000000000001010000100010110;
// 011111111111111011111111110110;
// 000000000000000000000000000000;

// 140
// .96
// ..42
// ...12
// ....2
// 100
// .32
// .24
// 20

// Run by Node.js
const readline = require("readline");

let dy = [-1, 0, 1, 0];
let dx = [0, 1, 0, -1];

const bfs = (x, y, checked, rx, ry, data, value) => {
  q = [];
  q.push([x, y]);
  checked[x][y] = 0;
  let cnt = 1;
  while (q.length) {
    let [x, y] = q.shift();
    for (let i = 0; i < 4; i++) {
      let X = x + dx[i];
      let Y = y + dy[i];
      if (
        0 <= X &&
        X < rx &&
        0 <= Y &&
        Y < ry &&
        data[X][Y] === value &&
        checked[X][Y] == -1
      ) {
        q.push([X, Y]);
        checked[X][Y] = 0;
        cnt += 1;
      }
    }
  }
  return cnt;
};

const bfs1 = (x, y, checked, rx, ry, data, value, level) => {
  // console.log(x, y, 99);
  let target = [];
  let flag = 0;
  q = [];
  q.push([x, y]);
  if (checked[x][y] != -1) {
    return 0;
  }
  checked[x][y] = level;
  let cnt = 1;

  while (q.length) {
    let [x, y] = q.shift();
    for (let i = 0; i < 4; i++) {
      let X = x + dx[i];
      let Y = y + dy[i];

      if (0 <= X && X < rx && 0 <= Y && Y < ry && checked[X][Y] == -1) {
        if (data[X][Y] == value) {
          q.push([X, Y]);
          checked[X][Y] = level;
          cnt += 1;
        } else {
          target.push([X, Y]);
        }
      }
    }
  }

  if (target.length >= 1) {
    target.forEach((e) => {
      let [x, y] = e;
      let c = bfs1(x, y, checked, rx, ry, data, (value + 1) % 2, level + 1);
      if (c !== 0) {
        console.log(c);
      }
    });
  }
  return [cnt, level];
};

const solution = (rx, ry, data) => {
  let checked = Array.from({ length: rx }, () => Array(ry).fill(-1));

  bfs(0, 0, checked, rx, ry, data, 0);
  for (let i = 0; i < rx; i++) {
    for (let j = 0; j < ry; j++) {
      if (checked[i][j] === 0) {
        data[i][j] = -1;
        checked[i][j] == -1;
      }
    }
  }
  let level = -100;
  for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[0].length; j++) {
      if (checked[i][j] === -1 && data[i][j] !== -1) {
        for (let k = 0; k < 4; k++) {
          let X = i + dx[k];
          let Y = j + dy[k];
          if (checked[X][Y] !== -1) {
            level = checked[X][Y];
            // console.log(level, 3);
          }
        }
        let [a, b] = bfs1(i, j, checked, rx, ry, data, data[i][j], level + 1);
        console.log(a, b);
        console.log("---");
      }
      // break
    }
  }
};

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let x = null;
  let y = null;
  let count = 0;
  let data = [];
  for await (const line of rl) {
    if (!x) {
      x = +line; // +는 형변환을 바로 해주기 위함임
    } else if (!y) {
      y = +line;
    } else {
      data.push(Array.from(line).map((el) => parseInt(el, 10)));
      count += 1;
    }
    if (count === y) {
      rl.close();
    }
  }

  solution(y, x, data);
  process.exit();
})();
