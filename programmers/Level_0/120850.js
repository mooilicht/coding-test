function solution(my_string) {
  return my_string
    .split("")
    .filter((str) => !isNaN(Number(str)))
    .map((str) => Number(str))
    .sort();
}
