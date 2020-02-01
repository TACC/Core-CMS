window.onload = function() {
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
               jQuery('.frontera-core-username').text(data['username']);
               jQuery('.frontera-core-dropdown').removeClass('d-none');
           },
           function(xhr) { console.error(xhr); }
  );
  
}
