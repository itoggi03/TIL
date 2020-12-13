import { createInstance } from './index'

const instance = createInstance()

function listMemo(articleno, success, fail) {
  instance
  .get(`memo/${articleno}`)
  .then(success)
  .catch(fail)
}

function registerMemo(memo, success, fail) {
  instance
  .post(`memo`, JSON.stringify(memo))
  .then(success)
  .catch(fail)
}

function modifyMemo(memo, success, fail) {
  instance
  .put(`memo`, JSON.stringify(memo))
  .then(success)
  .catch(fail)
}

function deleteMemo(articleno, memono, success, fail) {
  instance
  .delete(`memo/${articleno}/${memono}`)
  .then(success)
  .catch(fail)
}

export { listMemo, registerMemo, modifyMemo, deleteMemo }