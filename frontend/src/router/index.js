import Vue from 'vue';
import Router from 'vue-router';
import LogIn from '@/pages/LogIn.vue';
import HomeView from '@/pages/HomeView'

import Sale from '@/pages/Sale/SaleSection'
import Store from '@/pages/Stock/StoreSection'
import Transport from '@/pages/Transport/TransportSection'
import Humanresource from '@/pages/HR/HumanResourceSection'

import SaleManager from '@/pages/Sale/SaleManager'
import StoreManager from '@/pages/Stock/StoreManager'
import TransportManager from '@/pages/Transport/TransportManager'
import HRManager from '@/pages/HR/HRManager'
import FinancialManager from '@/pages/Finance/FinancialManager'

import WelcomeView from '@/pages/WelcomeView'
import AdminInfo from '@/pages/AdminInfo'
import OrderDetail from '@/pages/Sale/OrderDetail'
import AddOrder from '@/pages/Sale/AddOrder'
import ChangeOrder from '@/pages/Sale/ChangeOrder'

import AddBuy from '@/pages/Stock/AddBuy'
import AddOutbound from '@/pages/Stock/AddOutbound'
import GoodsInfo from '@/pages/Stock/GoodsInfo'
import CountRecord from '@/pages/Stock/CountRecord'
import WarehouseInfo from '@/pages/Stock/WarehouseInfo'
import StockInfo from '@/pages/Stock/StockInfo'
import AddWarehouse from '@/pages/Stock/AddWarehouse'
import ChangeGoods from '@/pages/Stock/ChangeGoods'

import AddTransRecord from '@/pages/Transport/AddTransRecord'
import TransInfo from '@/pages/Transport/TransInfo'
import TransRecord from '@/pages/Transport/TransRecord'
import BuyRecord from '@/pages/Transport/BuyRecord'
import OutboundRecord from '@/pages/Transport/OutboundRecord'
import AddTransInfo from '@/pages/Transport/AddTransInfo'

import AddTransfer from '@/pages/Finance/AddTransfer';
import TransferInfo from '@/pages/Finance/TransferInfo'
import FinancialSection from '@/pages/Finance/FinancialSection'

import StaffInfo from '@/pages/HR/StaffInfo'
import RecruitmentInfo from '@/pages/HR/RecruitmentInfo'

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {// 首页，非登录状态
      path: '/',
      component: HomeView,
      children:[{
          path:'',
          name: 'Home',
          component:WelcomeView
        },{
          path: '/sale',
          name: 'Sale',
          component: Sale
        },{
          path:'/store',
          component:Store,
          children: [
              {
                path: '',
                name: 'HGoodsInfo',
                component:GoodsInfo
              }, {
                path: '/warehouseinfo',
                name: 'HWarehouseInfo',
                component:WarehouseInfo
              },{
                path:'/CountRecord',
                name: 'HCountRecord',
                component:CountRecord
              },{
                path:'/StockInfo',
                name: 'HStockInfo',
                component:StockInfo
              }]
        },{
          path:'/transport',
          component:Transport,
          children:[
            {
              path:'',
              name:'Hbuyrecord',
              component:BuyRecord
            },{
              path:'/outboundrecord',
              name:'Houtboundrecord',
              component:OutboundRecord
            },{
              path:'/TransInfo',
              name:'HTransInfo',
              component:TransInfo
            },{
              path:'/TransRecord',
              name:'HTransRecord',
              component:TransRecord
            }
          ]
        },{
          path:'/humanresource',
          component:Humanresource,
          children:[{
            path:'',
            name:'StaffInfo',
            component:StaffInfo
          }]
        },{
          path:'/finance',
          name:'Finance',
          component:FinancialSection,
          children:[{
            path:'',
            name:'TransferInfo',
            component:TransferInfo
          }]
        }
      ]
    },{// 登陆界面
      path: '/login',
      name: 'Login',
      component: LogIn
    },{// 销售部门
      path:'/salemanager',
      component:SaleManager,
      children:[{
        path:'',
        name:'SaleHome',
        component:WelcomeView
      },{
        path:'/add_order',
        name:'AddOrder',
        component:AddOrder
      },{
        path:'/change_order',
        name:'ChangeOrder',
        component:ChangeOrder
      },{
        path:'/order_detail',
        name:'OrderDetail',
        component:OrderDetail
      }
    ]
    },{//库存部门
      path:'/storemanager',
      component:StoreManager,
      children:[{
        path:'',
        name:'StoreHome',
        component:WelcomeView
      },{
        path:'/warehouse_info',
        name:'WarehouseInfo',
        component:WarehouseInfo
      },{
        path:'/goods_info',
        name:'GoodsInfo',
        component:GoodsInfo
      },{
        path:'/stock_info',
        name:'StockInfo',
        component:StockInfo
      },{
        path:'/add_buy',
        name:'AddBuy',
        component:AddBuy
      },{
        path:'/add_outbound',
        name:'AddOutbound',
        component:AddOutbound
      },{
        path:'/stock_info',
        name:'StockInfo',
        component:AddOrder
      },{
        path:'/add_warehouse',
        name:'AddWarehouse',
        component:AddWarehouse
      },{
        path:'/outbound_record',
        name:'OutboundRecord',
        component:OutboundRecord
      },{
        path:'/change_goods',
        name:'ChangeGoods',
        component:ChangeGoods
      }
    ]
    },{//运输部门
      path:'/TransportManager',
      component:TransportManager,
      children:[{
        path:'',
        name:'TransHome',
        component:WelcomeView
      },{
        path:'/trans_info',
        name:'TransInfo',
        component:TransInfo
      },{
        path:'/trans_record',
        name:'TransRecord',
        component:TransRecord
      },{
        path:'/add_trans_record',
        name:'AddTransRecord',
        component:AddTransRecord
      },{
        path:'/add_trans_info',
        name:'AddTransInfo',
        component:AddTransInfo
      }
    ]
    },{//财务部门
      path:'/FinancialManager',
      component:FinancialManager,
      children:[{
        path:'',
        name:'FinanceHome',
        component:WelcomeView
      },{
        path:'/transfer_info',
        name:'TransferInfo',
        component:TransferInfo
      },{
        path:'/transfer',
        name:'AddTransfer',
        component:AddTransfer
      }
    ]
    },{//人力资源部门
      path:'/HRManager',
      component:HRManager,
      children:[{
        path:'',
        name:'HRHome',
        component:WelcomeView
      },{
        path:'/staff_info',
        name:'StaffInfo',
        component:StaffInfo
      },{
        path:'/recuitment',
        name:'recuitment',
        component:RecruitmentInfo
      }
    ]
    },{
      path:'/admin_info',
      name:'AdminInfo',
      component:AdminInfo
    },
  ]
});

export default router;
