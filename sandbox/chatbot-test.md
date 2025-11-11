---
layout: default
title: "Chatbot Test"
description: "Ask questions about Sunil Abraham's website content."
---

<h1>Ask SunilBot</h1>

<div id="chat-box">
  <div id="chat-output"></div>
  <form id="chat-form">
    <input id="chat-input" type="text" placeholder="Ask a question..." autocomplete="off" />
    <button type="submit">Ask</button>
  </form>
</div>

<script type="module" src="/assets/js/fuse-chatbot.js"></script>

<style>
  #chat-box {
    max-width: 700px;
    margin: 0 auto;
    background: #f8f9fa;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 0 6px rgba(0,0,0,0.1);
  }
  #chat-output {
    max-height: 400px;
    overflow-y: auto;
    padding: 0.5rem;
    background: #fff;
    border-radius: 8px;
    margin-bottom: 1rem;
  }
  #chat-input {
    width: 80%;
    padding: 0.5rem;
  }
  button {
    padding: 0.5rem 1rem;
    background: #0056b3;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }
  button:hover {
    background: #004494;
  }
  .user-msg { color: #000; margin-top: 0.5rem; }
  .bot-msg { color: #004494; margin-bottom: 1rem; }
</style>
