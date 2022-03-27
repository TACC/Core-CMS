#!/usr/bin/env node

/** Build CSS using the Core-Styles CLI */

const fs = require('fs');
const cmd = require('node-cmd');
const mininmist = require('minimist');

const ROOT = __dirname + '/..';
const CORE_NAME = 'core-cms';
const ARGS = mininmist(process.argv.slice(2));

const PROJECT_NAME = ARGS['project'] || '';
const BUILD_ID = ARGS['build-id'] || '';

/** Build stylesheets for Core and (optional) project */
(() => {
  // Get style paths
  const corePath = _getPath('taccsite_cms', 'site_cms');
  const projectPath = _getPath('taccsite_custom/' + PROJECT_NAME, PROJECT_NAME);
  const hasProject = (PROJECT_NAME && PROJECT_NAME !== CORE_NAME);

  // Get config paths
  const coreConfigPath = `${ROOT}/${corePath}/.postcssrc.yml`;
  const projectConfigPath = `${ROOT}/${projectPath}/.postcssrc.yml`;
  const configPaths = [coreConfigPath];

  // Always add relevant available project config
  // FAQ: Project can customize Core build (e.g. theme changes CSS env. values)
  if (hasProject && fs.existsSync(projectConfigPath)) {
    configPaths.push(projectConfigPath);
  }

  // Build
  _build('Core', corePath, configPaths, BUILD_ID);
  if (hasProject) {
    _build(PROJECT_NAME, projectPath, configPaths, BUILD_ID);
  }
})();

/**
 * Execute command to build stylesheets
 * @param {string} name - The name of the project
 * @param {string} path - The path to the project source CSS
 * @param {array.string} configs - The list of config file paths
 * @param {string} id - The value to identify the build
 */
 function _build(name, path, configs, id) {
  const configValues = '"' + configs.join('" "') + '"';

  console.log(`Building "${name}" styles:`);
  cmd.runSync(`
    core-styles build\
    --input-dir "${ROOT}/${path}/src"\
    --output-dir "${ROOT}/${path}/build"\
    --custom-configs ${configValues}\
    --build-id "${id}"\
    --verbose\
  `);
}

/**
 * Get path to CSS resources
 * @param {string} dirName - The name of the directory
 * @param {string} [subDirName=dirName] - The name of the sub-directory
 * @return {string}
 */
 function _getPath( dirName, subDirName ) {
  return dirName + '/static/' + (subDirName || dirName) + '/css';
}
