/* WARNING: This file is loaded by this codebase, and by an external codebase:
   - https://bitbucket.org/taccaci/frontera-tech-docs/src/staging/frontera_theme/base.html
   - https://gitlab.tacc.utexas.edu/wma-cms/frontera-cms/blob/master/taccsite_cms/templates/base.html#L74
*/
/* TODO: Split into modules, and document with JSDoc */


/* MODULE `flagLinkAsActive` */

/* MODULE `flagLinkAsActive`: Dependencies */
// Polyfill for `NodeList.prototype.forEach()`,
// because browser support is still "recent"
// SEE: https://developer.mozilla.org/en-US/docs/Web/API/NodeList/forEach#Polyfill
if (window.NodeList && !NodeList.prototype.forEach) {
   NodeList.prototype.forEach = Array.prototype.forEach;
}

/* MODULE `flagLinkAsActive`: "Private" */
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
    const doesPropertyMatch = (property) => (locationA[property] === locationB[property]);

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

/* MODULE `flagLinkAsActive`: Public */
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



window.onload = function() {

  /* MODULE `loadJSON`: Dependencies */
  /* `window.jQuery` */

  /* MODULE `loadJSON`: Define */
  /* MODULE `loadJSON`: Use */
  // Load user authentication JSON from Portal, and perform dependent actions
  // - If user is authenticated:
  //     - Populate username (to show that user is logged in)
  //     - Show portal nav dropdown (it is pre-hidden via classname)
  // - If user is NOT authenticated:
  //     - Show portal login link (it is pre-hidden via classname)
  function loadJSON(path, success, error)
  {
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function()
      {
          if (xhr.readyState === XMLHttpRequest.DONE) {
              if (xhr.status === 200) {
                  if (success)
                      success(JSON.parse(xhr.responseText));
              } else {
                  console.log('error state')
                  jQuery('#frontera-login-link').removeClass('d-none');
              }
          }
      };
      xhr.open("GET", path, true);
      xhr.send();
  }
  loadJSON('/api/users/auth/',
           function(data) { console.log(data);
               jQuery('#frontera-core-username').text(data['username']);
               jQuery('#frontera-core-dropdown').removeClass('d-none');
           },
           function(xhr) { console.error(xhr); }
  );

    /* MODULE `flagLinkAsActive`: Use */
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
    })();

}
