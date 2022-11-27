function solution(rsp) {
  let answer = "";
  for (i in rsp) {
    if (rsp[i] === "2") answer += "0";
    else if (rsp[i] === "0") answer += "5";
    else answer += "2";
  }
  return answer;
}
