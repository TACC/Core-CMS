/**
 * Get URL of external web article of which internal news article represents
 * @param {HTMLElement} article - The article within which to find external URL
 * @return {string|null} - The URL of the external article
 */
export function getArticleExternalURL(article) {
  if (!article) {
    console.warn('No article found', article);
    return;
  }

  // The admin of news promises leads/abstracts will only have 1 external link
  const contentLink = article.querySelector('.blog-lead a[href^="http"]');
  const isExternalLink = contentLink.hostname !== window.location.hostname;
  const URL = isExternalLink ? contentLink.href : null;

  return URL;
}

/**
 * Modify article links to point to external URLs based on tag name
 * @param {string} [extTagName='external'] - A tag that has been set on articles to select
 */
export function changeHowExternalArticleOpens(extTagName = 'external') {
  const articles = document.querySelectorAll(
    `.blog-list article.has-blog-tag-${extTagName}`
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
