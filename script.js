/**
 * Alias entrypoint linking to js/main.js
 * Enables direct script.js references if needed
 */

// If main.js isn't already loaded, this ensures parity
if (typeof initTheme === 'undefined') {
  const mainScript = document.createElement('script');
  mainScript.src = 'js/main.js';
  document.body.appendChild(mainScript);
}
