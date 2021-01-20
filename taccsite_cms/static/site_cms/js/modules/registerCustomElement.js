/**
 * Create an HTML Template element from a given HTML element string
 * @param {string} html - HTML for shadow DOM of custom element
 * @param {string} name - Name of custom element to register
 */
export function fromHTMLString(html, name) {
  let template = document.createElement('template');

  // Never return a text node of whitespace
  html = html.trim();

  template.innerHTML = html;
  template = document.head.appendChild(template);

  return fromTemplate(template, name);
}

/**
 * Populate custom element of given name with content of a given HTML template
 * @param {HTMLTemplateElement} template - HTML for shadow DOM of custom element
 * @param {string} name - Name of custom element to register
 */
export function fromTemplate(template, name) {
  window.customElements.define(name, class extends HTMLElement {
    constructor() {
      super();

      this.attachShadow({ mode: "open" });
      this.shadowRoot.appendChild(template.content.cloneNode(true));
    }
  });
}
