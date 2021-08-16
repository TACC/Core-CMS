// GH-295: Use server-side logic instead of client-side

/**
 * All system data
 * @typedef {array<System>} AllSystems
 * @see https://frontera-portal.tacc.utexas.edu/api/system-monitor/
 */

/**
 * Single system data
 * @typedef {object} System
 * @see https://frontera-portal.tacc.utexas.edu/api/system-monitor/
 */

// Allow system mointor to work(-ish) on local server
const USE_SAMPLE_DATA = (window.location.hostname === 'localhost');
const API_SAMPLE_DATA = JSON.parse('[{"hostname": "frontera.tacc.utexas.edu", "display_name": "Frontera", "ssh": {"type": "ssh", "status": true, "timestamp": "2021-07-30T19:45:02Z"}, "heartbeat": {"type": "heartbeat", "status": true, "timestamp": "2021-07-30T19:45:02Z"}, "status_tests": {"ssh": {"type": "ssh", "status": true, "timestamp": "2021-07-30T19:45:02.176Z"}, "heartbeat": {"type": "heartbeat", "status": true, "timestamp": "2021-07-30T19:45:02.174Z"}}, "resource_type": "compute", "jobs": {"running": 322, "queued": 1468, "other": 364}, "load_percentage": 99, "cpu_count": 472760, "cpu_used": 468616, "is_operational": true}, {"hostname": "stampede2.tacc.utexas.edu", "display_name": "Stampede2", "ssh": {"type": "ssh", "status": true, "timestamp": "2021-07-30T19:45:03Z"}, "heartbeat": {"type": "heartbeat", "status": true, "timestamp": "2021-07-30T19:45:03Z"}, "status_tests": {"heartbeat": {"type": "heartbeat", "status": true, "timestamp": "2021-07-30T19:45:03.069Z"}, "ssh": {"type": "ssh", "status": true, "timestamp": "2021-07-30T19:45:03.074Z"}}, "resource_type": "compute", "jobs": {"running": 1115, "queued": 1032, "other": 444}, "load_percentage": 96, "cpu_count": 1309056, "cpu_used": 1257184, "is_operational": true}]');

/**
 * The URL of the API endpoint
 * @type {string}
 */
const API_URL = '/api/system-monitor';

/**
 * The systems to show
 *
 * _Notice: This value is expected to be available from another script_
 * @type {string}
 */
const SYSTEM_HOSTNAME = window.SYSMON_SYSTEM_HOSTNAME;

/**
 * Load system status
 * @param {string} path
 * @param {function} onSuccess - Callback for success (receives JSON)
 * @param {function} onError - Callback for success (receives XMLHttpRequest)
 */
function loadStatus(path, onSuccess, onError) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
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
 * @param {System} system
 * @return {boolean}
 */
function isOperational(system) {
  if (system['load_percentage'] < 1 || system['load_percentage'] > 99) {
    system['load_percentage'] = 0;
    return system['jobs']['running'] > 1;
  }
  return true;
}

/**
 * Show system content in UI
 */
function showStatus() {
  document.getElementById('status').classList.remove('d-none');
}

/**
 * Style system status
 * @param {string} type - A type: "warning"
 */
function setStatusStyle(type) {
  switch (type) {
    case 'warning':
      document
        .getElementById('status')
        .classList.remove('badge-success');
      document.getElementById('status').removeAttribute('data-icon');
      document.getElementById('status').innerHTML = 'Maintenance';
      document.getElementById('status').classList.add('badge-warning');

    default:
      break;
  }
}

/**
 * Populate system status content in markup
 * @param {System} status
 */
function setStatusMarkup(status) {
  document.getElementById('load_percentage').innerHTML =
    status['load_percentage'] + '%';
  document.getElementById('jobs_running').innerHTML =
    status['jobs']['running'];
  document.getElementById('jobs_queued').innerHTML =
    status['jobs']['queued'];
}

/**
 * Populate system status in UI
 * @param {System} status
 */
function setStatus(status) {
  const isFound = status;
  const isWorking = isOperational(status);

  if (isFound && isWorking) {
    setStatusMarkup(status);
  } else {
    setStatusStyle('warning');
    if (isFound) {
      setStatusMarkup(status);
    }
  }
  showStatus();
}

/**
 * Populate monitor based on data
 * @param {AllSystems} systems
 */
function populate(systems) {
  let status;

  systems.forEach(function (system) {
    if (system['hostname'] === SYSTEM_HOSTNAME) {
      status = system;
      console.info(`System Monitor: System found (${SYSTEM_HOSTNAME})`);
      return false;
    }
  });

  setStatus(status);
}

/** Load and populate UI */
function init() {
  document.addEventListener(
    'DOMContentLoaded',
    function () {
      loadStatus(
        API_URL,
        function (data) {
          populate(data);
        },
        function (xhr) {
          if (USE_SAMPLE_DATA) {
            populate(API_SAMPLE_DATA);
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

init();
