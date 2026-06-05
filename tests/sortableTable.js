/**
 * Client-side sort for CMS tables with class `js-sortable` (List.js 2.3.1).
 * IMPORTANT: Coupled with `sortableTable.css`. Requires global `List` from CDN.
 *
 * NOTE: Not using tristen/tablesort cuz it forgoes button in header cell (a11y)
 * SEE: https://github.com/javve/list.js
 * SEE: https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/
 *
 * Editor markup:
 * - Table: `o-fixed-header-table js-sortable`
 * - Non-sortable column: `th.not-sortable` (e.g. Description)
 *
 * Runtime-only (do not document for editors): tbody.list, button.sort, data-sort, row data-*.
 *
 * Optional filters (page markup, not editor table cells):
 * - Control: class `js-sortable-filter`, `aria-controls="<table id>"`
 * - Table: stable `id` (filter values must match sortable column text in rows)
 * - Result count: `output.js-sortable-total` in same `.js-sortable-filter-list`
 *   as filters, with `for` listing filter control ids and `aria-atomic="true"`
 */

const SORT_TABLE_CLASS = 'js-sortable';
const FILTER_CLASS = 'js-sortable-filter';
const FILTER_LIST_CLASS = 'js-sortable-filter-list';
const OUTPUT_CLASS = 'js-sortable-total';
const LIST_CLASS = 'list';
const SORT_BUTTON_CLASS = 'sort';

const DEFAULT_TABLE_SELECTOR = 'table.' + SORT_TABLE_CLASS;
const NOT_SORTABLE_SELECTOR = 'th.not-sortable';

let listJsMissingLogged = false;

/**
 * @param {number} columnIndex
 * @returns {string}
 */
function columnKey(columnIndex) {
  return `col-${columnIndex}`;
}

/**
 * @param {HTMLTableCellElement | undefined} cell
 * @param {{ table: HTMLTableElement, warnedMissingCell?: boolean }} [logContext]
 * @returns {string}
 */
function getSortValue(cell, logContext) {
  if (!cell) {
    if (logContext && !logContext.warnedMissingCell) {
      logContext.warnedMissingCell = true;
      console.warn(
        '[sortableTable] A row is missing a cell for the sorted column. Use the same number of columns on every row in the CMS table (watch colspan/rowspan).',
        logContext.table
      );
    }
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
function filterGroupRoot(tableId, scopeElement) {
  const selector =
    '.' + FILTER_CLASS + '[aria-controls="' + CSS.escape(tableId) + '"]';
  const anchor = scopeElement.querySelector(selector);
  if (!anchor) {
    return null;
  }
  return anchor.closest('.' + FILTER_LIST_CLASS) ?? scopeElement;
}

/**
 * @param {string} tableId
 * @param {ParentNode} scopeElement
 * @returns {HTMLOutputElement[]}
 */
function findFilterTotalElements(tableId, scopeElement) {
  const root = filterGroupRoot(tableId, scopeElement);
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
function formatResultCount(count) {
  return count === 1 ? '1 result' : `${count} results`;
}

/**
 * @param {string} tableId
 * @param {SortableTableList} list
 * @param {ParentNode} scopeElement
 */
function wireFilterTotal(tableId, list, scopeElement) {
  const totals = findFilterTotalElements(tableId, scopeElement);
  if (!totals.length) {
    return;
  }

  const sync = () => {
    const text = formatResultCount(list.matchingItems.length);
    for (const output of totals) {
      output.value = text;
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

  const selector =
    '.' + FILTER_CLASS + '[aria-controls="' + CSS.escape(tableId) + '"]';
  const filters = scopeElement.querySelectorAll(selector);
  if (!filters.length) {
    return;
  }

  const apply = () => {
    const terms = [ ...filters ]
      .map((el) => (el instanceof HTMLInputElement || el instanceof HTMLSelectElement
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

  for (const el of filters) {
    const eventName =
      el instanceof HTMLInputElement &&
      (el.type === 'search' || el.type === 'text')
        ? 'input'
        : 'change';
    el.addEventListener(eventName, apply);
  }
}

/**
 * @param {HTMLTableElement} table
 * @param {ParentNode} scopeElement
 * @param {string} notSortableSelector
 * @param {string} buttonClass
 */
function prepSortableTable(table, scopeElement, notSortableSelector, buttonClass) {
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

  tbody.classList.add(LIST_CLASS);

  /** @type {SortableColumn[]} */
  const columns = [];
  /** @type {Array<{ data: string[] }>} */
  const valueNames = [];
  const logContext = { table, warnedMissingCell: false };

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

    const key = columnKey(columnIndex);
    cell.dataset.sortLabel = label;
    cell.innerHTML = '';

    const button = document.createElement('button');
    button.type = 'button';
    button.className = [ buttonClass, SORT_BUTTON_CLASS ].filter(Boolean).join(' ');
    button.textContent = label;
    button.setAttribute('data-sort', key);
    cell.append(button);

    valueNames.push({ data: [ key ] });
    columns.push({ th: cell, button, key, columnIndex });

    for (const row of tbody.rows) {
      row.setAttribute(`data-${key}`, getSortValue(row.cells[columnIndex], logContext));
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
    listClass: LIST_CLASS,
  });

  list.on('sortComplete', () => syncAriaFromListButtons(columns));
  syncAriaFromListButtons(columns);
  if (table.id) {
    wireFilters(table, list, scopeElement);
    wireFilterTotal(table.id, list, scopeElement);
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
