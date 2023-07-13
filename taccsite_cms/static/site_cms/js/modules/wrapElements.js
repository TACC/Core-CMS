/**
 * Create `<details>` around desired `<summary>` content and following siblings
 *
 * Move each content for `<summary>` into a `<summary>` of a `<details>`
 * which surrounds it and tags after it (but before next delimiter content)
 *
 * @param [string] startElementSelector - How to select which elements are the start of content to wrap
 * @param [string] endElementSelector - How to select which elements are the end of content to wrap
 * @param [string] wrapperTagName - The name of the tag to create
 * @param {object} [options]
 * @param {boolean} [options.mustWrapStarter=true] - Whether to wrap "startElement" also
 * @param {HTMLElement} [options.scopeElement=document] - The element within which to search for elements to wrap
 * @example
 * <script nonce="{{ CSP_NONCE }}" type="module">
 *   import wrapElements from '...';
 *   wrapElements('h3', 'hr', 'article', { wrapStarter: true });
 * </script>
 *
 * // BEFORE: A heading followed by sub-headings and <hr>'s
 * <h2>Heading</h2>
 * <h3>Sub-Heading A</h3>
 * <p>…</p>
 * <img />
 * <hr />
 * <h3>Sub-Heading B</h3>
 * <p>…</p>
 * <hr />
 *
 * // AFTER: A heading followed by articles (that wrap sub-headings) and <hr>'s
 * <h2>Heading</h2>
 * <article>
 *   <h3>Sub-Heading A</h3>
 *   <p>…</p>
 *   <img />
 * </article>
 * <hr />
 * <article>
 *   <h3>Sub-Heading B</h3>
 *   <p>…</p>
 * </article>
 * <hr />
 */
export default function wrapElements(
  startElementSelector,
  endElementSelector,
  wrapperTagName,
  options = {}
) {
  const opts = Object.assign({
    mustWrapStarter: true,
    scopeElement: document
  }, options );

  if ( ! opts.scopeElement ) {
    console.warn('The "scopeElement" options is not an element so "wrapElements" function is abandoned', opts.scopeElement );
    return;
  }

  const starters = opts.scopeElement.querySelectorAll( startElementSelector );
  const containerClassname = 'js-wrapElements-container';
  const wrapperClassname = 'js-wrapElements-wrapper';
  const starterClassname = 'js-wrapElements-starter';

  starters.forEach( starter => {
    starter.classList.add( starterClassname );

    const container = starter.parentNode;
          container.classList.add( containerClassname );
    const wrapper = document.createElement( wrapperTagName );
          wrapper.classList.add( wrapperClassname );
    const ender = _getNextSibling( starter, endElementSelector );
    const contents = _getNextSiblingsUntil( starter, endElementSelector );

    container.insertBefore( wrapper, ender );

    // Whether to wrap the starter element first
    // if ( opts.mustWrapStarter ) {
    //   wrapper.prepend( starter );
    // }

    wrapper.append( ...contents );
  });
}

/**
 * Get all siblings from one element to one that matches a given selector
 * (simple version of https://api.jquery.com/nextUntil)
 * @param {HTMLElement} startElement - The element from which to start looking
 * @param {HTMLElement} endElementSelector - The selector to match final element
 * @see https://gomakethings.com/how-to-get-all-sibling-elements-until-a-match-is-found-with-vanilla-javascript/
 */
function _getNextSiblingsUntil( startElement, endElementSelector ) {
  const siblings = [];

  let nextSibling = startElement.nextElementSibling;

  // Wrap all elements after start element, but before next end element
  while ( nextSibling ) {
    if ( nextSibling.matches( endElementSelector ) ) {
      break;
    }

    siblings.push( nextSibling );

    nextSibling = nextSibling.nextElementSibling;
  }

  siblings.unshift( startElement );

  return siblings;
}

/**
 * From given element, get the following element sibling matched by the selector
 * @param {HTMLElement} element - The element after which to search
 * @param {string} selector - The selector to match
 * @see https://gomakethings.com/finding-the-next-and-previous-sibling-elements-that-match-a-selector-with-vanilla-js/
 */
function _getNextSibling( element, selector ) {
  var sibling = element.nextElementSibling;

  if ( ! selector ) {
    return sibling;
  }

  while ( sibling ) {
    if ( sibling.matches( selector ) ) {
      return sibling;
    }
    sibling = sibling.nextElementSibling;
  }
};
