document.addEventListener('DOMContentLoaded', function() {

    console.log("dom loaded successfully")
    const hamburger = document.getElementById('hamburger');
    const navigation = document.getElementById('navigation');

    hamburger.addEventListener('click', () => {
        console.log('clicked but can you see anything?');

        if(navigation.classList.contains('show')){
            console.log('classlist contains show!!');
            navigation.classList.remove('show');

        }

        else{
            navigation.classList.add('show');
        }

    });
});
