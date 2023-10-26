let arr = [2, 3, 5, 7];

arr.map(function (element, index) {
  console.log(element);
  console.log(index);
  console.log(this);
  return element;
}, 80);
