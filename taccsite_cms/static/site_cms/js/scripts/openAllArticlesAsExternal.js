import { changeHowExternalArticleOpens } from '../modules/manageExternalArticles.js';

const TAG = 'force-external';

const articles = document.querySelectorAll('article.post-item:not(.post-detail)');
if (articles) {
    articles.forEach(a => a.classList.add(`has-blog-tag-${TAG}`));
    changeHowExternalArticleOpens(TAG);
}
