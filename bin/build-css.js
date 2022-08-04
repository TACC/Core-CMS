#!/usr/bin/env node

/** Build CSS using the Core-Styles API */

const fs = require('fs');
const buildStylesheets = require('@tacc/core-styles').buildStylesheets;
const mininmist = require('minimist');

const { getSourcePath } = require( __dirname + '/../bin/get-path.js');

const ROOT = __dirname + '/..';
const CORE_NAME = 'core-cms';
const ARGS = mininmist( process.argv.slice( 2 ) );

const PROJECT_NAME = ARGS['project'] || '';
const BUILD_ID = ARGS['build-id'] || '';

/** Build stylesheets for Core and (optional) project */
(() => {
  // Get style paths
  const corePath = getSourcePath(
    'taccsite_cms',
    'site_cms',
    'css'
  );
  const projPath = getSourcePath(
    'taccsite_custom/' + PROJECT_NAME,
    PROJECT_NAME,
    'css'
  );
  const hasProject = ( PROJECT_NAME && PROJECT_NAME !== CORE_NAME );

  // Get config paths
  const coreConfPath = `${ROOT}/${corePath}/.postcssrc.yml`;
  const projConfPath = `${ROOT}/${projPath}/.postcssrc.yml`;
  const confPaths = [coreConfPath];

  // Always add relevant available project config
  // FAQ: Project can customize Core build (e.g. theme changes CSS env. values)
  if ( hasProject && fs.existsSync( projConfPath ) ) {
    confPaths.push( projConfPath );
  }

  // Build
  _build('Core', corePath, confPaths, BUILD_ID );
  if ( hasProject ) {
    _build( PROJECT_NAME, projPath, confPaths, BUILD_ID );
  }
})();

/**
 * Execute command to build stylesheets
 * @param {string} name - The name of the project
 * @param {string} path - The path to the project source CSS
 * @param {array.string} configs - The list of config file paths
 * @param {string} id - The value to identify the build
 */
function _build( name, path, configs, id ) {
  const configValues = '"' + configs.join('" "') + '"';

  console.log(`Overriding config with:`, configs );
  console.log(`Building "${name}" styles:`);
  buildStylesheets(
    `${ROOT}/${path}/src/**/*.css`,
    `${ROOT}/${path}/build`, {
      customConfigs: configs,
      verbose: true,
      buildId: id
    }
  );
}
