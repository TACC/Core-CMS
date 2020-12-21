/**
 * Create an HTML Template element from a given HTML element string
 * @param {string} name - Name of custom element to register
 * @param {string} html - HTML for shadow DOM of custom element
 * @return {Element}
 */
export function fromHTMLString(name, html) {
  let template = document.createElement('template');

  // Never return a text node of whitespace
  html = html.trim();

  template.innerHTML = html;
  template = document.head.appendChild(template);

  return fromTemplate(name, template);
}

/**
 * Populate custom element of givenname with content of a given HTML template
 * @param {string} name - Name of custom element to register
 * @param {HTMLTemplateElement} template - HTML for shadow DOM of custom element
 * @return {Element}
 */
export function fromTemplate(name, template) {

  console.log({template});

  window.customElements.define(name, class extends HTMLElement {
    constructor() {
      super();

      console.log({content: template.content});

      this.attachShadow({ mode: "open" });
      this.shadowRoot.appendChild(template.content.cloneNode(true));
    }
  });
}
