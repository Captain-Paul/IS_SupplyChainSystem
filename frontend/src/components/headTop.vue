<template>
    <div class="header_container">
      <el-page-header @back="navigateToParentPage" content="管理员页面">
</el-page-header>
      <div class="avatar_container">
        <div class="avatar_frame">
          <el-image
            src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
            style="width: 32px; height: 32px; border-radius: 50%; cursor: pointer;"
            @click="GetAdminInfo"
          ></el-image>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'headTop',
    methods: {
      GetAdminInfo() {
        this.$router.push('/admin_info'); // 将'/admininfo' 替换为实际的子页面路径
      },
      navigateToParentPage() {
      this.$router.push('/') // 返回上一页
    }
    },
  };
  </script>
  
  <style lang="less">
  .header_container {
    background-color: #eff2f7;
    height: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-left: 20px;
  }
  
  .avatar_container {
    margin-right: 10px; /* 根据需要调整 margin 值以向左移动头像 */
  }
  
  .avatar_frame {
    width: 40px; /* 根据需要调整框的大小 */
    height: 40px; /* 根据需要调整框的大小 */
    border: 2px solid #999; /* 添加外侧头像框的样式 */
    border-radius: 50%; /* 确保外侧框与头像的边框半径一致 */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>
  