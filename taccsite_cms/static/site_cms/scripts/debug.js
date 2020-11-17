'use strict';

if ( window.DEBUG === true ) {
  // In DEBUG mode, notify developer in console
  console.warn('Debug Mode', window.DEBUG);
} else {
  // In production, prevent output from these `console` methods
  console.info = function () {};
  console.debug = function () {};
}
