/**
 * Convert Simple, Plain Tables into Sortable Tables
 * IMPORTANT: Requires global `List` from CDN.
 * API:
 *     - ../css/modules/sortableTable.css
 *     - ../js/modules/sortableTable.js
 *     - ../js/modules/sortableTable.html
 * SEE: https://github.com/javve/list.js
 * SEE: https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/
 */

const SORT_TABLE_CLASS = 'js-sortable';
const FILTER_CLASS = 'js-sortable-filter';
const FILTER_LIST_CLASS = 'js-sortable-filter-list';
const OUTPUT_CLASS = 'js-sortable-total';
const THEIR_LIST_CLASS = 'list';
const THEIR_BUTTON_CLASS = 'sort';

const DEFAULT_TABLE_SELECTOR = 'table.' + SORT_TABLE_CLASS;
const NOT_SORTABLE_SELECTOR = 'th.not-sortable';
const FILTERS_DATA_ATTR = 'data-sortable-filters';

/**
 * Filter chrome: clone <template> nodes from includes/sortable_table_filter_templates.html.
 * Captions, <option> text, and JSON placeholders use textContent / properties only.
 */
const FILTER_TEMPLATE_ID = 'sortable-table-filters';
const FILTER_SEARCH_LABEL_SELECTOR = 'label:has(input[type="search"])';
const FILTER_SELECT_LABEL_SELECTOR = 'label:has(select)';

let listJsMissingLogged = false;

/**
 * @typedef {FilterSpecForSearch | FilterSpecForSelect} FilterSpec
 * @typedef {{ type: 'search', placeholder?: string }} FilterSpecForSearch
 * @typedef {{ type: 'select', column: number, label?: string }} FilterSpecForSelect
 */

/**
 * @param {string} tableId
 * @param {ParentNode} scopeElement
 * @returns {NodeListOf<Element>}
 */
function findFilterControls(tableId, scopeElement) {
  return scopeElement.querySelectorAll(
    '.' + FILTER_CLASS + '[aria-controls="' + CSS.escape(tableId) + '"]'
  );
}

/**
 * @param {HTMLInputElement | HTMLSelectElement} control
 * @param {string} tableId
 */
function registerFilterControl(control, tableId) {
  control.classList.add(FILTER_CLASS);
  control.setAttribute('aria-controls', tableId);
}

/**
 * @param {HTMLTableElement} table
 * @returns {FilterSpec[] | null}
 */
function parseFilterSpecs(table) {
  const json = table.getAttribute(FILTERS_DATA_ATTR);
  if (!json) {
    return null;
  }
  try {
    const specs = JSON.parse(json);
    if (!Array.isArray(specs) || !specs.length) {
      return null;
    }
    return specs;
  } catch {
    console.warn(
      '[sortableTable] Invalid JSON in data-sortable-filters.',
      table
    );
    return null;
  }
}

/**
 * Trimmed text from the header cell at `columnIndex`, or a generic column name.
 *
 * @param {HTMLTableElement} table
 * @param {number} columnIndex
 * @returns {string}
 */
function getHeaderCellTextForColumn(table, columnIndex) {
  const textFallback = `Column ${columnIndex + 1}`;
  const cell = table.tHead?.rows[0]?.cells[columnIndex];
  const textTrimmed = cell?.textContent?.trim() ?? '';
  const text = textTrimmed || textFallback;

  return text;
}

/**
 * Puts `<option>` text in A–Z order (browser locale, case-insensitive).
 *
 * @param {string[]} optionTexts
 */
function sortSelectOptions(optionTexts) {
  optionTexts.sort((a, b) =>
    a.localeCompare(b, undefined, { sensitivity: 'base' })
  );
}

/**
 * @param {HTMLTableElement} table
 * @param {number} columnIndex
 * @returns {string[]}
 */
function collectSelectOptions(table, columnIndex) {
  const tbody = table.tBodies[0];
  if (!tbody) {
    return [];
  }
  const seen = new Set();
  /** @type {string[]} */
  const options = [];

  for (const row of tbody.rows) {
    const cell = row.cells[columnIndex];
    warnIfRowCellMissing(table, cell);

    const optionsFromCellText = getCellText(cell)
      .split(',')
      .map((piece) => piece.trim())
      .filter(Boolean);

    for (const optionText of optionsFromCellText) {
      if (seen.has(optionText)) {
        continue;
      }
      seen.add(optionText);
      options.push(optionText);
    }
  }

  sortSelectOptions(options);
  return options;
}

/**
 * @param {string} tableId
 * @param {string} key
 * @returns {string}
 */
function getFilterControlId(tableId, key) {
  return `${tableId}-filter-${key}`;
}

/**
 * @param {string} templateId
 * @returns {DocumentFragment}
 */
function clonePageTemplate(templateId) {
  const template = document.getElementById(templateId);

  if (!(template instanceof HTMLTemplateElement)) {
    throw new Error(
      '[sortableTable] Missing <template id="' +
        templateId +
        '">. Include includes/sortable_table_filter_templates.html once on the page.'
    );
  }

  return template.content.cloneNode(true);
}

/**
 * @param {HTMLLabelElement} searchLabel
 * @param {string} tableId
 * @param {FilterSpecForSearch} spec
 * @returns {string} control id
 */
function wireSearchFilterLabel(searchLabel, tableId, spec) {
  const input = searchLabel.querySelector('input[type="search"]');
  const controlId = getFilterControlId(tableId, 'search');

  searchLabel.htmlFor = controlId;
  input.id = controlId;
  if (spec.placeholder) {
    input.placeholder = spec.placeholder;
  }
  registerFilterControl(input, tableId);

  return controlId;
}

/**
 * @param {HTMLLabelElement} label
 * @param {HTMLTableElement} table
 * @param {FilterSpecForSelect} spec
 * @returns {string} control id
 */
function wireSelectFilterLabel(label, table, spec) {
  const caption = label.querySelector('.sortable-filter__label');
  const select = label.querySelector('select.sortable-filter__input');
  const controlId = getFilterControlId(table.id, `col-${spec.column}`);

  label.htmlFor = controlId;
  caption.textContent =
    spec.label ?? getHeaderCellTextForColumn(table, spec.column);
  select.id = controlId;
  registerFilterControl(select, table.id);

  for (const optionText of collectSelectOptions(table, spec.column)) {
    const option = document.createElement('option');
    option.textContent = optionText;
    select.append(option);
  }

  return controlId;
}

/**
 * @param {HTMLTableElement} table
 * @param {FilterSpec[]} specs
 * @returns {HTMLFieldSetElement}
 */
function buildFilterFieldset(table, specs) {
  const fragment = clonePageTemplate(FILTER_TEMPLATE_ID);
  const fieldset = /** @type {HTMLFieldSetElement} */ (
    fragment.querySelector('fieldset')
  );

  const searchSpec = specs.find((spec) => spec.type === 'search');
  const selectSpecs = specs.filter((spec) => spec.type === 'select');

  const searchField = fieldset.querySelector(FILTER_SEARCH_LABEL_SELECTOR);
  const selectField = fieldset.querySelector(FILTER_SELECT_LABEL_SELECTOR);
  const filterControlIds = [];

  /* buildSearchField */
  if (searchSpec) {
    filterControlIds.push(
      wireSearchFilterLabel(searchField, table.id, searchSpec)
    );
  } else {
    searchField.remove();
  }

  /* buildSelectField */
  for (const spec of selectSpecs) {
    const newSelectField = selectField.cloneNode(true);
    filterControlIds.push(
      wireSelectFilterLabel(newSelectField, table, spec)
    );
    fieldset.append(newSelectField);
  }
  selectField.remove();

  /* buildOutputField */
  if (searchSpec) {
    const output = fieldset.querySelector('output.' + OUTPUT_CLASS);
    output.setAttribute('for', filterControlIds.join(' '));
  }

  return fieldset;
}

/**
 * @param {HTMLTableElement} table
 */
function buildFilters(table) {
  const specs = parseFilterSpecs(table);
  if (!specs) {
    return;
  }
  if (!table.id) {
    console.warn(
      '[sortableTable] data-sortable-filters requires a table id; skipping filter UI.',
      table
    );
    return;
  }

  const fieldset = buildFilterFieldset(table, specs);

  table.parentNode?.insertBefore(fieldset, table);
}

/**
 * @param {HTMLTableElement} table
 * @param {HTMLTableCellElement | undefined} cell
 */
function warnIfRowCellMissing(table, cell) {
  if (!cell) {
    console.warn(
      '[sortableTable] A row is missing a cell for the sorted column. Use the same number of columns on every row in the CMS table (watch colspan/rowspan).',
      table
    );
  }
}

/**
 * Text List.js uses for sort, search, and filter options (link text when present).
 *
 * @param {HTMLTableCellElement | undefined} cell
 * @returns {string}
 */
function getCellText(cell) {
  if (!cell) {
    return '';
  }
  const link = cell.querySelector('a');
  const text = link ? link.textContent : cell.textContent;
  return (text ?? '').trim();
}

/**
 * @param {HTMLTableCellElement} th
 * @param {'ascending' | 'descending' | 'none'} ariaSort
 */
function setHeaderSortState(th, ariaSort) {
  th.setAttribute('aria-sort', ariaSort);
  const button = th.querySelector('button');
  if (!button) {
    return;
  }
  const label = th.dataset.sortLabel ?? '';
  button.setAttribute(
    'aria-label',
    ariaSort === 'none' ? label : `${label}, sorted ${ariaSort}`
  );
}

/**
 * @typedef {{ th: HTMLTableCellElement, button: HTMLButtonElement, key: string, columnIndex: number }} SortableColumn
 */

/**
 * List.js instance after sortable prep (subset used for client-side filter)
 * @typedef {object} SortableTableList
 * @property {(query?: string) => void} search
 * @property {object[]} matchingItems
 * @property {(event: string, callback: () => void) => void} on
 */

/**
 * @param {SortableColumn[]} columns
 */
function syncAriaFromListButtons(columns) {
  for (const { th, button } of columns) {
    let ariaSort = 'none';
    if (button.classList.contains('asc')) {
      ariaSort = 'ascending';
    } else if (button.classList.contains('desc')) {
      ariaSort = 'descending';
    }
    setHeaderSortState(th, ariaSort);
  }
}

/**
 * @param {string} tableId
 * @param {ParentNode} scopeElement
 * @returns {ParentNode | null}
 */
function findFilterGroupRoot(tableId, scopeElement) {
  const filters = findFilterControls(tableId, scopeElement);
  if (!filters.length) {
    return null;
  }
  return filters[0].closest('.' + FILTER_LIST_CLASS) ?? scopeElement;
}

/**
 * @param {string} tableId
 * @param {ParentNode} scopeElement
 * @returns {HTMLOutputElement[]}
 */
function findFilterCountElements(tableId, scopeElement) {
  const root = findFilterGroupRoot(tableId, scopeElement);
  if (!root) {
    return [];
  }
  return [ ...root.querySelectorAll('output.' + OUTPUT_CLASS) ].filter(
    (el) => el instanceof HTMLOutputElement
  );
}

/**
 * @param {number} count
 * @returns {string}
 */
function formatCount(count) {
  return (count === 1) ? '1 result' : `${count} results`;
}

/**
 * @param {string} tableId
 * @param {SortableTableList} list
 * @param {ParentNode} scopeElement
 */
function wireFilterCount(tableId, list, scopeElement) {
  const countElements = findFilterCountElements(tableId, scopeElement);
  if (!countElements.length) {
    return;
  }

  const sync = () => {
    const text = formatCount(list.matchingItems.length);
    for (const el of countElements) {
      el.value = text;
    }
  };

  list.on('searchComplete', sync);
  sync();
}

/**
 * @param {HTMLTableElement} table
 * @param {SortableTableList} list
 * @param {ParentNode} scopeElement
 */
function wireFilters(table, list, scopeElement) {
  const tableId = table.id;
  if (!tableId) {
    return;
  }

  const filterControls = findFilterControls(tableId, scopeElement);
  if (!filterControls.length) {
    return;
  }

  const applyFilters = () => {
    const terms = [ ...filterControls ].map(el =>
        (el instanceof HTMLInputElement || el instanceof HTMLSelectElement
          ? el.value
          : ''
      ).trim())
      .filter(Boolean);
    if (terms.length) {
      list.search(terms.join(' '));
    } else {
      list.search();
    }
  };

  for (const el of filterControls) {
    let eventName = 'change';
    if (el instanceof HTMLInputElement) {
      eventName =
        (el.type === 'search' || el.type === 'text' || el.type === '')
          ? 'input'
          : 'change';
    }
    el.addEventListener(eventName, applyFilters);
  }
}

/**
 * @param {HTMLTableElement} table
 * @param {ParentNode} scopeElement
 * @param {string} notSortableSelector
 * @param {string} buttonClass
 */
function prepSortableTable(table, scopeElement, notSortableSelector, buttonClass) {
  buildFilters(table);

  const headerRow = table.tHead?.rows[0];
  if (!headerRow) {
    console.warn(
      '[sortableTable] Table has no thead; skipping sortable enhancement.',
      table
    );
    return;
  }

  const tbody = table.tBodies[0];
  if (!tbody) {
    console.warn('[sortableTable] Table has no tbody; skipping.', table);
    return;
  }

  tbody.classList.add(THEIR_LIST_CLASS);

  /** @type {SortableColumn[]} */
  const columns = [];
  /** @type {Array<{ data: string[] }>} */
  const valueNames = [];
  [ ...headerRow.cells ].forEach((cell, columnIndex) => {
    if (!(cell instanceof HTMLTableCellElement)) {
      return;
    }
    if (cell.matches(notSortableSelector)) {
      return;
    }

    const label = (cell.textContent ?? '').trim();
    if (!label) {
      return;
    }

    const key = `col-${columnIndex}`;
    cell.dataset.sortLabel = label;

    const button = document.createElement('button');
    button.type = 'button';
    button.className = [ buttonClass, THEIR_BUTTON_CLASS ].filter(Boolean).join(' ');
    button.setAttribute('data-sort', key);
    while (cell.firstChild) {
      button.append(cell.firstChild);
    }
    cell.append(button);

    valueNames.push({ data: [ key ] });
    columns.push({ th: cell, button, key, columnIndex });

    for (const row of tbody.rows) {
      const rowCell = row.cells[columnIndex];
      warnIfRowCellMissing(table, rowCell);
      row.setAttribute(`data-${key}`, getCellText(rowCell));
    }
  });

  if (!columns.length) {
    console.warn(
      '[sortableTable] No sortable columns after prep; skipping.',
      table
    );
    return;
  }

  const list = new window.List(table, {
    valueNames,
    listClass: THEIR_LIST_CLASS,
  });

  list.on('sortComplete', () => syncAriaFromListButtons(columns));
  syncAriaFromListButtons(columns);
  if (table.id) {
    wireFilters(table, list, scopeElement);
    wireFilterCount(table.id, list, scopeElement);
  }
}

/**
 * @param {object} [options]
 * @param {ParentNode} [options.scopeElement=document]
 * @param {string} [options.tableSelector=table.js-sortable]
 * @param {string} [options.notSortableSelector=th.not-sortable]
 * @param {string} [options.buttonClass=''] // e.g. 'c-button c-button--as-link'
 */
export default function sortableTable({
  scopeElement = document,
  tableSelector = DEFAULT_TABLE_SELECTOR,
  notSortableSelector = NOT_SORTABLE_SELECTOR,
  buttonClass = '',
} = {}) {
  if (typeof window.List !== 'function') {
    if (!listJsMissingLogged) {
      listJsMissingLogged = true;
      console.error(
        '[sortableTable] List.js is not loaded; sortable tables will not be enhanced.'
      );
    }
    return;
  }

  scopeElement.querySelectorAll(tableSelector).forEach((table) => {
    if (table instanceof HTMLTableElement) {
      prepSortableTable(table, scopeElement, notSortableSelector, buttonClass);
    }
  });
}
