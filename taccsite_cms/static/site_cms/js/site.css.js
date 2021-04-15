// NOTE: Load this before `site.header.css` which relies on this script */
// NOTE: Only for Portal & Docs (CMS already sets theme class via template) */

import { getFromURL as getDataFromURL } from './modules/importData.js';

/**
 * Set application theme (by adding class to `<html>`)
 */
function setThemeClass() {
  getDataFromURL('/cms/api/settings/', 'json').then(data => {
    const { themeClassName } = data || {};

    if (themeClassName) {
      document.documentElement.classList.add(themeClassName);
    }
  });
}

setThemeClass();
