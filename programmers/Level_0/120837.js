function solution(hp) {
  const ants = [5, 3, 1];
  let count = 0;
  ants.forEach((ant) => {
    count += parseInt(hp / ant);
    hp = hp % ant;
  });
  return count;
}
