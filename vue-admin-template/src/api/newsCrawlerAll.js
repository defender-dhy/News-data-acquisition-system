import request from '@/utils/request'

export function newsCrawlerMany(token, strategy_name, beginDate) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/crawler/newsCrawlerMany/',
    method: 'get',
    params: {
      strategy_name: strategy_name,
      beginDate: beginDate
    }
  })
}

export function getXpathByColumn(token, column) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getXpathByColumn/',
    method: 'get',
    params: {
      column: column
    }
  })
}

export function getXpathByName(token, website_name) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getXpathByName/',
    method: 'get',
    params: {
      website_name: website_name
    }
  })
}

export function getAllXpath(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getXpathByName/',
    method: 'get',
    params: {
      website_name: ''
    }
  })
}

export function getXpathValueNameList(token, valuename) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/getXpathValueNameList/',
    method: 'get',
    params: {
      valuename: valuename
    }
  })
}

export function getXpathManage(token) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/xpathManage/',
    method: 'get'
  })
}

export function modifyXpathManage(token, cont) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/xpathManage/',
    method: 'post',
    params: {
      cont: cont
    }
  })
}

export function modifyOneSpecXpath(token, cont) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/modifyOneSpecXpath/',
    method: 'post',
    params: {
      cont: cont
    }
  })
}




