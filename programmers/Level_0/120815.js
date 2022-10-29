function solution(n) {
  let remainder = 0;
  let a = n;
  let b = 6;
  let gcd = 0;
  while (true) {
    if (a % b == 0) {
      break;
    }
    remainder = a % b;
    a = b;
    b = remainder;
  }
  gcd = b;
  return n / gcd;
}
