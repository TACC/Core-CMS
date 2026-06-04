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
 */

const SORT_TABLE_CLASS = 'js-sortable';
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
 * @param {HTMLTableElement} table
 * @param {string} notSortableSelector
 * @param {string} buttonClass
 */
function prepSortableTable(table, notSortableSelector, buttonClass) {
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
  });

  if (!columns.length) {
    console.warn(
      '[sortableTable] No sortable columns after prep; skipping.',
      table
    );
    return;
  }

  const logContext = { table, warnedMissingCell: false };
  for (const row of tbody.rows) {
    for (const { key, columnIndex } of columns) {
      row.setAttribute(`data-${key}`, getSortValue(row.cells[columnIndex], logContext));
    }
  }

  const list = new window.List(table, {
    valueNames,
    listClass: LIST_CLASS,
  });

  list.on('sortComplete', () => syncAriaFromListButtons(columns));
  syncAriaFromListButtons(columns);
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
      prepSortableTable(table, notSortableSelector, buttonClass);
    }
  });
}
