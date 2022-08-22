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
 * The default value for false text manually added into address
 * @const {string}
 */
const FAKE_TEXT = '__REMOVE_THIS__';

/**
 * Get the e-mail based on available data
 * @param {string} options
 * @param {string} [options.href]
 * @param {string} [options.user]
 * @param {string} [options.domain]
 * @param {string} [options.fakeText] - False text manually added into address
 */
function _getEmail({href, fakeText, user, domain} = {}) {
  const emailOld = href.replace('mailto:', '');
  const emailFix = emailOld.replace(fakeText, '');
  const emailNew = (user && domain) ? user + '@' + domain : undefined;
  const email = emailNew || emailFix || emailOld;

  // console.debug({emailOld, emailFix, emailNew, email});

  return email;
}

/**
 * Create query string based on available data
 * @param {string} options
 * @param {string} [options.subject]
 * @param {string} [options.body]
 */
function _createQuery({subject, body} = {}) {
  let query = '';

  if (subject || body) {
    query += '?';
  }
  if (subject) {
    query += 'subject=' + subject;
  }
  if (subject && body) {
    query += '&';
  }
  if (body) {
    query += 'body=' + body;
  }

  return query;
}

/**
 * Update `href` attribute, of one e-mail link, based on data attributes
 * @param {HTMLElement} element - The link element to update
 * @param {AttrNames} [attributes] - The names of attributes storing e-mail data
 * @param {string} [fakeText] - False text manually added into address
 */
function _updateHref(element, attributes, fakeText) {
  const user = element.getAttribute(attributes.user);
  const domain = element.getAttribute(attributes.domain);
  const subject = element.getAttribute(attributes.subject);
  const body = element.getAttribute(attributes.body);

  const email = _getEmail({href: element.href, user, domain, fakeText});
  const query = _createQuery({body, subject});

  element.href = 'mailto:' + email + query;
}

/**
 * Update `href` attribute, of all e-mail links, based on data attributes
 * @param {HTMLElement} [scopeElement=document] - Element within which to search for links
 * @param {AttrNames} [attributes] - The names of attributes with e-mail data
 * @param {string} [fakeText] - False text manually added into address
 */
export default function updateEmailLinkHrefs(
  scopeElement = document,
  attributes = ATTRIBUTE_NAMES,
  fakeText = FAKE_TEXT
) {
  const attrs = Object.assign(attributes, ATTRIBUTE_NAMES);
  const selector = [
    // For fake text, only search <a>, cuz <link> (irrelevant) supports `href`
    'a[href*="' + fakeText + '"]',
    // For attributes, search any element, so custom elements are supported
    '[' + attrs.body + ']',
    '[' + attrs.subject + ']',
    '[' + attrs.user + '][' + attrs.domain + ']',
  ].join(', ');

  scopeElement.querySelectorAll(selector).forEach(linkEl => {
    const updateHref = _updateHref.bind(this, linkEl, attrs, fakeText);

    linkEl.addEventListener('click', updateHref, {once: true});
  });
}
