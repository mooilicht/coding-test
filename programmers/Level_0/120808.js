function solution(denum1, num1, denum2, num2) {
  const top = denum1 * num2 + denum2 * num1;
  const bottom = num1 * num2;
  let gcd = 1;

  for (let i = 2; i <= Math.min(top, bottom); i++) {
    if (top % i === 0 && bottom % i === 0) {
      gcd = i;
    }
  }

  return [top / gcd, bottom / gcd];
}
