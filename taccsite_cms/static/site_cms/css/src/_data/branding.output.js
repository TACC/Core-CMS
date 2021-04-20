
const dotenv = require('dotenv');

const env = dotenv.config({ path: '.env' }).parsed;
const template = require('./branding.input.json');

let input = JSON.stringify(template);
    input = input.replace('{{THEME}}', env.THEME);
    input = input.replace('{{COLOR}}', env.COLOR);
const output = JSON.parse(input);

console.log(output);

module.exports = output;
