// Process CSS and output to desired directories
// FAQ: Not configuring via `package.json` so env variable access is simple

const dotenv = require('dotenv');

const { existsSync } = require('fs');
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
function buildStylesCore() {
  const dirMap = {
    source: `taccsite_cms/static/site_cms/styles/exports`,
    base: `taccsite_cms/static/site_cms/styles/exports`,
    output: `taccsite_cms/static/build/styles`,
  }

  buildStyles(dirMap);
}
function buildStylesCustom() {
  let assetDirs = [];
  const assetDirsString = env.CUSTOM_ASSET_DIRS;

  if (assetDirsString) {
    assetDirs = assetDirsString.split(',').map(val => val.trim());

    assetDirs.forEach(assetDir => {
      const dirMap = {
        source: `taccsite_custom/${assetDir}/static/${assetDir}/styles/exports`,
        base: `taccsite_custom/${assetDir}/static/${assetDir}/styles/exports`,
        output: `taccsite_custom/${assetDir}/static/build/styles`,
      };

      buildStyles(dirMap);
    });
  }
}
// FAQ: The CLI is the easiest and cheapest "PostCSS Runner",
// SEE: https://github.com/postcss/postcss-cli#readme
// FAQ: PostCSS JS API not used because it is for a "PostCSS Runner" not a user
// SEE: https://www.npmjs.com/package/postcss#js-api
function buildStyles(dirMap) {
  [ dirMap.source, dirMap.base ].forEach(path => {
    if ( ! existsSync(path)) {
      console.warn(`Directory ${path} not found.`);
    } else {
      // Quote globbed paths to prevent OS from parsing them
      // SEE: https://github.com/postcss/postcss-cli/issues/142#issuecomment-310681302
      exec(`postcss "${dirMap.source}/**/*.css" --base "${dirMap.base}" --dir "${dirMap.output}"`, execCallback);
    }
  });
}

// Build process for styles may be run in parallel because they are independent
// SEE: https://stackoverflow.com/a/10776939/11817077
parallel([
  buildStylesCore,
  buildStylesCustom,
], parallelCallback);
