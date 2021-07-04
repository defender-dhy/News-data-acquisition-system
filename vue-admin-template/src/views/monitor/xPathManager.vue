<template>
  <el-main>
    <el-table
      :data="tableList"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
      @cell-dblclick="tableEdit"
    >
      <el-table-column label="车辆类型" align="center">
        <template slot-scope="scope">{{ scope.row.type }}</template>
      </el-table-column>
      <el-table-column label="车架号" align="center">
        <template slot-scope="scope">{{ scope.row.frameNumber }}</template>
      </el-table-column>
    </el-table>
  </el-main>
</template>

<script>

export default {
  data() {
    return {
      tableList: [
        { type: '12', frameNumber: '23' }
      ]
    }
  },
  methods: {
    tableEdit(row, column, cell, event) {
      if (column.label) {
        var beforeVal = event.target.textContent
        event.target.innerHTML = ''
        cell.innerHTML = `<div class='cell'>
            <div class='el-input'>
              <input type='text' placeholder='请输入内容' class='el-input__inner'>
            </div>
        </div>`
        const cellInput = cell.children[0].children[0].children[0]
        cellInput.value = beforeVal
        cellInput.focus() // input自动聚焦
        // 失去焦点后  将input移除
        cellInput.onblur = function() {
          const onblurCont = `<div class='cell'>${cellInput.value}</div>`
          cell.innerHTML = onblurCont // 换成原有的显示内容
          // 调用axios接口
        };
      }
    }
  }
}
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.tb-edit .el-input {
  display: none;
}

.tb-edit .current-row .el-input {
  display: block;
}

.tb-edit .current-row .el-input + span {
  display: none;
}
</style>
