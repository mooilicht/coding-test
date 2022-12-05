function solution(my_string) {
  const numbers = my_string
    .split("")
    .filter((str) => !isNaN(Number(str)))
    .map((str) => Number(str));
  let sum = 0;
  numbers.forEach((num) => (sum += num));
  return sum;
}
