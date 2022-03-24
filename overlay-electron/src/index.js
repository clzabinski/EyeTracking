svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
svg.setAttribute('id', 'svg');
//TODO: change height width to dynamic change based on users resolution 
svg.setAttribute('height', '1080')
svg.setAttribute('width', '1920')
document.getElementById('tracking-cursor').appendChild(svg);

function getCoordinates() {
  const url = 'http://127.0.0.1:5000/coordinates'
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      let xCord = data.x;
      let yCord = data.y;
      drawSvg(xCord, yCord);
    })
  console.log('PATTER OG PIK haha');
}

//document.getElementById("tracking-cursor") = getCoordinates;

function drawSvg(x, y) {
  circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  circle.setAttribute('r', '20');
  circle.setAttribute('fill', 'transparent');
  circle.setAttribute('stroke', 'red');
  circle.setAttribute('stroke-width', '3');
  circle.setAttribute('cx', `${x}`);
  circle.setAttribute('cy', `${y}`);
  //document.getElementById("screenCoords").innerHTML = xpos + ", " + ypos;
  document.getElementById("svg").appendChild(circle);
}