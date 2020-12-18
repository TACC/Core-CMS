/**
 * Clone markup from an endpoint into a specific element
 * @param {HTMLElement} containerElement - The element in which to place the markup
 * @param {string} markupUrl - The URL at which to fetch the markup
 * @param {function} [callback] - A function to run after placing the markup
 * @todo Rewrite function to be a custom element
*/
export function fromURL(containerElement, markupUrl, callback) {
  if (markupUrl) {
    fetch(markupUrl).then((response) => {
      return response.text();
    }).then((data) => {
      containerElement.innerHTML = data;
    }, (err) => {
      containerElement.innerHTML = null;
      console.error(err);
    }).finally(() => {
      if (typeof callback === 'function') {
        callback();
      }
    });
  }
}
