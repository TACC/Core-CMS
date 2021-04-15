/**
 * Return data from an endpoint
 * @param {string} dataURL - The URL from which to get the data
 * @param {('html'|'json'|'text')} dataType - The type of data to retrieve
 * @returns {Promise<string>} Promise that returns markup if resolved
 */
export function getFromURL(dataURL, dataType) {
  const isValidURL = (dataURL && typeof dataURL === 'string');

  if (isValidURL) {
    return fetch(dataURL).then(response => {
      let data;

      switch (dataType) {
        case 'json':
          data = response.json();
          break;
        case 'html':
        case 'text':
        default:
          data = response.text();
          break;
      }

      return data;
    }).catch(err => {
      console.error(err);
    });
  } else {
    return Promise.reject(new Error('Invalid URL provided'));
  }
}
