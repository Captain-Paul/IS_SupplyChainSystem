<template>
  <el-container style="height: 200%; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-active="defaultActive" class="menu.container" router>
    
      <el-menu-item index="store">
        <i class="el-icon-box"></i> 货物详情
      </el-menu-item>

      <el-menu-item index="WarehouseInfo">
        <i class="el-icon-house"></i>仓库详情
      </el-menu-item>

    </el-menu>
  </el-aside> 
      <el-col  style="height: 100%;overflow: auto;">
			<keep-alive>
				<router-view></router-view>
			</keep-alive>
     </el-col>
</el-container>

</template>

<script>
  export default {
    computed: {
			defaultActive: function(){
				return this.$route.path.replace('/', '');
			}
		}
  };
</script>


<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 100px;
  }
  
  .el-aside {
    color: #333;
  }
</style>