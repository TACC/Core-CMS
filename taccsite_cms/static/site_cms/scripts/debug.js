'use strict';

console.warn('Debug Mode: TRUE');

// Let all other scripts know that we are in debug mode
// CAVEAT: To use, This file must load before other scripts (no `async`, no `defer`)
window.DEBUG = true;

// Re-assign `console` functions to only output in DEBUG mode
// FAQ: Any method NOT in this list WILL output in production
const consoleMethodNames = ['info', 'debug'];
// FAQ: Anonymous functions used only to ensure that `this` is unaltered
consoleMethodNames.forEach( (functionName) => {
  window.console[methodName] = (...args) => {
    // FAQ: Condition is redundant only because of knowledge external to script.
    //      Keep condition to retain logic if script becomes always loaded.
    //      (Would allow a not-yet-written feature to debug production.)
    if ( window.DEBUG ) {
      console[methodName].call(this, ...args);
    }
  }
});
