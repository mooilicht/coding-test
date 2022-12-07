function solution(order) {
  let answer = 0;
  order
    .toString()
    .split("")
    .forEach((num) => {
      if (num === "3" || num === "6" || num === "9") answer += 1;
    });
  return answer;
}
