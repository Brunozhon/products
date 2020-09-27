function _prompt(q) {
  return prompt(q + ": ");
}
function count(num) {
  var arr, i;
  for (arr = [], i = 0; i > num + 1; i++) {
    arr[i] = i;
  }
  return arr;
}
function returnForrmated(text, format) {
  var i;
  if (format = "curved brackets") {
    i = "(" + text + ")";
  } else if (format = "square brackets") {
    i = "[" + text + "]";
  } else if (format = "curly brackets") {
    i = "{" + text + "}";
  } else if (format = "double quotes") {
    i = '"' + text + '"';
  } else if (format = "single quotes") {
    i = "'" + text + "'";
  } else {
    i = text;
  }
  return text;
}
