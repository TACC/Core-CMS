/**
 * Show public runtime data about a TACC system
 *
 * - Manipulates attributes and text nodes within existing markup.
 * - Data is NOT dynamically updated after initial load.
 * @module systemMonitor
 */
// GH-295: Use server-side logic instead of client-side
// NOTE: If JavaScript is a long-term solution, then use a class.



/* Definitions */

/**
 * All system data
 * @typedef {array<module:systemMonitor~System>} AllSystems
 * @see https://frontera-portal.tacc.utexas.edu/api/system-monitor/
 */

/**
 * Single system data
 * @typedef {object} System
 * @see https://frontera-portal.tacc.utexas.edu/api/system-monitor/
 */



/* Constants */
/* IDEA: These could be static properties, once Safari support is widespread */

/**
 * Sample system data
 * @type {array<module:systemMonitor~System>}
 */
const API_SAMPLE_DATA = JSON.parse('[{"hostname": "frontera.tacc.utexas.edu", "display_name": "Frontera", "ssh": {"type": "ssh", "status": true, "timestamp": "2021-07-30T19:45:02Z"}, "heartbeat": {"type": "heartbeat", "status": true, "timestamp": "2021-07-30T19:45:02Z"}, "status_tests": {"ssh": {"type": "ssh", "status": true, "timestamp": "2021-07-30T19:45:02.176Z"}, "heartbeat": {"type": "heartbeat", "status": true, "timestamp": "2021-07-30T19:45:02.174Z"}}, "resource_type": "compute", "jobs": {"running": 322, "queued": 1468, "other": 364}, "load_percentage": 99, "cpu_count": 472760, "cpu_used": 468616, "is_operational": true}, {"hostname": "stampede2.tacc.utexas.edu", "display_name": "Stampede2", "ssh": {"type": "ssh", "status": true, "timestamp": "2021-07-30T19:45:03Z"}, "heartbeat": {"type": "heartbeat", "status": true, "timestamp": "2021-07-30T19:45:03Z"}, "status_tests": {"heartbeat": {"type": "heartbeat", "status": true, "timestamp": "2021-07-30T19:45:03.069Z"}, "ssh": {"type": "ssh", "status": true, "timestamp": "2021-07-30T19:45:03.074Z"}}, "resource_type": "compute", "jobs": {"running": 0, "queued": 1032, "other": 444}, "load_percentage": 0, "cpu_count": 1309056, "cpu_used": 1257184, "is_operational": true}]');

/**
 * The URL of the API endpoint
 * @type {string}
 */
const API_URL = '/api/system-monitor';



/* Exports */

/**
 * Populate a system monitor element
 */
export class SystemMonitor {



  /**
   * Initialize system monitor
   * @param {string} hostname - The systems to show
   * @param {HTMLElement} domElement - The DOM element for display
   * @param {HTMLElement} [shouldUseSampleData=false] - Whether to present fake data
   */
  constructor(hostname, domElement, shouldUseSampleData=false) {
    /**
     * The systems to show
     * @type {string}
     */
    this.hostname = hostname;

    /**
     * The DOM element for display
     * @type {HTMLElement}
     */
    this.domElement = domElement;

    /**
     * Whether to present fake data on a local server
     * @type {boolean}
     */
    this.shouldUseSampleData = shouldUseSampleData;



    this.init();
  }



  /**
   * Load system status
   * @param {string} path
   * @param {function} onSuccess - Callback for success (receives JSON)
   * @param {function} onError - Callback for success (receives XMLHttpRequest)
   */
  loadStatus(path, onSuccess, onError) {
    const xhr = new XMLHttpRequest();

    xhr.onreadystatechange = () => {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          if (onSuccess) onSuccess(JSON.parse(xhr.responseText));
        } else {
          if (onError) onError(xhr);
        }
      }
    };
    xhr.open('GET', path, true);
    xhr.send();
  }

  /**
   * Whether system is operational
   * @param {module:systemMonitor~System} system
   * @return {boolean}
   */
  isOperational(system) {
    if (system['load_percentage'] < 1 || system['load_percentage'] > 99) {
      system['load_percentage'] = 0;
      return system['jobs']['running'] > 1;
    }
    return true;
  }

  /**
   * Get element in UI by an ID
   * @param {string} id - The (internally unique) identifier of an element
   * @return {HTMLElement}
   */
  getElement(id) {
    // NOTE: To permit multiple instances,
    //       an ID must be reusable across instances,
    //       so `document.getElementById` SHOULD NOT be used.
    return this.domElement.querySelector(`[data-id="${id}"]`);
  }

  /**
   * Show system content in UI
   */
  showStatus() {
    this.getElement('status').classList.remove('d-none');
  }

  /**
   * Style system status
   * @param {string} type - A type: "warning"
   */
  setStatusStyle(type) {
    const element = this.getElement('status');

    switch (type) {
      case 'warning':
        element.classList.remove('badge-success');
        element.removeAttribute('data-icon');
        element.innerHTML = 'Maintenance';
        element.classList.add('badge-warning');

      default:
        break;
    }
  }

  /**
   * Populate system status content in markup
   * @param {module:systemMonitor~System} status
   */
  setStatusMarkup(status) {
    this.getElement('load_percentage').innerHTML =
      status['load_percentage'] + '%';
    this.getElement('jobs_running').innerHTML =
      status['jobs']['running'];
    this.getElement('jobs_queued').innerHTML =
      status['jobs']['queued'];
  }

  /**
   * Populate system status in UI
   * @param {module:systemMonitor~System} status
   */
  setStatus(status) {
    const isFound = status;
    const isWorking = this.isOperational(status);

    if (isFound && isWorking) {
      this.setStatusMarkup(status);
    } else {
      this.setStatusStyle('warning');
      if (isFound) {
        this.setStatusMarkup(status);
      }
    }
    this.showStatus();
  }

  /**
   * Populate monitor based on data
   * @param {module:systemMonitor~AllSystems} systems
   */
  populate(systems) {
    let status;

    systems.forEach((system) => {
      if (system['hostname'] === this.hostname) {
        status = system;
        console.info(`System Monitor: System found (${this.hostname})`);
        return false;
      }
    });

    this.setStatus(status);
  }

  /* Initialize (if using a class, Constructor) */

  /** Load and populate UI */
  init() {
    document.addEventListener(
      'DOMContentLoaded',
      () => {
        this.loadStatus(
          API_URL,
          (data) => {
            this.populate(data);
          },
          (xhr) => {
            if (this.shouldUseSampleData) {
              this.populate(API_SAMPLE_DATA);
            } else {
              console.error(xhr);
            }
          }
        );

        console.log('System Monitor: Load complete');
      },
      false
    );
  }
}
