// var headingName = "DATA STATS";
// var headers = ['Voltage_A', 'Voltage_B', 'Voltage_C'];
// var data = [[99, 100, 101], [88, 89, 90], [66, 67, 68]];
// var elementID = 'dataTableDisplay';

// ------------------------------------------------------------------
function createTableFromData(headingName, headers, data, elementID){
    var parentElement = document.getElementById(elementID);

    var heading = document.createElement('h3');
    heading.classList.add('mt-4');
    heading.textContent = headingName;
    
    // var div = document.createElement('div');
    parentElement.appendChild(heading);
    // div.appendChild(heading);
    // div.classList('bg-secondary');
    

    var tbl = document.createElement('table');

    tbl.classList.add('table');
    tbl.classList.add('table-striped');
    tbl.classList.add('table-sm');
    tbl.classList.add('fs-sm-4');
    tbl.classList.add('text-center');

    tbl.setAttribute('id', 'tableChart')
    parentElement.appendChild(tbl);

    var tr = document.createElement('tr');

    for(let i = 0; i < headers.length; i++){
        var th = document.createElement('th');
        th.textContent = headers[i];
        tr.appendChild(th)
    };

    var thead = document.createElement('thead');
    thead.appendChild(tr);

    tbl.appendChild(thead);

    var tbody = document.createElement('tbody');
    
    console.log(data.length)
    for (let j = 0; j < data[0].length; j++){

        var tr = document.createElement('tr');
        for (let i = 0; i < data.length; i++){
            var td = document.createElement('td');
            td.textContent = data[i][j]
            tr.appendChild(td)
            
        };
        tbody.appendChild(tr);
        // console.log(j);
    };
    
    



    tbl.appendChild(tbody);
    };


    
// createTableFromData(headingName, headers, data, elementID);