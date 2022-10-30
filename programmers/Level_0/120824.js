function solution(num_list) {
  let even = 0;
  let odd = 0;
  for (i in num_list) {
    if (num_list[i] % 2 == 0) {
      even++;
    } else {
      odd++;
    }
  }
  return [even, odd];
}
