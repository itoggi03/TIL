<template>
  <b-row class="mb-3 mt-2">
    <b-col cols="11">
      <b-form-textarea
        id="content"
        placeholder="댓글 입력..."
        rows="2"
        v-model="form.comment"
        @submit="onSubmit"
      ></b-form-textarea>
    </b-col>
    <b-col><b-button @click="onSubmit" variant="dark">댓글등록</b-button> </b-col>
  </b-row>
</template>

<script>
import { registerMemo } from '@/api/memo'
import { mapState } from 'vuex'

export default {
  name: "memowrite",
  data () {
    const articleno = Number(this.$route.params.articleno);
    return {
      form: {
        articleno: articleno,
        comment: "",
        memono: "",
        memotime: "",
        userid: ""        
      }
    }
  },
  computed: {
    ...mapState(['userInfo'])
  },
  methods: {
    onSubmit (event) {
      event.preventDefault()
      this.form.userid = this.userInfo.userid
      registerMemo(
        this.form,
        (res) => {
          console.log(res);
          this.$emit('regMemo')
        },
        (err) => {
          console.error(err);
        }
      )
    }
  }
};
</script>

<style></style>
