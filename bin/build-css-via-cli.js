#!/usr/bin/env node

/** Build CSS using the Core-Styles CLI */

const cmd = require('node-cmd');

const ROOT = __dirname + '/..';
const PROJECT_NAME = process.env.npm_config_project || undefined;

build(PROJECT_NAME);

/**
 * Execute command to build CSS for Core and optional project/directory
 * @param {string} [projectName] - The name of the custom project's directory
 */
function build( projectName ) {
  const corePath = getPath('taccsite_cms', 'site_cms');
  const projectPath = getPath('taccsite_custom/' + projectName, projectName);

  // To illustrate Project is built on top of Core:
  // // build Core first
  cmd.runSync(`
    core-styles build\
    --input-dir "${ROOT}/${corePath}/src"\
    --output-dir "${ROOT}/${corePath}/build"\
    --custom-configs\
      "${ROOT}/${corePath}/.postcssrc.yml"\
    --verbose\
  `);
  // // build Project next (if at all)
  if (projectName) {
    cmd.runSync(`
      core-styles build\
      --input-dir "${ROOT}/${projectPath}/src"\
      --output-dir "${ROOT}/${projectPath}/build"\
      --custom-configs\
        "${ROOT}/${corePath}/.postcssrc.yml"\
        "${ROOT}/${projectPath}/.postcssrc.yml"\
      --verbose\
    `);
  }
}

/**
 * Get path to CSS resources
 * @param {string} dirName - The name of the directory
 * @param {string} [subDirName=dirName] - The name of the sub-directory
 * @return {string}
 */
function getPath( dirName, subDirName ) {
  return dirName + '/static/' + (subDirName || dirName) + '/css';
}
