<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand
        ><router-link :to="{ name: 'home' }" class="link"
          ><img
            src="@/assets/nav_logo.png"
            class="d-inline-block align-middle"
            width="60px"
            alt="Kitten"
          />
          SSAFY</router-link
        >
      </b-navbar-brand>
      <!-- <b-navbar-brand href="/">SSAFY</b-navbar-brand> -->

      <b-navbar-nav class="ml-auto">
        <b-nav-item>
          <router-link :to="{ name: 'board-list' }" class="link"
            >게시판</router-link
          ></b-nav-item
        >
      </b-navbar-nav>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto" v-if="userInfo !== null">
          <b-nav-item
            ><b-avatar
              variant="primary"
              v-text="userInfo ? userInfo.userid.charAt(0).toUpperCase() : ''"
            ></b-avatar
            >{{ userInfo.username }}({{ userInfo.userid }})님
            환영합니다.</b-nav-item
          >
          <b-nav-item
            ><router-link :to="{ name: 'mypage' }" class="link"
              >내정보보기</router-link
            ></b-nav-item
          >
          <b-nav-item class="link" @click.prevent="onClickLogout"
            >로그아웃</b-nav-item
          >
          <!-- <b-nav-item href="/me">내정보보기</b-nav-item>
            <b-nav-item href="/logout">로그아웃</b-nav-item> -->
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto" v-else>
          <b-nav-item>
            <router-link :to="{ name: 'login' }" class="link"
              >로그인</router-link
            ></b-nav-item
          >
          <b-nav-item
            ><router-link :to="{ name: 'join' }" class="link"
              >회원가입</router-link
            ></b-nav-item
          >
          <!-- <b-nav-item href="/login">로그인</b-nav-item>
            <b-nav-item href="/join">회원가입</b-nav-item> -->
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "navi",
  computed: {
    ...mapState(["userInfo", "isLogin"])
  },
  methods: {
    onClickLogout() {
      this.$store
        .dispatch("LOGOUT")
        .then(() => {
          // this.$router.push({ name: "" });
          if (this.$route.path !== "/") this.$router.replace("/");
        })
        .catch(() => {
          console.log("로그아웃 문제!!!");
        });
    }
  }
};
</script>

<style scoped>
.link {
  color: azure;
}

.link:hover {
  color: cyan;
  text-decoration-line: none;
}
</style>
