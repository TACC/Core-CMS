// Process CSS and output to desired directories
// FAQ: Not configuring via `package.json` so env variable access is simple

const dotenv = require('dotenv');
const { parallel } = require('async');
const { exec } = require('child_process');

const env = dotenv.config({ path: '.env' }).parsed;
const standardConfigDir = 'conf/css/';

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
/**
 * Build styles for the Core CMS
 */
function buildStylesCore() {
  let command;

  const sourceDir = '';
  const configDir = standardConfigDir;

  // Quote globbed paths to prevent OS from parsing them
  // SEE: https://github.com/postcss/postcss-cli/issues/142#issuecomment-310681302
  command = `postcss "taccsite_cms/static/site_cms/css/src/${sourceDir}*.css" --base "taccsite_cms/static/site_cms/css/src/" --dir "taccsite_cms/static/site_cms/css/build" --verbose --colors --config "${configDir}"`;

  console.log(command);
  exec(command, execCallback);
}
/**
 * Build styles for custom CMS projects
 */
function buildStylesCustom() {
  // Quote globbed paths to prevent OS from parsing them
  // SEE: https://github.com/postcss/postcss-cli/issues/142#issuecomment-310681302
  const command = `postcss "taccsite_custom/${env.CUSTOM_ASSET_DIR}/static/${env.CUSTOM_ASSET_DIR}/css/src/*.css" --base "taccsite_custom/${env.CUSTOM_ASSET_DIR}/static/${env.CUSTOM_ASSET_DIR}/css/src/" --dir "taccsite_custom/${env.CUSTOM_ASSET_DIR}/static/${env.CUSTOM_ASSET_DIR}/css/build" --verbose --colors --config "${standardConfigDir}"`;

  console.log(command);
  exec(command, execCallback);
}

// To explain why output is not sequiential
console.warn('The output may be out of order because the commands are run in parallel.' + "\n");

// Build process for styles may be run in parallel because they are independent
// SEE: https://stackoverflow.com/a/10776939/11817077
parallel([
  buildStylesCore,
  buildStylesCustom
], parallelCallback);
