#!/usr/bin/env node

/** Build CSS using the Core-Styles API */

const buildStylesheets = require('@tacc/core-styles').buildStylesheets;
const mininmist = require('minimist');
const gitDescribe = require('./git-describe');

const ROOT = __dirname + '/..';
const ARGS = mininmist( process.argv.slice( 2 ) );
const BUILD_ID = ARGS['build-id'] || gitDescribe();

/** Build stylesheets */
(() => {
  const stylePath = _getPath('taccsite_cms', 'site_cms');

  // Build styles
  buildStylesheets(
    /* input */
    `${ROOT}/${stylePath}/src/**/*.css`,
    /* output */
    `${ROOT}/${stylePath}/build`,
    /* opts */
    {
      verbose: true,
      buildId: BUILD_ID,
      customConfigs: [
        `${ROOT}/${stylePath}/.postcssrc.yml`
      ]
    }
  );
})();

/**
 * Get path to CSS resources
 * @param {string} dirName - The name of the directory
 * @param {string} [subDirName=dirName] - The name of the sub-directory
 * @return {string}
 */
function _getPath( dirName, subDirName ) {
  return dirName + '/static/' + ( subDirName || dirName ) + '/css';
}
