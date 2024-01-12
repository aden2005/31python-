const item = document.querySelector(".item");
const placeholders = document.querySelectorAll(".placeholder");

item.addEventListener("dragstart", dragstart);
item.addEventListener("dragend", dragend);

for (const placeholder of placeholders) {
  placeholder.addEventListener("dragover", dragover);
  placeholder.addEventListener("drop", drop);
}

function dragstart(event) {
  event.target.classList.add("hold");
  setTimeout(() => event.target.classList.add("hide"), 0);
  console.log(event.target);
}

function dragend(event) {
  event.target.className = "item";
  console.log(event.target);
}

function dragover(event) {
  event.preventDefault();
}

function drop(event) {
  event.target.append(item);
}
