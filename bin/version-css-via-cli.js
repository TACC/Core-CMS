#!/usr/bin/env node

/** Create CSS version comment file using the Core-Styles CLI */

const cmd = require('node-cmd');

const BUILD_ID = process.env.npm_config_build_id || '';

const outputPath = __dirname + '/../taccsite_cms/static/site_cms/css/src/_version.css';

cmd.runSync(`
  core-styles version\
  --output-path "${outputPath}"\
  --build-id "${BUILD_ID}"\
`);
