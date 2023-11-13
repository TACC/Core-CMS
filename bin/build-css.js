#!/usr/bin/env node

/** Build CSS using the Core-Styles API */

const fs = require('fs');
const buildStylesheets = require('@tacc/core-styles').buildStylesheets;
const mininmist = require('minimist');

const ROOT = __dirname + '/..';
const CORE_NAME = 'core-cms';
const ARGS = mininmist( process.argv.slice( 2 ) );

const PROJECT_NAME = ARGS['project'] || '';
const BUILD_ID = ARGS['build-id'] || '';

/** Build stylesheets for Core and (optional) project */
(() => {
  // Get style paths
  const corePath = _getPath('taccsite_cms', 'site_cms');
  const projPath = _getPath(`taccsite_custom/${PROJECT_NAME}`, PROJECT_NAME );
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

  // Prepare for build
  defaultOpts = {
    verbose: true,
    buildId: BUILD_ID
  }

  // Build styles
  _build('Core', {
    input: `${ROOT}/${corePath}/src/**/*.css`,
    output: `${ROOT}/${corePath}/build`,
    opts: {...defaultOpts, ...{
      customConfigs: confPaths
    }}
  });
  if ( hasProject ) {
    _build( PROJECT_NAME, {
      input: `${ROOT}/${projPath}/src/**/*.css`,
      output: `${ROOT}/${projPath}/build`,
      opts: {...defaultOpts, ...{
        customConfigs: confPaths
      }}
    });
  }
})();

/**
 * Execute command to build stylesheets
 * @param {string} name - The name of the project
 * @param {object} opts - The value to identify the build
 * @param {string} opts.input - The path to project source CSS
 * @param {string} opts.output - The path to put the built CSS
 * @param {@tacc/core-styles.buildStylesheets.opts} opts.opts - Advanced options
 */
function _build( name, opts ) {
  console.log(`Overriding config with:`, opts.opts.customConfigs );
  console.log(`Building "${name}" styles:`);
  buildStylesheets( opts.input, opts.output, opts.opts );
}

/**
 * Get path to CSS resources
 * @param {string} dirName - The name of the directory
 * @param {string} [subDirName=dirName] - The name of the sub-directory
 * @return {string}
 */
function _getPath( dirName, subDirName ) {
  return dirName + '/static/' + ( subDirName || dirName ) + '/css';
}
