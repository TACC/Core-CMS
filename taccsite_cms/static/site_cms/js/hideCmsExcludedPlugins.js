/**
 * Hide CMS "Add plugin" items
 * SEE:
 *     - #portal-cms_excluded_plugins-list
 *     - CMS_PLACEHOLDER_CONF[None]['excluded_plugins']
 * HACK: "Add plugin" still lists CMS_PLACEHOLDER_CONF['excluded_plugins'],
 *       so we hide them in the UI until CMS honors config in the UI.
 */
(function hideCmsExcludedPlugins() {
    const configEl = document.getElementById('portal-cms_excluded_plugins-list');
    const cmsTop = document.getElementById('cms-top');
    if (!configEl || !cmsTop) return;

    let pluginNames;
    try { pluginNames = JSON.parse(configEl.textContent) } catch (e) { return }
    if (!pluginNames.length) return;

    function hideCurrentItems(root = cmsTop) {
        if (!root || root.nodeType !== Node.ELEMENT_NODE) return;
        pluginNames.forEach((pluginName) => {
            const selector = `[href="${pluginName}"]`;
            if (root.matches(selector)) root.hidden = true;
            root.querySelectorAll(selector).forEach((item) => {
                item.hidden = true;
            });
        });
    }
    function hideFutureItems(root = cmsTop) {
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                mutation.addedNodes.forEach((node) => hideCurrentItems(node));
            });
        });
        observer.observe(root, { childList: true, subtree: true });
    }

    hideCurrentItems();
    hideFutureItems();
})();
