// Typing effect
const text = "yesin.woow";
let i = 0;
const nameEl = document.getElementById("name");

function typing() {
  if (i < text.length) {
    nameEl.textContent += text.charAt(i);
    i++;
    setTimeout(typing, 120);
  }
}
typing();

// Copy username
function copyName() {
  navigator.clipboard.writeText("yesin.woow");
  alert("Copied Username!");
}

// Particles
tsParticles.load("tsparticles", {
  background: { color: "#0d1117" },
  particles: {
    number: { value: 60 },
    color: { value: "#ffffff" },
    links: {
      enable: true,
      color: "#ffffff",
      distance: 150
    },
    move: {
      enable: true,
      speed: 2
    },
    size: { value: 3 },
    opacity: { value: 0.5 }
  }
});