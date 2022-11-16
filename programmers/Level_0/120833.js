function solution(numbers, num1, num2) {
  const answer = [];
  for (let n = num1; n <= num2; n++) {
    answer.push(numbers[n]);
  }
  return answer;
}
