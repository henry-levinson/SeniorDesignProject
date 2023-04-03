const buttons = document.querySelectorAll("button");

buttons.forEach(button => {
  button.addEventListener("mouseover", () => {
    button.style.backgroundColor = "#5ec6e8";
  });
  
  button.addEventListener("mouseout", () => {
    button.style.backgroundColor = "#34bbe8";
  });
});
