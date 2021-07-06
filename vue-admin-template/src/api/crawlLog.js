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
