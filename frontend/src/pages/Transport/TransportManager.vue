<template>
  <div>
    <headTop/>
    <el-row style="height: 200%;">
      <el-col :span="4" style="height: 100%; overflow: auto;">
        <el-menu :default-active="defaultActive" @select="handleSelect" router>
          <el-menu-item index="/transportmanager">
            <i class="el-icon-s-home"></i> 主页
          </el-menu-item>
          <el-menu-item index="trans_info">
            <i class="el-icon-truck"></i> 载具状态
          </el-menu-item>
          <el-menu-item index="trans_record">
            <i class="el-icon-guide"></i> 运输详情
          </el-menu-item>

          <el-menu-item index="add_trans_record">
              <i class="el-icon-coordinate"></i> 指派运输
            </el-menu-item>
          <el-menu-item index="add_trans_info">
            <i class="el-icon-shopping-cart-2"></i> 购置载具
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
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
      this.defaultActive = key;
    }
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
