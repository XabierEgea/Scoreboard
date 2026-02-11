/**
 * Overlay state manager (OBS SAFE VERSION)
 */

const STATE_FILE = "scoreboard_state.json";
const UPDATE_INTERVAL = 500;

let previousState = null;

/* ===============================
   LOAD STATE
================================ */
async function loadState() {
  try {
    const response = await fetch(STATE_FILE + "?t=" + Date.now());
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Failed to load state:", error);
    return null;
  }
}

/* ===============================
   STATE COMPARISON
================================ */
function hasStateChanged(newState) {
  if (!previousState) return true;
  return JSON.stringify(newState) !== JSON.stringify(previousState);
}

/* ===============================
   UI UPDATE HELPERS
================================ */
function updateText(element, value) {
  if (element && element.textContent !== String(value)) {
    element.textContent = value;
  }
}

function updateScore(element, value) {
  if (!element) return;

  if (element.textContent !== String(value)) {
    element.classList.add("score-updated");
    element.textContent = value;

    setTimeout(() => {
      element.classList.remove("score-updated");
    }, 300);
  }
}

/* ===============================
   COLOR HANDLING (CSS VARIABLES)
================================ */

function setCSSVarSafe(name, value) {
  if (typeof value === "string" && value.trim() !== "") {
    document.documentElement.style.setProperty(name, value);
  }
}

function updateTeamColors(localColor, visitorColor) {
  const root = document.documentElement;

  setCSSVarSafe("--local-color", localColor);
  setCSSVarSafe("--visitor-color", visitorColor);
}

/* ===============================
   APPLY STATE
================================ */
function applyState(state) {
  if (!state) return;

  // Team names
  updateText(
    document.getElementById("local-name"),
    state.local.name
  );

  updateText(
    document.getElementById("visitor-name"),
    state.visitor.name
  );

  // Scores (3 sets)
  for (let i = 1; i <= 3; i++) {
    updateScore(
      document.getElementById(`local-set${i}`),
      state.local.sets[i - 1]
    );

    updateScore(
      document.getElementById(`visitor-set${i}`),
      state.visitor.sets[i - 1]
    );
  }

  // Colors via CSS variables
  updateTeamColors(
    state.local.color,
    state.visitor.color
  );

  previousState = structuredClone(state);
}

/* ===============================
   UPDATE LOOP
================================ */
async function updateLoop() {
  const state = await loadState();

  if (state && hasStateChanged(state)) {
    applyState(state);
  }

  setTimeout(updateLoop, UPDATE_INTERVAL);
}

/* ===============================
   START
================================ */
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", updateLoop);
} else {
  updateLoop();
}


