function loginvalidation(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if(email == "" || password == ""){
        document.getElementById("error").innerHTML = "Please fill all fields";
    }
    else{
        if(email == "admin@gmail.com"){
            if(password == "12345"){
                window.location.href = "address.html";
            }
            else{
                document.getElementById("error").innerHTML = "Invalid Password";
            }
        }
        else{
            document.getElementById("error").innerHTML = "Invalid Email";
        }
    }
}