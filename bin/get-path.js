#!/usr/bin/env node

/** Get paths to core or project assets */

const path = require('path');

/**
 * Get path to source file
 * @param {string} dirName - The name of the project directory
 * @param {string} [appName=dirName] - The name of the app directory
 * @param {string} [end] - Any thing to append to the path
 * @return {string}
 */
function getSourcePath( dirName, appName, end ) {
  const subDirName = appName || dirName;
  return path.join( dirName, 'static', subDirName, end );
}

/**
 * Get Django static file path
 * @param {string} appName - The name of the app directory
 * @param {string} [end] - Any thing to append to the path
 * @return {string}
 */
function getStaticFilePath( appName, end ) {
  return path.join( 'static', appName, end );
}

module.exports = { getSourcePath, getStaticFilePath };
