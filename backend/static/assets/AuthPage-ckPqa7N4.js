import{d as m,f as v,o as l,g as n,h as t,i as p,j as r,v as d,t as u,k as h,u as g,p as b,l as _,r as c}from"./index-BpeIn0B_.js";import{_ as y}from"./_plugin-vue_export-helper-x3n3nnut.js";const i=o=>(b("data-v-e4613a37"),o=o(),_(),o),f={class:"container"},w={id:"auth"},S={class:"row justify-content-center"},k=i(()=>t("p",{class:"fs-3 text-center mb-3"},"SberGigachat",-1)),I={key:0},x={class:"mb-3"},E={class:"input-group"},P=["type"],U={class:"input-group-text"},T=i(()=>t("div",{class:"d-grid gap-2 mb-3"},[t("button",{class:"btn btn-primary",type:"submit"},"Submit")],-1)),A={key:1},C={class:"input-group mb-3"},V=["type"],$={class:"input-group-text"},j=i(()=>t("div",{class:"d-grid gap-2 mb-3"},[t("button",{class:"btn btn-primary",type:"submit"},"Submit")],-1)),q=i(()=>t("a",{class:"btn btn-link",href:"https://developers.sber.ru/docs/ru/gigachat/api/integration",target:"_blank"},"Подключение API",-1)),B=m({__name:"AuthPage",setup(o){const e=v({visible:!1,authTypo:localStorage.getItem("gigachattypo")||"auth",gigaSecret:localStorage.getItem("gigachatsecret")||"",gigaUsername:localStorage.getItem("gigachatusername")||"",gigaPassword:localStorage.getItem("gigachatpassword")||"",switchForm:function(){this.authTypo==="logopass"?localStorage.setItem("gigachattypo","auth"):localStorage.setItem("gigachattypo","logopass")}});return(D,s)=>(l(),n("div",f,[t("div",w,[t("div",S,[k,e.value.authTypo==="auth"?(l(),n("div",I,[t("form",{class:"mb-3",onSubmit:s[2]||(s[2]=p(a=>g(c).push({name:"gigachat"}),["prevent"]))},[t("div",x,[t("div",E,[r(t("input",{class:"form-control",type:e.value.visible?"text":"password",autocomplete:"current-password",required:"","onUpdate:modelValue":s[0]||(s[0]=a=>e.value.gigaSecret=a),placeholder:"Enter Authorization Key"},null,8,P),[[d,e.value.gigaSecret]]),t("span",U,[t("a",{role:"button",onClick:s[1]||(s[1]=a=>e.value.visible=!e.value.visible)},u(e.value.visible?"Hide":"Show"),1)])])]),T],32)])):(l(),n("div",A,[t("form",{class:"mb-3",onSubmit:s[6]||(s[6]=p(a=>g(c).push({name:"gigachat"}),["prevent"]))},[r(t("input",{class:"form-control mb-3",type:"text",required:"","onUpdate:modelValue":s[3]||(s[3]=a=>e.value.gigaUsername=a),placeholder:"Enter username"},null,512),[[h,e.value.gigaUsername]]),t("div",C,[r(t("input",{class:"form-control",type:e.value.visible?"text":"password",autocomplete:"current-password",required:"","onUpdate:modelValue":s[4]||(s[4]=a=>e.value.gigaPassword=a),placeholder:"Enter password"},null,8,V),[[d,e.value.gigaPassword]]),t("span",$,[t("a",{role:"button",onClick:s[5]||(s[5]=a=>e.value.visible=!e.value.visible)},u(e.value.visible?"Hide":"Show"),1)])]),j],32)])),t("div",null,[t("a",{class:"btn btn-link",type:"button",onClick:s[7]||(s[7]=(...a)=>e.value.switchForm&&e.value.switchForm(...a))},u(e.value.authTypo==="auth"?"Enter with login/password":"Enter with authorization data"),1),q])])])]))}}),z=y(B,[["__scopeId","data-v-e4613a37"]]);export{z as default};