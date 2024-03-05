/**
 * Whether to log debug info to console
 * @const {string}
 */
const SHOULD_DEBUG = window.DEBUG;

/**
 * Set external links (automatically discovered) to open in new tab
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
    const isSameHost = link.host === baseDocHost || link.host === baseDocHostWithSubdomain

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
  });
}
