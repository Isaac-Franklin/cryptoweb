
// 
let planselectedselected = document.querySelector('.planselectedselected input').value;
planselectedselected = "bronzeplan"
let planselectedselectedmain = "bronzeplan";


let planproperone = document.querySelector('.planproperone')
let planpropertwo = document.querySelector('.planpropertwo')
let planproperthree = document.querySelector('.planproperthree')
let planproperfour = document.querySelector('.planproperfour')


let arrowdownone = document.querySelector('.arrowdownone')
let arrowdowntwo = document.querySelector('.arrowdowntwo')
let arrowdownthree = document.querySelector('.arrowdownthree')
let arrowdownfour = document.querySelector('.arrowdownfour')


planproperone.addEventListener('click', () => {
    planproperone.classList.remove('activeplan');
    arrowdownone.style.display = 'none';
    planpropertwo.classList.remove('activeplan');
    arrowdowntwo.style.display = 'none';
    planproperthree.classList.remove('activeplan');
    arrowdownthree.style.display = 'none';
    planproperfour.classList.remove('activeplan');
    arrowdownfour.style.display = 'none';
    
    planproperone.classList.add('activeplan');
    arrowdownone.style.display = 'block';
    planselectedselectedmain = "bronzeplan"
})


planpropertwo.addEventListener('click', () => {
    planproperone.classList.remove('activeplan');
    arrowdownone.style.display = 'none';
    planproperthree.classList.remove('activeplan');
    arrowdownthree.style.display = 'none';
    planproperfour.classList.remove('activeplan');
    arrowdownfour.style.display = 'none';
    
    planpropertwo.classList.add('activeplan');
    arrowdowntwo.style.display = 'block';
    planselectedselectedmain = "silverplan"
})


planproperthree.addEventListener('click', () => {
    planproperone.classList.remove('activeplan');
    arrowdownone.style.display = 'none';
    planpropertwo.classList.remove('activeplan');
    arrowdowntwo.style.display = 'none';
    planproperfour.classList.remove('activeplan');
    arrowdownfour.style.display = 'none';

    planproperthree.classList.add('activeplan');
    arrowdownthree.style.display = 'block';
    planselectedselectedmain = "goldplan"
})


planproperfour.addEventListener('click', () => {
    planproperone.classList.remove('activeplan');
    arrowdownone.style.display = 'none';
    planpropertwo.classList.remove('activeplan');
    arrowdowntwo.style.display = 'none';
    planproperthree.classList.remove('activeplan');
    arrowdownthree.style.display = 'none';

    planproperfour.classList.add('activeplan');
    arrowdownfour.style.display = 'block';
    planselectedselectedmain = "diamondplan"
})

setInterval(() => {
    document.querySelector('.planselectedselected input').value = planselectedselectedmain;
}, 1000);




















