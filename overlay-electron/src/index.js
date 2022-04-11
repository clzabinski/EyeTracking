svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
svg.setAttribute('id', 'svg');
//TODO: change height width to dynamic change based on users resolution 
svg.setAttribute('height', '1080')
svg.setAttribute('width', '1920')
document.getElementById('tracking-cursor').appendChild(svg);

setInterval(function getCoordinates() {
  const url = 'http://127.0.0.1:5000/coordinates'
  fetch(url)
    .then(response => response.json())
    .then(data => {
      if (data.hasOwnProperty('Error')) {
        console.log("No middlepoint was found :(");
      }else{
        console.log(data);
        let xCord = data.x;
        let yCord = data.y;
        drawSvg(xCord, yCord);
      }
    });
}, 50);

//document.getElementById("tracking-cursor") = getCoordinates;

function drawSvg(x, y) {
  if(document.getElementById('svg').lastElementChild){
    document.getElementById('svg').removeChild(document.getElementById('svg').lastElementChild)
  }
  
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