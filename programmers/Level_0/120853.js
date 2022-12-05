function solution(s) {
  const arr = s.split(" ");
  const answer = [];
  arr.forEach((s) => {
    if (s === "Z") answer.pop();
    else {
      answer.push(Number(s));
    }
  });
  return answer.length != 0 ? answer.reduce((a, b) => a + b) : 0;
}
