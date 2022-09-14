/**
 * Whether to log debug info to console
 * @const {string}
 */
const SHOULD_DEBUG = window.DEBUG;

/**
 * Set external links (automatically discovered) to open in new tab
 * @param {object} [options] - Optional parameters
 * @param {array.<string>} [options.pathsToExernalSite=[]] - A list of relative URL paths that should be treated like external URLs
 * @param {HTMLElement|Document} [options.scopeElement=document] - The element within which to search for links
 */
 export default function findLinksAndSetTargets(options) {
  const defaults = {
    pathsToExernalSite: [],
    scopeElement: document
  }
 const {pathsToExernalSite, scopeElement} = {...defaults, ...options};

  const links = scopeElement.getElementsByTagName('a');
  [ ...links ].forEach( function setTarget(link) {
      if ( ! link.href) {
        return false;
      }
      if (link.href.indexOf('javascript') === 0) {
        return false;
      }

      const isMailto = (link.href.indexOf('mailto:') === 0);
      const hasExternalRedirect = pathsToExernalSite.some(path => {
          return _doPathsMatch(path, link.pathname);
      });
      // FAQ: I am literally double-checking, because I don't trust JavaScript
      const isExternal = (link.origin !== document.location.origin);
      const isInternal = (link.host === document.location.host);
      const shouldOpenInNewWindow = (
          ! isInternal && (isExternal || hasExternalRedirect) && ! isMailto
      );

      if ( shouldOpenInNewWindow ) {
          if (link.target !== '_blank') {
              link.target = '_blank';
              if (SHOULD_DEBUG) {
                console.debug(`Link ${link.href} now opens in new tab`);
              }
          }
      }
  });
}

/**
* Does redirect path match link path (ignoring "/" link path)
* @param {string} redirectPath - A path known to redirect to an external site
* @param {string} testLinkPath - A path found on the page being updated
*/
function _doPathsMatch(redirectPath, testLinkPath) {
if (testLinkPath === '/') {
  return false;
}

return redirectPath === testLinkPath
    || redirectPath === testLinkPath.slice(1)
    || redirectPath === testLinkPath.slice(0, -1)
    || redirectPath === testLinkPath.slice(1).slice(0, -1);
}
