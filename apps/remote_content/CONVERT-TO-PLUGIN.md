# Converting Remote Content App to Django CMS Plugin

This document outlines the steps to convert the remote content app from Core-CMS into a Django CMS plugin.

## Source Analysis

The current remote content app in Core-CMS:
- View class `RemoteMarkup` that fetches and processes remote content
- Uses settings:
  - `PORTAL_REMOTE_CONTENT_SOURCE_ROOT` (default should be https://tacc.utexas.edu/)
  - ~~`PORTAL_REMOTE_CONTENT_CLIENT_PATH`~~ (to be removed)
- Simple template (`markup.html`) that renders fetched content
- URL transformation logic to handle relative paths and resource URLs

## Requirements

1. Keep most existing functionality, but as a CMS plugin
2. Let users input a path (not full URL) in the CMS interface 
3. Use `PORTAL_REMOTE_CONTENT_SOURCE_ROOT` setting as base URL
4. Keep URL transformation logic (no domain validation needed)
5. Display "No content found" when remote content unavailable
6. Use simple template approach with no additional options

## Implementation Steps

1. Create Plugin Files Structure
   - Follow pattern from `Core-CMS-Plugin-Image-Gallery` and `Core-CMS-Plugin-System-Monitor`
   - Package name: `djangocms_tacc_remote_content`

2. Create Model
   ```python
   class RemoteContent(CMSPlugin):
       path = models.CharField(
           max_length=255,
           help_text='Path to remote content (e.g. "about/staff")'
       )
   ```

3. Create Plugin Class
   ```python
   @plugin_pool.register_plugin
   class RemoteContentPlugin(CMSPluginBase):
       model = RemoteContent
       name = 'Remote Content'
       render_template = 'remote_content/plugin.html'
       # Port core functionality from RemoteMarkup view
   ```

4. Port Core Functionality
   - Move URL handling from view to plugin
   - Keep BeautifulSoup processing logic
   - Add error handling with "No content found" message

5. Templates
   - Rename `markup.html` to `plugin.html`
   - Keep same simple rendering approach

## Future Enhancements (Comments to Add)

1. Content Caching
   ```python
   # TODO: Consider adding cache to handle temporary failures
   # - Use Django's caching framework
   # - Add cache duration setting
   # - Implement cache invalidation strategy
   ```

2. Error Handling
   ```python
   # TODO: Enhance error handling
   # - Add specific error messages for different failure cases
   # - Add retry logic for temporary failures
   # - Consider fallback content option
   ```

## Testing Requirements

1. Basic Plugin Operation
   - Plugin appears in CMS editor
   - Plugin saves path input
   - Plugin renders remote content

2. URL Processing
   - Relative URLs transformed correctly
   - Resource URLs (images, etc.) transformed correctly
   - Error handling works

3. Settings
   - Plugin uses `PORTAL_REMOTE_CONTENT_SOURCE_ROOT` correctly
   - Default to https://tacc.utexas.edu/

## Migration Notes

1. Content Migration
   - Document how to migrate existing remote content instances
   - Add migration command if needed

2. Settings Migration
   - Remove `PORTAL_REMOTE_CONTENT_CLIENT_PATH` from projects
   - Ensure `PORTAL_REMOTE_CONTENT_SOURCE_ROOT` is set
