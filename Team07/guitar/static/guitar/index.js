
document.addEventListener('DOMContentLoaded', function(){

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
    var access_token;
    //get token
    fetch('getToken')
    .then(response => response.json())
    .then((data) => {
        //console.log("My Token is:")
        access_token = data.access_token;
        //console.log(access_token);
    });
});
