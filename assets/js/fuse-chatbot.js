// fuse-chatbot.js
import Fuse from "https://cdn.jsdelivr.net/npm/fuse.js@6.6.2/dist/fuse.esm.js";

async function initChatbot() {
  const response = await fetch("/index.json");
  const data = await response.json();

  // Build search index
  const fuse = new Fuse(data, {
    keys: ["title", "content"],
    includeScore: true,
    threshold: 0.4,
  });

  const chatInput = document.querySelector("#chat-input");
  const chatOutput = document.querySelector("#chat-output");
  const chatForm = document.querySelector("#chat-form");

  chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const question = chatInput.value.trim();
    if (!question) return;

    const results = fuse.search(question);
    let answer = "";

    if (results.length > 0) {
      const best = results[0].item;
      answer = best.content.slice(0, 300) + "...";
    } else {
      answer = "Sorry, I could not find anything relevant on this site.";
    }

    chatOutput.innerHTML += `
      <div class="user-msg"><strong>You:</strong> ${question}</div>
      <div class="bot-msg"><strong>Bot:</strong> ${answer}</div>
    `;

    chatInput.value = "";
    chatOutput.scrollTop = chatOutput.scrollHeight;
  });
}

document.addEventListener("DOMContentLoaded", initChatbot);
