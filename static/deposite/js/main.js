
let goldplanpop = document.querySelector('.goldplanpop')
let silverplanpop = document.querySelector('.silverplanpop')
let bronzeplanpop = document.querySelector('.bronzeplanpop')
let diamondplanpop = document.querySelector('.diamondplanpop')
let shadow = document.querySelector('.shadow')
let planpopupcancel = document.querySelectorAll('.planpopupcancel')

let choosegoldplan = document.querySelector('.choosegoldplan')
let choosesilverplan = document.querySelector('.choosesilverplan')
let choosebronzeplan = document.querySelector('.choosebronzeplan')
let choosediamondplan = document.querySelector('.choosediamondplan')


choosegoldplan.addEventListener('click', () => {
    goldplanpop.style.display = 'block'
    silverplanpop.style.display = 'none'
    bronzeplanpop.style.display = 'none'
    diamondplanpop.style.display = 'none'
    shadow.style.display = 'block'
})

choosesilverplan.addEventListener('click', () => {
    silverplanpop.style.display = 'block'
    goldplanpop.style.display = 'none'
    diamondplanpop.style.display = 'none'
    bronzeplanpop.style.display = 'none'
    shadow.style.display = 'block'
})

choosebronzeplan.addEventListener('click', () => {
    bronzeplanpop.style.display = 'block'
    goldplanpop.style.display = 'none'
    silverplanpop.style.display = 'none'
    diamondplanpop.style.display = 'none'
    shadow.style.display = 'block'
})

choosediamondplan.addEventListener('click', () => {
    diamondplanpop.style.display = 'block'
    bronzeplanpop.style.display = 'none'
    goldplanpop.style.display = 'none'
    silverplanpop.style.display = 'none'
    shadow.style.display = 'block'
})

planpopupcancel.forEach(e => {
    e.addEventListener('click', () => {
        goldplanpop.style.display = 'none'
        silverplanpop.style.display = 'none'
        bronzeplanpop.style.display = 'none'
        shadow.style.display = 'none'
        diamondplanpop.style.display = 'none'
    })
});




// time for disappearing notifications
let alertdeposite = document.querySelector('.alert')
setTimeout(() => { clearInterval(alertdeposite); }, 5000); 


// HANDLE FLASH MESSAGES ON DASHBOARD STARTS HERE
let flashdeposite = document.querySelector('#flashmessage')
// let flashdeposite = document.querySelector('.alert strong')
if(flashdeposite){
    setTimeout(() => {
        flashdeposite.style.display = 'none'
    }, 5000);
}
// HANDLE FLASH MESSAGES ON DASHBOARD ENDS HERE