<template>
  <el-container style="height: 500px; border: 1px solid #eee">
  <!-- <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu >
      <el-menu-item index="Stat"><i class="el-icon-house"></i> 统计数据</el-menu-item>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-message"></i>订单详情</template>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>导航二</template>
        <el-menu-item-group>
          <template slot="title">分组一</template>
          <el-menu-item index="2-1">选项1</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="2-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="2-4">
          <template slot="title">选项4</template>
          <el-menu-item index="2-4-1">选项4-1</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title"><i class="el-icon-setting"></i>导航三</template>
        <el-menu-item-group>
          <template slot="title">分组一</template>
          <el-menu-item index="3-1">选项1</el-menu-item>
          <el-menu-item index="3-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="3-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="3-4">
          <template slot="title">选项4</template>
          <el-menu-item index="3-4-1">选项4-1</el-menu-item>
        </el-submenu>
      </el-submenu>
    </el-menu>
  </el-aside> -->
  
  <el-container>
    <el-header style="text-align: right; font-size: 20px">
    </el-header>
    
    <el-main>
      <el-row display="margin-top:10px">
      <el-input v-model="input" placeholder="请输入订单号" style="display:inline-table; width: 30%; float:left">
      </el-input>
      <el-button type="success" @click="showorders">搜索</el-button>
      </el-row>
      

      <el-table v-show="showItem" :data="orderlist" style="width: 100%">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="订单数量">
                <span>{{ props.row.order_quantity }}</span>
              </el-form-item>
              <el-form-item label="实际售价">
                <span>{{ props.row.order_realprice }}</span>
              </el-form-item>
              <el-form-item label="客户姓名">
                <span>{{ props.row.client_name }}</span>
              </el-form-item>
              <el-form-item label="客户地址">
                <span>{{ props.row.client_addr }}</span>
              </el-form-item>
              <el-form-item label="客户电话">
                <span>{{ props.row.client_tel }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>

        <el-table-column label="订单编号" prop="order_id"></el-table-column>
        <el-table-column label="交易编码" prop="transfer"></el-table-column>
        <el-table-column label="出库编号" prop="out"></el-table-column>
        <el-table-column label="货物编码" prop="g"></el-table-column>
        <el-table-column label="生效时间" prop="order_time"></el-table-column>
      </el-table>
      
    </el-main>
  </el-container>
</el-container>

</template>

<script>
import axios from 'axios';

// const axios = require('axios');
const username = 'no_thanks';
const password = '123456';
const basicAuth = 'Basic ' + btoa(username + ':' + password);

  export default {

    name: 'ShowOrder',

    data () {
      return {
        input: '',
        orderlist: [],
        showItem:false
      }
    },

    created () {
      this.showorders()
    },

    methods:{
      showorders(){
        this.showItem = true;
        axios
        .get('http://127.0.0.1:8000/fresh/order/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {
            this.orderlist = response.data;
            console.log(this.orderlist);
          } else {
            this.$message.error('查询订单失败');
            console.log('fail');
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
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