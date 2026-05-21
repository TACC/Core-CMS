import { changeHowExternalArticleOpens } from './manageExternalArticles.js';

const TAG = 'force-external';

document.querySelectorAll('article.post-item:not(.post-detail)').forEach(a =>
  a.classList.add(`has-blog-tag-${TAG}`)
);

changeHowExternalArticleOpens(TAG);
