<template>
  <div>
    <el-row>
      <el-menu :default-active="defaultActive" class="menu.container" mode="horizontal" @select="handleSelect" router>
      <el-menu-item index=""><i class="el-icon-s-home"></i>首页</el-menu-item>
    
      <el-menu-item index="sale">
        <i class="el-icon-s-order"></i> 销售部门
      </el-menu-item>

      <el-menu-item index="store">
        <i class="el-icon-goods"></i>库存部门
      </el-menu-item>

      <el-menu-item index="transport"><i class="el-icon-truck"></i>运输部门</el-menu-item>
      <el-menu-item index="HumanResource"><i class="el-icon-office-building"></i>人事部门</el-menu-item>
      <el-menu-item index="login" class="menu-item-right"><i class="el-icon-user"></i>登录</el-menu-item>
      
    </el-menu>

      
    </el-row>
	

  <el-col  style="height: 100%;overflow: auto;">
			<keep-alive>
				<router-view></router-view>
			</keep-alive>
	</el-col>
  </div>
</template>

<script>
  export default {
	name:'HomeView',
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath)
      }
    },
    computed: {
			defaultActive: function(){
				return this.$route.path.replace('/', '');
			}
		},
  }
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