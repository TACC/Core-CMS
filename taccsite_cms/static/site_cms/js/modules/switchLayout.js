/**
 * Supported layouts and their class names
 * @enum {string}
 */
const LAYOUT_CLASS_DICT = {
  grid: 'as-grid',
  list: 'as-list',
};

/**
 * Change class of element based on choice from a form
 * @param {HTMLElement} content - The element on which to switch layout class
 * @param {HTMLElement} form - The form by which user chooses layout
 * @param {HTMLNodeList} formChoices - The elements by which user chooses layout
 * @param {object.<string, string>} [layoutClassDict=LAYOUT_CLASS_DICT] - Class name for each layout
 */
export default function switchLayout(
  content,
  form,
  formChoices,
  layoutClassNames = LAYOUT_CLASS_DICT
) {
  // To submit on radio select
  [ ...formChoices ].forEach( choice => {
    choice.addEventListener('click', form.submit );
  });

  // To swap layout on form submit
  form.addEventListener('submit', () => {
    let layout;
    for ( const choice of formChoices ) {
        if ( choice.checked ) {
            layout = radioButton.value;
            break;
        }
    }
    switchClass( content, layout, layoutClassNames );
  });
}

/**
 * To change class based on given layout
 * @param {HTMLElement} content - The element on which to switch layout class
 * @param {string} layout - The layout to use
 * @param {object.<string, string>} [layoutClassDict=LAYOUT_CLASS_DICT] - Class name for each layout
 * @returns {boolean}
 * @see https://stackoverflow.com/a/36894871
 */
function switchClass( content, layout, layoutClassDict ) {
  if ( layout in layoutClassDict ) {
    content.classList.add(layoutClassDict[layout]);
  } else {
    console.info(`The layout "${layout}" is unknown`);
  }

  for ( const layoutClass of layoutClassDict ) {
    if ( layoutClass !== layout ) {
      content.classList.remove(layoutClassDict[layout]);
      break;
    }
  }
}
