// HAMBURGER MENU STARTS HERE
let hamburger = document.querySelector('.hamburger')

hamburger.addEventListener('click' , () => {
    hamburger.classList.toggle("active");
  });


let userSectionResponsiveOut = document.querySelector('.userSectionResponsiveOut')
let hamburgerMain = document.querySelector('.hamburgerMain')
let nav = document.querySelector('.nav')

hamburgerMain.addEventListener('click', () => {
    userSectionResponsiveOut.classList.toggle('showIt')
})


// if (document.body.scrollTop >= 200 || document.documentElement.scrollTop >= 200 )
const myNav = document.querySelector('.nav');
window.onscroll = function () {
    if (document.body.scrollTop >= 50 || document.documentElement.scrollTop >= 50 ) {
        myNav.classList.add("nav-colored");
        myNav.classList.remove("nav-transparent");
    } 
    else {
        myNav.classList.add("nav-transparent");
        myNav.classList.remove("nav-colored");
    }
};

// class="VIpgJd-ZVi9od-ORHb" VIpgJd-ZVi9od-ORHb-OEVmcd skiptranslate
setInterval(() => {
    let navtitle = document.querySelector('.navtitle').innerHTML
    // console.log(navtitle)
    if (navtitle !== 'LOGO HERE'){
        nav.classList.add('translateactivestyle')
    }
    else{
        nav.classList.remove('translateactivestyle')
    }
}, 2000);

let cryptoprize = document.querySelectorAll('.cryptoprize')
const apiAccess = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd";
const runData = () => {
    let cryptoData;
    fetch(apiAccess)
        .then((response) => response.json())
        .then((response) => {
            cryptoData = response
            // console.log(cryptoData);
            for (let i = 0; i < cryptoData.length - 50; i++) {
                const element = cryptoData[i];
                let entryDate = '<div class="allscrollsection"><div class="coinandimage"><img src=" ' + element.image + ' "/>' + element.name + '</div><div class="cryptoprize"> $' + element.current_price.toLocaleString() + '</div>  Market Cap:  <div class="cryptocap">$' +  element.market_cap.toLocaleString() + '</div><div class="cryptochange">' + element.price_change_24h + '%</div><div  class="cryptorank"> Rank: ' + element.market_cap_rank + '</div> </div>'
                if (toString(element.price_change_24h).includes('-')){
                    cryptoprize.forEach(e => {
                        e.style.color = 'red';
                    });
                    // cryptoprize.style.color = 'red';
                } else { 
                    cryptoprize.forEach(e => {
                    e.style.color = 'green';
                    });
                    // e.style.color = 'green';
                }
                 document.querySelector(".allscrollsection2").insertAdjacentHTML("beforeend", entryDate);
                // document.querySelector(".scrollbar").innerHTML = entryDate;
            }
        })
}
runData();
// enterStaffUser.forEach(e => {
//     enterStaffUserArr.push(e)
//     if(e === ' '){
//         enterStaffUser = 'None'
//     }    
// });

// let cryptochangeinner = document.querySelector('.cryptochange').innerHTML
// if (cryptochangeinner.includes('-')){
//     console.log(cryptochangeinner)
//     cryptochangeinner.style.color = 'Red'
// }else{
//     cryptochangeinner.style.color = 'green'
// }



var overlay = document.getElementById("overlay");

window.addEventListener('load', function(){
  overlay.style.display = 'none';
})




// time for disappearing notifications
let alertgenonboard = document.querySelector('.alert')
setTimeout(() => { clearInterval(alertgenonboard); }, 5000); 


// HANDLE FLASH MESSAGES ON DASHBOARD STARTS HERE
let flashGeneralonboard = document.querySelector('#flashmessage')
// let flashGeneralonboard = document.querySelector('.alert strong')
if(flashGeneralonboard){
    setTimeout(() => {
        flashGeneralonboard.style.display = 'none'
    }, 5000);
}
// HANDLE FLASH MESSAGES ON DASHBOARD ENDS HERE