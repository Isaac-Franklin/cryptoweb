
let returntosignup = document.querySelector('.returntosignup')
let returntologin = document.querySelector('.returntologin')

let loginformproper = document.querySelector('.loginformproper')
let signupformproperinner = document.querySelector('.signupformproperinner')


returntosignup.addEventListener('click', () => {
    loginformproper.classList.add('fadout');
    signupformproperinner.classList.remove('fadout');
    setTimeout(() => {
        loginformproper.style.display = 'none';        
        signupformproperinner.style.display = 'block';
    }, 500);
})


returntologin.addEventListener('click', () => {
    signupformproperinner.classList.add('fadout');
    loginformproper.classList.remove('fadout');
    setTimeout(() => {
        signupformproperinner.style.display = 'none';        
        loginformproper.style.display = 'block';
    }, 500);
})


let flashonboardpop = document.querySelector('.alert strong')
if (flashonboardpop.innerHTML === 'Sorry, User Name Is Already Taken, Please Use Another User Name' || flashonboardpop.innerHTML === 'Sorry, Email Address Is Already Taken' ||  flashonboardpop.innerHTML ===  'Sorry, Phone Number Is Already Taken' || flashonboardpop.innerHTML.includes('Registration Failed')){
    signupformproperinner.style.display = 'block'
    loginformproper.style.display = 'none'
}
console.log(flashonboardpop.innerHTML)

// time for disappearing notifications
let alertonboard = document.querySelector('.alert')
setTimeout(() => { clearInterval(alertonboard); }, 5000); 


// HANDLE FLASH MESSAGES ON DASHBOARD STARTS HERE
let flashonboard = document.querySelector('#flashmessage')
// let flashonboard = document.querySelector('.alert strong')
if(flashonboard){
    setTimeout(() => {
        flashonboard.style.display = 'none'
    }, 5000);
}
// HANDLE FLASH MESSAGES ON DASHBOARD ENDS HERE