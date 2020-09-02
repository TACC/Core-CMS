'use strict';

console.warn('Debug Mode', window.DEBUG);

// In DEBUG mode, prevent output from these `console` methods
if ( ! window.DEBUG ) {
  console.info = function () {};
  console.debug = function () {};
}
