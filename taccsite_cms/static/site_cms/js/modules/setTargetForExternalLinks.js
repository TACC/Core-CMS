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
  const baseDocumentHost = document.location.host;
  const baseDocumentHostWithSubdomain= `www.${baseDocumentHost}`;

  [ ...links ].forEach( function setTarget(link) {
      if ( ! link.href) {
        return false;
      }

      const isMailto = (link.href.indexOf('mailto:') === 0);

      const isInternalLink = link.host === baseDocumentHost || link.host === baseDocumentHostWithSubdomain

      if (!isInternalLink || isMailto ) {    
        if (link.target !== '_blank') {
          link.target = '_blank';
          if (SHOULD_DEBUG) {
            console.debug(`Link ${link.href} now opens in new tab`);
          }
        }
        if (link.target === '_blank') {
          link.setAttribute('aria-description', 'Opens in new window.');
        }
        if (typeof setTargetCallback === 'function') {
          setTargetCallback( link );
        }
      }
  });
}
