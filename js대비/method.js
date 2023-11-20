// parseInt
console.log(parseInt("100", 10)); // 2번째 인자 필수
console.log(parseInt(123.6, 10)); // 소수점 절사

let arr1 = [1, 2, 3, 4];
let arr2 = [5, 6, 7, 8];

console.log(arr1.concat(arr2));
console.log(arr1); // 원본은 그대로임

// arr 항목 추가 또는 삭제
arr = [1, 2, 3, 4, 5];
console.log(arr);

arr.push(6);
console.log(arr);

arr.pop();
console.log(arr);

arr.shift(); // python의 arr.popleft()와 동일함
console.log(arr);

// splice
// 요소를 삭제하거나 교체 (단순 추가 가능)

let s_arr = ["one", "two", "three", "four"];
let del = s_arr.splice(2);
console.log(s_arr);
console.log(del); // 인덱스 2부터 배열 변경하겠다는 뜻
console.log(del.splice(0, 1)); // 2인자 : 배열에서 제거할 요소의 수 지정
console.log(del);

let s1_arr = [1, 2, 3, 4, 5, 6, 7, 8];

let s1_del = s1_arr.splice(2, 2, "hello", "hell", "add"); // deleteCount 초과하여 newItem 추가 가능
console.log(s1_del);
console.log(s1_arr);
s1_arr.splice(5, 0, "add2");
console.log(s1_arr);

// slice & length
var arr = [2, 3, 4, 6, 8, 2];
console.log(arr.slice(1, 2)); // 새로운 배열로 반환함
console.log(arr);
console.log(arr.length);

// fill
var arr = [1, 2, 3, 4, 5];
console.log(arr.fill(0));
console.log(arr.fill(1, 1, 3));
console.log(arr.fill(5, 2));

// filter
var score = [10, 40, 50, 20, 80];
console.log(score.filter((x) => x <= 40));
console.log(score);

// flat
var matrix = [1, 2, 3, [1, 2, 3, [10, 20]]];
console.log(matrix.flat()); // 한 번만 깜
console.log(matrix.flat(2)); // 두 번 깜

// includes
console.log(score.includes(50));
console.log(score.includes(90));

// join (배열의 요소를 특정 값으로 이어 붙여 문자열 생성)
console.log(score.join("-"));
console.log(typeof score.join(" "));

// map (배열을 순회하며 함수를 실행한 결과로 새로운 배열을 만들어 반환)
var arr = [1, 2, 3, 4, 5];
console.log(
  arr.map((x) => {
    return x ** 2;
  })
);
console.log(arr);

// sort (유니코드 정렬이 기본임 주의)
var arr = [1, 2, 100, 200, 300, 3, 33];
arr.sort();
console.log(arr);

// sort (오름차순 정렬)
var arr = [40, 80, 75, 90, 35, 81];
arr.sort((a, b) => {
  return a - b;
});
console.log(arr);

// sort (내림차순 정렬)
var arr = [40, 80, 75, 90, 35, 81];
arr.sort((a, b) => {
  return b - a; // 반환값이 양수일때만 swap됨
});
console.log(arr);

// sort (문자 오름차순 정렬)
var arr = ["C", "A", "B", "D"];
arr.sort();
console.log(arr);

// sort (문자 내림순 정렬)
var arr = ["C", "A", "B", "D"];
arr.sort((a, b) => {
  if (a > b) {
    return -1; // 두 문자를 비교했을 때 앞 문자가 더 크다면 swap할 필요 없으니 음수값 반환
  } else if (a < b) {
    return 1;
  } else {
    return 0;
  }
});
console.log(arr);

// reverse()
var arr = [1, 2, 3, 4, 5];
console.log(arr.reverse());

// set()
var arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5];
let s = new Set(arr);
console.log(s);

// set은 list와 달리 length가 아닌 size로 길이를 구할 수 있다
console.log(s.size);
console.log(s.length);

console.log(s.add(7));
console.log(s.has(3));
s.delete(5);
console.log(s);
s.clear();
console.log(s);

// map (key와 value를 같이 저장하는 객체)
var m = new Map();
m.set("one", 1);
m.set("two", 2);
m.set("three", 3);
console.log(m);
console.log(m.has("one")); // has는 객체 내 주어진 키의 값을 기준으로 존재하는 지 판단함
console.log(m.has(1));

// for-of문으로 map 순회하기
for (let [key, value] of m) {
  console.log(`${key}:${value}`);
}

// string
let str1 = "복잡한 세상 편하게 살자";
console.log(str1.split(" "));
console.log(str1.replace("편하게", "힘들게"));

// 정규표현식 활용
var str = "abc abcd abcde ab cd def";
console.log(str.replace(/abc/g, "!"));
console.log(str.replace(/ /g, "!"));

var str = "눈떠보니 코딩 테스트 전날";
console.log(str.indexOf("코딩 테스트"));
console.log(str.slice(5, 11));

var str = "abc abcd abcde ab cd def ABC";
let re = /abc/gi; //전역에서 대소문자 구별하지 않고 찾겠다!

console.log(str.match(re)); //["abc", "abc", "abc", "ABC"]

// toLowerCase(), toUpperCase()
var str = "abcABCdeFg";
console.log(str.toLowerCase());
console.log(str.toUpperCase());

// 여러 형태의 for 문
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let result = 0;

// 1 for
for (let i = 0; i < arr.length; i++) {
  result += arr[i];
}
console.log(result);

// 2 for in
let result2 = 0;
for (let i in arr) {
  result2 += arr[i];
}
console.log(result2);

// 3 for of (python의 in과 똑같음)
let result3 = 0;
for (let a of arr) {
  result3 += a;
}

// 4 forEach (오직 array 객체일때만 가능)
let result4 = 0;
arr.forEach((x) => {
  result4 += x;
});
console.log(result4);

// math
console.log(Math.abs(-4));
console.log(Math.max(3, 4, 5));
console.log(Math.min(3, 10));
console.log(Math.pow(2, 4));
console.log(Math.random());
console.log(Math.round(3.12));
console.log(Math.round(3.89));

// 배열 초기화
var arr = new Array(5).fill(0);
console.log(arr);

// 2차원 배열 생성 및 0으로 초기화
var r = 5;
var c = 5;
var arr = Array.from(new Array(c), () => new Array(r).fill(0));
console.log(arr);
var arr = Array.from({ length: c }, () => new Array(r).fill(0));
console.log(arr);

// 2차원 배열 생성 및 0으로 초기화
var arr = Array.from(new Array(r), (v, r) => {
  return Array.from({ length: 5 }, (v, c) => r * 5 + (c + 1));
});
console.log(arr);

var arr = Array.from({ length: c }, () => new Array(r).fill(0));
console.log(arr);

for (let i = 0; i < r; i++) {
  for (let j = 0; j < c; j++) {
    arr[i][j] = i * c + j;
    console.log(arr[i][j]);
  }
}

arr.forEach((rowArr) =>
  rowArr.forEach((col) => {
    console.log(col);
  })
);

var arr = Array.from({ length: c }, () => new Array(r).fill(0));
console.log(arr);

// 문자열 -> 배열
var str = "hello";
var arr = Array.from(str);
console.log(arr);
var arr = [...str];
console.log(arr);

// 비교함수 정의하여 정렬하기
var arr = [
  [3, 2],
  [3, 1],
  [1, 2],
  [1, 4],
  [4, 3],
];
arr = arr.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
console.log(arr);

// slice & length
var arr = [2, 3, 4, 6, 8, 2];
console.log(arr.slice(1, 5)); // 새로운 배열로 반환함
