'use strict';

// In DEBUG mode, notify developer in console
if ( window.DEBUG === true ) {
  console.warn('Debug Mode', window.DEBUG);
}

// In production, prevent output from these `console` methods
if ( window.DEBUG === false ) {
  console.info = function () {};
  console.debug = function () {};
}
