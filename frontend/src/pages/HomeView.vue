<template>
  <div>
    <el-row>
      <el-menu :default-active="defaultActive" class="menu-container" mode="horizontal" @select="handleSelect" router>
        <el-menu-item index=""><i class="el-icon-house"></i>首页</el-menu-item>
        <el-menu-item index="sale"><i class="el-icon-shopping-cart-2"></i> 销售部门</el-menu-item>
        <el-menu-item index="store"><i class="el-icon-box"></i>库存部门</el-menu-item>
        <el-menu-item index="transport"><i class="el-icon-truck"></i>运输部门</el-menu-item>
        <el-menu-item index="humanresource"><i class="el-icon-office-building"></i>人事部门</el-menu-item>
        <el-menu-item index="Finance"><i class="el-icon-money"></i>财务部门</el-menu-item>
        <el-menu-item index="login" class="menu-item-right"><i class="el-icon-user"></i>登录</el-menu-item>
      </el-menu>
    </el-row>
    <el-col style="height: 100%;overflow: auto;">
      <router-view></router-view>
    </el-col>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  methods: {
    handleSelect(key, keyPath) {
      if (key === '') {
        // 点击首页选项时进行特定处理，例如跳转到首页路由
        this.$router.push('/');
      } else {
        console.log(key, keyPath);
      }
    }
  },
  computed: {
    defaultActive: function() {
      return this.$route.path.replace('/', '');
    }
  }
};
</script>

<style>
.menu-container {
  display: flex;
  justify-content: space-between;
}

.menu-item-right {
  margin-left: auto;
}
</style>
