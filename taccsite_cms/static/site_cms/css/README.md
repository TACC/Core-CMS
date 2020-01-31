# TACC CMS - Static CSS

One file in this directory is compiled from source code in `/src/styles` that happens to load files from this directory. This unclear architecture (indirect confluence of source and output) is temporary in order to provide a single CSS file for CMS and Portal to use for the unified header markup.

To compile the CSS, run `npm run build:css`.
