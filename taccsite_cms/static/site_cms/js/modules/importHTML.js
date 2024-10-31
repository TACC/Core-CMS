/**
 * Create element from HTML string
 * @param {String} - HTML representing a single element
 * @return {Element|null} - Created element or null if HTML is empty
 * @see https://stackoverflow.com/a/35385518
 */
export function htmlToElement(html) {
  const trimmedHtml = html ? html.trim() : '';

  // To never return a text node of whitespace
  if (!trimmedHtml) {
    return null;
  }

  var template = document.createElement('template');
  template.innerHTML = trimmedHtml;

  return template.content.firstChild;
}

/**
 * Create elements from HTML string
 * @param {String} - HTML representing any number of sibling elements
 * @return {NodeList}
 * @see https://stackoverflow.com/a/35385518
 */
export function htmlToElements(html) {
  var template = document.createElement('template');
  template.innerHTML = html;
  return template.content.childNodes;
}

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
 * Insert markup into a specific element from an endpoint
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
    return Promise.reject(new Error('No `markupURL` provided'));
  }
}

/**
 * Replace a specific element with markup from an endpoint
 * @param {string} markupURL - The URL from which to get the markup
 * @param {HTMLElement} placeholder - The element to replace with the markup
 * @returns {Promise<HTMLElement>} Promise that returns the new element
 */
export function replaceFromURL(markupURL, placeholder) {
  if (markupURL) {
    return getFromURL(markupURL).then(markup => {
      const newElement = htmlToElement(markup);

      if (newElement) {
        placeholder.replaceWith(newElement);
        return newElement;
      } else {
        return placeholder;
      }
    });
  } else {
    return Promise.reject(new Error('No `markupURL` provided'));
  }
}
