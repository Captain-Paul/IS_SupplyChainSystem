<template>
	<div class="header_container">
 <el-breadcrumb separator="/">
		<el-breadcrumb-item :to="{ path: '/manage' }">首页</el-breadcrumb-item>
		<el-breadcrumb-item v-for="(item, index) in $route.meta" :key="index">{{ item }}</el-breadcrumb-item>
  </el-breadcrumb>
  <el-image
		src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
		style="width: 36px; height: 36px; border-radius: 50%; cursor: pointer;"
		@click="navigateToChildPage"
  ></el-image>
	</div>
  </template>
  
  <script>
  export default {
	name: 'headTop',
	methods: {
  navigateToChildPage() {
		this.$router.push('/admininfo'); // 将'/childPage'替换为实际的子页面路径
  },
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
  </style>
  