/**
 * Update `href` attribute, of all e-mail links, based on data attributes
 * @param {HTMLElement} [scopeElement=document] - Element within which to search for links
 * @param {string} [fakeText=FAKE_TEXT] - False text manually added into address
 * @param {AttrNames} [attributes=ATTRIBUTE_NAMES] - The names of attributes with e-mail data
 */
 export default function updateEmailLinkHrefs(
  scopeElement = document,
  fakeText = FAKE_TEXT,
  attributes = ATTRIBUTE_NAMES
) {
  const attrs = Object.assign(attributes, ATTRIBUTE_NAMES);
  const selector = 'a[href*="' + fakeText + '"]';

  scopeElement.querySelectorAll(selector).forEach(linkEl => {
    _addData(linkEl, fakeText, attrs);

    const editHref = _editHref.bind(this, linkEl, fakeText, attrs);
    linkEl.addEventListener('click', editHref, {once: true});
  });
}

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
 * Whether to log debug info to console
 * @const {string}
 */
const SHOULD_DEBUG = window.DEBUG;

/**
 * Get the e-mail based on available data
 * @param {object} options
 * @param {string} [options.href]
 * @param {string} [options.fakeText] - False text manually added into address
 */
function _getEmail({href, fakeText} = {}) {
  const emailOld = href.replace('mailto:', '');
  const email = emailOld.replace(fakeText, '');

  if (SHOULD_DEBUG) console.debug({emailOld, email});

  return email;
}

/**
 * Get user and domain based on email
 * @param {string} email
 */
function _getEmailParts(email) {
  const parts = email.split('@');
  const user = parts[0];
  const domain = parts[1];

  if (SHOULD_DEBUG) console.debug({email, parts, user, domain});

  return {user, domain};
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

  if (SHOULD_DEBUG) console.debug({subject, body, query});

  return query;
}

/**
 * Edit `href` attribute, of one e-mail link, based on given data
 * @param {HTMLElement} element - The link element to update
 * @param {string} fakeText - False text manually added into address
 * @param {AttrNames} attributes - The names of attributes storing e-mail data
 */
function _editHref(element, fakeText, attributes) {
  const subject = element.getAttribute(attributes.subject);
  const body = element.getAttribute(attributes.body);

  const email = _getEmail({href: element.href, fakeText});
  const query = _createQuery({body, subject});

  // So link opens mail program with correct address
  element.href = 'mailto:' + email + query;
}

/**
 * Add data attributes, of one e-mail link, based on given data
 * (CSS can use these to hide fake e-mail and show reconstructed e-mail)
 * @param {HTMLElement} element - The link element to update
 * @param {string} fakeText - False text manually added into address
 * @param {AttrNames} attributes - The names of attributes storing e-mail data
 */
function _addData(element, fakeText, attributes) {
  const email = _getEmail({href: element.href, fakeText});
  const {user, domain} = _getEmailParts(email);

  // So CSS can replace link text with virtual address
  element.setAttribute(attributes.user, user);
  element.setAttribute(attributes.domain, domain);
}
