function move_guard() {
    let elements = document.querySelectorAll('.my-element');
    let i;

    for (i = 0; i < elements.length; i++) {
        //console.log(Math.round((i+1)/2));
        elements[i].classList.add('animate__animated', 'animate__zoomOutDown','animate__delay-'+Math.round((i+1)/2)+'s');
        //elements[i].classList.add('animate__animated', 'animate__zoomOutDown','animate__delay-3s');
    }

}



function move_aggression() {
    let elements = document.querySelectorAll('.my-element');
    let i;

    for (i = 0; i < elements.length; i++) {
        elements[i].classList.add('animate__animated', 'animate__zoomOutDown','animate__delay-'+Math.round((i+1)/2)+'s');
    }
}