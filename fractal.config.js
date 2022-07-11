'use strict';

const path = require('path');
const mandelbrot = require('@frctl/mandelbrot');

const fractal = require('@tacc/core-styles/fractal.config.js');
const themeConfig = require('@tacc/core-styles/fractal.config.theme.js');

const theme = mandelbrot(Object.assign(themeConfig, {
  skin: Object.assign(themeConfig.skin, {
    accent: '#000000',
    complement: '#ffffff',
    links: '#877453',
  })
}));

const coreStylesRoot = path.join(
  path.dirname(require.resolve('@tacc/core-styles')),
  // The '../' exits 'src/' which require.resolve returns a file from
  '../'
);

fractal.components.set('path',
  path.join(coreStylesRoot, 'src/lib/_imports')
);
fractal.components.set('default.context', {
  styles: {
    internal: [
      '/settings/border.css',
      '/settings/max-width.css',
    ],
    external: [
      '/static/site_cms/css/build/color.css',
      '/static/site_cms/css/build/font.css',
      '/static/site_cms/css/build/space.css',
    ]
  }
});

fractal.web.set('static.path',
  path.join(coreStylesRoot, 'dist')
);
fractal.web.set('builder.dest', __dirname + '/taccsite_ui');

fractal.web.theme(theme);

module.exports = fractal;
