#!/usr/bin/env node

/** Build CSS using the Core-Styles CLI */

const cmd = require('node-cmd');
const mininmist = require('minimist');

const ROOT = __dirname + '/..';
const CORE_NAME = 'core-cms';
const ARGS = mininmist(process.argv.slice(2));

const PROJECT_NAME = ARGS['project'] || '';
const BUILD_ID = ARGS['build-id'] || '';

/** Execute command to build CSS for Core and optional project/directory */
(() => {
  const corePath = _getPath('taccsite_cms', 'site_cms');
  const projectPath = _getPath('taccsite_custom/' + PROJECT_NAME, PROJECT_NAME);

  // To illustrate Project is built on top of Core:
  // // build Core first
  console.log(`Building Core styles:`);
  cmd.runSync(`
    core-styles build\
    --input-dir "${ROOT}/${corePath}/src"\
    --output-dir "${ROOT}/${corePath}/build"\
    --custom-configs\
      "${ROOT}/${corePath}/.postcssrc.yml"\
    --build-id "${BUILD_ID}"\
    --verbose\
  `);
  // // build Project next (if at all)
  if (PROJECT_NAME && PROJECT_NAME !== CORE_NAME ) {
    console.log(`Building "${PROJECT_NAME}" styles:`);
    cmd.runSync(`
      core-styles build\
      --input-dir "${ROOT}/${projectPath}/src"\
      --output-dir "${ROOT}/${projectPath}/build"\
      --custom-configs\
        "${ROOT}/${corePath}/.postcssrc.yml"\
        "${ROOT}/${projectPath}/.postcssrc.yml"\
      --build-id "${BUILD_ID}"\
      --verbose\
    `);
  }
})();

/**
 * Get path to CSS resources
 * @param {string} dirName - The name of the directory
 * @param {string} [subDirName=dirName] - The name of the sub-directory
 * @return {string}
 */
function _getPath( dirName, subDirName ) {
  return dirName + '/static/' + (subDirName || dirName) + '/css';
}
