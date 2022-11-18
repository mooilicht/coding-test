function solution(age) {
  let answer = "";
  age
    .toString()
    .split("")
    .map((a) => Number(a))
    .forEach((a) => {
      answer += String.fromCharCode(a + 97);
    });
  return answer;
}
