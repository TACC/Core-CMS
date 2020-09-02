'use strict';

console.warn('Debug Mode: TRUE');

// Let all other scripts know that we are in debug mode
// CAVEAT: To use, This file must load before other scripts (no `async`, no `defer`)
window.DEBUG = true;

// In DEBUG mode, prevent output from these `console` methods
if ( ! window.DEBUG ) {
  console.info = function () {};
  console.debug = function () {};
}
