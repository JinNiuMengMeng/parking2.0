webpackJsonp([2],{NAS8:function(e,t,i){"use strict";var s={deepClone:function(e){var t,i=this.getType(e);if("array"===i)t=[];else{if("object"!==i)return e;t={}}if("array"===i)for(var s=0,o=e.length;s<o;s++)t.push(this.deepClone(e[s]));else if("object"===i)for(var r in e)t[r]=this.deepClone(e[r]);return t},getType:function(e){return null===e?"null":void 0===e?"undefined":Object.prototype.toString.call(e).slice(8,-1).toLowerCase()}};t.a=s},Ngmm:function(e,t,i){"use strict";Object.defineProperty(t,"__esModule",{value:!0});i("NAS8");var s=i("N/5j"),o={data:function(){var e=this,t=/^\/[a-zA-Z]*$/,i=/^:[a-zA-Z]*$/;return{isdisabled:!1,isRoot:!1,isEdit:!1,level:0,hasUrl:null,role_id:this.$store.getters.roleInfo.role_id,role_name:this.$store.getters.roleInfo.role_name,parent_id:null,dialogVisible:!1,getRoleListUrl:httpConfig+"role/list",roleList:[],permisionList:[],defaultPermisionList:[],defaultCheckKey:[],roleInfo:this.$store.getters.roleInfo,defaultProps:{children:"children",label:"name"},defaultProps2:{children:"children",label:"pri_name"},permissionForm:{pri_type:null,name:null,url:"",icon:null,parent_code:null,target:null,leaf_flag:1,remark:null},permissionFormRule:{pri_type:[{required:!0,message:"请选择权限类型"}],name:[{required:!0,message:"请输入权限名称"}],icon:[{required:!0,message:"请输入图标名称"}],url:[{required:!0,message:"请输入路由"},{validator:function(s,o,r){!o||t.test(o)||i.test(o)?(e.permissionForm.pri_type?1==e.permissionForm.pri_type&&o&&!t.test(o)&&r(new Error("权限类型为菜单，路由只能以/开头")):r(new Error("请先选择权限类型")),r()):r(new Error("路由只能是由/或:开头的字母串"))}}]}}},created:function(){this.getRoleList(),this.getPermisionList()},mounted:function(){},methods:{getRoleList:function(){var e=this;Object(s.a)({method:"post",url:httpConfig+"getallrole",data:{},done:function(t,i,s){if(t)e.$message.error(t.msg);else{e.roleList=e.formateRoleList(i.role_list,null),e.level=i.role_level;var o=e.roleInfo.role_id;e.$nextTick(function(){e.$refs.roleTree.setCurrentKey(o)})}},function:function(t){e.$message.error(t.msg)}})},getPermisionList:function(e){var t=this;Object(s.a)({method:"post",url:httpConfig+"getrolepri",data:{role_id:t.role_id,parent_id:t.parent_id},done:function(e,i,s){if(e)t.$message.error(e.msg);else{var o=i.pri_list,r=i.parent_pri_list,n=t.defaultPermisionList,l=[];t.parent_id?(n.forEach(function(e){var t=!0;r.forEach(function(i){e.pri_code===i.pri_code&&(t=!1)}),o.forEach(function(t){e.pri_code===t.pri_code&&l.push(e.pri_code)}),e.disabled=t}),t.permisionList=t.formatePermissionList(n,null),t.defaultCheckKey=l):(t.defaultPermisionList=t.deepClone(o),o.forEach(function(e){e.disabled=!0,l.push(e.pri_code)}),t.permisionList=t.formatePermissionList(o,null),t.defaultCheckKey=l)}},function:function(e){t.$message.error(e.msg)}})},getDefaultPermisionList:function(){var e=this,t=this.$store.getters.privilegeList;t.forEach(function(t){t.disabled=!0,e.defaultCheckKey.push(t.pri_code)}),this.permisionList=this.formatePermissionList(t,null),this.defaultPermisionList=this.formatePermissionList(t,null)},formateRoleList:function(e,t){for(var i=[],s=void 0,o=0;o<e.length;o++)if(e[o].parent_id==t){var r=e[o];(s=this.formateRoleList(e,e[o].code)).length>0&&(r.children=s),i.push(r)}return i},formatePermissionList:function(e,t){for(var i=[],s=void 0,o=0;o<e.length;o++)if(e[o].parent_code==t){var r=e[o];(s=this.formatePermissionList(e,e[o].pri_code)).length>0&&(r.children=s),i.push(r)}return i},deepClone:function(e){var t,i=this.getType(e);if("array"===i)t=[];else{if("object"!==i)return e;t={}}if("array"===i)for(var s=0,o=e.length;s<o;s++)t.push(this.deepClone(e[s]));else if("object"===i)for(var r in e)t[r]=this.deepClone(e[r]);return t},getType:function(e){return null===e?"null":void 0===e?"undefined":Object.prototype.toString.call(e).slice(8,-1).toLowerCase()},handleNodeClick:function(e,t){this.role_id=e.code,this.parent_id=e.parent_id,this.role_name=e.name,this.getPermisionList()},handlePerNodeClick:function(e,t){console.log(e,t)},addRole:function(e,t){var i=this,o=this;this.$prompt("请输入角色名","提示",{confirmButtonText:"确定",cancelButtonText:"取消",inputPattern:/^.{1,20}$/,inputErrorMessage:"角色名格式不正确"}).then(function(i){var r=i.value,n={};n.name=r,n.parent_id=t.code,Object(s.a)({method:"post",url:httpConfig+"addrole",data:n,done:function(t,i,s){if(t)o.$message.error(t.msg);else{o.$message({type:"success",message:"新建角色名是: "+r});var n=i.code;o.appendRoleNode(e,n,r)}},function:function(e){o.$message({type:"error",message:e.msg})}})}).catch(function(){i.$message({type:"info",message:"取消输入"})})},appendRoleNode:function(e,t,i){var s={parent_id:e.data.code,code:t,name:i,children:[]};e.data.children||this.$set(e.data,"children",[]),e.data.children.push(s)},delRole:function(e,t){var i=this,o=this;this.$confirm("确认删除该角色?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){Object(s.a)({method:"post",url:httpConfig+"delrole",data:{role_id:t.code},done:function(i,s,r){if(i)o.$message.error(i.msg);else{var n=e.parent,l=n.data.children||n.data,a=l.findIndex(function(e){return e.code===t.code});l.splice(a,1)}},function:function(e){o.$message.error(e.msg)}})}).catch(function(){i.$message({type:"info",message:"取消删除"})})},editRole:function(e,t){var i=this,o=this;this.$prompt("请输入修改角色名","提示",{confirmButtonText:"确定",cancelButtonText:"取消",inputPattern:/^.{1,20}$/,inputErrorMessage:"角色名格式不正确"}).then(function(i){var r=i.value,n={};n.name=r,n.role_id=t.code,Object(s.a)({method:"post",url:httpConfig+"editrole",data:n,done:function(t,i,s){t?o.$message.error(t.msg):(o.$message({type:"success",message:"修改角色名为: "+r}),e.data.name=r)},function:function(e){o.$message({type:"error",message:e.msg})}})}).catch(function(){i.$message({type:"info",message:"取消输入"})})},delPri:function(e,t){var i=this,o=this;this.$confirm("确认删除该权限?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){Object(s.a)({method:"post",url:httpConfig+"delpri",data:{pri_code:t.pri_code,role_id:i.roleInfo.role_id},done:function(i,s,r){if(i)o.$message.error(i.msg);else{var n=e.parent,l=n.data.children||n.data,a=l.findIndex(function(e){return e.pri_code===t.pri_code});l.splice(a,1)}},function:function(e){o.$message.error(e.msg)}})}).catch(function(){i.$message({type:"info",message:"取消删除"})})},getCheckedNodes:function(){var e=this,t=this.$refs.permissionTree.getCheckedKeys(),i=this.$refs.permissionTree.getHalfCheckedKeys();t.concat(i);this.$confirm("是否保存权限授权？","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){e.$message({type:"success",message:"保存成功!"})}).catch(function(){e.$message({type:"info",message:"已取消"})})},addPri:function(e,t){t.url?this.hasUrl=t.url:this.hasUrl=null,1===t.pri_type&&1===t.leaf_flag||2===t.pri_type?(this.isdisabled=!0,this.permissionForm.pri_type=2):this.isdisabled=!1,this.isRoot=!1,this.permissionForm.parent_code=t.pri_code,this.dialogVisible=!0},editPri:function(e,t){if(console.log(t),this.permissionForm.pri_type=t.pri_type,this.permissionForm.name=t.pri_name,this.permissionForm.icon=t.icon,this.permissionForm.parent_code=t.parent_code,this.permissionForm.target=t.target,this.permissionForm.leaf_flag=t.leaf_flag,this.permissionForm.remark=t.remark,-1!==t.url.indexOf(":")){var i=t.url.lastIndexOf(":");this.hasUrl=t.url.slice(0,i),this.permissionForm.url=t.url.slice(i)}else if(-1!==t.url.indexOf("/")){var s=t.url.lastIndexOf("/");this.hasUrl=t.url.slice(0,s),this.permissionForm.url=t.url.slice(s)}this.isEdit=!0,this.dialogVisible=!0},openDialog:function(e){1===e&&(this.isdisabled=!0,this.isRoot=!0,this.permissionForm.pri_type=1,this.permissionForm.leaf_flag=0),this.dialogVisible=!0},dialogSave:function(){var e=this,t=this,i=this.permissionForm;this.$refs.permissionForm.validate(function(o){if(!o)return!1;i.role_id=e.roleInfo.role_id;var r="",n="";t.hasUrl&&(i.url=t.hasUrl+i.url),t.isEdit?(r="editpri",n="编辑成功"):(r="addpri",n="添加成功"),Object(s.a)({method:"post",url:httpConfig+r,data:i,done:function(e,i,s){e?t.$message({type:"error",message:e.msg}):(t.$message({type:"success",message:n}),t.dialogVisible=!1,t.getPermisionList())},catch:function(e){t.$message({type:"error",message:e.msg})}})})},clearData:function(){this.permissionForm.pri_type=null,this.permissionForm.name=null,this.permissionForm.url="",this.permissionForm.icon=null,this.permissionForm.parent_code=null,this.permissionForm.target=null,this.permissionForm.leaf_flag=1,this.permissionForm.remark=null,this.hasUrl=null,this.dialogVisible=!1,this.isRoot=!1,this.isEdit=!1},dialogCancel:function(){this.clearData(),this.$refs.permissionForm.resetFields()}}},r={render:function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("div",{staticStyle:{padding:"20px 40px"},attrs:{id:"role"}},[i("el-row",{attrs:{gutter:20}},[i("el-col",{attrs:{span:8}},[i("div",{staticClass:"role-tree-container"},[i("div",{staticClass:"role-list"},[e._v("角色列表")]),e._v(" "),i("el-tree",{ref:"roleTree",attrs:{"default-expand-all":"",data:e.roleList,"node-key":"code","highlight-current":"",props:e.defaultProps,"expand-on-click-node":!1},on:{"node-click":e.handleNodeClick},scopedSlots:e._u([{key:"default",fn:function(t){var s=t.node,o=t.data;return i("span",{staticClass:"custom-tree-node"},[i("span",[e._v(e._s(s.label))]),e._v(" "),i("span",{staticClass:"action-btn"},[i("button",{staticClass:"el-icon-circle-plus btn-add",attrs:{disabled:s.level+e.level===3},on:{click:function(t){t.stopPropagation(),e.addRole(s,o)}}}),e._v(" "),i("button",{staticClass:"el-icon-edit-outline btn-edit",attrs:{disabled:null==s.data.parent_id},on:{click:function(t){t.stopPropagation(),e.editRole(s,o)}}}),e._v(" "),i("button",{staticClass:"el-icon-circle-close btn-del",attrs:{disabled:null==s.data.parent_id},on:{click:function(t){t.stopPropagation(),e.delRole(s,o)}}})])])}}])})],1)]),e._v(" "),i("el-col",{attrs:{span:12}},[i("div",{staticClass:"role-tree-container"},[i("div",{staticClass:"role-list"},[i("span",[e._v("权限列表")]),e._v(" "),i("el-button",{attrs:{type:"primary",size:"middle",disabled:null==e.parent_id},on:{click:e.getCheckedNodes}},[e._v("保存授权")])],1),e._v(" "),i("el-tree",{ref:"permissionTree",attrs:{data:e.permisionList,props:e.defaultProps2,"default-checked-keys":e.defaultCheckKey,"node-key":"pri_code","show-checkbox":"","default-expand-all":"","expand-on-click-node":!1},on:{"node-click":e.handlePerNodeClick},scopedSlots:e._u([{key:"default",fn:function(t){var s=t.node,o=t.data;return i("span",{staticClass:"custom-tree-node"},[i("span",[e._v(e._s(s.label))]),e._v(" "),"超级管理员"===e.role_name?i("span",{staticClass:"action-btn"},[i("button",{staticClass:"el-icon-circle-plus btn-add",on:{click:function(t){t.stopPropagation(),e.addPri(s,o)}}}),e._v(" "),i("button",{staticClass:"el-icon-edit-outline btn-edit",on:{click:function(t){t.stopPropagation(),e.editPri(s,o)}}}),e._v(" "),i("button",{staticClass:"el-icon-circle-close btn-del",on:{click:function(t){t.stopPropagation(),e.delPri(s,o)}}})]):e._e()])}}])})],1)]),e._v(" "),i("el-col",{attrs:{span:4}},["超级管理员"===e.role_name?i("el-button",{attrs:{type:"success",size:"middle"},on:{click:function(t){e.openDialog(1)}}},[e._v("新增权限")]):e._e()],1)],1),e._v(" "),i("el-dialog",{attrs:{title:"权限信息",visible:e.dialogVisible,width:"50%",center:""},on:{"update:visible":function(t){e.dialogVisible=t},close:e.dialogCancel}},[i("el-form",{ref:"permissionForm",attrs:{model:e.permissionForm,rules:e.permissionFormRule,"label-width":"120px","label-position":"left"}},[i("el-form-item",{attrs:{label:"权限类型:",prop:"pri_type"}},[i("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择",disabled:e.isdisabled||e.isEdit},model:{value:e.permissionForm.pri_type,callback:function(t){e.$set(e.permissionForm,"pri_type",t)},expression:"permissionForm.pri_type"}},[i("el-option",{attrs:{label:"菜单",value:1}}),e._v(" "),i("el-option",{attrs:{label:"权限",value:2}})],1)],1),e._v(" "),i("el-form-item",{attrs:{label:"权限名称:",prop:"name"}},[i("el-input",{attrs:{placeholder:"请输入权限名称",clearable:""},model:{value:e.permissionForm.name,callback:function(t){e.$set(e.permissionForm,"name",t)},expression:"permissionForm.name"}})],1),e._v(" "),e.isRoot&&1===e.permissionForm.pri_type?i("el-form-item",{attrs:{label:"图标名称:"}},[i("el-input",{attrs:{placeholder:"请输入图标名称",clearable:""},model:{value:e.permissionForm.icon,callback:function(t){e.$set(e.permissionForm,"icon",t)},expression:"permissionForm.icon"}})],1):e._e(),e._v(" "),1===e.permissionForm.pri_type?i("el-form-item",{attrs:{label:"是否弹窗:"}},[i("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择是否弹窗显示"},model:{value:e.permissionForm.target,callback:function(t){e.$set(e.permissionForm,"target",t)},expression:"permissionForm.target"}},[i("el-option",{attrs:{label:"是",value:"_blank"}}),e._v(" "),i("el-option",{attrs:{label:"否",value:null}})],1)],1):e._e(),e._v(" "),e.isRoot?i("el-form-item",{attrs:{label:"路由:"}},[i("el-input",{attrs:{placeholder:"请输入路由",clearable:""},model:{value:e.permissionForm.url,callback:function(t){e.$set(e.permissionForm,"url",t)},expression:"permissionForm.url"}})],1):i("el-form-item",{attrs:{label:"路由:",prop:"url"}},[i("el-input",{attrs:{"auto-complete":"off"},model:{value:e.permissionForm.url,callback:function(t){e.$set(e.permissionForm,"url",t)},expression:"permissionForm.url"}},[e.hasUrl?i("template",{slot:"prepend"},[e._v(e._s(e.hasUrl))]):e._e()],2)],1),e._v(" "),i("el-form-item",{attrs:{label:"描述:"}},[i("el-input",{attrs:{placeholder:"请输入描述",clearable:""},model:{value:e.permissionForm.remark,callback:function(t){e.$set(e.permissionForm,"remark",t)},expression:"permissionForm.remark"}})],1)],1),e._v(" "),i("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{on:{click:e.dialogCancel}},[e._v("取 消")]),e._v(" "),i("el-button",{attrs:{type:"primary"},on:{click:e.dialogSave}},[e._v("确 定")])],1)],1)],1)},staticRenderFns:[]};var n=i("C7Lr")(o,r,!1,function(e){i("dFSX"),i("u/Gg")},"data-v-7147fd0c",null);t.default=n.exports},dFSX:function(e,t){},"u/Gg":function(e,t){}});
//# sourceMappingURL=2.2da22cab5784edcf7a43.js.map