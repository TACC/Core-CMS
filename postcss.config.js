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
      ]
    }),
    require('cssnano')({
      preset: 'default'
    })
  ]
}
