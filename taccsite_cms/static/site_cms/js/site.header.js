/**
 * Header-relevant scripts that must only run after header imports are complete
 * (and cannot be placed after relevant markup without requiring duplication)
 * @module
 */
// FAQ: Use of jQuery should remain limited to directly hooking into Bootstrap



const ELEMENT_NAV_PORTAL = document.querySelector('.s-header .s-portal-nav');
const ELEMENT_NAV_CMS = document.querySelector('.s-header .s-cms-nav');



// To prevent Portal menu from closing if user clicks on it
// NOTE: Wes tested this in different locations with unsuccessful results:
//      - within portal nav markup, did not work across all sites
//      - after portal nav container, needed duplicate across all sites
$(ELEMENT_NAV_PORTAL).on('click', '.dropdown.show', (showEvent) => {
  showEvent.stopPropagation();
});



// FAQ: This allows menu style differences based on child dropdown state
/**
 * To add classname, for CSS, to menu, when a child dropdown is open
 * @param {HTMLElement} menu - The parent menu
 */
function updateMenuClassname(menu) {
  const openMenuClassname = 'js-has-open-menu';
  const openMenus = menu.querySelectorAll('.dropdown.show');
  const hasOpenMenus = (openMenus && openMenus.length > 0);

  if (hasOpenMenus)
    menu.classList.add(openMenuClassname);
  else
    menu.classList.remove(openMenuClassname);
}

$(ELEMENT_NAV_CMS).on('hidden.bs.dropdown shown.bs.dropdown', () => {
  updateMenuClassname(ELEMENT_NAV_CMS);
});
