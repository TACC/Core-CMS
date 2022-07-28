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
const cmsCSSFile = 'cms/site.css';
const projCSSFile = ( projName )
  ? `projects/${projName}/static/${projName}/css/build/site.css`
  : null;

// Set source paths
// (for components)
fractal.components.set('exclude', '*.md');
fractal.components.set('path', __dirname + '/patterns');
// (for stylesheets)
fractal.components.set('default.context', {
  styles: {
    shouldSkipBase: true, // true, because site.css includes components
    internal: {
      global: [ cmsCSSFile ].concat( ( projCSSFile ) ? [ projCSSFile ] : [] )
    },
    external: {
      global: [
        'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'
      ]
    }
  }
});
fractal.cli.log(`+ Included CSS for "${cmsName}": '${cmsCSSFile}'`);
if ( projCSSFile ) {
  fractal.cli.log(`+ Included CSS for "${projName}": '${projCSSFile}'`);
}

// Set website paths
/*
fractal.web.set('static.path',
  path.dirname( require.resolve('@tacc/core-styles')) +
  '/..' + // exits 'src/' which is at the end of what require.resolve returns
  '/dist'
);
*/
fractal.web.set('static.path', __dirname + '/styles');
fractal.web.set('builder.dest', __dirname + '/dist');

// Customize theme
const theme = mandelbrot( Object.assign( themeConfig, {
  skin: Object.assign( themeConfig.skin, {
    links: '#877453',
  })
}));
fractal.web.theme( theme );

// Export
module.exports = fractal;
