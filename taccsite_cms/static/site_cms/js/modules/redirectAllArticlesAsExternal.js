import { redirectExternalArticle } from './manageExternalArticles.js';

const TAG = 'force-external';

const appBlog = document.querySelector('article.post-detail');
if (appBlog) appBlog.classList.add(`has-blog-tag-${TAG}`);

redirectExternalArticle(TAG);
