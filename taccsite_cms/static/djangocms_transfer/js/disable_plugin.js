/** To disable plugins from "Add plugin" list for CMS editors */

const pluginNames = [
  'PluginImporter'
];
const cmsUiWrapper = document.getElementById('cms-top');

function disableItem(item) {
    item.classList.add('js-disabled');
}

// To disable current items
pluginNames.forEach((pluginName) => {
    const pluginMenuItem = (cmsUiWrapper) && cmsUiWrapper.querySelector(`[href="${pluginName}"]`);
    if (pluginMenuItem) disableItem(pluginMenuItem);
});

// Hide future items
const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        mutation.addedNodes.forEach((node) => {
            pluginNames.forEach((pluginName) => {
                const isElement = node.nodeType === Node.ELEMENT_NODE;
                const pluginMenuItem = (isElement) && node.querySelector(`[href="${pluginName}"]`);
                if (pluginMenuItem) disableItem(pluginMenuItem);
            });
        });
    });
});
observer.observe(cmsUiWrapper, { childList: true, subtree: true });
