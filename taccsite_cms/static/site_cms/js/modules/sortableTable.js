/**
 * Client-side sort for CMS tables with class `is-sortable` on the table.
 *
 * Load with `sortableTable.css` (same folder under `site_cms/css/modules/`).
 * TODO: Consider TACC/Core-Components as a shared sortable-table component.
 *
 * Not using tristen/tablesort: focusable `<th>` only; no button-in-header (APG);
 * no `th.is-not-sortable` or link-text sort keys without duplicating this module.
 *
 * Editor markup:
 * - Table: `o-fixed-header-table is-sortable`
 * - Non-sortable column: `th.is-not-sortable` (e.g. Description)
 */

const SORT_TABLE_CLASS = 'is-sortable';
const NOT_SORTABLE_CLASS = 'is-not-sortable';
const SORT_BUTTON_CLASS = 'is-sortable__sort';

const DEFAULT_TABLE_SELECTOR = 'table.' + SORT_TABLE_CLASS;
const NOT_SORTABLE_SELECTOR = 'th.' + NOT_SORTABLE_CLASS;

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
 * @param {HTMLTableElement} table
 * @param {HTMLTableRowElement} headerRow
 */
function warnIfIrregularRows(table, headerRow) {
  const tbody = table.tBodies[0];
  if (!tbody) {
    return;
  }

  const expected = headerRow.cells.length;

  for (let i = 0; i < tbody.rows.length; i++) {
    const row = tbody.rows[i];
    if (row.cells.length < expected) {
      console.warn(
        `[sortableTable] Row ${i + 1} has ${row.cells.length} cells but the header has ${expected}. Fix table markup in the CMS before publishing.`,
        table
      );
      return;
    }
  }
}

/**
 * @param {HTMLTableElement} table
 * @param {number} columnIndex
 * @param {'ascending' | 'descending'} direction
 */
function sortTable(table, columnIndex, direction) {
  const tbody = table.tBodies[0];
  if (!tbody) {
    return;
  }

  const rows = [ ...tbody.rows ];
  const multiplier = direction === 'ascending' ? 1 : -1;
  const logContext = { table, warnedMissingCell: false };

  rows.sort((rowA, rowB) => {
    const a = getSortValue(rowA.cells[columnIndex], logContext);
    const b = getSortValue(rowB.cells[columnIndex], logContext);
    return multiplier * a.localeCompare(b, undefined, { sensitivity: 'base' });
  });

  rows.forEach((row) => tbody.appendChild(row));
}

/**
 * @param {HTMLTableCellElement} headerCell
 * @param {'ascending' | 'descending' | 'none'} ariaSort
 */
function setHeaderSortState(headerCell, ariaSort) {
  headerCell.setAttribute('aria-sort', ariaSort);
  const button = headerCell.querySelector('button');
  if (button) {
    button.setAttribute(
      'aria-label',
      ariaSort === 'none'
        ? headerCell.dataset.sortLabel
        : `${headerCell.dataset.sortLabel}, sorted ${ariaSort}`
    );
  }
}

/**
 * @param {HTMLTableElement} table
 * @param {string} notSortableSelector
 * @param {string} buttonClass
 */
function initSortableTable(table, notSortableSelector, buttonClass) {
  const headerRow = table.tHead?.rows[0];
  if (!headerRow) {
    return;
  }

  warnIfIrregularRows(table, headerRow);

  /** @type {HTMLTableCellElement[]} */
  const sortableHeaders = [];

  [ ...headerRow.cells ].forEach((cell, index) => {
    if (!(cell instanceof HTMLTableCellElement)) {
      return;
    }
    if (cell.matches(notSortableSelector)) {
      cell.classList.add(NOT_SORTABLE_CLASS);
      return;
    }

    const label = cell.textContent?.trim() ?? `Column ${index + 1}`;
    cell.dataset.sortLabel = label;
    cell.innerHTML = '';

    const button = document.createElement('button');
    button.type = 'button';
    button.className = buttonClass + ' ' + SORT_BUTTON_CLASS;
    button.textContent = label;
    cell.append(button);

    button.addEventListener('click', () => {
      const current = cell.getAttribute('aria-sort');
      const next =
        current === 'ascending' ? 'descending' : 'ascending';

      sortableHeaders.forEach((other) => {
        if (other !== cell) {
          setHeaderSortState(other, 'none');
        }
      });

      setHeaderSortState(cell, next);
      sortTable(table, index, next);
    });

    sortableHeaders.push(cell);
  });

  if (sortableHeaders.length) {
    const first = sortableHeaders[0];
    const firstIndex = [ ...headerRow.cells ].indexOf(first);
    setHeaderSortState(first, 'ascending');
    sortTable(table, firstIndex, 'ascending');
  }
}

/**
 * @param {object} [options]
 * @param {ParentNode} [options.scopeElement=document]
 * @param {string} [options.tableSelector=table.is-sortable]
 * @param {string} [options.notSortableSelector=th.is-not-sortable]
 * @param {string} [options.buttonClass=''] // e.g. 'c-button c-button--as-link'
 */
export default function sortableTable({
  scopeElement = document,
  tableSelector = DEFAULT_TABLE_SELECTOR,
  notSortableSelector = NOT_SORTABLE_SELECTOR,
  buttonClass = '',
} = {}) {
  scopeElement.querySelectorAll(tableSelector).forEach((table) => {
    if (table instanceof HTMLTableElement) {
      initSortableTable(table, notSortableSelector, buttonClass);
    }
  });
}
