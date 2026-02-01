---
layout: default
title: Contact
categories: [Project pages]
description: "Get in touch with Sunil Abraham for questions, collaborations, or discussions related to open documentation, research, and technology."
created: 2025-10-19
---

<div class="contact-container">
  <div class="contact-intro">
    <p>Thank you for your interest in our work. Whether you have a question about a project, wish to collaborate, or simply want to share a thought, we welcome meaningful conversations related to open documentation, research, and technology.</p>
  </div>

  <div class="contact-section">
    <h2>Email</h2>
    <p>You can reach us directly at</p>
    <a href="mailto:sunilabraham@proton.me" class="email-link">sunilabraham@proton.me</a>
  </div>

  <div class="contact-section">
    <h2>Notes</h2>
    <div class="notes-content">
      <p>We regularly read the messages sent to the email above, though replies may take a few days depending on the nature of the enquiry.</p>
      <p>For detailed or technical discussions, please include relevant links or background context so we can respond effectively.</p>
    </div>
  </div>
</div>

<style>
/* Contact page specific styles matching TSAP theme */
.contact-container {
  max-width: 92%;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.contact-intro {
  font-size: 1.1rem;
  line-height: 1.7;
  margin-bottom: 2.5rem;
  color: #333;
  animation: fadeInUp 0.6s ease-out;
}

.contact-section {
  background: #f9f9f9;
  border-left: 4px solid #2c5282;
  padding: 1.5rem 2rem;
  margin: 2rem 0;
  border-radius: 4px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  animation: fadeInUp 0.8s ease-out;
}

.contact-section:hover {
  transform: translateX(8px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.contact-section h2 {
  margin-top: 0;
  font-size: 1.4rem;
  color: #1a202c;
  font-weight: 600;
}

.email-link {
  display: inline-block;
  font-size: 1.15rem;
  color: #2563eb;
  text-decoration: none;
  padding: 0.5rem 0;
  border-bottom: 2px solid transparent;
  transition: border-color 0.3s ease, color 0.3s ease;
}

.email-link:hover {
  color: #1d4ed8;
  border-bottom-color: #2563eb;
}

.email-link::before {
  content: "✉ ";
  margin-right: 0.5rem;
  opacity: 0.7;
}

.notes-content {
  line-height: 1.8;
  color: #4a5568;
}

.notes-content p {
  margin-bottom: 1rem;
}

.notes-content p:last-child {
  margin-bottom: 0;
}

/* Animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive adjustments */
@media (max-width: 640px) {
  .contact-section {
    padding: 1.25rem 1.5rem;
  }
  
  .contact-section:hover {
    transform: translateX(4px);
  }
}

/* Print-friendly styles */
@media print {
  .contact-section {
    break-inside: avoid;
    border: 1px solid #ccc;
    box-shadow: none;
  }
}
</style>
