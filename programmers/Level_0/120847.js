function solution(numbers) {
  const sort_num = numbers.sort((a, b) => b - a);
  return sort_num[0] * sort_num[1];
}
