/**
 * Set value of input field in given context from search parameter
 *
 * NOTE: Multiple fields of the same name will be updated, but it is recommended to provide a scope with only one matching field.
 *
 * @param {Element|ShadowRoot} context - The element or shadow DOM that has the field
 * @param {string} name - Name of the search parameter and input field
 * @param {string} [fieldName] - Name of the field (if different from search parameter)
 */
export function update(context, name, fieldName) {
  const urlSearchParams = new URLSearchParams(window.location.href);
  const query = urlSearchParams.get(name);
  const fields = context.querySelectorAll(`[name="${name || fieldName}"]`);

  // Support multiple fields (though there should only be one)
  [...fields].forEach(field => {
    field.value = query;
  });
}
