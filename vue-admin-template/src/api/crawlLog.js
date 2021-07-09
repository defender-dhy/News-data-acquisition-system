import request from '@/utils/request'

export function getAllCrawlerLog(token, filter) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/crawlerLog/',
    method: 'get',
    params: {
      filter: filter
    }
  })
}

export function modifyLog(token, log) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/modifyLog/',
    method: 'post',
    params: {
      log: log
    }
  })
}
