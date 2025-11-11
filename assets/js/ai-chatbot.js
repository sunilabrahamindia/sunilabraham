// ai-chatbot.js

// Load the Transformers.js library safely
(async () => {
  // Load the Transformers.js library dynamically
  const { pipeline } = await import("https://cdn.jsdelivr.net/npm/@xenova/transformers@2.6.0/dist/transformers.min.js");

  // Load a multilingual question-answering model
  const qa = await pipeline("question-answering", "Xenova/distilbert-base-multilingual-cased-distilled-squad");

  // Wait until the DOM is ready
  document.addEventListener("DOMContentLoaded", initAIChatbot);

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
      e.preventDefault(); // stops refresh
      const question = input.value.trim();
      if (!question) return;
      addMessage("user", question);
      input.value = "";
      addMessage("bot", "Thinking...");

      try {
        // For now, use the About page as context (later we’ll expand)
        const relevant = pages.find(p => p.title && p.title.toLowerCase().includes("about")) || pages[0];
        const answer = await qa(question, relevant.content);
        const reply = answer.answer ? answer.answer : "Sorry, I could not find an answer.";
        output.lastElementChild.innerHTML = `<strong>Bot:</strong> ${reply}`;
      } catch (err) {
        console.error(err);
        output.lastElementChild.innerHTML = `<strong>Bot:</strong> I ran into a small issue processing your question.`;
      }
    });
  }
})();
