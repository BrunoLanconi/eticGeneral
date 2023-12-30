const ss = document.styleSheets;

for (let i = 0; i < ss.length; i++) {
  for (let j = 0; j < ss[i].cssRules.length; j++) {
    dump(`${ss[i].cssRules[j].selectorText}\n`);
  }
}
