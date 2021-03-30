// Configure PostCSS processor
// SEE: https://www.npmjs.com/package/postcss#js-api
// FAQ: Not configuring via `package.json` so env variable access is simple

const dotenv = require('dotenv');

const env = dotenv.config({ path: '.env' }).parsed;

module.exports = {
  plugins: [
    require('postcss-import')({
      path: [
        './taccsite_cms/static/site_cms/css/src',
        `./taccsite_custom/${env.CUSTOM_ASSET_DIR}/static/${env.CUSTOM_ASSET_DIR}/css/src`
      ],
      filter: path => ! RegExp('^/static').test(path)
    }),
    require('postcss-extend')(),
    require('postcss-preset-env')({
      // SEE: https://github.com/csstools/postcss-preset-env#features
      stage: false,
      // SEE: https://github.com/csstools/postcss-preset-env/blob/master/src/lib/plugins-by-id.js#L35
      features: {
        'custom-media-queries': true,
        'media-query-ranges': true,
      }
    }),
    require('cssnano')({
      preset: ['default', {
        // Disabled to avoid sweeping bad CSS under the rug
        // NOTE: Also fixes comparability in tests by retaining expectation code
        discardDuplicates: { exclude: true },
        mergeRules: { exclude: true },
      }]
    })
  ]
}
