function change_password(){
        let modal = document.getElementById("myModal");
        modal.style.display = "block";
        var span = document.getElementById("close");
        span.focus();
        span.onclick = function() {
        modal.style.display = "none";
               }
    }


function change_password_ajax(){
    var oldPassword = document.getElementById('old_password').value;
    var newPassword = document.getElementById('new_password').value;
    $.ajax({
        type:'POST',
        url:'/change_password/',
        data:{
            old_password : oldPassword,
            new_password : newPassword,
            csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()
            },
        success:function(data){
                if (data == "changed"){
                    document.getElementById('change_password_text').style.color="green";
                    document.getElementById('change_password_text').innerHTML = "Your Password Change Successfully";
                    }
                else if(data == "not_valid"){
                    document.getElementById('change_password_text').style.color="red";
                    document.getElementById('change_password_text').innerHTML = "old Password doesn't match with your password";
                }
            }
    });
}