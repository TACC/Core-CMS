/**
 * Whether to log debug info to console
 * @const {string}
 */
const SHOULD_DEBUG = window.DEBUG;

/**
 * Function to perform after setting link target
 * @callback setTargetCallback
 * @param {HTMLElement} link
 */

/**
 * Set external links (automatically discovered) to open in new tab
 * @param {object} [options] - Optional parameters
 * @param {array.<string>} [options.pathsToExernalSite=[]] - (DEPRECATED) A list of relative URL paths that should be treated like external URLs
 * @param {array.<string|RegExp>} [options.pathsToForceSetTarget=[]] - A list of relative URL paths (or patterns) that should trigger setting a target
 * @param {HTMLElement|Document} [options.scopeElement=document] - The element within which to search for links
 * @param {setTargetCallback} [options.setTargetCallback] - A callback for after a target is set
 */
 export default function findLinksAndSetTargets(options) {
  const defaults = {
    target: '_blank',
    pathsToExernalSite: [],
    pathsToForceSetTarget: [],
    scopeElement: document
  }
  const {target, pathsToExernalSite, scopeElement, setTargetCallback} = {...defaults, ...options};
  let {pathsToForceSetTarget} = {...defaults, ...options};

  if ( pathsToExernalSite.length && ! pathsToForceSetTarget.length ) {
    pathsToForceSetTarget = pathsToExernalSite;
  }

  const links = scopeElement.getElementsByTagName('a');
  [ ...links ].forEach( function setTarget(link) {
      if ( ! link.href) {
        return false;
      }
      if (link.href.indexOf('javascript') === 0) {
        return false;
      }

      const isMailto = (link.href.indexOf('mailto:') === 0);
      const shouldForceSetTarget = pathsToForceSetTarget.some(path => {
        let shouldForce;
        if (path instanceof RegExp) {
          shouldForce = path.test(link.pathname);
        }
        if (typeof path === 'string') {
          shouldForce = _doPathsMatch(path, link.pathname);
        }
        if (SHOULD_DEBUG && shouldForce) {
          console.debug(`Path "${link.pathname}" matches "${path}"`);
        }
        return shouldForce;
      });
      // FAQ: I am literally double-checking, because I don't trust JavaScript
      const isExternal = (link.origin !== document.location.origin);
      const isInternal = (link.host === document.location.host);
      const shouldSetTarget = shouldForceSetTarget || (
          ! isInternal && isExternal && ! isMailto
      );

      if ( shouldSetTarget ) {
          if (link.target !== '_blank') {
              link.target = '_blank';
              if (SHOULD_DEBUG) {
                console.debug(`Link ${link.href} now opens in new tab`);
              }
          }
          if (typeof setTargetCallback === 'function') {
            setTargetCallback( link );
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

  const isMatch = redirectPath === testLinkPath
    || redirectPath === testLinkPath.slice(1)
    || redirectPath === testLinkPath.slice(0, -1)
    || redirectPath === testLinkPath.slice(1).slice(0, -1);

  return isMatch;
}
