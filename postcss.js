// Process CSS and output to desired directories
// FAQ: Not configuring via `package.json` so env variable access is simple

const dotenv = require('dotenv');
const { parallel } = require('async');
const { exec } = require('child_process');

const env = dotenv.config({ path: '.env' }).parsed;

// Isolate boilerplate error/ouput handling logic
function execCallback(err, stdout, stderr) {
  if (err) {
    console.error(err);
    return;
  }
  if (stderr) {
    console.error(stderr);
    return;
  }
  console.log(stdout);
}
function parallelCallback(err, results) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(results);
}

// Process via CLI (`postcss-cli`) via Node (this script)
// FAQ: The CLI is the easiest and cheapest "PostCSS Runner",
// SEE: https://github.com/postcss/postcss-cli#readme
// FAQ: PostCSS JS API not used because it is for a "PostCSS Runner" not a user
// SEE: https://www.npmjs.com/package/postcss#js-api
function buildStylesCore() {
  // Quote globbed paths to prevent OS from parsing them
  // SEE: https://github.com/postcss/postcss-cli/issues/142#issuecomment-310681302
  const command = `postcss "taccsite_cms/static/site_cms/css/src/*.css" --dir "taccsite_cms/static/site_cms/css/build" --verbose --colors`;

  console.log(command);
  exec(command, execCallback);
}
function buildStylesCustom() {
  // Quote globbed paths to prevent OS from parsing them
  // SEE: https://github.com/postcss/postcss-cli/issues/142#issuecomment-310681302
  const command = `postcss "taccsite_custom/${env.CUSTOM_ASSET_DIR}/static/${env.CUSTOM_ASSET_DIR}/css/src/*.css" --dir "taccsite_custom/${env.CUSTOM_ASSET_DIR}/static/${env.CUSTOM_ASSET_DIR}/css/build" --verbose --colors`;

  console.log(command);
  exec(command, execCallback);
}

// The confusing is worth explaining (and fixing if we know how)
console.warn('The commands are run in parallel so the output may be out of order.' + "\n");

// Build process for styles may be run in parallel because they are independent
// SEE: https://stackoverflow.com/a/10776939/11817077
parallel([
  buildStylesCore,
  buildStylesCustom,
], parallelCallback);
