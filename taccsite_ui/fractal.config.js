'use strict';

const path = require('path');
const mandelbrot = require('@frctl/mandelbrot');
const minimist = require('minimist');

// Get base config
const fractal = require('@tacc/core-styles/fractal.config.js');
const themeConfig = require('./fractal.theme.js');
const defaultContext = fractal.components.get('default.context');

// Get project
// (name)
const args = minimist( process.argv.slice( 2 ));
let cmsName = 'core-cms';
let projName = args['project'] || '';
    projName = ( projName !== cmsName ) ? projName : '';
// (stylesheet)
const escapeDemoDir = '/../..'; // i.e. back out of '/static/ui'
const cmsCSSFiles = [
  ...defaultContext.cmsStyles,
  {
    isInternal: false,
    layer: 'project',
    path: `${escapeDemoDir}/static/site_cms/css/build/site.cms.css`
  },
];
const projCSSFiles = ( projName ) ? [
  {
    isInternal: false,
    layer: 'cosmetic',
    path: `${escapeDemoDir}/static/${projName}/css/build/site.cms.css`
  },
] : [];

// Set source paths
// (for components)
fractal.components.set('exclude', '*.md');
fractal.components.set('path', __dirname + '/patterns');
// (for stylesheets)
fractal.components.set('default.context', {
  ...fractal.components.get('default.context'),
  shouldSkipPattern: true, // true, because …base.css loads most components
  cmsStyles: cmsCSSFiles.concat( projCSSFiles )
});
fractal.cli.log(`+ Included CSS for "${cmsName}"`);
cmsCSSFiles.forEach( file => { fractal.cli.log(file.path) });
if ( projCSSFiles.length > 0 ) {
  fractal.cli.log(`+ Included CSS for "${projName}"`);
  projCSSFiles.forEach( file => { fractal.cli.log(file.path) });
}

// Set website paths
// FAQ: Setting static.path results in `shouldSkipPattern: false` letting ONLY Core-CMS assets load, because that directory ONLY has Core-CMS assets
// FAQ: Not setting static.path results in `shouldSkipPattern: false` letting ONLY Core-Styles assets load, because Core-Styles config loads ONLY its assets
// fractal.web.set('static.path', __dirname + '/../taccsite_cms/static/site_cms/css/build');
fractal.web.set('builder.dest', __dirname + '/dist');

// Customize theme
const theme = mandelbrot( themeConfig );
fractal.web.theme( theme );

// Export
module.exports = fractal;
