#!/usr/bin/env node

/** Create CSS file to import that prints project version */

const fs = require('fs');
const childProcess = require('child_process');

const package = require('../package.json');
const root = __dirname;
const outFile = root + '/../taccsite_cms/static/site_cms/css/src/_version.css';

/**
 * Whether a Git revision look like something we can use
 * @param {string} rev - The revision to check
 * @return {boolean}
 */
 function isGitRevOkay(rev) {
  const isOkay = /[\da-z]+/.test(rev);

  return isOkay;
}

/**
 * Get the Git revision of the current working directory code
 * @return {string}
 * @see https://stackoverflow.com/a/34518749/11817077
 */
function getGitRev() {
  const rev = childProcess.execSync('git rev-parse HEAD').toString();
  const isRevOkay = isGitRevOkay(rev);

  if ( ! isRevOkay) {
    console.warn(`Revision looks odd. Is this okay?` + rev);
  }

  return rev;
}

/**
 * Get data and write content to version file
 * @return {string}
 * @see https://stackoverflow.com/a/34518749/11817077
 */
(async function writeRevToFile() {
  // FP-1544: IF tags are annotated THEN replace ver + rev with `git describe`
  const ver = package.version;
  const rev = await getGitRev().substring(0, 7);

  const cssVersion = `#${rev} (≥ v${ver})`;
  const cssLicense = package.license;

  const output = `/*! @tacc/core-styles${cssVersion} | ${cssLicense} | github.com/TACC/Core-Styles */` + "\n";

  console.log(`Updating CSS version to ${cssVersion}`);

  fs.writeFileSync(outFile, output, 'utf8');
})();
