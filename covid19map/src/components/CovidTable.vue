    <template>
    <div>
      <el-table
        :data="tableData"
        style="width: 100%;margin-bottom: 20px;"
        row-key="name"
        border      
        :tree-props="{children: 'city', hasChildren: 'hasChildren'}">
        <el-table-column
          prop="name"
          label="state"
          sortable
          width="300">
        </el-table-column>
        <el-table-column
          prop="confirm"
          label="confirmed"
          sortable
          width="180">
        </el-table-column>
        <el-table-column
          prop="death"
          label="death"
          sortable
          >
        </el-table-column>
      </el-table>
    </div>
    </template>
    <script>
    import todaydata from '../assets/today.json'
    export default {
        data() {
          return {
            tableData: []
          }
        },
        mounted(){
        this.tableData = todaydata.children
  }
      }
    </script>