/**
 * The standard lnsk to open in new windows
 * @const {string}
 */
export const DEFAULT_LINKS = document.querySelectorAll('body > :is(header, main, footer) a');

/**
 * Make links with absolute URLs open in new tab, and:
 * - add accessible markup
 * - fix absolute URLs that should be relative paths
 * @param {NodeList} links - Custom links to open in new tab
 * @param {object} options
 * @param {boolean} [options.shouldDebug=false] - Whether to log debug statements
 * @param {boolean} [options.shouldFilter=true] - Whether to filter which links to adjust
 */
export default function findLinksAndSetTargets( links = DEFAULT_LINKS, options = {
  shouldDebug: false,
  shouldFilter: true,
}) {
  const baseDocHost = document.location.host;
  const baseDocHostWithSubdomain= `www.${baseDocHost}`;

  console.log({ links, options });

  links.forEach( function setTarget( link ) {
    const linkHref = link.getAttribute('href');

    if ( ! linkHref ) {
      return false;
    }

    const isMailto = ( linkHref.indexOf('mailto:') === 0 );
    const isAbsolute = ( linkHref.indexOf('http') === 0 );
    const isSameHost = ( link.host === baseDocHost || link.host === baseDocHostWithSubdomain );
    const shouldOpenInNewTab = ( ! isSameHost || isMailto );

    if (shouldDebug) {
      console.debug({ isMailto, isAbsolute, isSameHost, linkHref });
    }

    // So either all or some links open in new tab
    if ( ! shouldFilter || ( shouldFilter && shouldOpenInNewTab )) {
      if ( link.target !== '_blank') {
        link.target = '_blank';
        if (shouldDebug) {
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
