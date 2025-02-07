document.body.style.transform = "scale(0.25)";  // Extreme zoom out
document.body.style.transformOrigin = "center"; // Centering the scaling effect

// Centering using flexbox (best approach)
document.body.style.display = "flex";
document.body.style.justifyContent = "center";
document.body.style.alignItems = "center";
document.body.style.height = "100vh"; // Full viewport height to keep content centered
document.body.style.overflow = "hidden"; // Prevents scrollbars


//reset animations
setInterval(()=>{
  let el = document.getElementById('love')
  var newone = el.cloneNode(true);
  el.parentNode.replaceChild(newone, el);
}, 4000)
