<template>
  <el-container style="height: 200%; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-active="defaultActive" class="menu.container" @select="handleSelect" router>
      <el-menu-item index="staff_info">
        <i class="el-icon-document"></i> 员工信息
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