import { createInstance } from './index'

const instance = createInstance()

function listArticle(para, success, fail) {
  instance
  .get(`article`, {params: para})
  .then(success)
  .catch(fail)
}

function registerArticle(article, success, fail) {
  instance
  .post(`article`, JSON.stringify(article))
  .then(success)
  .catch(fail)
}

function getArticle(articleno, success, fail) {
  instance
  .get(`article/${articleno}`)
  .then(success)
  .catch(fail)
}

function modifyArticle(article, success, fail) {
  instance
  .put(`article`, JSON.stringify(article))
  .then(success)
  .catch(fail)
}

function deleteArticle(articleno, success, fail) {
  instance
  .delete(`article/${articleno}`)
  .then(success)
  .catch(fail)
}

export { listArticle, getArticle, registerArticle, modifyArticle, deleteArticle }