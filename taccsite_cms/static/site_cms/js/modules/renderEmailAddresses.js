/**
 * Convert data-attribute-name to dataset.propName
 * @param {string} attr
 * @returns {string}
 */
 function _dataAttrFromDatasetProp(attr) {
  const datasetPropName = attr.replace(/-[a-z]/g, match => match.toUpperCase());

  return datasetPropName;
}

/**
 * Update hyperlinks from `[data-email="…"]` to `href="mailto:…"`
 * @param {string} [hostAttrName='data-host'] - Which attribute has host
 * @param {string} [domainAttrName='data-domain'] - Which attribute has domain
 * @param {HTMLElement} [scopeElement=document] - Element within which to search for link
 * @return {boolean}
*/
export default function renderEmailAddresses({
  hostAttrName = 'data-host',
  domainAttrName = 'data-domain',
  scopeElement = document
} = {}) {
  const querySelector = '[' + hostAttrName + '][' + domainAttrName + ']';

  scopeElement.querySelector(querySelector).addEventListener('click', event => {
    event.preventDefault();

    const linkEl = event.target;
    const hostPropName = _dataAttrFromDatasetProp(hostAttrName);
    const domainPropName = _dataAttrFromDatasetProp(domainAttrName);

    linkEl.href = 'mailto:'
    + linkEl.dataset[hostPropName]
    + '@'
    + linkEl.dataset[domainPropName];
  });
}
