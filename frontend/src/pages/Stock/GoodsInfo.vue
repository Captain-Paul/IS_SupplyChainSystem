<template>
  <el-container style="height: 1000px; border: 1px solid #eee">
    <el-main>
      <el-input v-model="input" placeholder="请输入货物编号" style="display:inline-table; width: 30%; float:left">
      </el-input>
      <el-button type="success" @click="showgoodsdetails">搜索货物信息</el-button>
      <el-table v-show="showItem" :data="goodslist" style="width: 100%">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="供应商">
                <span>{{ props.row.g_vender }}</span>
              </el-form-item>
              <el-form-item label="地址">
                <span>{{ props.row.g_loc }}</span>
              </el-form-item>
              <el-form-item label="客户姓名">
                <span>{{ props.row.client_name }}</span>
              </el-form-item>
              <el-form-item label="储存温度">
                <span>{{ props.row.g_tempreture }}</span>
              </el-form-item>
              <el-form-item label="储存湿度">
                <span>{{ props.row.g_humidity }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>

        <el-table-column label="货物编号" prop="g_id"></el-table-column>
        <el-table-column label="货物名称" prop="g_name"></el-table-column>
        <el-table-column label="货物品牌" prop="g_brand"></el-table-column>
        <el-table-column label="货物种类" prop="g_category"></el-table-column>
        <el-table-column label="保质期" prop="g_life"></el-table-column>
      </el-table>
    </el-main>

</el-container>

</template>

<script>
import axios from 'axios';

const username = 'staff0005';
const password = '123456';
const basicAuth = 'Basic ' + btoa(username + ':' + password);

  export default {

    data () {
      return {
        input: '',
        showItem:false,
        goodslist: [],  //这里是从后端获取的所有数据
      }
    },
    created () {
      this.showgoods();
    },
    methods:{
      showgoodsdetails() {
        this.goodslist = [];
        this.showItem = true;
        axios.get('http://127.0.0.1:8000/fresh/goods/detail/?function=id&g_id=' + this.input, {
          headers: { Authorization: basicAuth }
        })
        .then((response) => {
          if (response.status === 200) {this.goodslist = [response.data];}
            else {this.$message.error('查询货物失败');}
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('查询货物失败');
          return false;
        });

      },
      showgoods(){
        this.showItem = true;
        axios
        .get('http://127.0.0.1:8000/fresh/goods/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {
            this.goodslist = response.data.results;}
            else {this.$message.error('获取全部货物信息失败');}})
        .catch((error) => {
          console.log(error);
          this.$message.error('获取全部货物信息失败');
          return false;});
      },
},
};
</script>
<style>
  .el-pagination__wrapper {
          position: absolute;
          bottom: 0;
          width: 100%;
  }
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>