/**
 * Return markup from an endpoint
 * @param {string} markupURL - The URL from which to get the markup
 * @returns {Promise<string>} Promise that returns markup if resolved
 */
export function getFromURL(markupURL) {
  if (markupURL) {
    return fetch(markupURL).then(response => {
      const markup = response.text();
      return markup;
    }).catch(err => {
      console.error(err);
    });
  } else {
    return Promise.reject(new Error('Invalid `markupURL` provided'));
  }
}

/**
 * Insert markup from an endpoint into a specific element
 * @param {string} markupURL - The URL from which to get the markup
 * @param {HTMLElement} container - The element into which to place the markup
 * @returns {Promise<HTMLElement>} Promise that returns the container
 */
export function insertFromURL(markupURL, container) {
  if (markupURL) {
    return getFromURL(markupURL).then(markup => {
      container.innerHTML = markup;
      return container;
    });
  } else {
    return Promise.reject(new Error('Invalid `container` provided'));
  }
}
