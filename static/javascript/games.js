getGamesList()

// 
// 
//  FUNCTIONS BELOW
// 
// 

function getGamesList() {
    var queryString = `/api/games`
  
    $.ajax({url: queryString,
            type: 'GET',
            success: function(result) {
              fillGamesTable(result)
              // document.getElementById('testPlayers1').innerHTML = JSON.stringify(result)
            }
    });
  }

function fillGamesTable(gamesData) {
    var gamesTable = document.getElementById("gamesTable");
    gamesTable.innerHTML = ""
    var listLength = gamesData.length

    for (var i = 0; i < listLength; i++ ) {
        var game = gamesData[i]
        console.log(gamesData[i])
        const row = document.createElement("tr")
        row.innerHTML = `
            <td>${game['home_team']}</td>
            <td>${game['away_team']}</td>
            <td>${game['home_goals']} - ${game['away_goals']}</td>
            <td>${game['date']}</td>
            <td>${game['kick_off']}</td>
        `
        gamesTable.appendChild(row)
        }
    }