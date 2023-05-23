# IS_SupplyChain

## 功能

- 已实现
    - 根据id查询
    - 查询近一周内要过期的货物
    - 查询某一类型货物的采购信息（蔬菜、肉类、乳制品等）
    - 查询最近7天的订单
- 待实现
    - OutboundList & OutboundDetail类
    - 查询距离已知位置最近的仓库√
    - 查询最近7天的出库记录√
    - 使用全局临时表，记录用户登陆状态，防止重复登陆√

## 结构

- FreshPagination——*分页属性*
- GoodsList
    - get——*返回所有数据*
    - post——*新增一条数据*
- GoodsDetail
    - get_object——*Get object according to given primary key.*
    - get——
    - put——*修改一条数据*
- WarehouseList
    - get
    - post
- WarehouseDetail
    - get_object
    - get
    - put
    - delete
- OrderList
    - get
    - post
- OrderDetail
    - get_object——*Get object according to given primary key.*
    - get
        - ?function=latest——*查询最近7天的订单*
    - put
    - delete——*Delete objects according to order_id.*
- BuyList
    - get
    - post
- BuyDetail
    - get
        - ?function=neardue——*查询近一周内要过期的货物*
        - ?function=type——*查询某一类型货物的采购信息（蔬菜、肉类、乳制品等）*

- OutboundList

    - get
    - post

- OutboundDetail

    - get
        - ?function=id——
        - ?function=latest——

    - 
