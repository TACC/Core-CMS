/**
 * Export appropriate theme file based on settings value
 */
const rootPath = __dirname + '/../../../../../../';
const settings = require( rootPath + 'taccsite_cms/settings.json');
const theme = settings.THEME || 'default';

/**
 * Perform `require` but on fail:
 * - execute callback
 * - exit program (as fatal exception)
 * @param {string} modulePath - Path to the module to require
 * @param {function} callback - Callback (returns exception from `require()`)
 * @return {*} Content of the module (if successfully required)
 * @see https://stackoverflow.com/a/34005010/11817077
 */
function requireOrElse(modulePath, callback) {
  try {
    return require(modulePath);
  }
  catch (e) {
    if (typeof callback === 'function') {
      callback(e);
    }
    process.exit(1);
  }
}

const data = requireOrElse(`./theme.${theme}.json`, () => {
  console.error(`Unable to find '${__dirname}/theme.${theme}.json'`);
});

module.exports = data;
