/**
 * Client-side sort for CMS tables marked with `table.o-sortable-table`.
 *
 * Not using tristen/tablesort: it sorts focusable <th> (Enter/aria-sort) without a
 * button in the header (W3C APG); no `th.is-not-sortable` or link-text sort keys.
 * Matching our editor/CSS contract would duplicate this module.
 *
 * Editor markup:
 * - Table: `o-fixed-header-table o-sortable-table`
 * - Non-sortable column: `th.is-not-sortable` (e.g. Description)
 */

const DEFAULT_TABLE_SELECTOR = 'table.o-sortable-table';
const NOT_SORTABLE_SELECTOR = 'th.is-not-sortable';

/**
 * @param {HTMLTableCellElement} cell
 * @returns {string}
 */
function getSortValue(cell) {
  const link = cell.querySelector('a');
  const text = link ? link.textContent : cell.textContent;
  return (text ?? '').trim();
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

  rows.sort((rowA, rowB) => {
    const a = getSortValue(rowA.cells[columnIndex]);
    const b = getSortValue(rowB.cells[columnIndex]);
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
 */
function initSortableTable(table, notSortableSelector) {
  const headerRow = table.tHead?.rows[0];
  if (!headerRow) {
    return;
  }

  /** @type {HTMLTableCellElement[]} */
  const sortableHeaders = [];

  [ ...headerRow.cells ].forEach((cell, index) => {
    if (!(cell instanceof HTMLTableCellElement)) {
      return;
    }
    if (cell.matches(notSortableSelector)) {
      cell.classList.add('is-not-sortable');
      return;
    }

    const label = cell.textContent?.trim() ?? `Column ${index + 1}`;
    cell.dataset.sortLabel = label;
    cell.innerHTML = '';

    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'o-sortable-table__sort';
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
 * @param {string} [options.tableSelector=table.o-sortable-table]
 * @param {string} [options.notSortableSelector=th.is-not-sortable]
 */
export default function sortableTable({
  scopeElement = document,
  tableSelector = DEFAULT_TABLE_SELECTOR,
  notSortableSelector = NOT_SORTABLE_SELECTOR,
} = {}) {
  scopeElement.querySelectorAll(tableSelector).forEach((table) => {
    if (table instanceof HTMLTableElement) {
      initSortableTable(table, notSortableSelector);
    }
  });
}
