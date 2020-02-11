window.onload = function() {

  // Load user authentication JSON from Portal, and perform dependent actions
  // - If user is authenticated:
  //     - Populate username (to show that user is logged in)
  //     - Show portal nav dropdown (it is pre-hidden via classname)
  // - If user is NOT authenticated:
  //     - Show portal login link (it is pre-hidden via classname)
  /* NOTE: This file is loaded by this codebase, and by an external codebase:
    - https://bitbucket.org/taccaci/frontera-tech-docs/src/429f05f23d95196f723c4f5fecd20823ceb73fe3/frontera_theme/base.html
    - https://gitlab.tacc.utexas.edu/wma-cms/frontera-cms/blob/188cd859a2fe3b37ecae7b6457e06be1b4acd6b2/taccsite_cms/templates/base.html#L67
  */
  /* WARNING: Code on this file will run on fronteraweb.tacc.utexas.edu/user-guide/, also. */
  /* SEE: ___link_coming___ */
  function loadJSON(path, success, error)
  {
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function()
      {
          if (xhr.readyState === XMLHttpRequest.DONE) {
              if (xhr.status === 200) {
                  if (success)
                      success(JSON.parse(xhr.responseText));
              } else {
                  console.log('error state')
                  jQuery('#frontera-login-link').removeClass('d-none');
              }
          }
      };
      xhr.open("GET", path, true);
      xhr.send();
  }
  loadJSON('/api/users/auth/',
           function(data) { console.log(data);
               jQuery('#frontera-core-username').text(data['username']);
               jQuery('#frontera-core-dropdown').removeClass('d-none');
           },
           function(xhr) { console.error(xhr); }
  );

}
