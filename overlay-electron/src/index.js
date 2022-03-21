function findScreenCoords(mouseEvent)
{
  var xpos;
  var ypos;
  if (mouseEvent)
  {
    //FireFox
    xpos = mouseEvent.screenX;
    ypos = mouseEvent.screenY;
  }
  else
  {
    //IE
    xpos = window.event.screenX;
    ypos = window.event.screenY;
  }
  document.getElementById("screenCoords").innerHTML = xpos + ", " + ypos;
  console.log(xpos + "," + ypos);
}
document.getElementById("tracking-cursor").onmousemove = findScreenCoords;
