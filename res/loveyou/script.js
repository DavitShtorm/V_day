document.body.style.transform = "scale(0.25)"; // Adjust scale value (0.1 is extreme zoom out)
document.body.style.transformOrigin = "top left"; // Prevents misalignment

//reset animations
setInterval(()=>{
  let el = document.getElementById('love')
  var newone = el.cloneNode(true);
  el.parentNode.replaceChild(newone, el);
}, 4000)
