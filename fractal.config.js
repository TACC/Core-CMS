'use strict';

const path = require('path');
const mandelbrot = require('@frctl/mandelbrot');

const fractal = require('@tacc/core-styles/fractal.config.js');
const themeConfig = require('@tacc/core-styles/fractal.config.theme.js');

themeConfig.styles = [
  'default'
];
const theme = mandelbrot(themeConfig);

const coreStylesRoot = path.dirname(require.resolve('@tacc/core-styles'));

fractal.components.set('path',
  // FAQ: The '../' (a) avoids a 'src/src' path, (b) shows path is in 'src/'
  path.join(coreStylesRoot, '../src/lib/_imports')
);

fractal.web.set('static.path',
  path.join(coreStylesRoot, 'dist')
);
fractal.web.set('builder.dest', __dirname + '/taccsite_ui');

fractal.web.theme(theme);

module.exports = fractal;
