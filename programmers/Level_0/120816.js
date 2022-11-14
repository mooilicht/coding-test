function solution(slice, n) {
  let pizza = 1;

  while (true) {
    if (pizza * slice >= n) break;
    pizza++;
  }

  return pizza;
}
