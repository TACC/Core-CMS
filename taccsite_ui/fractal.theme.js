'use strict';

// Get base theme
const themeConfig = require('@tacc/core-styles/fractal.theme.js');

// Extend base theme
const newThemeConfig = Object.assign( themeConfig, {
  skin: Object.assign( themeConfig.skin, {
    links: '#003399', // from tup-cms
  })
});

// Export new theme
module.exports = newThemeConfig;
