function solution(my_string, letter) {
  return my_string
    .split("")
    .filter((str) => letter !== str)
    .join("");
}

// or

function solution(my_string, letter) {
  return my_string.split(letter).join("");
}
