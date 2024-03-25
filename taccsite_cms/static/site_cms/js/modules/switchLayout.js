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
 * @param {HTMLNodeList} formChoices - The elements by which user chooses layout
 * @param {object.<string, string>} [layoutClassDict=LAYOUT_CLASS_DICT] - Class name for each layout
 */
export default function switchLayout(
  content,
  formChoices,
  layoutClassDict = LAYOUT_CLASS_DICT
) {
  [ ...formChoices ].forEach( choice => {
    choice.addEventListener('click', () => {
      const layout = getLayout( formChoices );

      switchClass( content, layout, layoutClassDict );
    });
  });
}

/**
 * To get the chosen layout
 * @param {HTMLNodeList} formChoices - The elements by which user chooses layout
 * @returns {string}
 * @see https://stackoverflow.com/a/36894871
 */
function getLayout(formChoices) {
    let layout;
    for ( const choice of formChoices ) {
        if ( choice.checked ) {
            layout = choice.value;
            break;
        }
    }
    return layout;
}

/**
 * To change class based on given layout
 * @param {HTMLElement} content - The element on which to switch layout class
 * @param {string} layout - The layout to use
 * @param {object.<string, string>} [layoutClassDict=LAYOUT_CLASS_DICT] - Class name for each layout
 * @see https://stackoverflow.com/a/36894871
 */
function switchClass( content, layout, layoutClassDict ) {
  let layoutClass;

  // Remove unselected
  for ( const layoutName in layoutClassDict ) {
    if ( layoutName !== layout ) {
      layoutClass = layoutClassDict[layoutName];
      content.classList.remove( layoutClass );
    }
  }

  // Add selected
  if ( layout in layoutClassDict ) {
    layoutClass = layoutClassDict[layout];
    content.classList.add( layoutClass );
  } else {
    console.info(`The layout "${layout}" is unknown`);
  }
}
