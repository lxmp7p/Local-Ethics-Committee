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
            tr.innerHTML = '<td id="'+ objectId +'_research1">' + object + '</td> <td id="'+ objectId +'_research2"><button type="button" researchId="'+ objectId + '" class="btn" onclick="deleteInMeetingList(this, `research`, '+ objectId + ')">'
            + '<svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-clipboard-minus" fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
            +'<path fill-rule="evenodd" d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"/>'
            +'<path fill-rule="evenodd" d="M9.5 1h-3a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3zm-1 9.5A.5.5 0 0 1 6 9h4a.5.5 0 0 1 0 1H6a.5.5 0 0 1-.5-.5z"/>'
            +'</svg></button></td>';
        }
        else {
            tr.innerHTML = '<td id="'+ objectId +'_user1">' + object + '</td> <td id="'+ objectId +'_user2"><button type="button" class="btn" onclick="deleteInMeetingList(this, `user`, '+ objectId + ')">'
            +'<svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-person-dash" fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
            +'<path fill-rule="evenodd" d="M11 14s1 0 1-1-1-4-6-4-6 3-6 4 1 1 1 1h10zm-9.995-.944v-.002.002zM1.022 13h9.956a.274.274 0 0 0 .014-.002l.008-.002c-.001-.246-.154-.986-.832-1.664C9.516 10.68 8.289 10 6 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664a1.05 1.05 0 0 0 .022.004zm9.974.056v-.002.002zM6 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm3-2a3 3 0 1 1-6 0 3 3 0 0 1 6 0zm2 2.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5z"/>'
          + '</svg></button></td>';
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