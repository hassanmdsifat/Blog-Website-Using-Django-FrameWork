function my_function()
{
    let email=document.getElementById("email")
    let emailtext=email.value;
    emailtext=emailtext.trim()
    let message=document.getElementById("textcomments");
    let text=message.value
    text=text.trim()
    if(text=="")
    {
        alert("Comments Cannot Be Empty!!");
        return false;
    }
    else if(emailtext=="")
    {
        alert("Email Cannot Be Empty!!!");
        return false;
    }
    else
    {
        alert("Comments Posted!!");
        return true;
    }
}