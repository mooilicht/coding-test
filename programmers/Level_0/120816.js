function solution(slice, n) {
  const answer = parseInt(n / slice);
  return n % slice == 0 ? answer : answer + 1;
}
