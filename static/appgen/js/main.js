// NEW ITEMS STARTS HERE

function showTime(){
    const date = new Date();
    let datehere = document.querySelector('.datehere')
    let dateheremobile = document.querySelector('.dateheremobile')
	// Getting current time and date
	let time = new Date();
	let hour = time.getHours();
	let min = time.getMinutes();
	let sec = time.getSeconds();
	am_pm = "AM";

	// Setting time for 12 Hrs format
	if (hour >= 12) {
		if (hour > 12) 
            hour -= 12;
            am_pm = "PM";
	} else if (hour == 0) {
		hr = 12;
		am_pm = "AM";
	}

	hour = hour < 10 ? "0" + hour : hour;
	min = min < 10 ? "0" + min : min;
	sec = sec < 10 ? "0" + sec : sec;

	let currentTime =
		hour +
		":" +
		min +
		":" +
		sec +
		am_pm;

    datehere.innerHTML = `${date.toDateString()}, ${currentTime}`;
    dateheremobile.innerHTML = `${date.toDateString()}, ${currentTime}`;
}


setInterval(showTime, 1000);

$('.container').click(function(){
    if( $('.dot-arrow').hasClass('active') ){
      $('.dot-arrow').addClass('reverse');
      $('.dot-arrow').removeClass('active');
    }else{
      $('.dot-arrow').removeClass('reverse');
      $('.dot-arrow').addClass('active');
    }
  });


let acctbalanceimg = document.querySelector('.acctbalanceimg')
acctbalanceimg.addEventListener('click', () => {
    acctbalanceimg.classList.toggle("transformarrow");
})


let navmainmenuintro = document.querySelector('.navmainmenuintro img')
let closearrow = document.querySelector('.closearrow')
let sidebarmini = document.querySelector('.sidebarmini')
let sidebarsection = document.querySelector('.sidebarsection')
let navmainmenuintroTxts = document.querySelector('.sidebarsectioninner')
let main = document.querySelector('.main')

closearrow.addEventListener('click', () => {
    setTimeout(() => {
        sidebarsection.classList.toggle('cleartext')
    }, 200);
    setTimeout(() => {
        sidebarmini.classList.toggle('show')
        navmainmenuintroTxts.classList.toggle('hide')
        sidebarsection.classList.toggle('hide')
        closearrow.classList.toggle('turnarrow')
		main.classList.toggle("mainunmarginleft")       
    }, 500);
})




let closearrow2 = document.querySelector('.closearrow2')
let resposidemini = document.querySelector('.resposidemini ul')
let resposidebar = document.querySelector('.resposidebar')

closearrow2.addEventListener('click', () => {
	resposidemini.classList.toggle('hideicons')
    setTimeout(() => {
        resposidebar.classList.toggle('cleartext')
		resposidemini.classList.toggle('hide')
        closearrow2.classList.toggle('turnarrow')
		resposidebar.classList.toggle('showmainavrespo')
        resposidebar.classList.toggle('show')
    }, 400);
})



const navsection = document.querySelector('.navsection');
window.onscroll = function () {
    if (document.body.scrollTop >= 50 || document.documentElement.scrollTop >= 50 ) {
        navsection.classList.add("nav-colored");
        navsection.classList.remove("nav-transparent");
    } 
    else {
        navsection.classList.add("nav-transparent");
        navsection.classList.remove("nav-colored");
    }
};

// HAMBURGER MENU STARTS HERE
let hamburger = document.querySelector('.hamburger')

hamburger.addEventListener('click' , () => {
    hamburger.classList.toggle("active");
  });


  let userSectionResponsiveOut = document.querySelector('.userSectionResponsiveOut')
  let hamburgerMain = document.querySelector('.hamburgerMain')
  let resposideminishow = document.querySelector('.responsivesidebar')
  let resposideminiopen = document.querySelector('.resposidemini')
  
  hamburgerMain.addEventListener('click', () => {
	if (resposideminishow.style.display != 'block') {
		resposideminishow.style.display = 'block'
		resposideminiopen.style.display = 'block'
	}else{
		resposideminishow.style.display = 'none';
		resposideminiopen.style.display = 'block'
	}
	//   resposideminishow.classList.toggle("unhide")
	//   resposideminiopen.classList.toggle("unhide")
	//   setTimeout(() => {
	// 	  resposideminishow.classList.toggle("unhide")
	// 	  resposideminiopen.classList.toggle("unhide")
	//   }, 300);
  })
  





























