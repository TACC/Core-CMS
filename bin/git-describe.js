#!/usr/bin/env node

/** Get tag-based description from Git */
function gitDescribe() {
  const { execSync } = require('child_process');

  let gitDescribe = undefined;

  try {
    gitDescribe = execSync(`
      git describe --tags 2>/dev/null || git rev-parse --short HEAD
    `, { encoding: 'utf8' }).trim();
    console.log('Output from `git describe`:', gitDescribe);
  } catch (error) {
    console.error('Error running `git describe`:', error.message);
  }

  return gitDescribe;
}

module.exports = gitDescribe;
