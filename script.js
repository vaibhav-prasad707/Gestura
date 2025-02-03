document.addEventListener('DOMContentLoaded', () => {
    const text = "Welcome to Gestura!\nYour accessible communication platform!\nOur platform supports multiple accessibility features.";
    const typingText = document.getElementById('typing-text');
    let index = 0;
  
    function typeText() {
      if (index < text.length) {
        typingText.textContent += text.charAt(index);
        index++;
        setTimeout(typeText, 50);
      }
    }
  
    // Start typing animation
    typeText();
  
    // Reset typing animation when page is reloaded
    window.addEventListener('beforeunload', () => {
      typingText.textContent = '';
      index = 0;
    });
  });
  