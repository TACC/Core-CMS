import { redirectExternalArticle } from '../modules/manageExternalArticles.js';

const TAG = 'force-external';

const article = document.querySelector('article.post-detail');
if (article) {
    article.classList.add(`has-blog-tag-${TAG}`);
    redirectExternalArticle(TAG);
}
