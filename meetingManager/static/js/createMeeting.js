function setResearchAndUserInPost(){
    researchIdList = $("tbody#researchList button:disabled")
    var parent = document.getElementById("createMenu");

    $.each(researchIdList, function(index, value) {
        var input = document.createElement("input");
        input.setAttribute('type', 'text');
        input.setAttribute('name', 'researchIdList');
        input.setAttribute('value', value.id);
        input.setAttribute('hidden', true);
        parent.appendChild(input);
    });

    userIdList = $("tbody#userList button:disabled")
    $.each(userIdList, function(index, value) {
        var input = document.createElement("input");
        input.setAttribute('type', 'text');
        input.setAttribute('name', 'userIdList');
        input.setAttribute('value', value.id);
        input.setAttribute('hidden', true);
        parent.appendChild(input);
    });
}

function addInMeetingList(self, listId, object, objectId){
    self.disabled = true;
    var table = document.getElementById(listId);
    var faucet1 = 1;
    var tr = document.createElement("tr");
    if (faucet1 == 1) {
        if (listId == 'researchInMeeting') {
            tr.innerHTML = '<td id="'+ objectId +'_research1">' + object + '</td> <td id="'+ objectId +'_research2"><button type="button" researchId="'+ objectId + '" class="btn btn-danger" onclick="deleteInMeetingList(this, `research`, '+ objectId + ')">Удалить</button></td>';
        }
        else {
            tr.innerHTML = '<td id="'+ objectId +'_user1">' + object + '</td> <td id="'+ objectId +'_user2"><button type="button" class="btn btn-danger" onclick="deleteInMeetingList(this, `user`, '+ objectId + ')">Удалить</button></td>';
        } 
        table.appendChild(tr);
    }
    else {
        console.log('error');
    }
}

function deleteInMeetingList(self, type, object){
    if (type == "research") {
        var button = $("tbody#researchList").find("button#" + object)[0];
        console.log(object)
        $("#"+ object + "_research1").remove();
        $("#"+ object + "_research2").remove();
    }
    else {
        var button = $("tbody#userList").find("button#" + object)[0];
        $("#"+ object + "_user1").remove();
        $("#"+ object + "_user2").remove();
    }
    button.disabled = false;
}   

function filterResearchList(self){
    $("#researchList tr").each(function() {
        filterType = self.id.slice(0, -6);
        if ($(this).attr('id') != filterType) {
            this.hidden = true;
        }
        if ($(this).attr('id') == filterType) {
            this.hidden = false;
        }
        if (filterType == 'allRequests') {
            this.hidden = false;
        }
    });

    $("#filterPanel button:disabled").each(function() {
        ($(this.disabled = false))
    });

    self.disabled = true;
};