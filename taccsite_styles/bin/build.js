#!/usr/bin/env node

/** Build CSS using the Core-Styles API */

const fs = require('fs');
const buildStylesheets = require('@tacc/core-styles').buildStylesheets;
const mininmist = require('minimist');

const ROOT = __dirname + '/../..';
const CMS_NAME = 'core-cms';
const ARGS = mininmist( process.argv.slice( 2 ) );

const PROJECT_NAME = ARGS['project'] || '';
const BUILD_ID = ARGS['build-id'] || '';

/** Build stylesheets for Core and (optional) project */
(() => {
  const hasProject = ( PROJECT_NAME && PROJECT_NAME !== CMS_NAME );

  // Get root paths
  const cmsStylesRoot = `${ROOT}/taccsite_styles`;
  const projStylesRoot = `${ROOT}/taccsite_custom/${PROJECT_NAME}/static/${PROJECT_NAME}/css`;

  // Get config paths
  const cmsConfPath = `${cmsStylesRoot}/.postcssrc.yml`;
  const projConfPath = `${projStylesRoot}/.postcssrc.yml`;
  const confPaths = [cmsConfPath];
  // Always add relevant available project config
  // FAQ: Project can customize Core build (e.g. theme changes CSS env. values)
  if ( hasProject && fs.existsSync( projConfPath ) ) {
    confPaths.push( projConfPath );
  }

  // Get source & dest paths
  const cmsInputPath = `${cmsStylesRoot}/src/**/*.css`;
  const projInputPath = `${projStylesRoot}/src/**/*.css`;
  const cmsOutputDir = `${ROOT}/taccsite_cms/static/site_cms/css/build`;
  const projOutputDir = `${projStylesRoot}/build`;

  // Build
  _build('Core', cmsInputPath, cmsOutputDir, confPaths, BUILD_ID );
  if ( hasProject ) {
    _build( PROJECT_NAME, projInputPath, projOutputDir, confPaths, BUILD_ID );
  }
})();

/**
 * Execute command to build stylesheets
 * @param {string} name - The name of the project
 * @param {string} inputPath - The path to the project source CSS files
 * @param {string} outputDir - The path to a directory for compiled CSS
 * @param {array.string} configs - The list of config file paths
 * @param {string} id - The value to identify the build
 */
function _build( name, inputPath, outputDir, configs, id ) {
  console.log(`Overriding config with:`, configs );
  console.log(`Building "${name}" styles:`);

  buildStylesheets(
    inputPath,
    outputDir,
    {
      customConfigs: configs,
      verbose: true,
      buildId: id
    }
  );
}
