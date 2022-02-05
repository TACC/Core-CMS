#!/usr/bin/env node

const { exec } = require('child_process');

const dotenv = require('dotenv');
const env = dotenv.config({ path: '.env' }).parsed;
const projectName = env.CUSTOM_ASSET_DIR;

// SEE: https://stackoverflow.com/a/63530170
process.env.FORCE_COLOR = true

/**
 * Callback on execution (Node `exec()` callback)
 * @see https://nodejs.org/api/child_process.html#child_processexeccommand-options-callback
 */
function execCallback(err, stdout, stderr) {
  if (err) { console.error(err); return; }
  if (stderr) { console.error(stderr); return; }
  console.log(stdout);
}

/** Build styles for custom CMS projects via external repos */
function buildCustom() {
  const customDir = `taccsite_custom/${projectName}/static/${projectName}/css`;

  const command = `tacc-core-styles -i "${customDir}/src" -o "${customDir}/build" -c "taccsite_custom/.postcssrc.yml" --verbose`;

  exec(command, execCallback);
  // console.log(command); // only shown if command execution is commented out
}

if (projectName !== 'core-cms') {
  buildCustom();
} else {
  console.log(`Skipping '${projectName}'. It should not have custom styles.`)
}
