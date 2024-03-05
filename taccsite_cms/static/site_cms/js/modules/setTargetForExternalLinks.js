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
  const baseDocumentHost = document.location.host;
  const baseDocumentHostWithSubdomain= `www.${baseDocumentHost}`;

  [ ...links ].forEach( function setTarget(link) {
      if ( ! link.href) {
        return false;
      }

      const isMailto = (link.href.indexOf('mailto:') === 0);
      const isAbsolute = (link.href.indexOf('http') === 0);
      const isInternalLink = link.host === baseDocumentHost || link.host === baseDocumentHostWithSubdomain

      if (!isInternalLink || isMailto) {
        if (link.target !== '_blank') {
          link.target = '_blank';
          if (SHOULD_DEBUG) {
            console.debug(`Link ${link.href} now opens in new tab`);
          }
        }
        if (link.target === '_blank') {
          link.setAttribute('aria-description', 'Opens in new window.');
        }
      }

      // Links w/ absolute URL to page on same domain should use relative path
      if (isAbsolute && isInternalLink) {
        link.href = link.pathname;
      }
  });
}
