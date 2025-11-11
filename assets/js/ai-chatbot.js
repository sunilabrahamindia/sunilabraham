// ai-chatbot.js
import { pipeline } from "https://cdn.jsdelivr.net/npm/@xenova/transformers@2.6.0";

// Load multilingual QA model (supports Hindi, English, Tamil, etc.)
const qa = await pipeline("question-answering", "Xenova/distilbert-base-multilingual-cased-distilled-squad");

async function initAIChatbot() {
  const response = await fetch("/index.json");
  const pages = await response.json();

  const input = document.querySelector("#chat-input");
  const output = document.querySelector("#chat-output");
  const form = document.querySelector("#chat-form");

  function addMessage(sender, text) {
    output.innerHTML += `<div class="${sender}-msg"><strong>${sender === "user" ? "You" : "Bot"}:</strong> ${text}</div>`;
    output.scrollTop = output.scrollHeight;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const question = input.value.trim();
    if (!question) return;
    addMessage("user", question);
    input.value = "";

    addMessage("bot", "Thinking...");

    // Pick the most relevant page by keyword (simple filter)
    const relevant = pages.find(p => p.content.toLowerCase().includes("sunil")) || pages[0];

    try {
      // Run question-answering on the relevant content
      const answer = await qa(question, relevant.content);
      const reply = answer.answer ? answer.answer : "Sorry, I could not find a clear answer.";
      output.lastElementChild.innerHTML = `<strong>Bot:</strong> ${reply}`;
    } catch (err) {
      output.lastElementChild.innerHTML = `<strong>Bot:</strong> Sorry, I ran into a small error.`;
      console.error(err);
    }
  });
}

document.addEventListener("DOMContentLoaded", initAIChatbot);
