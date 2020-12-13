<template>
  <div>
    <navi />
    <b-container class="bv-example-row">
      <b-row>
        <b-col></b-col>
        <b-col cols="8">
          <b-card
            class="text-center mt-3"
            header-html="<h3>로그인</h3>"
            style="max-width: 40rem;"
            align="left"
          >
            <b-form class="text-left">
              <b-alert show variant="danger" v-if="isLoginError"
                >아이디 또는 비밀번호를 확인하세요.</b-alert
              >
              <b-form-group label="아이디:" label-for="userid">
                <b-form-input
                  id="userid"
                  v-model="user.userid"
                  required
                  placeholder="아이디 입력...."
                  @keyup.enter="confirm"
                ></b-form-input>
              </b-form-group>
              <b-form-group label="비밀번호:" label-for="userpwd">
                <b-form-input
                  type="password"
                  id="userpwd"
                  v-model="user.userpwd"
                  required
                  placeholder="비밀번호 입력...."
                  @keyup.enter="confirm"
                ></b-form-input>
              </b-form-group>
              <b-button
                type="button"
                variant="primary"
                class="m-1"
                @click="confirm"
                >로그인</b-button
              >
              <router-link :to="{ name: 'join' }">
                <b-button type="button" variant="success" class="m-1"
                  >회원가입</b-button
                >
              </router-link>
            </b-form>
          </b-card>
        </b-col>
        <b-col></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { login } from "@/api/user.js";
import Navi from "@/components/common/Navi";

export default {
  name: "login",
  components: {
    Navi
  },
  data() {
    return {
      user: {
        userid: null,
        userpwd: null
      },
      isLoginError: false
    };
  },
  methods: {
    confirm() {
      localStorage.setItem("access-token", "");
      login(
        this.user,
        (response) => {
          if (response.data.message === "success") {
            let token = response.data["access-token"];
            this.$store.commit("setIsLogined", true);
            localStorage.setItem("access-token", token);

            this.$store.dispatch("GET_MEMBER_INFO", token);
            this.$router.push("/");
          } else {
            this.isLoginError = true;
          }
        },
        (error) => {
          console.error(error);
          alert("아이디 또는 비밀번호가 일치하지 않습니다.");
        }
      );
    }
  }
};
</script>
