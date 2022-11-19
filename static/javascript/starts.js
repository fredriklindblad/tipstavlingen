getStartsList()

// 
// 
//  FUNCTIONS BELOW
// 
// 

function getStartsList() {
    var queryString = `/api/team-players`
    $.ajax({url: queryString,
            type: 'GET',
            success: function(result) {
              fillStartsTable(result)
              // document.getElementById('testPlayers1').innerHTML = JSON.stringify(result)
            }
    });
  }

function checkStarts() {
    for (var i = 0; i < listLength; i++ ) {
    console.log(document.getElementById("player"+i))
    }
}

function fillStartsTable(teamPlayersData) {
    var gkTable = document.getElementById("gkTable");
    gkTable.innerHTML = ""
    var defTable = document.getElementById("defTable");
    gkTable.innerHTML = ""
    var mfTable = document.getElementById("mfTable");
    gkTable.innerHTML = ""
    var fwdTable = document.getElementById("fwdTable");
    gkTable.innerHTML = ""
    var listLength = teamPlayersData.length

    for (var i = 0; i < listLength; i++ ) {
        var pl = teamPlayersData[i]
        var pl_id = "player"+i
        if (pl['start'] == 1) {var checked = 'checked'} else {var checked = ''}
        if (pl['position'] ==  'GK') {
            const row = document.createElement("tr")
            row.innerHTML = `
                <td>${pl['last_name']}<br>${pl['club_id']}</td>
                <td>${pl['position']}</td>
                <td>${pl['price']}</td>
                <td></td>
                <td>ÖIF (B)</td>
                <td class="text-end">
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" role="switch" id=${pl_id} onclick=checkStarts() ${checked}/>
                    </div>
                </td>
                <td><a class="btn btn-sm btn-info" href="#!" role="button">i</a></td>
            `
            gkTable.appendChild(row)
            }
        else if (pl['position'] ==  'DEF') {
            const row = document.createElement("tr")
            row.innerHTML = `
                <td>${pl['last_name']}<br>${pl['club_id']}</td>
                <td>${pl['position']}</td>
                <td>${pl['price']}</td>
                <td></td>
                <td>ÖIF (B)</td>
                <td class="text-end">
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" ${checked}/>
                    </div>
                </td>
                <td><a class="btn btn-sm btn-info" href="#!" role="button">i</a></td>
            `
            defTable.appendChild(row)
            }
        else if (pl['position'] ==  'MF') {
            const row = document.createElement("tr")
            row.innerHTML = `
                <td>${pl['last_name']}<br>${pl['club_id']}</td>
                <td>${pl['position']}</td>
                <td>${pl['price']}</td>
                <td></td>
                <td>ÖIF (B)</td>
                <td class="text-end">
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" ${checked}/>
                    </div>
                </td>
                <td><a class="btn btn-sm btn-info" href="#!" role="button">i</a></td>
            `
            mfTable.appendChild(row)
            }
        else if (pl['position'] ==  'FWD') {
            const row = document.createElement("tr")
            if (pl['start'] == 1) {var checked = 'checked'}
            row.innerHTML = `
                <td>${pl['last_name']}<br>${pl['club_id']}</td>
                <td>${pl['position']}</td>
                <td>${pl['price']}</td>
                <td></td>
                <td>ÖIF (B)</td>
                <td class="text-end">
                    <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" ${checked}/>
                    </div>
                </td>
                <td><a class="btn btn-sm btn-info" href="#!" role="button">i</a></td>
            `
            fwdTable.appendChild(row)
            }

        }
    }