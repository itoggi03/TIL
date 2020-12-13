<template>
  <b-container class="bv-example-row mt-3">
    <b-row>
      <b-col>
        <h3>글목록</h3>
      </b-col>
    </b-row>
    <b-row class="mb-1">
      <b-col style="text-align: right;">
        <b-button variant="outline-primary" @click="writeArticle"
          >글쓰기</b-button
        >
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-table
          striped
          hover
          :items="items"
          :fields="fields"
          @row-clicked="viewArticle"
        >
        </b-table>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Vue from "vue";
import VueRouter from "vue-router";
import { listArticle } from '@/api/board'

Vue.use(VueRouter);

export default {
  name: "list",
  data() {
    return {
      fields: [
        { key: "articleno", label: "글번호", tdClass: "tdClass" },
        { key: "subject", label: "제목", tdClass: "tdSubject" },
        { key: "userid", label: "작성자", tdClass: "tdClass" },
        { key: "hit", label: "조회수", tdClass: "tdClass" },
        { key: "regtime", label: "작성일", tdClass: "tdClass" }
      ],
      items: []
    };
  },
  created() {
    let para = {
      pg: 1,
      spp: 20,
      key: '',
      word: '',
    }
    listArticle(
      para,
      (res) =>{
        this.items = res.data
      },
      (err) => {
        console.error(err);
      },
    )
  },
  methods: {
    writeArticle() {
      this.$router.push({ name: "board-register" });
    },
    viewArticle(item) {
      console.log(item.articleno + "글보자!!");
      this.$router.replace({
        name: "board-view",
        params: { articleno: item.articleno }
      });
      // this.$router.push({ path: `/board/view/${item.articleno}` });
    }
  }
};
</script>

<style scope>
.tdClass {
  width: 50px;
  text-align: center;
}
.tdSubject {
  width: 300px;
  text-align: left;
}
</style>
