import request from '@/utils/request'

export function wechatCrawler(token, name) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/crawler/wechatCrawler/',
    method: 'get',
    params: {
      wechatName: name
    }
  })
}
