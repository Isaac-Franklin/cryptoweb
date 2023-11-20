

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
                let entryDate = '<div class="allscrollsection"><div class="coinandimage"><img src=" ' + element.image + ' "/>' + element.name + '</div><div class="cryptoprize"> $' + element.current_price.toLocaleString() + '</div>  Market Cap:  <div class="cryptocap">$' +  element.market_cap.toLocaleString() + '</div><div class="cryptochange">' + element.price_change_24h + '%</div><div  class="cryptorank"> Rank: ' + element.market_cap_rank + '</div> </div> | '
                // if (toString(element.price_change_24h).includes('-')){
                //     cryptoprize.forEach(e => {
                //         e.style.color = 'red';
                //     });
                //     // cryptoprize.style.color = 'red';
                // } else { 
                //     cryptoprize.forEach(e => {
                //     e.style.color = 'green';
                //     });
                //     // e.style.color = 'green';
                // }
                 document.querySelector(".allscrollsection2").insertAdjacentHTML("beforeend", entryDate);
                // document.querySelector(".scrollbar").innerHTML = entryDate;
            }
        })
}
runData();




var overlay = document.getElementById("overlay");

window.addEventListener('load', function(){
  overlay.style.display = 'none';
})

let navmainmenuintro = document.querySelector('.navmainmenuintro img')
let navminimenuintro = document.querySelector('.navminimenuintro')
let navmainmenumini = document.querySelector('.navmainmenumini')
let navmainmenu = document.querySelector('.navmainmenu')
let navmainmenuintroTxts = document.querySelectorAll('.allsection p')

navminimenuintro.addEventListener('click', () => {
    setTimeout(() => {        
        navmainmenuintroTxts.forEach(e => {
            e.style.display = 'none'})
    }, 0);
    navmainmenu.classList.add('hidemenu')    
    setTimeout(() => {
        navmainmenumini.style.display = 'none'
    }, 100);
    setTimeout(() => {        
        navmainmenuintroTxts.forEach(e => {
            e.style.display = 'block'})
    }, 800);
    navmainmenu.style.display = 'block'    
})

navmainmenuintro.addEventListener('click', () => {
    navmainmenumini.classList.add('showmenu')
    setTimeout(() => {
        navmainmenu.style.display = 'none'
    }, 100);
    navmainmenumini.style.display = 'block'
})





