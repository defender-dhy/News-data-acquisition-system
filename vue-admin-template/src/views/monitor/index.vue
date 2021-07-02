<template xmlns:el-col="http://www.w3.org/1999/html" xmlns:el-form-item="http://www.w3.org/1999/html">
  <el-main>
    <el-row>
      <el-col>
        <span style="margin: 5px"><el-tag>共计：{{ totalCount }}</el-tag></span>
        <el-tag type="success" style="margin: 5px">新增：{{ incrementCount }}</el-tag>
        <el-tag type="danger" style="margin: 5px">删除：{{ decrementCount }}</el-tag>
      </el-col>
    </el-row>

    <el-row>
      <el-card class="box-card">
        <el-form ref="form" :model="addEntryForm" :inline="true">
          <el-form-item>
            <el-select
              v-model="addEntryForm.websiteName"
              filterable
              reserve-keyword
              placeholder="网站名称"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.websiteType"
              filterable
              reserve-keyword
              placeholder="网站类型"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.country"
              filterable
              reserve-keyword
              placeholder="国别"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.language"
              filterable
              reserve-keyword
              placeholder="语言"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.field"
              filterable
              reserve-keyword
              placeholder="所属领域"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.columnName"
              filterable
              reserve-keyword
              placeholder="栏目名称"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.resourceType"
              filterable
              reserve-keyword
              placeholder="资源类型"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.resourceRelevance"
              filterable
              reserve-keyword
              placeholder="资源相关性"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.updateFrequency"
              filterable
              reserve-keyword
              placeholder="更新频率"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.dataQuality"
              filterable
              reserve-keyword
              placeholder="数据质量"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="addEntryForm.storageTime"
              filterable
              reserve-keyword
              placeholder="入库时间"
              style="border-radius: 25%;"
              size="small"
            >
              <el-option
                v-for="item in websiteList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-input
              v-model="addEntryForm.comment"
              placeholder="注释"
              style="width: 300px"
            />
          </el-form-item>

          <el-form-item>
            <el-button type="primary" icon="el-icon-circle-plus-outline">添加</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </el-row>

    <el-row>
      <el-col :span="12">
        <el-button type="primary" icon="el-icon-circle-plus-outline">导入数据</el-button>
      </el-col>

      <el-col :span="7">
        <el-form ref="form" :model="crawlingForm" :inline="true">
          <el-form-item>
            <el-link icon="el-icon-edit" type="primary" @click="strategySettingDialogVisible = true">设置策略</el-link>
          </el-form-item>

          <el-form-item>
            <el-radio-group v-model="crawlingForm.crawlingRadio" size="mini">
              <el-radio-button :label="0">自动模式</el-radio-button>
              <el-radio-button :label="1">手动模式</el-radio-button>
            </el-radio-group>
          </el-form-item>

          <el-form-item>
            <el-button type="primary">爬取</el-button>
          </el-form-item>
        </el-form>
      </el-col>

      <el-col :span="5">
        <el-input
          v-model="crawlingForm.searchText"
          placeholder="查询"
          prefix-icon="el-icon-search"
        />
      </el-col>
    </el-row>

    <el-table
      class="dataTable tb-edit"
      :data="newsTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
      highlight-current-row
      stripe="true"
      fit="true"
    >
      <el-table-column type="selection" width="35" />

      <el-table-column label="序号" sortable />

      <el-table-column label="网站名称" sortable />

      <el-table-column label="网站类型" />

      <el-table-column label="国别" />

      <el-table-column label="语言" />

      <el-table-column label="所属领域" />

      <el-table-column label="栏目名称" />

      <el-table-column label="详情" />
    </el-table>

    <el-pagination
      class="pagination"
      align="center"
      :current-page="currentPage"
      :page-sizes="[1,5,10,20]"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="newsTableData.length"
    />

    <el-dialog
      title="设置策略"
      :visible.sync="strategySettingDialogVisible">
      <el-form ref="form" :model="strategySettingForm" label-width="80px">
        <el-form-item label="策略名称">
          <el-input v-model="strategySettingForm.name" />
        </el-form-item>

        <el-form-item label="爬取范围">
          <el-select v-model="strategySettingForm.scope" placeholder="请选择爬取范围">
            <el-option label="区域一" value="shanghai" />
            <el-option label="区域二" value="beijing" />
          </el-select>
        </el-form-item>

        <el-form-item label="启动频率">
          <el-radio-group v-model="strategySettingForm.frequency">
            <el-radio label="一次" />
            <el-radio label="每天" />
            <el-radio label="每周" />
            <el-radio label="自定义" />
          </el-radio-group>
        </el-form-item>

        <el-form-item label="启动日期">
          <el-radio-group v-model="strategySettingForm.date">
            <el-radio label="今天" />
            <el-radio label="自定义" />
          </el-radio-group>
        </el-form-item>

        <el-form-item label="启动时间">
          <el-radio-group v-model="strategySettingForm.startTime">
            <el-radio label="现在" />
            <el-radio label="自定义" />
          </el-radio-group>
        </el-form-item>

        <el-form-item label="停止时间">
          <el-radio-group v-model="strategySettingForm.stopTime">
            <el-radio label="采集完成" />
            <el-radio label="自定义" />
          </el-radio-group>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="onSaveStrategy">保存当前策略</el-button>
        </el-form-item>
      </el-form>

      <el-divider />

      <el-form ref="form" :model="strategyChooseForm" label-width="80px">
        <el-form-item>
          <el-button type="primary" @click="onChooseStrategy">确定</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <el-dialog
      title="监控源详情"
      :visible.sync="monitorSourceDetailDialogVisible">
      <el-form ref="form" :model="strategySettingForm" label-width="80px">
        <el-form-item label="网站名称："></el-form-item>
        <el-form-item label="网址："></el-form-item>
        <el-form-item label="简介："></el-form-item>
        <el-form-item label="国别："></el-form-item>
        <el-form-item label="语言："></el-form-item>
        <el-form-item label="所属领域："></el-form-item>
        <el-form-item label="入库时间："></el-form-item>
        <el-form-item>
          <el-button type="primary">我要修改</el-button>
        </el-form-item>
      </el-form>

      <el-table
        class="dataTable tb-edit"
        :data="newsTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        highlight-current-row
        stripe="true"
        fit="true"
      >
        <el-table-column type="selection" width="35" />
        <el-table-column label="栏目序号" sortable />
        <el-table-column label="栏目名称" sortable />
        <el-table-column label="资源类型" />
        <el-table-column label="资源相关性" />
        <el-table-column label="更新频率" />
        <el-table-column label="质量" />
        <el-table-column label="备注" />
      </el-table>
    </el-dialog>

    <el-dialog
      title="爬取日志详情"
      :visible.sync="crawlLogDetailDialogVisible">
      <el-form ref="form" :model="strategySettingForm" label-width="80px">
        <el-form-item label="日期："></el-form-item>
        <el-form-item label="开始时间："></el-form-item>
        <el-form-item label="结束时间："></el-form-item>
        <el-form-item label="模式："></el-form-item>
        <el-form-item label="数据：">
          <el-button type="primary">一键下载</el-button>
          <el-button type="primary">数据预览</el-button>
        </el-form-item>
      </el-form>

      <el-table
        class="dataTable tb-edit"
        :data="newsTableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        highlight-current-row
        stripe="true"
        fit="true"
      >
        <el-table-column label="序号" sortable />
        <el-table-column label="网站名称" sortable />
        <el-table-column label="栏目名称" />
        <el-table-column label="数据量" />
        <el-table-column label="状态" />
        <el-table-column label="备注" />
      </el-table>

      <el-pagination
        class="pagination"
        align="center"
        :current-page="currentPage"
        :page-sizes="[1,5,10,20]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="newsTableData.length"
      />
    </el-dialog>
  </el-main>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      newsTableData: [],
      currentPage: 1, // 当前页码
      total: 20, // 总条数
      pageSize: 10, // 每页的数据条数
      websiteValue: '', // 选中
      websiteList: [], // select框数据
      columnValue: '', // 选中
      columnList: [],
      websites: [],
      columns: [],

      totalCount: 0,
      incrementCount: 0,
      decrementCount: 0,

      addEntryForm: {
        websiteName: '',
        websiteType: '',
        country: '',
        language: '',
        field: '',
        columnName: '',
        resourceType: '',
        resourceRelevance: '',
        updateFrequency: '',
        dataQuality: '',
        storageTime: '',
        comment: ''
      },

      crawlingForm: {
        crawlingRadio: 0,
        searchText: ''
      },

      strategySettingDialogVisible: false,
      strategySettingForm: {
        name: '',
        scope: '',
        frequency: '',
        date: '',
        startTime: '',
        stopTime: ''
      },
      strategyChooseForm: {
        strategyChosenList: []
      },

      monitorSourceDetailDialogVisible: false,

      crawlLogDetailDialogVisible: false
    }
  },
  methods: {
    onSaveStrategy() {
      return null
    },

    onChooseStrategy() {
      return null
    }
  }
}
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}
.tb-edit .el-input {
  display: none
}
.tb-edit .current-row .el-input {
  display: block
}
.tb-edit .current-row .el-input+span {
  display: none
}
</style>
