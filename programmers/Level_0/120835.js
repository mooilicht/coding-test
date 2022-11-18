function solution(emergency) {
  let emerSort = [...emergency].sort((a, b) => b - a);
  let answer = [];
  emergency.forEach((e) => {
    answer.push(emerSort.indexOf(e) + 1);
  });
  return answer;
}
