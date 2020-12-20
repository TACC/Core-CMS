/**
 * Populate custom element of givenname with content of a given HTML template
 * @param {String} name - Name of the custom element to register
 * @param {HTMLTemplateElement} template - An HTML template
 * @return {Element}
 */
export function fromTemplate(name, template) {
  console.log({template});

  window.customElements.define(name, class extends HTMLElement {
    constructor() {
      super();

      console.log({content: template.content});

      this.attachShadow({ mode: "open" });
      this.shadowRoot.appendChild(template.content);
    }
  });
}
