function solution(my_string, n) {
  let answer = "";
  my_string.split("").forEach((s) => {
    for (let i = 0; i < n; i++) {
      answer += s;
    }
  });
  return answer;
}
