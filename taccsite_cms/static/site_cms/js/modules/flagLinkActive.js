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
* Normalize URL path:
*
* - Trim beginning and ending slashes
*
* @param {string} path - Path to normalize
* @return {string}
*/
function _normalizePath(path) {
  return path.split('/').filter(x => x != '').join('/');
}

/**
* Whether two given URLs are "matching":
*
* 1. Exactly the same `href`
* 2. Matching set of defined URL properties
*
* @param {HTMLAnchorElement|HTMLAreaElement|Location} locationA
* @param {HTMLAnchorElement|HTMLAreaElement|Location} locationB
* @param {string[]} [propsToMatch] - List of properties that must match
* @return {boolean}
*/
function _areMatchingURLs(locationA, locationB, propsToMatch) {
  const isExactMatch = locationA.href === locationB.href;
  const doAllRequiredPropsMatch = propsToMatch.every(doesPropertyMatch);

  function doesPropertyMatch(property) {
    const isExactMatch = locationA[property] === locationB[property];
    const isFuzzyMatch = !isExactMatch && _normalizePath(locationA[property]) === _normalizePath(locationB[property]);

    return isExactMatch || isFuzzyMatch;
  };

  return isExactMatch || doAllRequiredPropsMatch;
}

/**
* Add an "active" classname on any link whose `href` matches the current page URL
* @param {string} [activeClassname='active'] - Name of the class to add on active link
* @param {string} [linkSelector='a'] - Selector to match links
* @param {string} [ancestorActiveElementSelector=undefined] - A selector to match link ancestor on which to apply `activeClassname``
* @param {HTMLElement} [scopeElement=document] - Element within which to search for link
* @todo Consider converting some or all parameters into keys of options object
*/
export default function flagLinkActive({
  activeClassname = 'active',
  linkSelector = 'a',
  scopeElement = document,
  ancestorActiveElementSelector = undefined
} = {}) {
  const linkElements = scopeElement.querySelectorAll(linkSelector);

  linkElements.forEach((linkElement) => {
    const propsToMatch = ['pathname', 'hostname'];
    const shouldBeActive = linkElement.getAttribute('href') && _areMatchingURLs(linkElement, document.location, propsToMatch);

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
