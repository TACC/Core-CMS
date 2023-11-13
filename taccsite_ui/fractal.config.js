'use strict';

const fractal = require('@tacc/core-styles/fractal.config.js');
const defaultContext = fractal.components.get('default.context');

// Customize styles
const cmsStyles = [
  ...defaultContext.cmsStyles,
  {
    isInternal: false,
    layer: 'project',
    // FAQ: The '/../..' backs out of '/static/ui'
    path: `/../../static/site_cms/css/build/core-cms.css`
  },
];

// Set source paths
// (for components)
fractal.components.set('exclude', '*.md');
fractal.components.set('path', __dirname + '/patterns');
// (for stylesheets)
fractal.components.set('default.context', {
  ...defaultContext,
  shouldSkipPattern: true, // true, because Core-Styles loads most patterns
  cmsStyles: cmsStyles
});
fractal.cli.log(`+ Included Core-CMS stylesheets`);
cmsStyles.forEach( file => { fractal.cli.log(file.path) });

// Set website paths
// FAQ: Setting static.path results in `shouldSkipPattern: false` letting ONLY Core-CMS assets load, because that directory ONLY has Core-CMS assets
// FAQ: Not setting static.path results in `shouldSkipPattern: false` letting ONLY Core-Styles assets load, because Core-Styles config loads ONLY its assets
// fractal.web.set('static.path', __dirname + '/../taccsite_cms/static/site_cms/css/build');
fractal.web.set('builder.dest', __dirname + '/dist');

// Customize theme
const mandelbrot = require('@frctl/mandelbrot');
const themeConfig = require('./fractal.theme.js');
const theme = mandelbrot( themeConfig );
fractal.web.theme( theme );

// Export
module.exports = fractal;
