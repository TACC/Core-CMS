'use strict';

const path = require('path');
const mandelbrot = require('@frctl/mandelbrot');
const minimist = require('minimist');

// Get base config
const fractal = require('@tacc/core-styles/fractal.config.js');
const themeConfig = require('@tacc/core-styles/fractal.theme.js');

// Get project
// (name)
const { getStaticFilePath } = require( __dirname + '/bin/get-path.js');
const args = minimist( process.argv.slice( 2 ));
let projectName = args['project'] || '';
    projectName = ( projectName !== 'core-cms' ) ? projectName : '';
// (stylesheet)
const projectCSSFile = projectName
  ? path.join( '/', getStaticFilePath( projectName, 'css/build/site.css'))
  : null;

// Get base path
const coreStylesRoot = path.join(
  path.dirname( require.resolve('@tacc/core-styles')),
  // The '../' exits 'src/' which is at the end of what require.resolve returns
  '../'
);

// Set source paths
// (for components)
fractal.components.set('path',
  path.join( coreStylesRoot, 'src/lib/_imports')
);
// (for stylesheets)
fractal.components.set('default.context', {
  styles: {
    shouldSkipBase: true, // true, because site.css includes components
    external: {
      global: [
        'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
        '/static/site_cms/css/build/site.css'
      ].concat(
        ( projectCSSFile ) ? [ projectCSSFile ] : []
      )
    }
  }
});
if ( projectCSSFile ) {
  fractal.cli.log(`+ Included CSS for "${projectName}": '${projectCSSFile}'`);
}

// Set website paths
fractal.web.set('static.path', path.join( coreStylesRoot, 'dist'));
fractal.web.set('builder.dest', __dirname + '/taccsite_ui');

// Customize theme
const theme = mandelbrot( Object.assign( themeConfig, {
  skin: Object.assign( themeConfig.skin, {
    links: '#877453',
  })
}));
fractal.web.theme( theme );

// Export
module.exports = fractal;