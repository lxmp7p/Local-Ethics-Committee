function dublicateInputs(cloneId, parentId) {
    var p = document.getElementById(cloneId);
    var p_prime = p.cloneNode(true);
    var parentDiv = document.getElementById(parentId);
    parentDiv.appendChild(p_prime)
}