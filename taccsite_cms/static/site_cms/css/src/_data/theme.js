const dotenv = require('dotenv');

const env = dotenv.config({ path: '.env' }).parsed;
const theme = env.THEME || 'default'
const data = require(`./theme.${theme}.json`);

console.log(data);

module.exports = data;
