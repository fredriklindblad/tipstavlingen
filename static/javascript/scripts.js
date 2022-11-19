// Website Functions

function pickPlayer() {
    var newPlayer = document.getElementById("exampleDataList").value;
    var playerSpot = document.getElementById("GK1");
    playerSpot.innerHTML = `
    <td>Nilsson</td>
    <td>ÖIF</td>
    <td>4.5</td>
    <td>4.5</td>
    <td>4.5</td>
    <td>190</td>
    <td>5</td>
    <td>HBK (H)</td>
    <td>
    <a class="btn btn-danger" href="#!" role="button">X</a>
    <a class="btn btn-info" href="#!" role="button">i</a>
    </td>
    `;
  }

function addPlayerToTeam(player_id) {
  // saves the id of the added player and adds the player to the current team in the view. In other function: When confirming team --> adds to team_players
  var teamPosition = 'DEF1'
  var playerId = player_id
  var playerName = 'Silverholt' // TODO how do i run functions from db_utils or how do i create similar in js?
  var playerClub = 'ÖIF'
  document.getElementById(teamPosition + "_name").innerHTML = playerId;
  document.getElementById(teamPosition + "_club").innerHTML = playerName;
  document.getElementById(teamPosition + "_price").innerHTML = playerClub;
}

function getPlayer(player_id) {
  //
  $.ajax({url: `/api/players/${player_id}`,
    type: 'GET',
    success: function(result) {
      console.log(result)
      // document.getElementById('testPlayers1').innerHTML = JSON.stringify(result)
  }
});  
}

function showPlayerStats() {
  // this function shows a modal with player stats. Player stats will be taken from player_statistics db.
}

function getPlayersList() {
  var position = document.getElementById("filtPosition").value;
  var club = document.getElementById("filtClub").value;
  var queryString = `/api/players?position=${position}&club=${club}`

  $.ajax({url: queryString,
          type: 'GET',
          success: function(result) {
            // console.log(result)
            fillPlayersTable(result)
            // document.getElementById('testPlayers1').innerHTML = JSON.stringify(result)
          }
  });
}

function getPlayersStats() {
  var position = document.getElementById("filtPositionStats").value;
  if (position !== '') {
    var queryString = `/api/players?position=${position}`
  } else {
    var queryString = `/api/players`
  }
  $.ajax({url: queryString,
          type: 'GET',
          success: function(result) {
            // console.log(result)
            fillStatsTable(result)
            // document.getElementById('testPlayers1').innerHTML = JSON.stringify(result)
          }
  });
}

function fillStatsTable(playerData) {
  // takes playerdata as input and fills the table
  var statsTable = document.getElementById("statsTable");
  statsTable.innerHTML = ""
  var listLength = playerData.length
  // console.log(playerData)

  for (var i = 0; i < listLength; i++ ) {
    var player = playerData[i]
    // console.log(player)
    const row = document.createElement("tr")
    row.innerHTML = `
      <td>${player['last_name']}<br>${player['club_id']}</td>
      <td></td>
      <td>${player['price']}</td>
      <td></td>
      <td></td>
    `
    statsTable.appendChild(row)
  }
}


function fillPlayersTable(playerData) {
  // takes playerdata as input and fills the table
  var playersTable = document.getElementById("playersTable");
  playersTable.innerHTML = ""
  var listLength = playerData.length
  // console.log(playerData)

  for (var i = 0; i < listLength; i++ ) {
    var player = playerData[i]
    // console.log(player)
    const row = document.createElement("tr")
    row.innerHTML = `
      <td>${player['last_name']}<br>${player['club_id']}</td>
      <td>${player['price']}</td>
      <td>
        <a class="btn btn-primary btn-sm" onclick="addPlayerToTeam(${player['player_id']})" role="button">+</a>
        <a class="btn btn-info btn-sm" onclick="getPlayer(${player['player_id']})" role="button">i</a>
      </td>
    `
    playersTable.appendChild(row)
  }
}

function filterButton() {
  getPlayersList(fillPlayersTable)
}

function switchToPreviousRound() {
  // switch round_id, min=1, max=30
}

function switchToNextRound() {
  // switch round_id, min=1, max=30
}

function fillGamesTable(gamesData, round_id) {
  // takes gamesdata as input and fills the table
  // TODO make a loop so only the round_id-round is viewed.
  var gamesTable = document.getElementById("gamesTable");
  gamesTable.innerHTML = ""
  var listLength = gamesData.length
  var round = round_id

  console.log(round_id)

  for (var i = 0; i < listLength; i++) {
    var game = gamesData[i]
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

function removePlayer(deleteButton) {
  deleteButton.parentElement.innerHTML = `
    <a class="btn btn-primary" onclick="resetPlayer(this)" role="button">Reset</a>
    <a class="btn btn-primary" onclick="listPlayers()" role="button">Add</a>
    <a class="btn btn-info" href="#!" role="button">i</a>
    `
}

function resetPlayer(resetButton) {
  resetButton.parentElement.innerHTML = `
    <a class="btn btn-danger" onclick="removePlayer(this)" role="button">X</a>
    <a class="btn btn-info" href="#!" role="button">i</a>
    `
}

function calcMoneyLeft() {
  pos = ['GK1', 'GK2', 'DEF1', 'DEF2', 'DEF3', 'DEF4', 'DEF5', 'MF1', 'MF2', 'MF3', 'MF4', 'MF5', 'FWD1', 'FWD2']
  posLength = pos.length
  moneyLeft = 100.0
  for (var i = 0; i < posLength; i++ ) {
    playerPrice = document.getElementById(pos[i] + '_price').value;
    console.log(playerPrice)
    if (isNaN(playerPrice)) {
      console.log(playerPrice + 'is not a number')
    } else {
      moneyLeft = moneyLeft - playerPrice
      console.log(moneyLeft)
    }
  }
  document.getElementById("moneyLeft").innerHTML = `
  <p>${moneyLeft}</p>
  `;
}