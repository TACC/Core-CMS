/**
 * Names of the attributes storing e-mail data
 * @typedef {Object} AttrNames
 * @property {string} [user] - Which attribute has user name
 * @property {string} [domain] - Which attribute has e-mail domain
 * @property {string} [subject] - Which attribute has e-mail subject
 * @property {string} [body] - Which attribute has e-mail body
 */

/**
 * The default values for {AttrNames}
 * @enum {string}
 */
const ATTRIBUTE_NAMES = {
  user: 'data-user',
  domain: 'data-domain',
  subject: 'data-subject',
  body: 'data-body',
};

/**
 * Update `href` attribute, of one e-mail link, based on data attributes
 * @param {HTMLElement} element - The link element to update
 * @param {AttrNames} attributes - The names of attributes storing e-mail data
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
 * Update `href` attribute, of all e-mail links, based on data attributes
 * @param {HTMLElement} [scopeElement=document] - Element within which to search for links
 * @param {AttrNames} attributes - The names of attributes with e-mail data
 * @return {boolean}
 */
export default function updateEmailLinkHrefs(
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
