/**
 * Whether to log debug info to console
 * @const {string}
 */
const SHOULD_DEBUG = window.DEBUG;

/**
 * The standard lnsk to open in new windows
 * @const {string}
 */
export const DEFAULT_LINKS = document.querySelectorAll('body > :is(header, main, footer) a');

/**
 * Make links with absolute URLs open in new tab, and:
 * - add accessible markup
 * - fix absolute URLs that should be relative paths
 * @param {NodeList} links - additional links to open in new tab
 */
export default function findLinksAndSetTargets( links = DEFAULT_LINKS ) {
  const baseDocHost = document.location.host;
  const baseDocHostWithSubdomain= `www.${baseDocHost}`;

  console.log({ SHOULD_DEBUG, links });

  links.forEach( function setTarget( link ) {
    const linkHref = link.getAttribute('href');

    if ( ! linkHref ) {
      return false;
    }

    const isMailto = ( linkHref.indexOf('mailto:') === 0 );
    const isAbsolute = ( linkHref.indexOf('http') === 0 );
    const isSameHost = ( link.host === baseDocHost || link.host === baseDocHostWithSubdomain );
    const isDefaultLink = Array.from( DEFAULT_LINKS ).includes( link );
    const shouldOpenInNewTab = ( ! isSameHost || isMailto );

    if (SHOULD_DEBUG) {
      console.debug({ isMailto, isAbsolute, isSameHost, linkHref, isDefaultLink });
    }

    // So custom links or links to pages at different host open in new tab
    if ( ! isDefaultLink || shouldOpenInNewTab ) {
      if ( link.target !== '_blank') {
        link.target = '_blank';
        if (SHOULD_DEBUG) {
          console.debug(`Link ${linkHref} now opens in new tab`);
        }
      }
      if ( link.target === '_blank') {
        link.setAttribute('aria-label', 'Opens in new window.');
      }
    }

    // So links w/ absolute URL to page on same domain use relative path
    if ( isAbsolute && isSameHost ) {
      link.href = link.pathname;
    }
  });
}
