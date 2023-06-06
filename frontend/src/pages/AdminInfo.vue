<template>
  <div>
    <el-card>
      <el-descriptions title="开发者信息">
        <el-descriptions-item label="前端页面">夏宇烨 高梓越</el-descriptions-item>
        <el-descriptions-item label="地点">北京市</el-descriptions-item>
        <el-descriptions-item label="备注">
          <el-tag size="small">学校</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="后端数据">赵晟浩 谢奕飞</el-descriptions-item>
        
        <el-descriptions-item label="联系地址">北京市海淀区知春路29号大运村学生公寓</el-descriptions-item>
      </el-descriptions>
    </el-card>
    <el-button icon="el-icon-back" circle class="card-button" @click="goBack"></el-button>
  </div>
</template>

<script>
export default {
  name: 'AdminInfo',
  methods: {
    goBack() {
      this.$router.go(-1); // 返回上一个路由
    },
  },
}
</script>

<style scoped>
.el-card {
  margin: 100px auto;
  width: 600px;
  padding: 20px;
  text-align: center;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.card-button {
  position: absolute;
  top: 20px;
  left: 20px;
}
</style>
