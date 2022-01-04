const app = Vue.createApp({
    data() {
        return {
            task:'',
            show: false,
            task_name:'',
            modal:false,
            form: {
                id:'',
                category_id:'',
                name:'',
                start_date:'',
                end_date:'',
                incharge_user:'',
                percentage:''
            },
            categories: [
            {
                id: 1,
                name: 'テストA',
                collapsed: false,
            }, 
            {
                id: 2,
                name: 'テストB',
                collapsed: false,
            },
                {
                id: 3,
                name: 'テストC',
                collapsed: false,
            },             
            ],
            tasks: [
            {
                id: 1,
                category_id: 1,
                name: 'テスト1',
                start_date: '2020-12-18',
                end_date: '2020-12-20',
                incharge_user: '鈴木',
                percentage: 100,
            },
            {
                id: 2,
                category_id: 1,
                name: 'テスト2',
                start_date: '2020-12-19',
                end_date: '2020-12-23',
                incharge_user: '佐藤',
                percentage: 90,
            },
            {
                id: 3,
                category_id: 3,
                name: 'テスト3',
                start_date: '2020-12-19',
                end_date: '2020-12-21',
                incharge_user: '鈴木',
                percentage: 40,
            },
            {
                id: 4,
                category_id: 2,
                name: 'テスト4',
                start_date: '2020-12-21',
                end_date: '2020-12-30',
                incharge_user: '山下',
                percentage: 60,
            },
            {
                id: 5,
                category_id: 2,
                name: 'テスト5',
                start_date: '2020-12-20',
                end_date: '2020-12-22',
                incharge_user: '佐藤',
                percentage: 5,
            },
            {
                id: 6,
                category_id: 1,
                name: 'テスト6',
                start_date: '2020-12-28',
                end_date: '2020-12-08',
                incharge_user: '佐藤',
                percentage: 0,
            },
            ],
        }
    },
computed: {
    displayCategories() {
        let categories = [];
        let tasks = ""
        this.categories.map(category => {
            tasks = this.tasks.filter(task => task.category_id === category.id);
            categories.push({
                id: category.id,
                name: category.name,
                tasks
            })
        })
        return categories;
    }
},
methods:{
    dragTask(task){
        this.task = task;
    },
    dragOverTask(overTask){
        if (overTask.id !== this.task.id) {
            let deleteIndex;
            let addIndex;
            this.tasks.map((task, index) => { if (task.id === this.task.id) deleteIndex = index })
            this.tasks.map((task, index) => { if (task.id === overTask.id) addIndex = index })
            this.tasks.splice(deleteIndex, 1)
            this.task.category_id = overTask.category_id //追加
            this.tasks.splice(addIndex, 0, this.task)
        }    
    },
    dragOverCategory(overCategory){
        if (this.task.category_id !== overCategory.id) {
            let tasks = this.tasks.filter(task => task.category_id === overCategory.id)
            if (tasks.length === 0) this.task.category_id = overCategory.id;
        }         
    },
    taskAdd(task_name, category_id) {
        this.tasks.push({
            id: Date.now(),
            category_id,
            name: task_name
        })
    },
    openModal(category, task) {
        this.category = category;
        Object.assign(this.form, task);
        this.modal = true;
    },
    taskUpdate() {
        let task = this.tasks.find(task => task.id === this.form.id)
        Object.assign(task, this.form)
        this.modal = false;
    },
},
delimiters: ['[[', ']]'],
})



app.component('task-add', {
  props: ['category_id'],
  data() {
    return {
      show: false,
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
    },
    addTask() {
        if (this.task_name != '') {
            this.$emit('TaskAdded', this.task_name, this.category_id)
            this.show = false;
            this.task_name = '';
        }
        },
  },
  template: `
  <div class="flex mx-2 hover:bg-gray-300 rounded-lg" v-if="!show" @click="showInput">
    <span class="p-2">タスクを追加</span>
  </div>
  <div class="mx-2" v-else>
    <div>
        <input type="text" class="w-full p-2" placeholder="新しいタスク名を入力してください" v-model="task_name" ref="input"/>
    </div>
    <div class="flex m-2">
        <button class="px-4 py-2 bg-green-500 hover:bg-green-700 text-white rounded-lg mr-2 font-bold text-xs" @click="addTask">追加</button>
        <button class="px-4 py-2 bg-red-500 hover:bg-red-700 text-white rounded-lg font-bold text-xs" @click="closeInput">キャンセル</button>
    </div>
  </div>
  `
})

app.mount('#app')