'use strict';

// Get base theme
const themeConfig = require('@tacc/core-styles/fractal.theme.js');

// To let any client extend
module.exports = Object.assign( themeConfig, {
  skin: Object.assign( themeConfig.skin, {
    links: '#877453',
  })
});
