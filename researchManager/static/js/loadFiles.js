function changePage(thisPage, nextPage){
	$("#" + thisPage)[0].hidden = true;
	$("#" + nextPage)[0].hidden = false;
}

function checkRelationship(){
	if ($("#relationshipTrueBtn")[0].disabled == true) {
		$("#getInfoBtn")[0].hidden = false;
	}
	if ($("#relationshipTrueBtn")[0].disabled == false) {
		$("#getInfoBtn")[0].hidden = true;
	}
}


