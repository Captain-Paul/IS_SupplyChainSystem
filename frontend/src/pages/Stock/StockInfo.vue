<template>
    <el-container style="height: 1000px; border: 1px solid #eee">
      <el-main>
        <el-table v-show="showItem" :data="stocklist" style="width: 100%">
          <el-table-column label="货物编码" prop="g"></el-table-column>
          <el-table-column label="仓库编码" prop="wh"></el-table-column>
          <el-table-column label="库存数量" prop="s_quantity"></el-table-column>
        </el-table>
      </el-main>
    </el-container>
</template>
  
<script>
import axios from 'axios';
const username = 'staff0004';
const password = '123456';
const basicAuth = 'Basic ' + btoa(username + ':' + password);
  export default {
    data () {
      return {
        input: '',
        showItem:false,
        stocklist: [],  //这里是从后端获取的所有数据

      }
    },
    created () {
      this.showstock();
    },
    methods:{
      showstock(){
        this.showItem = true;
        axios
        .get('http://127.0.0.1:8000/fresh/stock/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {this.stocklist = response.data;} else {this.$message.error('获取全部库存盘点信息失败');}
        })
        .catch((error) => {console.log(error);this.$message.error('获取全部库存盘点信息失败');
          return {
            "code": 400,
            "message": "对不起，获取全部库存盘点信息失败"
          };
        });
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