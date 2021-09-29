function changePage(thisPage, nextPage){
	$("#" + thisPage)[0].hidden = true;
	$("#" + nextPage)[0].hidden = false;
}

function checkRelationship(){
	if ($("#relationshipTrueBtn")[0].disabled == true) {
		$("#getInfoBtn")[0].hidden = false;
	}ы
	if ($("#relationshipTrueBtn")[0].disabled == false) {
		$("#getInfoBtn")[0].hidden = true;
	}
}

function checkError() {
	errorSatus = false;
	$("#page4 input").each(function() {
	    if (!this.value) {
	        errorSatus = true;
	    }    
	});
	if (errorSatus) {
		$("#error")[0].innerHTML = "Поля обязательны для заполнения!";
	}
	else {
		$("#error")[0].innerHTML = "";
		changePage('page4', 'page5');
	}
}

function dublicateInputs(cloneId, parentId) {
    var p = document.getElementById(cloneId);
    var p_prime = p.cloneNode(true);
    var parentDiv = document.getElementById(parentId);
    parentDiv.appendChild(p_prime)
}

function deleteDublicateInputs(fieldClass) {
    if ($("." + fieldClass).length != 1) {
        $("." + fieldClass).last().remove()
    }
}

