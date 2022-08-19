/**
 * Names of the URL search parameter and the input field
 * @typedef {Object} AttrNames
 * @property {string} [user] - Which attr. has user name
 * @property {string} [domain] - Which attr. has mail domain
 * @property {string} [subject] - Which attr. has mail subject
 * @property {string} [body] - Which attr. has mail body
 */

/**
 * The default names for attributes
 * @enum {string}
 */
const ATTRIBUTE_NAMES = {
  user: 'data-user',
  domain: 'data-domain',
  subject: 'data-subject',
  body: 'data-body',
};

/**
 * Update link href from `[data-email="…"]` to `href="mailto:…"`
 * @param {HTMLElement} element - The link element to update
 * @param {AttrNames} attributes - The names of attributes with e-mail data
 */
function _updateHref(element, attributes) {
  const user = element.getAttribute(attributes.user);
  const domain = element.getAttribute(attributes.domain);
  const subject = element.getAttribute(attributes.subject);
  const body = element.getAttribute(attributes.body);

  element.href = 'mailto:' + user + '@' + domain;
  if (subject || body) {
    element.href += '?';
  }
  if (subject) {
    element.href += 'subject=' + subject;
  }
  if (subject && body) {
    element.href += '&';
  }
  if (body) {
    element.href += 'body=' + body;
  }
}

/**
 * Update hyperlinks from `[data-email="…"]` to `href="mailto:…"`
 * @param {HTMLElement} [scopeElement=document] - Element within which to search for links
 * @param {AttrNames} attributes - The names of attributes with e-mail data
 * @return {boolean}
 */
export default function renderEmailAddresses(
  scopeElement = document,
  attributes
) {
  const selector = '[' + attributes.user + '][' + attributes.domain + ']';
  const attributesMerged = Object.assign(attributes, ATTRIBUTE_NAMES);

  scopeElement.querySelectorAll(selector).forEach(linkEl => {
    const updateHref = _updateHref.bind(this, linkEl, attributesMerged);

    linkEl.addEventListener('click', updateHref, {once: true});
  });
}
