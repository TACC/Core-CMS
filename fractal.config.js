'use strict';

const path = require('path');
const mandelbrot = require('@frctl/mandelbrot');

const { getStaticFilePath } = require( __dirname + '/bin/get-path.js');


const fractal = require('@tacc/core-styles/fractal.config.js');
const themeConfig = require('@tacc/core-styles/fractal.theme.js');

const theme = mandelbrot(Object.assign(themeConfig, {
  skin: Object.assign(themeConfig.skin, {
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
    external: {
      global: [
        'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
        '/static/site_cms/css/build/site.css'
      ]
    }
  }
});



fractal.cli.command(
  'build-project [project]',
  function buildProject( args, done ) {
    // The Core site is named 'core-cms', but its Python app name is 'site_cms'
    const coreName = 'site_cms';
    let   projName = args.project || coreName;
          projName = ( projName === 'core-cms' ) ? coreName : projName;

    const context = this.fractal.components.get('default.context');
    const projCSSFile = getStaticFilePath( projName, 'css/build/site.css');

    if ( projName ) {
      context.styles.external.global.push( projCSSFile );
    }
    this.fractal.components.set('default.context', context);

    this.fractal.cli.exec('build');

    done();
  }, {
    description: 'Lists components in the project'
  }
);



fractal.web.set('static.path',
  path.join(coreStylesRoot, 'dist')
);
fractal.web.set('builder.dest', __dirname + '/taccsite_ui');

fractal.web.theme(theme);

module.exports = fractal;
