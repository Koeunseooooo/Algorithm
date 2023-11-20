var arr = [];
var arr = [1, 2, 3, 4, 5];

// 1차원 배열
// 1. 0으로 초기화
var arr = Array.from({ length: 5 }, () => 0);
// 2. 1씩 증가
var arr = Array.from({ length: 5 }, (v, c) => c);
console.log(arr);
var arr = new Array(5).fill(0);
var arr;
(arr = []).length = 5;
arr.fill(1);
console.log(arr);

// 2차원 배열
// 1. 0으로 초기화
var arr = Array.from({ length: 5 }, () => Array(5).fill(0));
console.log(arr);

// 2. 1씩 증가
var arr = [...Array(5)].map((v, r) =>
  [...Array(5)].map((v, c) => 5 * r + (c + 1))
);
console.log(arr);

console.log(!1);
console.log(false == 0);
