/**
 * Whether to log debug info to console
 * @const {string}
 */
const SHOULD_DEBUG = window.DEBUG;

/**
 * Set external links (automatically discovered) to open in new tab
 */
export default function findLinksAndSetTargets() {
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
