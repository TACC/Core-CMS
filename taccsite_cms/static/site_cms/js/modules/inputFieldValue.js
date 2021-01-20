/**
 * Names of the URL search parameter and the input field
 * @typedef {Object} Names
 * @property {string} parameter - Name (i.e. key) of the URL search parameter
 * @property {string} field - Name of the input field
 */

/**
 * Set value of input field in given context from URL search parameter
 *
 * NOTE: Multiple fields of the same name will be updated, but it is recommended to provide a scope with only one matching field.
 *
 * @param {Element|ShadowRoot} context - The element or shadow DOM that has the field
 * @param {string|Names} name - Name(s) of the search parameter and input field
 */
export function update(context, name) {
  const fieldName = (typeof name === 'string') ? name : name.field;
  const parameterName = (typeof name === 'string') ? name : name.parameter;

  const urlSearchParams = new URLSearchParams(window.location.href);
  const query = urlSearchParams.get(parameterName);
  const fields = context.querySelectorAll(`[name="${fieldName}"]`);

  // Support multiple fields (though there should only be one)
  [...fields].forEach(field => {
    field.value = query;
  });
}

/**
 * On event of given type, perform `update`
 * @param {Element|ShadowRoot} context - The element or shadow DOM that has the field
 * @param {string|Names} name - Name(s) of the search parameter and input field
 * @param {string} eventType - The type of event on which to update
 */
export function updateOnEvent(context, name, eventType) {
  window.addEventListener(eventType, e => {
    update(context, name);
  });
}
