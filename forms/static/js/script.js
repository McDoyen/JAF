function addRow() {
    var inputTypes = querySet.replace(/['\[\],]/g, '').split(' ')
    var table = document.getElementById("table");
    var row = table.insertRow(-1);

    inputTypes.map((type, index) => {
        cell = row.insertCell(index);
        cell.innerHTML = `<div class="input-group-lg"><input type='${type}' class="form-control"/></div>`;
    });
}
