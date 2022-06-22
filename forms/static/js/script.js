function addRow() {
    var inputTypes = querySet
        .replace(/[^a-z]/g, "")
        .replace(/u/g, " ")
        .trim()
        .split(" ");
    var table = document.getElementById("table");
    var row = table.insertRow(-1);

    inputTypes.map((type, index) => {
        cell = row.insertCell(index);
        cell.innerHTML = `<input type='${type}'/>`;
    });
}
