<template>
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
              v-model="columnValue"
              filterable
              reserve-keyword
              placeholder="栏目名称"
              style="border-radius: 25%;"
            >
              <el-option
                v-for="item in columnList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-select
              v-model="resourceTypeValue"
              filterable
              reserve-keyword
              placeholder="资源类型"
              style="border-radius: 25%;"
            >
              <el-option
                v-for="item in resourceTypeList"
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
            <el-link icon="el-icon-edit" type="primary" @click="strategySettingDialogVisible = true">新增策略</el-link>
          </el-form-item>

          <el-form-item>
            <el-radio-group v-model="crawlingForm.crawlingRadio" size="mini">
              <el-radio-button label="自动模式" />
              <el-radio-button label="手动模式" />
            </el-radio-group>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="onCrawler">爬取</el-button>
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

      <el-table-column label="序号" prop="_id" sortable />

      <el-table-column label="网站名称" prop="website_name" sortable />

      <el-table-column label="网站类型" prop="type" />

      <el-table-column label="国别" prop="lang" />

      <el-table-column label="语言" prop="lang" />

      <el-table-column label="所属领域" prop="resource_type" />

      <el-table-column label="栏目名称" prop="column" />

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
      :visible.sync="strategySettingDialogVisible"
    >
      <el-form ref="form" :model="strategySettingForm" label-width="80px">
        <el-form-item label="策略名称">
          <el-input v-model="strategySettingForm.name" />
        </el-form-item>

        <el-form-item label="爬取范围">
          <el-select v-model="strategySettingForm.column" placeholder="请选择爬取栏目">
            <el-option
              v-for="item in columnList"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="启动频率">
          <el-radio-group v-model="strategySettingForm.freq">
            <el-radio label="一次" />
            <el-radio label="每天" />
            <el-radio label="每周" />
            <el-radio label="自定义" />
          </el-radio-group>
          <el-input
            v-if="strategySettingForm.freq === '自定义'"
            v-model="strategySettingForm.customFrequency"
          >
            <template slot="append">/ 小时</template>
          </el-input>
        </el-form-item>

        <el-form-item label="启动日期">
          <el-radio-group v-model="strategySettingForm.beginDate">
            <el-radio label="今天" />
            <el-radio label="自定义" />
            <el-date-picker
              v-if="strategySettingForm.beginDate === '自定义'"
              v-model="strategySettingForm.customDate"
              type="date"
              placeholder="选择日期"
            />
          </el-radio-group>
        </el-form-item>

        <el-form-item label="启动时间">
          <el-radio-group v-model="strategySettingForm.beginTime">
            <el-radio label="现在" />
            <el-radio label="自定义" />
            <el-time-picker
              v-if="strategySettingForm.beginTime === '自定义'"
              v-model="strategySettingForm.customStartTime"
              placeholder="自定义启动时间"
            />
          </el-radio-group>
        </el-form-item>

        <el-form-item label="停止时间">
          <el-radio-group v-model="strategySettingForm.endTime">
            <el-radio label="采集完成" />
            <el-radio label="自定义" />
            <el-time-picker
              v-if="strategySettingForm.endTime === '自定义'"
              v-model="strategySettingForm.customStopTime"
              placeholder="自定义停止时间"
            />
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
      title="监测源详情"
      :visible.sync="monitorSourceDetailDialogVisible"
    >
      <el-form ref="form" :model="monitorSourceDetailForm" label-width="80px">
        <el-form-item label="网站名称">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.websiteName }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.websiteName"
            placeholder="网站名称"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="网址">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.websiteUrl }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.websiteUrl"
            placeholder="网址"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="简介">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.description }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.description"
            placeholder="简介"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="国别">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.country }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.country"
            placeholder="国别"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="语言">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.language }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.language"
            placeholder="语言"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="所属领域">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.scope }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.scope"
            placeholder="所属领域"
            style="width: 300px"
          />
        </el-form-item>
        <el-form-item label="入库时间">
          <span v-if="!monitorSourceDetailForm.modifyMode">{{ monitorSourceDetailForm.addTime }}</span>
          <el-input
            v-else
            v-model="monitorSourceDetailForm.addTime"
            placeholder="入库时间"
            style="width: 300px"
          />
        </el-form-item>
        <el-button
          type="primary"
          @click="monitorSourceDetailForm.modifyMode = !monitorSourceDetailForm.modifyMode"
        >
          {{ monitorSourceDetailForm.modifyMode ? '保存修改' : '修改数据' }}
        </el-button>
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
      :visible.sync="crawlLogDetailDialogVisible"
    >
      <el-form ref="form" :model="strategySettingForm" label-width="80px">
        <el-form-item label="日期" />
        <el-form-item label="开始时间" />
        <el-form-item label="结束时间" />
        <el-form-item label="模式" />
        <el-form-item label="数据">
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
import { newsCrawlerMany, getXpathByColumn, getXpathByName, getXpathValueNameList } from '@/api/newsCrawlerAll'
import { addStrategy } from '@/api/crawlStrategy'

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
      resourceTypeValue: '',
      resourceTypes: [],
      resourceTypeList: [],

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
        crawlingRadio: '自动模式',
        searchText: ''
      },

      strategySettingDialogVisible: false,
      strategySettingForm: {
        name: '',
        freq: '一次',
        customFrequency: '',
        beginDate: '今天',
        customDate: '',
        beginTime: '现在',
        customStartTime: '',
        endTime: '采集完成',
        customStopTime: '',
        column: '',
        urlList: [],
        freqType: ''
      },
      strategyChooseForm: {
        strategyChosenList: []
      },

      monitorSourceDetailDialogVisible: false,
      monitorSourceDetailForm: {
        modifyMode: false,
        websiteName: '名字',
        websiteUrl: '网址',
        description: '简介',
        country: '国别',
        language: '语言',
        scope: '所属领域',
        addTime: '入库时间'
      },

      crawlLogDetailDialogVisible: false
    }
  },
  watch: {
    columnValue(newValue, oldValue) {
      getXpathByColumn(this.token, newValue).then(response => {
        this.newsTableData = response['data']
      }).catch()
    }
  },
  mounted() {
    getXpathValueNameList(this.token, 'column').then(response => {
      this.columns = response['data']
      this.columnList = this.columns.map(item => {
        return { value: `${item}`, label: `${item}` }
      })
    }).catch()
    getXpathValueNameList(this.token, 'resource_type').then(response => {
      this.resourceTypes = response['data']
      this.resourceTypeList = this.resourceTypes.map(item => {
        return { value: `${item}`, label: `${item}` }
      })
    }).catch()
  },
  methods: {
    onSaveStrategy() {
      addStrategy(this.token, this.strategySettingForm)
    },

    onChooseStrategy() {
      return null
    },

    onCrawler() {
      newsCrawlerMany(this.token, this.strategySettingForm.name, this.strategySettingForm.beginDate)
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

.tb-edit .current-row .el-input + span {
  display: none
}
</style>
