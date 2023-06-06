<template>
    <el-container style="height: 1000px; border: 1px solid #eee">
      <el-main>
        <el-select v-model="goods_type" placeholder="请选择货物种类" style="margin-right: 2%;">
          <el-option
          v-for="item in g_select"
          :key="item"
          :label="item"
          :value="item">
          </el-option>
        </el-select>
        <el-tooltip content="根据货物种类搜索" placement="top-end">
          <el-button type="primary" @click="selectCategory" icon="el-icon-search" circle></el-button>
        </el-tooltip>
        <el-tooltip content="快过期货物" placement="top-start">
          <el-button type="warning" @click="selectNeardue" icon="el-icon-alarm-clock" circle></el-button>
        </el-tooltip>
        
        <el-table :data="buyrecord" style="width: 100%">
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="采购价格">
                  <span>{{ props.row.buy_price }}</span>
                </el-form-item>
                <el-form-item label="采购数量">
                  <span>{{ props.row.buy_quantity }}</span>
                </el-form-item>
                <el-form-item label="退货原因">
                  <span>{{ props.row.return_reason }}</span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>

          <el-table-column label="批次编码" prop="buy_id"></el-table-column>
          <el-table-column label="货物编码" prop="g"></el-table-column>
          <el-table-column label="仓库编码" prop="wh"></el-table-column>
          <el-table-column label="到达日期" prop="buy_intime"></el-table-column>
          <el-table-column label="生产日期" prop="buy_pdate"></el-table-column>
          <el-table-column label="是否生效" prop="buy_valid"></el-table-column>
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
        buyrecord: [],  //这里是从后端获取的所有数据
        g_category:[],
        g_select:[],
        goods_type:'',
      }
    },created () {this.initialize();this.showbuyrecord();},
    methods:{
      initialize(){
        axios
          .get('http://127.0.0.1:8000/fresh/goods/list', {headers:{Authorization:basicAuth}})
          .then((response) => {
            if (response.status === 200) {this.g_category = response.data.results.map((item) => item.g_category);
            this.g_select=[...new Set(this.g_category)]
            } else {this.$message.error('获取后端数据失败');}
          }).catch((error) => {console.log(error);return false;});
          
      },
      selectCategory() {
        this.buyrecord = [];
        axios.get('http://127.0.0.1:8000/fresh/buy/detail/?function=type&goods_type='+this.goods_type, {
          headers: { Authorization: basicAuth }
        })
        .then((response) => {
          if (response.status === 200) {this.buyrecord = response.data;} 
          else {this.$message.error('查询采购记录失败');}
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('查询采购记录失败');
          return false;
        });
      },
      selectNeardue() {
        this.buyrecord = [];
        axios.get('http://127.0.0.1:8000/fresh/buy/detail/?function=neardue', {
          headers: { Authorization: basicAuth }
        })
        .then((response) => {
          if (response.status === 200) {this.buyrecord = response.data;} 
          else {this.$message.error('查询采购记录失败');}
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('查询采购记录失败');
          return false;
        });
      },
      showbuyrecord(){
        axios
        .get('http://127.0.0.1:8000/fresh/buy/list/', {
          headers: { Authorization: basicAuth },
        })
        .then((response) => {
          if (response.status === 200) {this.buyrecord = response.data;} 
          else {this.$message.error('获取全部采购记录失败');}
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('获取全部采购记录失败');
          return false;
        });
      },
      showNeardue(){
        this.buyrecord = [];
        this.showItem = true;
        axios.get('http://127.0.0.1:8000/fresh/buy/detail/?function=id&buy_id=' + this.input, {
          headers: { Authorization: basicAuth }
        })
        .then((response) => {
          if (response.status === 200) {this.buyrecord = [response.data];} 
          else {this.$message.error('查询采购记录失败');}
        })
        .catch((error) => {
          console.log(error);
          this.$message.error('查询采购记录失败');
          return false;
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