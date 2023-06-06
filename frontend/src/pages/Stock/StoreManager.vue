<template>
  <div>
    <headTop/>
    <el-row style="height: 200%;">
      <el-col :span="4" style="height: 100%; overflow: auto;">
        <el-menu :default-active="defaultActive" router>
          <el-menu-item index="/storemanager">
            <i class="el-icon-s-home"></i> 主页
          </el-menu-item>
          <el-menu-item index="warehouse_info">
            <i class="el-icon-office-building"></i> 仓库详情
          </el-menu-item>

          <el-submenu index="1">
            <template slot="title">
                <i class="el-icon-folder-opened"></i> <span>库存详情</span> 
            </template>
            
            <el-menu-item index="goods_info">
              <i class="el-icon-box"></i> 货物详情
            </el-menu-item>
            <el-menu-item index="stock_info">
              <i class="el-icon-takeaway-box"></i> 现有库存
            </el-menu-item>
            <el-menu-item index="outbound_record">
              <i class="el-icon-document-checked"></i> 出库记录
            </el-menu-item>
            <el-menu-item index="buyrecord">
              <i class="el-icon-notebook-2"></i> 购买记录
            </el-menu-item>
          </el-submenu>

          <el-submenu index="2">
            <template slot="title">
                <i class="el-icon-shopping-cart-1"></i> <span>变更库存</span> 
            </template>
            <el-menu-item index="change_goods">
              <i class="el-icon-goods"></i> 更改货物
            </el-menu-item>
            <el-menu-item index="add_buy">
              <i class="el-icon-sell"></i> 物资采购
            </el-menu-item>
            <el-menu-item index="add_outbound">
              <i class="el-icon-sold-out"></i> 物资出库
            </el-menu-item>
            
          </el-submenu>
          <el-menu-item index="add_warehouse">
            <i class="el-icon-office-building"></i> 新建仓库
          </el-menu-item>
                

        </el-menu>
      </el-col>
      <el-col :span="20" style="height: 100%; overflow: auto;">
        <keep-alive>
          <router-view style="height: 200%;"></router-view>
        </keep-alive>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import headTop from '@/components/headTop.vue';

export default {
  name: 'HomeView',
  components: {
    headTop
  },
  data() {
    return {
      defaultActive: 'storemanager' // 默认选中的导航菜单项
    };
  },
  mounted() {
    this.defaultActive = this.$route.name; // 设置初始选中的导航菜单项为当前路由的名称
  }
};
</script>

<style>
.el-row {
  height: 100%;
}

.el-col:first-child {
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
}

.el-col:last-child {
  padding: 10px;
  overflow: auto;
}
</style>
