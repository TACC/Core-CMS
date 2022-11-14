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
const cmsCSSFile = `${escapeDemoDir}/static/site_cms/css/build/site.css`;
const projCSSFile = ( projName )
  ? `${escapeDemoDir}/static/${projName}/css/build/site.css`
  : null;

// Set source paths
// (for components)
fractal.components.set('exclude', '*.md');
fractal.components.set('path', __dirname + '/patterns');
// (for stylesheets)
fractal.components.set('default.context', {
  styles: {
    shouldSkipBase: true, // true, because site.css includes components
    external: {
      global: [
        'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
        cmsCSSFile,
      ].concat( ( projCSSFile ) ? [ projCSSFile ] : [] )
    }
  }
});
fractal.cli.log(`+ Included CSS for "${cmsName}": '${cmsCSSFile}'`);
if ( projCSSFile ) {
  fractal.cli.log(`+ Included CSS for "${projName}": '${projCSSFile}'`);
}

// Set website paths
fractal.web.set('static.path', __dirname + '/../node_modules/@tacc/core-styles/build');
fractal.web.set('builder.dest', __dirname + '/dist');

// Customize theme
const theme = mandelbrot( themeConfig );
fractal.web.theme( theme );

// Export
module.exports = fractal;
