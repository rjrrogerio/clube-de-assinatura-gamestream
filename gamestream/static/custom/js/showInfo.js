
var button = document.getElementById('icon');
var button2 = document.getElementById('icon2');
var button3 = document.getElementById('icon3');

button.addEventListener('click', function(){

    var container = document.getElementById('container');

    if(container.style.display === 'none') {
        container.style.display = 'block';
    }else {
        container.style.display = 'none';
    }

});

button2.addEventListener('click', function(){

    var container2 = document.getElementById('container2');

    if(container2.style.display === 'none') {
        container2.style.display = 'block';
    }else {
        container2.style.display = 'none';
    }

});

button3.addEventListener('click', function(){

    var container3 = document.getElementById('container3');

    if(container3.style.display === 'none') {
        container3.style.display = 'block';
    }else{
        container3.style.display = 'none';
    }
});








