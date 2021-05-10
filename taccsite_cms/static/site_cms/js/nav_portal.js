/* WARNING: This code is deprecated. It must be removed AFTER GH-195/FP-1015. */

/**
 * Load JSON from an endpoint, and perform success-dependent actions
 * @param {string} path - The path to an API endpoint
 * @param {function} onSuccess - Callback for data retrieval success
 * @param {function} onError - Callback for data retrieval success
 */
function getData(path, onSuccess, onError) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        if (typeof onSuccess === 'function') {
          onSuccess(JSON.parse(xhr.responseText));
        }
      } else {
        // NOTE: The original code did not ever log an error, thus `undefined`
        onError(xhr, undefined);
      }
    }
  };
  xhr.open("GET", path, true);
  xhr.send();
}

(function () {
  /*
   * Show (and populate) correct Portal navigation menu
   * - If user is authenticated:
   *     - Populate username (to show that user is logged in)
   *     - Show portal nav dropdown (it is pre-hidden via classname)
   * - If user is NOT authenticated:
   *     - Show portal login link (it is pre-hidden via classname)
   */
  getData('/api/users/auth/',
    function populateData(data) {
      console.info('portal user data', data);

      document.getElementById('portal-username').textContent = data.username;
      // FAQ: Show the auth'd menu
      document.getElementById('auth-menu').classList.remove('d-none');
    },
    function outputRequest(xhr, isFatal) {
      if (isFatal) console.error(xhr);

      // FAQ: Show the un-auth'd menu
      document.getElementById('unauth-menu').classList.remove('d-none');
    }
  );
})();
