function solution(numbers) {
  let answer = [];
  for (i in numbers) {
    answer.push(numbers[i] * 2);
  }
  return answer;
}

// or

const solution = (numbers) => numbers.map((number) => number * 2);
