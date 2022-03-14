#!/usr/bin/env node

/** Create CSS file to import that prints project version */

const fs = require('fs');
const path = require('../package.json');
const childProcess = require('child_process');

// Get data
const appLicense = path.license;
const appGitRef = childProcess.execSync('git describe --always').toString();
const filePath = __dirname + '/../taccsite_cms/static/site_cms/css/src/_version.css';
const fileContent = `/*! @tacc/core-cms ${appGitRef} | ${appLicense} | github.com/TACC/Core-CMS */` + "\n";

// Tell user
console.log(`Updating CSS version to ${appGitRef}`);

// Write version
fs.writeFileSync( filePath, fileContent );
