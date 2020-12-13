import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store";
import Home from "../views/Home.vue";
import Join from "../views/user/Join.vue";
import Login from "../views/user/Login.vue";
import Board from "../views/Board.vue";

Vue.use(VueRouter);

// https://router.vuejs.org/kr/guide/advanced/navigation-guards.html
const onlyAuthUser = async (to, from, next) => {
  let token = localStorage.getItem("access-token");
  if (store.state.userInfo == null && token) {
    await store.dispatch("GET_MEMBER_INFO", token);
  }
  if (store.state.userInfo === null) {
    alert("로그인이 필요한 페이지입니다..");
    // next({ name: "login" });
    router.push({ name: "login" });
  } else {
    next();
  }
};

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/join",
    name: "join",
    component: Join
  },
  {
    path: "/login",
    name: "login",
    component: Login
  },
  {
    path: "/mypage",
    name: "mypage",
    beforeEnter: onlyAuthUser,
    component: () => import("@/views/user/MyPage.vue")
  },
  {
    name: "board",
    path: "/board",
    component: Board,
    children: [
      {
        path: "",
        name: "board-list",
        component: () => import("@/components/board/List.vue")
      },
      {
        path: "register",
        name: "board-register",
        beforeEnter: onlyAuthUser,
        component: () => import("@/components/board/Register.vue")
      },
      {
        path: "detail/:articleno",
        name: "board-view",
        beforeEnter: onlyAuthUser,
        component: () => import("@/components/board/Detail.vue")
      },
      {
        path: "modify/:articleno",
        name: "board-modify",
        beforeEnter: onlyAuthUser,
        component: () => import("@/components/board/Modify.vue")
      }
    ],
    redirect: () => {
      return "/board";
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  duplicateNavigationPolicy: "ignore"
});

export default router;
