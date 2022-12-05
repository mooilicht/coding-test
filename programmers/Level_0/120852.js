function solution(n) {
  let answer = new Set();
  while (n % 2 === 0) {
    answer.add(2);
    n /= 2;
  }
  for (let i = 3; i <= n; i += 2) {
    while (n % i === 0) {
      answer.add(i);
      n /= i;
    }
  }
  return Array.from(answer);
}
