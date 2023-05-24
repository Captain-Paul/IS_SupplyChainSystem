<template>    
    <div>
        <h1>{{ name }}</h1><br><br>
        <el-button @click="showOrder">点击</el-button><br><br>
        <el-input v-model="input" placeholder="输入查询内容"></el-input>
    </div>
</template>

<script>

export default {
    data() {
        return {
        name:'展示',
        tableData:[],
        input:''
        }
    },
    methods: {
        showOrder(){
            alert(this.name)
        },
    },
}
</script>

<style>

</style>