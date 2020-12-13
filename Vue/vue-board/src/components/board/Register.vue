<template>
  <b-container class="bv-example-row mt-3">
    <b-row>
      <b-col>
        <h3>글쓰기</h3>
      </b-col>
    </b-row>
    <b-row class="mb-1">
      <b-col style="text-align: left;">
        <b-form @submit="onSubmit" @reset="onReset">
          <b-form-group
            id="subject-group"
            label="제목:"
            label-for="subject"
            description="제목을 입력하세요."
          >
            <b-form-input
              id="subject"
              v-model="form.subject"
              type="text"
              required
              placeholder="제목 입력..."
            ></b-form-input>
          </b-form-group>

          <b-form-group id="content-group" label="내용:" label-for="content">
            <b-form-textarea
              id="content"
              v-model="form.content"
              placeholder="내용 입력..."
              rows="10"
              max-rows="15"
            ></b-form-textarea>
          </b-form-group>

          <b-button type="submit" variant="primary" class="m-1"
            >글작성</b-button
          >
          <b-button type="reset" variant="danger" class="m-1">취소</b-button>
        </b-form>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { registerArticle } from '@/api/board'
import { mapState } from "vuex"

export default {
  name: "register",
  data() {
    return {
      form: {
        userid: "",
        subject: "",
        content: ""
      }
    };
  },
  computed: {
    ...mapState(['userInfo'])
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      this.form.userid = this.userInfo.userid
      registerArticle(
        this.form,
        (res) => {
          console.log(res);
          this.$router.push({ name: "board-list" })
        }, 
        (err) => {
          console.error(err)
        }
      )
    },
    onReset(event) {
      event.preventDefault();
      this.form.subject = "";
      this.form.content = "";
      this.$router.push({ name: "board-list" });
    }
  }
};
</script>

<style></style>
