/* WARNING: This is merely a polished version of Frontera CMS rush code */
/* SEE: https://gitlab.tacc.utexas.edu/wma-cms/frontera-cms/blob/4a0d198/taccsite_cms/static/site_cms/scripts/base.js#L10 */

/* RFC: Use ES Modules.
        - Convert to modules in CMS
        - Load as modules in Portal
        - Load as modules in User Guide
*/





/* MODULE `includeCMSPagesHTML` */



/* Public Functions */

/**
* Clone markup from an endpoint into a specific element
*
* WARNING: Implicit requirements
* - The specific element must be a `ul` tag
* - The specific element must have the ID `cms-nav-pages`
* - The specific element must have the attribute `data-cms-nav-endpoint`
* @todo Rewrite function to either take parameters or be a custom element
* @todo Use `insertAdjacentHTML` (not `innerHTML`) to insert markup
*/
function includeCMSNavMarkup() {
  const cmsPagesElement = document.getElementById('cms-nav-pages');
  const cmsPagesEndpoint = cmsPagesElement && cmsPagesElement.dataset.cmsNavEndpoint;

  if (cmsPagesEndpoint) {
    fetch(cmsPagesEndpoint).then((response) => {
      return response.text();
    }).then((data) => {
      cmsPagesElement.innerHTML = data;
    }, (err) => {
      cmsPagesElement.innerHTML = null;
      console.error(err);
    }).finally(() => {
      cmsPagesElement.removeAttribute('data-cms-nav-endpoint');
    });
  }
}





/* MODULE `flagLinkAsActive` */



/* Dependencies */

// Polyfill for `NodeList.prototype.forEach()`,
// because browser support is still "recent"
// SEE: https://developer.mozilla.org/en-US/docs/Web/API/NodeList/forEach#Polyfill
if (window.NodeList && !NodeList.prototype.forEach) {
  NodeList.prototype.forEach = Array.prototype.forEach;
}



/* Private Functions */

/**
* Whether given entity is an HTML elment or document
* @param {*} entity - The entity to test
* @returns {boolean}
* @see https://stackoverflow.com/a/36894871
*/
function _isElement(entity) {
  return entity instanceof Element || entity instanceof HTMLDocument;
}
/**
* Whether two given URLs are "matching":
*
* 1. Exactly the same `href`
* 2. Matching set of defined URL properties
*
* @param {HTMLAnchorElement|HTMLAreaElement|Location} locationA
* @param {HTMLAnchorElement|HTMLAreaElement|Location} locationB
* @param {string[]} [propertiesToMatch] - a list of properties that must match
* @return {boolean}
*/
function _areMatchingURLs(locationA, locationB, propertiesToMatch) {
  const doesPropertyMatch = (property) => (locationA[property] === location[property]);

  if (locationA.href && locationA.href === locationB.href) {
    return true;
  }
  /* FAQ: Do not save results, for condition, earlier into variable,
      because the logic could be unnecessary by this line */
  if (propertiesToMatch.every(doesPropertyMatch)) {
    return true;
  }

  return false;
}



/* Public Functions */

/**
* Add an "active" classname on any link whose `href` matches the current page URL
* @param {string} activeClassname - The name of the class to add on active link
* @param {string} linkSelector - A selector with which to search for the link
* @param {string} [ancestorActiveElementSelector] - A selector to find the ancestor on which to apply the classname (if provided, the classname will be applied to this element)
* @param {HTMLElement} [scopeElement=document] - An ancestor element within which to search for link
*/
function flagLinkAsActive(activeClassname, linkSelector, scopeElement, ancestorActiveElementSelector) {
  scopeElement = _isElement(scopeElement) ? scopeElement : document;

  const linkElements = scopeElement.querySelectorAll(linkSelector);

  linkElements.forEach((linkElement) => {
    const propertiesToMatch = ['pathname', 'hostname'];
    const shouldBeActive = _areMatchingURLs(linkElement, document.location, propertiesToMatch);

    if (shouldBeActive) {
      console.info('Found link that is active', linkElement);

      const activeElement = (ancestorActiveElementSelector)
        ? linkElement.closest(ancestorActiveElementSelector)
        : linkElement;

      console.info('Will flag element as active', activeElement);
      activeElement.classList.add(activeClassname);
    }
  });
}



/* EXECUTE */

(function () {
  const activeClassname = 'active';
  /* FAQ: Relying on semantic HTML instead of Bootstrap class names,
          because Bootstrap could be adandoned for modules like a nav */
  const linkSelector = 'a';
  /* TODO: Use an ID when a reliable one exists
          (Wes plans to change the current IDs) */
  const scopeElement = document.getElementsByClassName('s-cms-nav')[0];
  const ancestorActiveElementSelector = 'li';

  flagLinkAsActive(activeClassname, linkSelector, scopeElement, ancestorActiveElementSelector);
  includeCMSNavMarkup();
})();
