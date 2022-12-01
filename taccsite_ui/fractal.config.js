'use strict';

const path = require('path');
const mandelbrot = require('@frctl/mandelbrot');
const minimist = require('minimist');

// Get base config
const fractal = require('@tacc/core-styles/fractal.config.js');
const themeConfig = require('./fractal.theme.js');

// Get project
// (name)
const args = minimist( process.argv.slice( 2 ));
let cmsName = 'core-cms';
let projName = args['project'] || '';
    projName = ( projName !== cmsName ) ? projName : '';
// (stylesheet)
const escapeDemoDir = '/../..'; // i.e. back out of '/static/ui'
const cmsCSSFiles = [
  {
    isInternal: false,
    layer: 'foundation',
    path: `${escapeDemoDir}/static/site_cms/css/build/core-styles.base.css`,
  },
  {
    isInternal: false,
    layer: 'base',
    path: `${escapeDemoDir}/static/site_cms/css/build/core-styles.base.css`,
  },
  {
    isInternal: false,
    layer: 'base',
    path: `${escapeDemoDir}/static/site_cms/css/build/core-styles.cms.css`,
  },
  {
    isInternal: false,
    layer: 'base',
    path: `${escapeDemoDir}/static/site_cms/css/build/core-styles.header.css`,
  },
  {
    isInternal: false,
    layer: 'project',
    path: `${escapeDemoDir}/static/site_cms/css/build/site.cms.css`,
  },
];
const projCSSFiles = ( projName ) ? [
  {
    isInternal: false,
    layer: 'cosmetic',
    path: `${escapeDemoDir}/static/${projName}/css/build/site.css`
  },
] : [];

// Set source paths
// (for components)
fractal.components.set('exclude', '*.md');
fractal.components.set('path', __dirname + '/patterns');
// (for stylesheets)
fractal.components.set('default.context', {
  shouldSkipCMS: true, // true, because CMS loads its own styles
  shouldSkipBootstrap: true, // true, because CMS loads its own styles
  shouldSkipPattern: true, // true, because CMS loads patterns itself
  globalStyles: cmsCSSFiles.concat( projCSSFiles )
});
fractal.cli.log(`+ Included CSS for "${cmsName}"`);
cmsCSSFiles.forEach( file => { fractal.cli.log(file.path) });
if ( projCSSFiles.length > 0 ) {
  fractal.cli.log(`+ Included CSS for "${projName}"`);
  projCSSFiles.forEach( file => { fractal.cli.log(file.path) });
}

// Set website paths
fractal.web.set('static.path', __dirname + '/../node_modules/@tacc/core-styles/dist');
fractal.web.set('builder.dest', __dirname + '/dist');

// Customize theme
const theme = mandelbrot( themeConfig );
fractal.web.theme( theme );

// Export
module.exports = fractal;
