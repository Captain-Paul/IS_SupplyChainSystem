<template>
  <div>
    <headTop/>
    <el-row style="height: 200%;">
      <el-col :span="4" style="height: 100%; overflow: auto;">
        <el-menu :default-active="defaultActive" @select="handleSelect" router>
          <el-menu-item index="/financialmanager">
            <i class="el-icon-s-home"></i> 主页
          </el-menu-item>
          <el-menu-item index="transfer_info">
            <i class="el-icon-data-line"></i> 财务信息
          </el-menu-item>
          <el-menu-item index="transfer">
            <i class="el-icon-bank-card"></i> 转账
          </el-menu-item>

          
                

        </el-menu>
      </el-col>
      <el-col :span="20" style="height: 100%; overflow: auto;">
        <keep-alive>
          <router-view></router-view>
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
      defaultActive: 'financialmanager' // 默认选中的导航菜单项
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
