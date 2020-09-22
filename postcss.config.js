// Configure PostCSS processor
// SEE: https://www.npmjs.com/package/postcss#js-api
// FAQ: Not configuring via `package.json` so env variable access is simple

const dotenv = require('dotenv');

const env = dotenv.config({ path: '.env' }).parsed;
let importPathsForCustomAsset = [];

if (env.CUSTOM_ASSET_DIR) {
  importPathsForCustomAsset.push(
    `./taccsite_custom/${env.CUSTOM_ASSET_DIR}/static/${env.CUSTOM_ASSET_DIR}/styles`
  );
}

module.exports = {
  plugins: [
    require('postcss-import')({
      path: [
        './taccsite_cms/static/site_cms/styles'
      ].concat(
        importPathsForCustomAsset
      )
    }),
    require('cssnano')({
      preset: 'default'
    })
  ]
}
