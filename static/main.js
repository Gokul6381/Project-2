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


function ok(){
    box1=document.querySelector('.book .container')
    box2=document.querySelector('.book .end')

    box1.style.display='block'
    box2.style.display='none'

    location.reload()
}