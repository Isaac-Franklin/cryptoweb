

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
            for (let i = 0; i < cryptoData.length - 90; i++) {
                const element1 = cryptoData[i];
				
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



// CRYPTO TABLE SETUP STARTS HERE
function getUrl(start = 0) {
    return 'https://api.coinlore.com/api/tickers/?start=' +  start + '&limit=6';
}
function getData(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => loadDataIntoTable(data))
        .catch(err => console.log(err));
}

function loadDataIntoTable(data) {
    let coinName = [];
    let coinSymbol = [];
    let coinRank = [];
    let coinPrice = [];
    let coin24Change = [];

    data['data'].forEach((coin) => {
        coinName.push(coin.name);
        coinSymbol.push(coin.symbol);
        coinRank.push(coin.rank);
        coinPrice.push(coin.price_usd);
        coin24Change.push(coin.percent_change_24h);
    });

    let tableBody = document.getElementById('crypto-table-body');

    let html = "";

    for(let i = 0; i < coinName.length; i++) {
        html += "<tr>";
        html += "<td>" + coinName[i] + " (" + coinSymbol[i] + ")" + "</td>";
        html += "<td>" + coinRank[i] + "</td>";
        html += "<td>$" + coinPrice[i].toLocaleString() + "</td>";
        if (coin24Change[i] > 0) {
            html += "<td class='green-text text-darken-4'>+" + coin24Change[i] + "</td>";
        } else {
            html += "<td class='red-text text-darken-4'>" + coin24Change[i] + "</td>";
        }
        
        html += "</tr>";
    }

    tableBody.innerHTML = html;
}


function handleLeftArrowClick(activePageNumber, leftArrow, rightArrow) {
    //move to previous page
    let previousPage = document.querySelectorAll('li')[activePageNumber-1];
    previousPage.classList = "active";
    url = getUrl(((activePageNumber-1) * 10) - 10);
    getData(url);
    
    if (activePageNumber === 10) {
        enableRightArrow(rightArrow);
    }

    if (activePageNumber - 1 === 1) {
        disableLeftArrow(leftArrow);
    }
}

function handleRightArrowClick(activePageNumber, leftArrow, rightArrow) {
    //move to next page
    let nextPage = document.querySelectorAll('li')[activePageNumber+1];
    nextPage.classList = "active";

    url = getUrl(((activePageNumber+1) * 10) - 10);
    getData(url);

    if (activePageNumber === 1) {
        enableLeftArrow(leftArrow);
    }

    if (activePageNumber + 1 === 10) {
        disableRightArrow(rightArrow);
    }
}

function disableLeftArrow(leftArrow) {
    leftArrow.classList = "disabled arrow-left";
}

function enableLeftArrow(leftArrow) {
    leftArrow.classList = "waves-effect arrow-left";
}

function disableRightArrow(rightArrow) {
    rightArrow.classList = "disabled arrow-right";
}

function enableRightArrow(rightArrow) {
    rightArrow.classList = "waves-effect arrow-right";
}

function init() {
    const url = getUrl();
    getData(url);
}

init();

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















