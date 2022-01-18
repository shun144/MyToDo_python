const app = Vue.createApp({
  delimiters: ['[[', ']]'],
  data() {
    return {
      task:'',
      todos:[],
      tasks:[],
      edit_modal:false,
      bfr_task_title:'',
      category:'',
      category_id:'',
      disp_no:0,

      del_check:false,

      form:{
        // id:'',
        task_id:'',
        disp_no:'',
        title:'',
        description:'',
        user_name:'',
        status:'',
      },
    }
  },
  mounted () {
    this.getList();
  },
  computed: {
    displayCategories() {
      
      // jsonをネスト化
      let todos = [];
      let tasks = ""
      this.todos.map(todo => {
        tasks = this.tasks.filter(task => task.status === todo.id);
        todos.push({
          id: todo.id,
          status: todo.status,
          tasks
        })
      })

      // disp_noで並び替え
      todos.forEach(function(item){
        if (item !== undefined)
        {
          item.tasks.sort( function compare( a, b ){
            var r = 0;
            if( a.disp_no < b.disp_no ){ r = -1; }
            else if( a.disp_no > b.disp_no ){ r = 1; }
            return r;
          });
        }
      });
      return todos;
    },
  },

  methods:{
    taskDelete(task){

      this.tasks = this.tasks.filter(a => a.task_id!==task.task_id);
      axios.delete('/api/todo/' + task.task_id + '/').catch((err) => {console.log(err); });
    },


    openModal(category, task) {
      this.category = category;
      this.bfr_task_title = task.title
      
      Object.assign(this.form, task);
      this.edit_modal = true;
    },
    taskUpdate() {
      let task = this.tasks.find(task => task.task_id === this.form.task_id)
      Object.assign(task, this.form);

      axios.patch('/api/todo/' + this.form.task_id + '/', {
        title:this.form.title,
        description:this.form.description,
        user_name:this.form.user_name,
        status:this.form.status,
      }).catch((err) => {console.log(err); });
      
      this.edit_modal = false;
    },
    getList(){
      axios.get('/api/status/').then(response => (this.todos = response.data));
      axios.get('/api/todo/').then(response => (this.tasks = response.data));
    },
    patchTask(task)
    {

      axios.patch('/api/todo/' + task.task_id + '/', {
        disp_no: task.disp_no,
        title: task.title,
        description: task.description,
        user_name: task.user_name,
        status: task.status,
      }).catch((err) => {console.log(err);});
    },
    patchAllTask()
    {
      this.tasks.map((task) => {
        axios.patch('/api/todo/' + task.task_id + '/', {
          disp_no: task.disp_no,
          title: task.title,
          description: task.description,
          user_name: task.user_name,
          status: task.status,
        }).catch((err) => {console.log(err);});
      })
    },
    dropTask(){

      this.patchAllTask();

    },

    dragTask(task){
      
      this.task = task;

    },

    dragOverTask(overTask){ 
    

      if (overTask.task_id !== this.task.task_id) {
        let deleteIndex;    // 削除用Index
        let addIndex;       // 追加用Index
        this.tasks.map((task, index) => { if (task.task_id === this.task.task_id) deleteIndex = index  })
        this.tasks.map((task, index) => { if (task.task_id === overTask.task_id) addIndex = index })

        this.tasks.splice(deleteIndex, 1)
        this.task.status = overTask.status
        this.tasks.splice(addIndex, 0, this.task)

        // disp_no 更新
        let cnt = 0;
        this.tasks.map((task) => { task.disp_no =  cnt++ })

      }
    },

    dragOverCategory(overCategory){

      if (this.task.status !== overCategory.id) {
        let tasks = this.tasks.filter(task => task.status === overCategory.id)
        if (tasks.length === 0) 
        {
          this.task.status = overCategory.id;
          
          this.patchTask(this.task);  
        }
      }   
    },

    taskAdd(task_name, task_description, task_username, category_id) {

      let max_disp_no = 0;
      let max_task_id = 0;

      // tasks = this.tasks.filter(task => task.status === category_id);      
      if (this.tasks.length !== 0)
      {
        let tmp_disp_no = this.tasks.map(item => item.disp_no );
        max_disp_no = Math.max.apply(null, tmp_disp_no) + 1;

        let tmp_task_id = this.tasks.map(item => item.task_id );
        max_task_id = Math.max.apply(null, tmp_task_id) + 1;
      }

      this.tasks.push({
        task_id: max_task_id,
        disp_no:  max_disp_no,
        title: task_name,
        description: task_description,
        user_name: task_username,
        status: category_id
      })

      axios.post('/api/todo/', {
        task_id: max_task_id,
        disp_no: max_disp_no,
        title:task_name,
        description: task_description,
        user_name: task_username,
        status: category_id
      })
      .catch((err) => { console.log(err); });
    },
  },
})

app.component('task-add',{
  props: ['category_id'],
  data() {
    return {
      show: false,
      task_name:'',
      task_description:'',
      task_username:'',
    }
  },
  methods: {
    focusInput() {
      this.$refs.input.focus();
    },
    showInput() {
      this.show = true;
      Vue.nextTick(() => {
        this.focusInput();
      });
    },
    closeInput() {
      this.show = false;
      this.task_name = '';
      this.task_description = '';
      this.task_username = '';
    },
    addTask() {
      if (this.task_name != '') {
        this.$emit('TaskAdded', this.task_name, this.task_description, this.task_username, this.category_id)
        this.show = false;
        this.task_name = '';
        this.task_description = '';
        this.task_username = '';
      }
    },
  },
  template: `
  <div class="flex mx-2 hover:bg-gray-300 rounded-lg" v-if="!show" @click="showInput">
    <span class="p-2">タスクを追加</span>
  </div>

  <div class="mx-2 w-full" v-else>
    <div class="mt-3 mb-2 px-2 py-3 bg-white shadow text-xs rounded">

      <div class="input_grid">
        <label class="text-xs">タスク名</label>
        <input type="text" class="border rounded-lg px-2 text-xs" v-model="task_name" ref="input">

        <label class="text-xs">担当者</label>
        <input type="text" class="border rounded-lg px-2 text-xs" v-model="task_username">

        <label class="text-xs">詳細</label>
        <textarea type="text" class="border rounded-lg px-2 py-2 text-xs" v-model="task_description"></textarea>
      </div>

    </div>

    <div class="flex justify-end mt-1 mb-3">
      <button class="px-4 py-2 bg-green-500 hover:bg-green-700 text-white rounded-lg mr-2 font-bold text-xs" @click="addTask">追加</button>
      <button class="px-4 py-2 bg-red-500 hover:bg-red-700 text-white rounded-lg font-bold text-xs" @click="closeInput">キャンセル</button>
    </div>
  </div>
  `
})

app.component('task-del-check',{
  // props: ['category_id'],
  data() {
    return {
    }
  },
  methods: {
  },
  template: `
  <div class="flex justify-end mt-1 mb-3">
    <button class="px-4 py-2 bg-green-500 hover:bg-green-700 text-white rounded-lg mr-2 font-bold text-xs">追加</button>
    <button class="px-4 py-2 bg-red-500 hover:bg-red-700 text-white rounded-lg font-bold text-xs">キャンセル</button>
  </div>
  `
})

app.mount('#app');