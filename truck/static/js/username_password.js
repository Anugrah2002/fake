var username_check = 0
function username_validator(username){
    if (username.length <= 16 && username.length >= 6 )
    {
    $.ajax({
        type:'POST',
        url:'/username_checker/',
        data:{
            username : username,
            csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()
            },
        success:function(data){
                if (data == "valid"){
                    document.getElementById('username-text').style.color="green";
                    document.getElementById('username-text').innerHTML = "Available";
                    username_check = 1
                    }
                else if(data == "not_valid"){
                    document.getElementById('username-text').style.color="red";
                    document.getElementById('username-text').innerHTML = "These username is already taken by someone";
                    username_check = 0
                }
            }
    });
    }
    else
        {
       document.getElementById('username-text').style.color="red";
       document.getElementById('username-text').innerHTML="Username must be in 6 to 16 character";
            username_check = 0
        }
}

function owner_registration(){
    name = document.getElementById('id_name').value;
    email = document.getElementById('id_email').value;
    password = document.getElementById('id_password').value;
    if (username_check == 1 && name != "" && email != "" && password != "")
        document.getElementById('owner_registration_form').submit();
}

function add_vehicle(){
    if (username_check == 1)
        document.getElementById('add_vehicle_form').submit();


}