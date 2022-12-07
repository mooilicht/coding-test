function solution(array, n) {
  array.sort((a, b) => a - b);
  let answer = [];
  array.forEach((arr) => answer.push(Math.abs(arr - n)));
  return array[answer.indexOf(Math.min(...answer))];
}
