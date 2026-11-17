/**
 * Get URL of external web article of which internal news article represents
 * @param {HTMLElement} article - The article within which to find external URL
 * @return {string|null} - The URL of the external article
 */
function resolveHttpRedirectUrl(href) {
  if (!href) {
    return null;
  }
  const trimmedHref = href.trim();
  try {
    const resolved = new URL(trimmedHref, window.location.href);
    const isProtocolRelative = trimmedHref.startsWith('//');
    const isHttp = resolved.protocol === 'http:' || resolved.protocol === 'https:';
    const isSameOrigin = resolved.origin === window.location.origin;
    const isSameHostname = resolved.hostname === window.location.hostname;
    const sameOriginPath = resolved.pathname + resolved.search + resolved.hash;
    if (!isHttp) {
      return null;
    } else if (isProtocolRelative) {
      if (isSameHostname) {
        return sameOriginPath;
      } else {
        return trimmedHref;
      }
    } else if (isSameOrigin) {
      return sameOriginPath;
    } else {
      return resolved.href;
    }
  } catch {
    return null;
  }
}

/**
 * Resolve redirect target from `.blog-lead` anchors (hidden canonical first).
 * Validates with `new URL(href, window.location.href)` (including `//host/path`);
 * returns the lead anchor's `href` string when it is protocol-relative.
 */
function resolveRedirectUrlFromLeadAnchor(article) {
  const lead = article.querySelector('.blog-lead');
  if (!lead) {
    return null;
  }

  const hiddenCanonical = lead.querySelector('p[hidden] a[href]');
  if (hiddenCanonical) {
    const hiddenHref = hiddenCanonical.getAttribute('href');
    const hiddenUrl = resolveHttpRedirectUrl(hiddenHref);
    if (hiddenUrl) {
      return hiddenUrl;
    }
  }

  const anchors = lead.querySelectorAll('a[href]');
  for (const anchor of anchors) {
    const href = anchor.getAttribute('href');
    const isMailto = href && href.startsWith('mailto:');
    const isTel = href && href.startsWith('tel:');
    if (isMailto || isTel) {
      continue;
    }
    const resolvedUrl = resolveHttpRedirectUrl(href);
    if (resolvedUrl) {
      return resolvedUrl;
    }
  }

  return null;
}

export function getArticleExternalURL(article) {
  if (!article) {
    console.warn('No article given');
    return;
  }

  const URL = resolveRedirectUrlFromLeadAnchor(article);
  if (!URL) {
    console.warn('No redirect URL found for article', article);
  }

  return URL;
}

/**
 * Modify article links to point to external URLs based on tag name
 * @param {string} [extTagName='external'] - A tag that has been set on articles served externally
 */
export function changeHowExternalArticleOpens(extTagName = 'external') {
  const articles = document.querySelectorAll(
    `.has-blog-tag-${extTagName}`
  );

  console.debug(`Found ${articles.length} article(s) with tag "${extTagName}"`, articles );

  [ ...articles ].forEach( article => {
    const externalLinkUrl = getArticleExternalURL( article );

    if ( externalLinkUrl ) {
      const links = article.querySelectorAll(':is(h3, footer) a');

      // all links to the post should open external URL in new window
      [ ...links ].forEach( link => {
        console.debug(`Changed article link to "${externalLinkUrl}"`, link );

        link.href = externalLinkUrl;
        link.setAttribute('target', '_blank');
      });
    }
  });
}

/**
 * Redirect article to external URL if it has certain tag name
 * @param {string} [extTagName='external'] - A tag that has been set on articles served externally
 */
export function redirectExternalArticle(extTagName = 'external') {
  const params = new URLSearchParams( window.location.search );
  const isEditing = params.has('edit');
  const article = document.querySelector(`
    .has-blog-tag-${extTagName}
  `);

  if ( ! article ) return;

  const URL = getArticleExternalURL( article );

  if ( ! URL ) {
    console.debug('Cannot redirect to URL', URL );
  } else if ( isEditing ) {
    console.info(`Skipping redirect to "${URL}", because user is editing`);
  } else {
    console.debug(`Redirecting to "${URL}"`);
    window.location.href = URL;
  }
}
