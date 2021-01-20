// Configure PostCSS processor (for hardcoding variable values)

const defaultConfig = require('../postcss.config.js');

// Avoid error caused by `undefined` values left by `postcss-css-variables`
// FAQ: Error is from `cssnano` which knows that `undefined` is invalid
defaultConfig.plugins.pop();

module.exports = {
  ...defaultConfig,
  plugins: defaultConfig.plugins.concat([
    // CAVEAT: This plugin is INFERIOR to `postcss-custom-properties`, but it (with the right configuration) blindly replaces variable calls with values
    require('postcss-css-variables')({
      preserve: 'computed',
      preserveAtRulesOrder: true
    })
  ])
};
