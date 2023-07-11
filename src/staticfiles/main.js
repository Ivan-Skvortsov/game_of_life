let currentGameState;

const renderBoard = async (gameState) => {
  let table = document.getElementById("board");
  table.innerHTML = "";
  for (let i = 0; i < gameState.length; i++) {
    let tr = document.createElement("tr");
    for (let j = 0; j < gameState[i].length; j++) {
      let cell = document.createElement("td");
      tr.appendChild(cell);
      let cellStatus = gameState[i][j] === 0 ? "dead" : "alive";
      cell.setAttribute("class", cellStatus);
    }
    table.appendChild(tr);
  }
};

const getNewGame = async () => {
  let gameState = await fetch("/game");
  return await gameState.json();
};

const updateCurrentGame = async () => {
  const fetchOptions = {
    method: "POST",
    credentials: "same-origin",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(currentGameState),
  };
  let updatedGameData = await fetch("/game", fetchOptions);
  currentGameState = await updatedGameData.json();
  await renderBoard(currentGameState.board);
};

const initGame = async () => {
  currentGameState = await getNewGame();
  await renderBoard(currentGameState.board);
};

window.onload = initGame;
