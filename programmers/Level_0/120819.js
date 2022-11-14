function solution(money) {
  return [parseInt(money / 5500), money % 5500];
}

// or

const solution = (money) => [parseInt(money / 5500), money % 5500];
