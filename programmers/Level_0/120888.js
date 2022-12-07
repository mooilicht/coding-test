function solution(my_string) {
  let my_set = new Set();
  my_string.split("").forEach((str) => my_set.add(str));
  return Array.from(my_set).join("");
}

// or

function solution(my_string) {
  return [...new Set(my_string)].join("");
}
