'use strict';

const path = require('path');
const mandelbrot = require('@frctl/mandelbrot');
const minimist = require('minimist');

const { getStaticFilePath } = require( __dirname + '/bin/get-path.js');

const args = minimist( process.argv.slice( 2 ));
let projectName = args['project'] || '';
    projectName = ( projectName !== 'core-cms' ) ? projectName : '';
const projectCSSFile = projectName
  ? path.join( '/', getStaticFilePath( projectName, 'css/build/site.css'))
  : null;

const fractal = require('@tacc/core-styles/fractal.config.js');
const themeConfig = require('@tacc/core-styles/fractal.theme.js');

const theme = mandelbrot( Object.assign( themeConfig, {
  skin: Object.assign( themeConfig.skin, {
    links: '#877453',
  })
}));

const coreStylesRoot = path.join(
  path.dirname( require.resolve('@tacc/core-styles')),
  // The '../' exits 'src/' which require.resolve returns a file from
  '../'
);

fractal.components.set('path',
  path.join( coreStylesRoot, 'src/lib/_imports')
);
fractal.components.set('default.context', {
  styles: {
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

fractal.web.set('static.path',
  path.join( coreStylesRoot, 'dist')
);
fractal.web.set('builder.dest', __dirname + '/taccsite_ui');

fractal.web.theme( theme );

module.exports = fractal;
