/**
 * The standard links that should open in a new tab
 * @const {string}
 */
export const DEFAULT_LINKS = document.querySelectorAll('body > :is(header, main, footer) a');

/**
 * Check if two hosts are effectively the same domain
 * @param {string} linkHost - The host from the link
 * @param {string} baseHost - The current page's host
 * @param {string[]} subdomains - List of valid subdomains
 * @returns {boolean}
 */
function isSameDomain(linkHost, baseHost, subdomains) {
  // Direct match
  if (linkHost === baseHost) return true;

  // Link is to subdomain of base host
  if (subdomains.some(subdomain => linkHost === `${subdomain}.${baseHost}`)) return true;

  // Link is to root domain while we're on subdomain
  if (subdomains.some(subdomain => 
    baseHost.startsWith(`${subdomain}.`) && 
    linkHost === baseHost.replace(`${subdomain}.`, '')
  )) return true;

  return false;
}

/**
 * Make links with absolute URLs open in new tab, and:
 * - add accessible markup
 * - fix absolute URLs that should be relative paths
 * @param {NodeList} links - Custom links to open in new tab
 * @param {object} opts
 * @param {boolean} [opts.shouldDebug=false] - Whether to log debug statements
 * @param {boolean} [opts.shouldFilter=true] - Whether to filter which links to adjust
 */
export default function findLinksAndSetTargets( links = DEFAULT_LINKS, opts = {
  shouldDebug: false,
  shouldFilter: true,
}) {
  const baseDocHost = document.location.host;
  const standardSubdomains = ['www', 'pprd', 'prod', 'dev'];
  const similarHosts = standardSubdomains.map(
    subdomain => `${subdomain}.${baseDocHost}`
  );

  if ( opts.shouldDebug ) {
    console.log({ links, opts });
  }

  links.forEach( function setTarget( link ) {
    const linkHref = link.getAttribute('href');

    if ( ! linkHref ) {
      return false;
    }

    const isMailto = ( linkHref.indexOf('mailto:') === 0 );
    const isAbsolute = ( linkHref.indexOf('http') === 0 );
    const isSameHost = isSameDomain(link.host, baseDocHost, standardSubdomains);
    const shouldOpenInNewTab = ( ! isSameHost || isMailto );

    if (opts.shouldDebug) {
      console.debug({ isMailto, isAbsolute, isSameHost, linkHref, shouldOpenInNewTab });
    }

    // So either all or some links open in new tab
    if ( ! opts.shouldFilter || ( opts.shouldFilter && shouldOpenInNewTab )) {
      if ( link.target !== '_blank') {
        link.target = '_blank';
        if ( opts.shouldDebug ) {
          console.debug(`Link "${ linkHref }" now opens in new tab`);
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
