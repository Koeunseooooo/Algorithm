function solution(arr) {
  var answer = [];
  let cnt = {
    0: 0,
    1: 0,
  };
  const isSame = (arr) => {
    arr = arr.flat();
    let cnt_0 = arr.filter((e) => e === 0).length;
    if (cnt_0 == arr.length) {
      return true;
    }
    let cnt_1 = arr.filter((e) => e === 1).length;
    if (cnt_1 == arr.length) {
      return true;
    }
    return false;
  };
  const zip = (arr) => {
    let n = arr.length;
    if (n === 1) {
      cnt[arr[0]] += 1;
      return;
    }
    if (isSame(arr)) {
      cnt[arr[0][0]] += 1;
      return;
    } else {
      let mid = n / 2; // 무조건 정수이므로 Math.floor나 parseInt 해 줄 필요 없음
      zip(arr.slice(0, mid).map((col) => col.slice(0, mid)));
      zip(arr.slice(0, mid).map((col) => col.slice(mid)));
      zip(arr.slice(mid).map((col) => col.slice(mid)));
      zip(arr.slice(mid).map((col) => col.slice(0, mid)));
    }
  };
  zip(arr);
  answer = [cnt[0], cnt[1]];
  // console.log(cnt)
  return answer;
}
