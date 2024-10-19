function filterFlights() {
    let searchValue = document.getElementById('searchInput').value.toLowerCase();

    let table = document.getElementById('flightTable');
    let rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        let row = rows[i];
        let matchFound = false;

        let cells = row.getElementsByTagName('td');
        
        for (let j = 0; j < cells.length; j++) {
            let cell = cells[j];
            if (cell) {
                let cellValue = cell.textContent || cell.innerText;

                if (cellValue.toLowerCase().indexOf(searchValue) > -1) {
                    matchFound = true;
                    break;
                }
            }
        }

        if (matchFound) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    }
}


function openMenu(){
    menu=document.querySelector('.header .menu')

    menu.style.display='block'
}
function closeMenu(){
    menu=document.querySelector('.header .menu')

    menu.style.display='none'
}


var slide1=document.querySelector(".index .cont-2 .slide-1")
var slide2=document.querySelector(".index .cont-2 .slide-2")
var slide3=document.querySelector(".index .cont-2 .slide-3")
var slide4=document.querySelector(".index .cont-2 .slide-4")
var b=document.getElementById("less").value



function slide(){

        if(b>=4){
            b=0
        }
        b=parseInt(b)
        b=b+1
    
    if(b==1){
        slide1.style.display='none'
        slide2.style.display='block'
        slide3.style.display='none'
        slide4.style.display='none'
    }
    if(b==2){
        slide1.style.display='none'
        slide2.style.display='none'
        slide3.style.display='block'
        slide4.style.display='none'
    }
    if(b==3){
        slide1.style.display='none'
        slide2.style.display='none'
        slide3.style.display='none'
        slide4.style.display='block'
    }
    if(b==4){
        slide1.style.display='block'
        slide2.style.display='none'
        slide3.style.display='none'
        slide4.style.display='none'
    }
}

function pass_id(){
    f_id=document.getElementsByName('flight_id').value
    btn=document.getElementById('pass')

    f_id=btn.value

    console.log(f_id)
}

function show_detail(){
    box_1=document.querySelector('.profile .cont-2 .history')
    box_2=document.querySelector('.profile .cont-2 .pop')

    box_1.style.display='none'
    box_2.style.display='block'
}
function close_detail(){
    box_1=document.querySelector('.profile .cont-2 .history')
    box_2=document.querySelector('.profile .cont-2 .pop')

    box_1.style.display='block'
    box_2.style.display='none'
}

function open_edit(){
    box_1=document.querySelector('.profile .cont-1 .detail')
    box_2=document.querySelector('.profile .cont-1 .edit')
    box_3=document.querySelector('.profile .cont-2')

    box_1.style.display='none'
    box_2.style.display='block'
    box_3.style.display='none'
}
function close_edit(){
    box_1=document.querySelector('.profile .cont-1 .detail')
    box_2=document.querySelector('.profile .cont-1 .edit')
    box_3=document.querySelector('.profile .cont-2')

    box_1.style.display='block'
    box_2.style.display='none'
    box_3.style.display='block'
}