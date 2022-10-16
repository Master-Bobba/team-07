
document.addEventListener('DOMContentLoaded', function(){

    console.log("THIS IS CALLED")
    fetch('is-authenticated')
    .then((response) => response.json())
    .then((data) => {
        //console.log(data.status);
        if (!data.status){
            //authenticate
            fetch('get-auth-url')
            .then(response => response.json())
            .then((data) => {
            window.location.replace(data.url);
            });
        }
    });
});
