import request from '@/utils/request'

export function getWebSite(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getWebSite/',
    method: 'get',
    params: {
      database: 'news_xpath'
    }
  })
}

export function getColumn(token, websiteName) {
  return request({
    url: '/mongo/getColumn/',
    method: 'get',
    params: {
      database: 'news_xpath',
      websiteName: websiteName
    }
  })
}
export function newsCrawler(token, website, column) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/crawler/newsCrawler/',
    method: 'get',
    params: {
      website: website,
      column: column
    }
  })
}
