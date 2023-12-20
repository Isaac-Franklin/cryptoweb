
let closearrowdash = document.querySelector('.closearrow')
let maindash = document.querySelector('.main')

closearrowdash.addEventListener('click', () => {
    setTimeout(() => {
		maindash.classList.toggle("mainunmarginleft")       
    }, 500);
})



const apiAccess = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd";
const runData = () => {
    let cryptoData;
    fetch(apiAccess)
        .then((response) => response.json())
        .then((response) => {
			
            cryptoData = response

			// cryptoData.forEach(element => {
			// 	let coindetails1 = document.querySelector('.coindetails1')
			// 	let coindetails2 = document.querySelector('.coindetails2')

			// 	// let coinimg = document.querySelector('.coinimg')
			// 	const coinimg = document.createElement('div');
			// 	coinimg.innerHTML = `${'<img src=' + element.image + '/>'}`;
        	// 	coinimg.classList.add('coinimg');

			// 	// let coinname = document.querySelector('.coinname')
			// 	const coinname = document.createElement('p');
        	// 	coinname.classList.add('coinname');
			// 	coinname.innerHTML = element.name;

			// 	coindetails1.appendChild(coinimg)
			// 	coindetails1.appendChild(coinname)

			// 	// let coinprice = document.querySelector('.coinprice')
			// 	const coinprice = document.createElement('p');
        	// 	coinprice.classList.add('coinprice');
			// 	coinprice.textContent  = element.current_price.toLocaleString();


			// 	// let cointpercentinc = document.querySelector('.cointpercentinc')
			// 	const cointpercentinc = document.createElement('p');
			// 	cointpercentinc.innerHTML = element.price_change_percentage_24h;
        	// 	cointpercentinc.classList.add('cointpercentinc');
			// 	cointpercentinc.innerHTML = element.price_change_percentage_24h;

			// 	coindetails2.appendChild(coinprice)
			// 	coindetails2.appendChild(cointpercentinc)

			// })

            // console.log(cryptoData);
            // for (let i = 0; i < cryptoData.length - 90; i++) {
            for (let i = 0; i < cryptoData.length; i++) {
                const element1 = cryptoData[i];
                // console.log(element1)
                if (element1.id === 'bitcoin'){
                    let bitcoinPrice = element1.current_price.toLocaleString()
                    let bitcoinPriceMain = document.querySelector('#bitcoin-current-price')
                    bitcoinPriceMain.innerHTML = `$${bitcoinPrice}`
                    let bitcoinPriceChange = element1.price_change_percentage_24h
                    let bitcoinChangeMain = document.querySelector('#bitcoin-percent-change')
                    bitcoinChangeMain.innerHTML = `${bitcoinPriceChange}%`
                }
                else if(element1.id === "litecoin"){
                    let litcoinPrice = element1.current_price.toLocaleString()
                    let litecoinPriceMain = document.querySelector('#litecoin-current-price')
                    litecoinPriceMain.innerHTML = `$${litcoinPrice}`
                    let litcoinPriceChange = element1.price_change_percentage_24h
                    let litecoinChangeMain = document.querySelector('#litecoin-percent-change')
                    litecoinChangeMain.innerHTML = `${litcoinPriceChange}%`
                }
                else if(element1.id === "ethereum"){
                    let ethereumPrice = element1.current_price.toLocaleString()
                    let ethereumPriceMain = document.querySelector('#ethereum-current-price')
                    ethereumPriceMain.innerHTML = `$${ethereumPrice}`
                    let ethereumPriceChange = element1.price_change_percentage_24h
                    let ethereumChangeMain = document.querySelector('#ethereum-percent-change')
                    ethereumChangeMain.innerHTML = `${ethereumPriceChange}%`
                }
                else if(element1.id === "cardano"){
                    let cardanoPrice = element1.current_price.toLocaleString()
                    let cardanoPriceMain = document.querySelector('#dash-current-price')
                    cardanoPriceMain.innerHTML = `$${cardanoPrice}`
                    let cardanoPriceChange = element1.price_change_percentage_24h
                    let cardanoChangeMain = document.querySelector('#dash-percent-change')
                    cardanoChangeMain.innerHTML = `${cardanoPriceChange}%`
                }
                else if(element1.id === "ripple"){
                    let ripplePrice = element1.current_price.toLocaleString()
                    let ripplePriceMain = document.querySelector('#ripple-current-price')
                    ripplePriceMain.innerHTML = `$${ripplePrice}`
                    let ripplePriceChange = element1.price_change_percentage_24h
                    let rippleChangeMain = document.querySelector('#ripple-percent-change')
                    rippleChangeMain.innerHTML = `${ripplePriceChange}%`
                }
                else if(element1.id === "binancecoin"){
                    let binancecoinPrice = element1.current_price.toLocaleString()
                    let bnbPriceMain = document.querySelector('#bnb-current-price')
                    bnbPriceMain.innerHTML = `$${binancecoinPrice}`
                    let binancecoinPriceChange = element1.price_change_percentage_24h
                    let bnbChangeMain = document.querySelector('#bnb-percent-change')
                    bnbChangeMain.innerHTML = `${binancecoinPriceChange}%`
                }
                else if(element1.id === "staked-ether"){
                    let staked = element1.current_price.toLocaleString()
                    let stakedPriceMain = document.querySelector('#staked-current-price')
                    stakedPriceMain.innerHTML = `$${staked}`
                    let stakedChange = element1.price_change_percentage_24h
                    let stakedChangeMain = document.querySelector('#staked-percent-change')
                    stakedChangeMain.innerHTML = `${stakedChange}%`
                }
                // console.log(element1)
                
				
                // let entryDate = '<div class="allscrollsection"><div class="coinandimage"><img src=" ' + element.image + ' "/>' + element.name + '</div><div class="cryptoprize"> $' + element.current_price.toLocaleString() + '</div>  Market Cap:  <div class="cryptocap">$' +  element.market_cap.toLocaleString() + '</div><div class="cryptochange">' + element.price_change_24h + '%</div><div  class="cryptorank"> Rank: ' + element.market_cap_rank + '</div> </div> | '
                //  document.querySelector(".allscrollsection2").insertAdjacentHTML("beforeend", entryDate);
				


				//  var list = document.getElementById("myList");
				// 	 let li = document.createElement("li");
				// 	 li.innerText = `${element.name} ${element.current_price.toLocaleString()} ${element.price_change_percentage_24h}`;
				// 	 list.appendChild(li);
				//  })
            }
        })
}

runData();

const date = new Date();

let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();

// This arrangement can be altered based on how we want the date's format to appear.
let currentDate = `${day}-${month}-${year}`;
let lastlogindate = document.querySelector('.lastlogindate')
lastlogindate.innerHTML = currentDate
// console.log(currentDate); // "17-6-2022"



// // CRYPTO TABLE SETUP STARTS HERE
// function getUrl(start = 0) {
//     return 'https://api.coinlore.com/api/tickers/?start=' +  start + '&limit=6';
// }
// function getData(url) {
//     fetch(url)
//         .then(response => response.json())
//         .then(data => loadDataIntoTable(data))
//         .catch(err => console.log(err));
// }

// function loadDataIntoTable(data) {
//     let coinName = [];
//     let coinSymbol = [];
//     let coinRank = [];
//     let coinPrice = [];
//     let coin24Change = [];

//     data['data'].forEach((coin) => {
//         coinName.push(coin.name);
//         coinSymbol.push(coin.symbol);
//         coinRank.push(coin.rank);
//         coinPrice.push(coin.price_usd);
//         coin24Change.push(coin.percent_change_24h);
//     });

//     let tableBody = document.getElementById('crypto-table-body');

//     let html = "";

//     for(let i = 0; i < coinName.length; i++) {
//         html += "<tr>";
//         html += "<td>" + coinName[i] + " (" + coinSymbol[i] + ")" + "</td>";
//         html += "<td>" + coinRank[i] + "</td>";
//         html += "<td>$" + coinPrice[i].toLocaleString() + "</td>";
//         if (coin24Change[i] > 0) {
//             html += "<td class='green-text text-darken-4'>+" + coin24Change[i] + "</td>";
//         } else {
//             html += "<td class='red-text text-darken-4'>" + coin24Change[i] + "</td>";
//         }
        
//         html += "</tr>";
//     }

//     tableBody.innerHTML = html;
// }


// function handleLeftArrowClick(activePageNumber, leftArrow, rightArrow) {
//     //move to previous page
//     let previousPage = document.querySelectorAll('li')[activePageNumber-1];
//     previousPage.classList = "active";
//     url = getUrl(((activePageNumber-1) * 10) - 10);
//     getData(url);
    
//     if (activePageNumber === 10) {
//         enableRightArrow(rightArrow);
//     }

//     if (activePageNumber - 1 === 1) {
//         disableLeftArrow(leftArrow);
//     }
// }

// function handleRightArrowClick(activePageNumber, leftArrow, rightArrow) {
//     //move to next page
//     let nextPage = document.querySelectorAll('li')[activePageNumber+1];
//     nextPage.classList = "active";

//     url = getUrl(((activePageNumber+1) * 10) - 10);
//     getData(url);

//     if (activePageNumber === 1) {
//         enableLeftArrow(leftArrow);
//     }

//     if (activePageNumber + 1 === 10) {
//         disableRightArrow(rightArrow);
//     }
// }

// function disableLeftArrow(leftArrow) {
//     leftArrow.classList = "disabled arrow-left";
// }

// function enableLeftArrow(leftArrow) {
//     leftArrow.classList = "waves-effect arrow-left";
// }

// function disableRightArrow(rightArrow) {
//     rightArrow.classList = "disabled arrow-right";
// }

// function enableRightArrow(rightArrow) {
//     rightArrow.classList = "waves-effect arrow-right";
// }

// function init() {
//     const url = getUrl();
//     getData(url);
// }

// init();

// //handle pagination
// let pageLinks = document.querySelectorAll('a');
// let activePageNumber;
// let clickedLink;
// let leftArrow;
// let rightArrow;
// let url = '';

// pageLinks.forEach((element) => {
//     element.addEventListener("click", function() {
//         leftArrow = document.querySelector('.arrow-left');
//         rightArrow = document.querySelector('.arrow-right');
//         activeLink = document.querySelector('.active');

//         //get active page number 
//         activePageNumber = parseInt(activeLink.innerText);

//         if ((this.innerText === 'chevron_left' && activePageNumber === 1) || (this.innerText === 'chevron_right' && activePageNumber === 10)) {
//             return;
//         }

//         //update active class
//         activeLink.classList = "waves-effect";

//         if (this.innerText === 'chevron_left') {
//             handleLeftArrowClick(activePageNumber, leftArrow, rightArrow);
//         } else if (this.innerText === 'chevron_right') {
//             handleRightArrowClick(activePageNumber, leftArrow, rightArrow);
//         } else {
//             handleNumberClick(this, leftArrow, rightArrow);
//         }

//     });
// });




let copyreferallink = document.querySelector('.copyreferallink');
let referallinkproper = document.querySelector('.copyreferallink input').value;
// const copyContent = async () => {
//   try {
//     await navigator.clipboard.writeText(referallinkproper);
//     console.log(referallinkproper);
//     console.log('Content copied to clipboard');
//   } catch (err) {
//     console.error('Failed to copy: ', err);
//   }
// }

copyreferallink.addEventListener('click', async() => {
    try {
      await navigator.clipboard.writeText(referallinkproper);
      alert(`Your Referal Code (${referallinkproper}) is Copied to Clipboard`)
    } catch (err) {
      console.error('Failed to copy: ', err);
    }

})











