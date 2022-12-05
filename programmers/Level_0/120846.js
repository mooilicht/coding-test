function solution(n) {
  let answer = 0;
  for (let i = 1; i <= n; i++) {
    let count = 0;
    for (let j = 1; j <= parseInt(i ** 0.5); j++) {
      if (i % j == 0) count += 1;
    }
    if (count > 1) answer += 1;
  }
  return answer;
}
