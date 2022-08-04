/** A controller to hide siblings of elment targeted by URL hash */
export default class TargetSiblingHider {
  #CLASSNAME = {
    hidden: 'js-hideUntargeted-hidden',
    showAll: 'js-hideUntargeted-show-all',
  };

  #opts;

  /**
   * Create a hide/show toggler
   * @param {object} [options]
   * @param {boolean} [options.mustCreateShowAllLink=true] - Whether to create "show all" link
   * @param {boolean} [options.mustScrollToTarget=false] - Whether to scroll to target element
   * @param {array<string>} [options.showAllLinkClassNames=[]] - List of extra classnames for "show all" link (only works with `mustCreateShowAllLink: true`)
   * @param {HTMLElement} [options.showAllLink] - A "show all" link to use
   * @param {HTMLElement} [options.scopeElement=document] - The element within which to control toggling
   * @param {string} [options.ancestorSelector] - Whether & How to select ancestor to toggle (instead of target)
   * @param {array<HTMLElement>} [options.ignoreElements] - A list of elements to not hide nor show
   */
  constructor( options ) {
    this.#opts = Object.assign({
      scopeElement: document,
      showAllLinkClassNames: [],
      ignoreElements: []
    }, options );

    this.showAllLink;

    if ( ! options.mustCreateShowAllLink && ! options.showAllLink ) {
      console.error('A "Show All" link must be provided or auto-created. Pass either "mustCreateShowAllLink" or "showAllLink".');
    }
    if ( options.mustCreateShowAllLink && options.showAllLink ) {
      console.error('A "Show All" link can not be both provided and auto-created. Pass either "mustCreateShowAllLink" or "showAllLink".');
    }

    if ( this.#opts.mustCreateShowAllLink === true ) {
      this.showAllLink = this.createShowAllLink({
        classNames: this.#opts.showAllLinkClassNames
      });
      this.#opts.scopeElement.prepend( this.showAllLink );
    } else if ( this.#opts.showAllLink ) {
      this.showAllLink = this.#opts.showAllLink;
      this.showAllLink.classList.add( this.#CLASSNAME.showAll );
      this.showAllLink.href = '#'; /* triggers hide on click */
    }

    this.showAllLink.addEventListener('click',
      this.showAll( this.#opts.scopeElement )
    );
    this.hide( this.showAllLink );

    if ( this.#opts.mustScrollToTarget ) {
      this.enableScrollFix();
    }
  }

  /** When URL hash changes, toggle element visibility */
  toggleOnHashChange() {
    window.addEventListener('hashchange', event => {
      // Do first, because if toggling fails, at least browser can still scroll
      this.showAll( this.#opts.scopeElement );
      this.hide( this.showAllLink );

      const target = document.getElementById( location.hash.substring(1) );

      // Check because auto "show all" link's empty hash results in no target
      if ( target ) {
        const elementsToHide = this.getElementsToHide( target );

        this.hide( ...elementsToHide );
        this.show( this.showAllLink );

        if ( this.#opts.mustScrollToTarget ) {
          event.preventDefault();

          this.scrollTo( target );
          // Fix only seems necessary for first event, so clean up
          this.disableScrollFix();
        }

        // To restore focus to targets whose focus is lost on successive toggles
        if ( document.activeElement !== target ) {
          target.focus();
        }
      }
    });
  }

  /** Prevent scroll jolt (that seems to happen only on first event) */
  enableScrollFix() {
    document.documentElement.style.scrollBehavior = 'smooth';
  }

  /**
   * Scroll to given element
   * @param {HTMLElement} element - The element to which to scroll
   */
  scrollTo( element ) {
    document.documentElement.scrollTop = element.offsetTop;
  }

  /** Restore normal scrolling */
  disableScrollFix() {
    document.documentElement.style.removeProperty('scroll-behavior');
  }

  /**
   * Get the elements that should be hidden
   * @param {HTMLElement} target - The targeted element
   */
   getElementsToHide( target ) {
    const elementToShow = ( this.#opts.ancestorSelector )
      ? target.closest( this.#opts.ancestorSelector )
      : target;

    const siblings = [ ...elementToShow.parentNode.children ].filter( child =>
      child !== elementToShow
    );

    const siblingsToHide = siblings.filter( sibling =>
      /* Do not hide "show all" link */
      sibling !== this.showAllLink
      /* Do not hide ignored elements */
      && this.#opts.ignoreElements.every( el => sibling !== el )
    );

    return siblingsToHide;
  }

  /**
   * Get siblings of a given element
   * @param {HTMLElement} element - The element of which to get siblings
   */
  getSiblings( element ) {
    const siblings = [ ...element.parentNode.children ].filter( child =>
      child !== element
    );

    return siblings;
  }

  /**
   * Show all hidden elements within scope
   * @param {HTMLElement} scopeElement - The element within which to search
   */
  showAll( scopeElement ) {
    const els = scopeElement.getElementsByClassName( this.#CLASSNAME.hidden );

    this.show( ...els );
  }

  /**
   * Hide all given elements
   * @param {array<HTMLElement>} els - The elements to hide
   */
  hide( ...els ) {
    els.forEach( el => {
      el.classList.add( this.#CLASSNAME.hidden );
      el.hidden = true;
    });
  }

  /**
   * Show all given elements
   * @param {array<HTMLElement>} els - The elements to show
   */
  show( ...els ) {
    els.forEach( el => {
      el.classList.remove( this.#CLASSNAME.hidden );
      el.hidden = false;
    });
  }

  /**
   * Create a "show all" link
   * @param {object} [options]
   * @param {array<string>} [options.classNames=[]] - Extra class names for link
   */
  createShowAllLink( options = {} ) {
    const defaults = { classNames: [] };
    const opts = Object.assign( defaults, options );

    const link = document.createElement('a');

    link.classList.add( this.#CLASSNAME.showAll, ...opts.classNames );

    link.href = '#';
    link.innerText = 'Show All';

    return link;
  }
}
