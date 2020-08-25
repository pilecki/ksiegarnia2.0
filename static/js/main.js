function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
  document.body.style.backgroundColor = "white";
}

// Variables for up and down quantity buttons and input field 

let downBtn = document.querySelectorAll('.decrement-qty');
downBtn = [...downBtn]
let upBtn = document.querySelectorAll('.increment-qty');
upBtn = [...upBtn]
let allInput = document.querySelectorAll('.qty_input')
allInput = [...allInput]


// Increment value

for (let i = 0; i <  upBtn.length; i++){
    upBtn[i].addEventListener('click', (event) => {
        
        //Switch off default action of the button

        event.preventDefault()
        //Read the value of the input field and increment 

        allInput[i].value = parseInt(allInput[i].value) +1 ;         
        
        //Disable and enable buttons

        if ( allInput[i].value == 99 ){
            
           upBtn[i].setAttribute('disabled', '');
        }
        if ( allInput[i].value > 0 ){
            
           downBtn[i].removeAttribute('disabled', '');
        }             
        })
    }

// Decrement value

for (let i = 0; i <  downBtn.length; i++){
    downBtn[i].addEventListener('click', (event) => {

        //Switch off default action of the button
        
        event.preventDefault()   
        
        //Read the value of the input field and decrement
    
        allInput[i].value = parseInt(allInput[i].value) -1 ;         
        
        //Disable and enable buttons
        
        if ( allInput[i].value == 0 ){ 
            
           downBtn[i].setAttribute('disabled', '');
        }
        if ( allInput[i].value < 99 ){
            
           upBtn[i].removeAttribute('disabled', '');
        }                   
        }) 
    }



