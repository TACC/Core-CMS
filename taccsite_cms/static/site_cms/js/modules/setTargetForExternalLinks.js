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
  const links = document.getElementsByTagName('a');
  const baseDocHost = document.location.host;
  const baseDocHostWithSubdomain= `www.${baseDocHost}`;

  [ ...links ].forEach( function setTarget(link) {
    if ( ! link.href) {
      return false;
    }

    const isMailto = ( link.href.indexOf('mailto:') === 0 );
    const isAbsolute = (link.href.indexOf('http') === 0);
    const isSameHost = link.host === baseDocHost || link.host === baseDocHostWithSubdomain

    // Links to pages at different host should open in new tab
    if ( ! isSameHost || isMailto ) {
      if ( link.target !== '_blank') {
        link.target = '_blank';
        if (SHOULD_DEBUG) {
          console.debug(`Link ${link.href} now opens in new tab`);
        }
      }
      if ( link.target === '_blank') {
        link.setAttribute('aria-description', 'Opens in new window.');
      }
    }

    // Links w/ absolute URL to page on same domain should use relative path
    if ( isAbsolute && isInternalLink ) {
      link.href = link.pathname;
    }
  });
}
