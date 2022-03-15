function initDraw(canvas) {
    var ctx = canvas.getContext("2d")
    ctx.beginPath();
    ctx.rect(20, 20, 150, 100);
    ctx.stroke();
}