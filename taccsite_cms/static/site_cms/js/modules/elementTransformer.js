/**
 * Transform elements (when CSS cannot)
 *
 * - Manipulates attributes within existing markup.
 * - Transformations are NOT dynamically updated after initial load.
 *
 * This is a back-up solution. Try using CSS to solve the problem first.
 * @module elementTransformer
 */

/** Resize first child element to match parent height (track state in markup) */
export class SizeContentToFit {



  // FAQ: Offers clarity of intent and consistency with state attr.
  // NOTE: Could faciliate programmatic transforms (like as a plugin option)
  /** A suggested selector to match the container */
  static containerSelector = '[data-transform="size-content-to-fit"]';



  /**
   * Initialize and resize
   * @param {HTMLElement} container - The direct parent of the content to resize
   */
  constructor (container) {
    /** The `HTMLElement` containing the content to resize */
    this.container = container;
    /** The `HTMLElement` to resize */
    this.content = container.querySelector(':scope > *');

    // GH-320: Test whether `this.content` was in the DOM at runtime
    // FAQ: Use `cloneNode` to NOT watch element reference that is updated later
    // console.log({
    //   container: this.container.cloneNode(true),
    //   content: this.content.cloneNode(true)
    // });

    this.resizeContent();
  }



  /** Mark transformation as in the given state */
  setState(state) {
    this.container.dataset.transformState = state;
  }

  /** Mark transformation as NOT in the given state */
  removeState(state) {
    // NOTE: Multiple states are not supported, so there is no use for `state`
    this.container.dataset.transformState = null;
  }

  /** Whether transformation is in the given state */
  isState(state) {
    return (this.container.dataset.transformState === state);
  }

  /** Whether to resize the content */
  shouldResizeContent() {
    if (this.container.getAttribute('hidden') !== null) {
      this.content.style.offsetHeight = '0';
      this.container.removeAttribute('hidden');
    }
  }


  /** Resize the content */
  resizeContent() {
    /* To prevent natural height of content from increasing container height */
    /* FAQ: Script will set wrong height if content is taller than is desired */
    if (this.container.getAttribute('hidden') !== null) {
      this.content.style.height = '0';
      this.container.removeAttribute('hidden');
    }

    /* To inform observers that this transformation is active */
    this.setState('resizing-content');

    /* To make container (and its content) the same height as a root element */
    /* FAQ: With tall content… container height = excessive content height */
    /* FAQ: With hidden content… container height = desired content height */
    this.container.style.height = '100%';
    this.content.style.height = this.container.offsetHeight + 'px';
    this.container.style.height = null;

    /* To clean up mess (only if it appears to be the mess of this script) */
    if (this.isState('resizing-content')) {
      this.removeState('resizing-content');
      if (this.container.getAttribute('style') === '') {
        this.container.removeAttribute('style');
      }
    }

    /* To inform observers that this module is done */
    this.setState('complete');
  }
}
