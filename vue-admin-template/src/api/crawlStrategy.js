import request from '@/utils/request'

export function addStrategy(token, strategySettingForm) {
  return request({
    // url: '/vue-admin-template/user/info',
    url: '/mongo/addStrategy/',
    method: 'post',
    params: {
      strategy: strategySettingForm
    }
  })
}
