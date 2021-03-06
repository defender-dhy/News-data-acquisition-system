import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'dashboard' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/mainPage',
    children: [{
      path: 'mainPage',
      name: 'mainPage',
      component: () => import('@/views/monitor/index'),
      meta: { title: '主操作', icon: 'el-icon-menu' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/xpathManage',
    children: [{
      path: 'xpathManage',
      name: 'xpathManage',
      component: () => import('@/views/monitor/xPathManager'),
      meta: { title: '监测源字段管理', icon: 'el-icon-edit-outline' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/newsCrawlerAll',
    children: [{
      path: 'newsCrawlerAll',
      name: 'newsCrawlerAll',
      component: () => import('@/views/crawler/newsCrawlerAll'),
      meta: { title: '新闻数据一键爬取', icon: 'el-icon-circle-plus' }
    }]
  },
  {
    path: '/',
    component: Layout,
    redirect: '/newsCrawler',
    children: [{
      path: 'newsCrawler',
      name: 'newsCrawler',
      component: () => import('@/views/crawler/newsCrawler'),
      meta: { title: '新闻数据具体爬取', icon: 'el-icon-plus' }
    }]
  },
  // {
  //   path: '/',
  //   component: Layout,
  //   redirect: '/wechatCrawler',
  //   children: [{
  //     path: 'wechatCrawler',
  //     name: 'wechatCrawler',
  //     component: () => import('@/views/crawler/wechatCrawler'),
  //     meta: { title: '微信公众号爬虫', icon: 'el-icon-circle-plus' }
  //   }]
  // },
  // {
  //   path: '/',
  //   component: Layout,
  //   redirect: '/urlCRU',
  //   children: [{
  //     path: 'urlCRU',
  //     name: 'urlCRU',
  //     component: () => import('@/views/main/urlCRU'),
  //     meta: { title: '高校url标准库', icon: 'el-icon-folder-checked' }
  //   }]
  // },
  // {
  //   path: '/',
  //   component: Layout,
  //   redirect: '/updateAll',
  //   children: [{
  //     path: 'updateAll',
  //     name: 'updateAll',
  //     component: () => import('@/views/main/updateAll'),
  //     meta: { title: '学者详情更新', icon: 'el-icon-refresh' }
  //   }]
  // },
  // {
  //   path: '/',
  //   component: Layout,
  //   redirect: '/updateByXpath',
  //   children: [{
  //     path: 'updateByXpath',
  //     name: 'updateByXpath',
  //     component: () => import('@/views/main/updateByXpath'),
  //     meta: { title: '学者详情新增', icon: 'el-icon-circle-plus' }
  //   }]
  // },
  // {
  //   path: '/',
  //   component: Layout,
  //   redirect: '/updateByOrganization',
  //   children: [{
  //     path: 'updateByOrganization',
  //     name: 'updateByOrganization',
  //     component: () => import('@/views/main/updateByOrganization'),
  //     meta: { title: '选择高校更新', icon: 'el-icon-school' }
  //   }]
  // },
  // {
  //   path: '/',
  //   component: Layout,
  //   redirect: '/search',
  //   children: [{
  //     path: 'search',
  //     name: 'Search',
  //     component: () => import('@/views/main/search'),
  //     meta: { title: '数据统计', icon: 'el-icon-s-data' }
  //   }]
  // },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
