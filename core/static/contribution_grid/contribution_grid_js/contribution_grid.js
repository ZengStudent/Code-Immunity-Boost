// Add squares

var squares;


//==================================
//副程式
//==================================
function showsquare() {
    squares = document.getElementById("qfthf");
    for (var i = 1; i < 365; i++) {
        const level = Math.floor(Math.random() * 3);
        squares.insertAdjacentHTML('beforeend', `<li data-level="${level}"></li>`);
    }
}