function validate(){
    var fname=document.forms['#form']['fname'].value;
    var lname=document.forms['#form']['lname'].value;
    var uname=document.forms['#form']['uname'].value;
    var email=document.forms['#form']['email'].value;
    var phone=document.forms['#form']['phone'].value;    
    var pwd=document.forms['#form']['password'].value;
    var cpwd=document.forms['#form']['confirm password'].value;
    var alphaExp=/^[a-zA-Z]+$/;
    var numExp=/^[0-9]+$/;
    var emailExp=/^[a-zA-Z0-9.]+@[a-zA-Z]+.[a-zA-Z]+$/;
    var unameExp=/^[a-zA-Z0-9]+$/;
    var pwdEXP=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,}$/
    var status=status1=status2=status3=status4=status5=status6=status7=false;
    if (fname==""){
        alert('please enter first name');
        status=false;
    }
    else{
        if (fname.match(alphaExp)){            
            status=true;
        }
        else{
            alert('please enter characters only');
            status=false;
        }
    }
    if(lname==""){
        alert('please enter last name');
        status1=false;
    }
    else{
        if (lname.match(alphaExp)){
            status1=true;
        }
        else{
            alert('please enter characters only');
            status1=false;
        }
    }
    if(email==""){
        alert('please enter email');
        status2=false;
    }
    else{
        if(email.match(emailExp)){
            status2=true;
        }
        else{
            alert('please enter valid email id');
            status2=false;
        }
    }
    if(phone==""){
       alert('please enter phone no');
        status3=false;
    }
    else{
        if(phone.match(numExp)){
            if(phone.length==10){
                status3=true;
            }
            else{
                alert('phone no must have 10 digits');
                status3=false;
            }
        }
        else{
            alert('please enter valid phone no');
            status3=false;
        }
    }
    if(uname==""){
        alert('please enter username');
        status4=false;
    }
    else{
        if(phone.match(unameExp)){
            status4=true;                
            }
        
        else{
            alert('please enter valid username');
            status4=false;
        }
    }
    if (pwd==""){
        alert('please enter password');
        status5=false;
    }
    else{
        if(pwd.match(pwdEXP)){
        status5=true;
        if (cpwd==""){
            alert('please enter confirm password');
            status6=false;
        }
        else{
            if(pwd == cpwd){
            status6=true;} 
        else{
            alert('password and confirm password are not same');
            status6=false;
        } }
        }
        else{
            alert('Must contain at least one number and one uppercase and lowercase letter and one special charater, and at least 8 or more characters');

            status5=true;
        }

    }
    if(dob=""){
        alert('Please enter the date of birth');
        status7=false;
    }
    else{
        status7=true;
    }
    
    if(status==true && status1==true && status2==true && status3==true){
        return true;
    }
    else{
        return false;
    }
    
 }