import Vue from 'vue';
import Router from 'vue-router';
import LogIn from '@/pages/LogIn.vue';
import HomeView from '@/pages/HomeView'
import Sale from '@/pages/SaleSection'
import WelcomeView from '@/pages/WelcomeView'
import Store from '@/pages/StoreSection'
import Transport from '@/pages/TransportSection'
import SaleManager from '@/pages/SaleManager'
import StoreManager from '@/pages/StoreManager'
import TransportManager from '@/pages/TransportManager'
import HRManager from '@/pages/HRManager'
import FinancialManager from '@/pages/FinancialManager'
import AdminInfo from '@/pages/AdminInfo'
import HumanResource from '@/pages/HumanResourceSection'

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
      children:[{
          path:'/home',
          name: 'Welcome',
          component:WelcomeView
        },{
          path: '/Sale',
          name: 'Sale',
          component: Sale
        },{
          path:'/Store',
          name:'Store',
          component:Store
        },{
          path:'/Transport',
          name:'Transport',
          component:Transport
        },{
          path:'/HumanResource',
          name:'HumanResource',
          component:HumanResource
        }
      ]
    },{
      path: '/login',
      name: 'Login',
      component: LogIn
    },{
      path:'/salemanager',
      name:'SaleManager',
      component:SaleManager,
      children:[{
        path:'/admininfo',
        name:'AdminInfo',
        component:AdminInfo
      }]
    },{
      path:'/storemanager',
      name:'StoreManager',
      component:StoreManager
    },{
      path:'/TransportManager',
      name:'TransportManager',
      component:TransportManager
    },{
      path:'/FinancialManager',
      name:'FinancialManager',
      component:FinancialManager
    },{
      path:'/HRManager',
      name:'HRManager',
      component:HRManager
    }
  ]
});

export default router;
