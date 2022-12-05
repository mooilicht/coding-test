function solution(n) {
  let num = 0;
  while (true) {
    num += 1;
    let total = 1;
    for (let i = 1; i <= num; i++) {
      total *= i;
    }
    if (total >= n) return total == n ? num : num - 1;
  }
}
