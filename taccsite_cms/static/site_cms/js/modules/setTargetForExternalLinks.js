/**
 * Whether to log debug info to console
 * @const {string}
 */
const SHOULD_DEBUG = window.DEBUG;

/**
 * Make links with absolute URLs open in new tab, and:
 * - add accessible markup
 * - fix absolute URLs that should be relative paths
 */
export default function findLinksAndSetTargets() {
  const links = document.querySelectorAll('body > :is(header, main, footer) a');
  const baseDocHost = document.location.host;
  const baseDocHostWithSubdomain= `www.${baseDocHost}`;

  [ ...links ].forEach( function setTarget(link) {
    const linkHref = link.getAttribute('href');

    if ( ! linkHref ) {
      return false;
    }

    const isMailto = ( linkHref.indexOf('mailto:') === 0 );
    const isAbsolute = ( linkHref.indexOf('http') === 0 );
    const isSameHost = link.host === baseDocHost || link.host === baseDocHostWithSubdomain

    if (SHOULD_DEBUG) {
      console.debug({ isMailto, isAbsolute, isSameHost, linkHref });
    }

    // Links to pages at different host should open in new tab
    if ( ! isSameHost || isMailto ) {
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

    // Links w/ absolute URL to page on same domain should use relative path
    if ( isAbsolute && isSameHost ) {
      link.href = link.pathname;
    }
  });
}
