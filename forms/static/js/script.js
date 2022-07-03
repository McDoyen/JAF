function addRow() {
    var inputTypes = querySet.replace(/['\[\],]/g, '').split(' ')
    var title = columnTitle.replace(/['\[\]']/g, '').split(',').map(element => {
        return element.trim()
    })
    var table = document.getElementById("table");
    var row = table.insertRow(-1);

    inputTypes.map((type, index) => {
        cell = row.insertCell(index);
        cell.innerHTML = `<div class="input-group-lg"><input class="form-control" type="text" onfocus="(this.type='${type}')" placeholder="${title[index]}"/></div>`;

    });
}
