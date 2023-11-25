// // if (document.body.scrollTop >= 200 || document.documentElement.scrollTop >= 200 )
// console.log('active')
// const myNav = document.querySelector('.nav');
// window.onscroll = function () { 
//     if (document.body.scrollTop >= 200 ) {
//         myNav.classList.add("nav-colored");
//         myNav.classList.remove("nav-transparent");
//     } 
//     else {
//         myNav.classList.add("nav-transparent");
//         myNav.classList.remove("nav-colored");
//     }
// };



// const apiAccess = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd";


// const runData = () => {
//     let cryptoData;
//     fetch(apiAccess)
//         .then((response) => response.json())
//         .then((response) => {
//             cryptoData = response, console.log(cryptoData);
//             for (let i = 0; i < cryptoData.length - 80; i++) {
//                 const element = cryptoData[i];
//                 console.log(element);
//                 // let entryDate = '<table><tr><td class="coinandimage"><img src=" ' + element.image + ' "/>' + element.id + '</td><td>$' + element.current_price + '</td><td>$' + element.market_cap + '</td><td>%' + element.price_change_24h + '</td><td>' + element.market_cap_rank + '</td></tr></table>'
//             //     document
//             //         .querySelector("table")
//             //         .insertAdjacentHTML("beforeend", entryDate);
//             }
//         })
// }
// runData();





class CountUp {
    constructor(triggerEl, counterEl) {
    const counter = document.querySelector(counterEl)
    const trigger = document.querySelector(triggerEl)
    let num = 0
    const decimals = counter.dataset.decimals
  
    const countUp = () => {
      if (num < counter.dataset.stop)
        
        // Do we want decimals?
        if (decimals) {
          num += 0.01
          counter.textContent = new Intl.NumberFormat('en-GB', { 
            minimumFractionDigits: 2,
            maximumFractionDigits: 2 
  }).format(num)
     }
      else {
        // No decimals
        num++
        counter.textContent = num
      }
    }
    
    const observer = new IntersectionObserver((el) => {
      if (el[0].isIntersecting) {
        const interval = setInterval(() => {
          (num < counter.dataset.stop) ? countUp() : clearInterval(interval)
        }, counter.dataset.speed)
      }
    }, { threshold: [0] })
  
    observer.observe(trigger)
    }
  }
  
  // Initialize any number of counters:
  new CountUp('#start1', '#counter3')
  new CountUp('#start1', '#counter2')
  new CountUp('#start1', '#counter1')
  new CountUp('#start1', '#counter4')







var navbar = document.querySelector('nav')
var google_translate_element = document.querySelector('#google_translate_element')

window.onscroll = function() {

  // pageYOffset or scrollY
  if (window.scrollY > 0) {
    navbar.classList.add('scrolled')
    google_translate_element.classList.add('scrolled')
  } else {
    navbar.classList.remove('scrolled')
    google_translate_element.classList.remove('scrolled')
  }
}

let visionin = document.querySelector('.visionin')
let missionin = document.querySelector('.missionin')
let vision = document.querySelector('.vision')
let mission = document.querySelector('.mission')


vision.addEventListener('click', () => {
    missionin.style.display = 'none'
    visionin.style.display = 'block'
    vision.classList.remove('inactive')
    vision.classList.add('active')
    mission.classList.add('inactive')
    mission.classList.remove('active')
})


mission.addEventListener('click', () => {
    missionin.style.display = 'block'
    visionin.style.display = 'none'
    vision.classList.add('inactive')
    vision.classList.remove('active')
    mission.classList.remove('inactive')
    mission.classList.add('active')
})



var overlay = document.getElementById("overlay");

window.addEventListener('load', function(){
  overlay.style.display = 'none';
})
















