function solution(balls, share) {
  return Math.round(
    factorial(balls) / (factorial(balls - share) * factorial(share))
  );
}

function factorial(num) {
  if (num === 0) return 1;
  else return num * factorial(num - 1);
}
