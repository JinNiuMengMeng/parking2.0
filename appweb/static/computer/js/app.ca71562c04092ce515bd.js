webpackJsonp([5],{0:function(e,t,n){n("briU"),e.exports=n("NHnr")},1:function(e,t){},GhCB:function(e,t){},LicG:function(e,t){},NHnr:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i=n("/xf8"),o={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},staticRenderFns:[]};var a=n("C7Lr")({name:"App"},o,!1,function(e){n("GhCB")},null,null).exports,r=n("aozt"),u=n.n(r),c=n("DVuL"),s=n.n(c),l=(n("LicG"),n("R4Sj")),p=n("rVsN"),d=n.n(p),f={state:{isLogin:!1},mutations:{getUserInfoSuccess:function(e,t){e.isLogin=t},getUserInfoFailed:function(e){e.isLogin=!1}},actions:{getUserInfo:function(e,t){var n=this,i=e.commit;return new d.a(function(e,o){n._vm.ajax({method:"post",url:"/parking2/getuserinfo",data:{}}).then(function(t){e(t)}).catch(function(e){i("getUserInfoFailed",t)})})}},getters:{isLogin:function(e){return e.isLogin}}};i.default.use(l.a);var m=new l.a.Store({strict:!0,modules:{common:f}}),h=n("KGCO");i.default.use(h.a);var g=new h.a({routes:[{path:"/login",name:"login",component:function(){return n.e(1).then(n.bind(null,"K31e"))}},{path:"/pay",name:"pay",component:function(){return n.e(3).then(n.bind(null,"mTUd"))}},{path:"/",component:function(){return n.e(0).then(n.bind(null,"sRWR"))},children:[{path:"",name:"index",component:function(){return n.e(2).then(n.bind(null,"r72v"))}}]}]}),v=(n("y1+5"),n("QZQP"),n("uxEr"),n("KPSb")),b=n.n(v),w=n("mtg+"),x=n.n(w),y=n("a7o1"),L=n.n(y),E=location.protocol+"//"+document.domain+":"+location.port,F=new L.a(E,{transports:["websocket"]});i.default.use(new x.a({debug:!0,connection:F})),i.default.prototype.$md5=b.a,i.default.prototype.ajax=u.a,i.default.use(l.a),i.default.use(h.a),i.default.use(s.a),i.default.config.productionTip=!1,g.beforeEach(function(e,t,n){"/login"!==e.path?m.dispatch("getUserInfo").then(function(e){0===e.data.error_code?n():n({path:"/login"})}).catch(function(e){n({path:"/login"})}):n()}),new i.default({el:"#app",router:g,store:m,components:{App:a},template:"<App/>"})},QZQP:function(e,t){window.httpConfig="/parking2/"},uxEr:function(e,t){},"y1+5":function(e,t){!function(e,t){var n,i=e.document,o=i.documentElement,a=i.querySelector('meta[name="viewport"]'),r=i.querySelector('meta[name="flexible"]'),u=0,c=0,s=t.flexible||(t.flexible={});if(a){console.warn("将根据已有的meta标签来设置缩放比例");var l=a.getAttribute("content").match(/initial\-scale=([\d\.]+)/);l&&(c=parseFloat(l[1]),u=parseInt(1/c))}else if(r){var p=r.getAttribute("content");if(p){var d=p.match(/initial\-dpr=([\d\.]+)/),f=p.match(/maximum\-dpr=([\d\.]+)/);d&&(u=parseFloat(d[1]),c=parseFloat((1/u).toFixed(2))),f&&(u=parseFloat(f[1]),c=parseFloat((1/u).toFixed(2)))}}if(!u&&!c){e.navigator.appVersion.match(/android/gi);var m=e.navigator.appVersion.match(/iphone/gi),h=e.devicePixelRatio;c=1/(u=m?h>=3&&(!u||u>=3)?3:h>=2&&(!u||u>=2)?2:1:1)}if(o.setAttribute("data-dpr",u),!a)if((a=i.createElement("meta")).setAttribute("name","viewport"),a.setAttribute("content","initial-scale="+c+", maximum-scale="+c+", minimum-scale="+c+", user-scalable=no"),o.firstElementChild)o.firstElementChild.appendChild(a);else{var g=i.createElement("div");g.appendChild(a),i.write(g.innerHTML)}function v(){var t=o.getBoundingClientRect().width/10;o.style.fontSize=t+"px",s.rem=e.rem=t}e.addEventListener("resize",function(){clearTimeout(n),n=setTimeout(v,300)},!1),e.addEventListener("pageshow",function(e){e.persisted&&(clearTimeout(n),n=setTimeout(v,300))},!1),"complete"===i.readyState?i.body.style.fontSize=12*u+"px":i.addEventListener("DOMContentLoaded",function(e){i.body.style.fontSize=12*u+"px"},!1),v(),s.dpr=e.dpr=u,s.refreshRem=v,s.rem2px=function(e){var t=parseFloat(e)*this.rem;return"string"==typeof e&&e.match(/rem$/)&&(t+="px"),t},s.px2rem=function(e){var t=parseFloat(e)/this.rem;return"string"==typeof e&&e.match(/px$/)&&(t+="rem"),t}}(window,window.lib||(window.lib={}))}},[0]);
//# sourceMappingURL=app.ca71562c04092ce515bd.js.map