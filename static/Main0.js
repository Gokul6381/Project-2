function openMenu(){

  box=document.querySelector('.header .menu')
  btn=document.querySelector('.header .bar')
  
  box.style.display='block'
  btn.style.display='none'

}

function closeMenu(){

    box=document.querySelector('.header .menu')
    btn=document.querySelector('.header .bar')
    
    box.style.display='none'
    btn.style.display='block'
  
  }

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

function history(){
  let his = document.querySelector('.history')
  let pro = document.querySelector('.profile')
  let up = document.querySelector('.update')

  his.style.display="block"
  pro.style.display="none"
  up.style.display="none"
}

function update(){
  let his = document.querySelector('.history')
  let pro = document.querySelector('.profile')
  let up = document.querySelector('.update')

  his.style.display="none"
  pro.style.display="none"
  up.style.display="block"
}