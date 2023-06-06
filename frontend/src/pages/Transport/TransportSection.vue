<template>
  <el-container style="height: 200%; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-active="defaultActive" class="menu.container" router>
    
      <el-menu-item index="Transport">
        <i class="el-icon-box"></i> 采购记录
      </el-menu-item>

      <el-menu-item index="outboundrecord">
        <i class="el-icon-house"></i> 出库记录
      </el-menu-item>

      <el-menu-item index="TransInfo">
        <i class="el-icon-edit-outline"></i> 载具信息
      </el-menu-item>

      <el-menu-item index="TransRecord">
        <i class="el-icon-receiving"></i> 运输记录
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