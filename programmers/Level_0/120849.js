function solution(my_string) {
  const word = ["a", "e", "i", "o", "u"];
  return my_string
    .split("")
    .filter((str) => !word.includes(str))
    .join("");
}
