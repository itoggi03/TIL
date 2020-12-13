<template>
  <b-row class="mb-1">
    <b-col>
      <b-card border-variant="info" class="mb-2" no-body>
        <template>
          <b-row class="m-1">
            <b-col class="text-left ml-3"
              ><strong>{{ memo.userid }}</strong> {{ memo.memotime }}
            </b-col>
            <b-col class="text-right mr-3">
              <b-button @click="modify" variant="link">수정</b-button>
              <b-button variant="link">삭제</b-button>
            </b-col>
          </b-row>
        </template>
        <b-card-body class="text-left">
          <div>
            {{ memo.comment }}
          </div>
        </b-card-body>
      </b-card>
    </b-col>
  </b-row>
</template>

<script>
import { modifyMemo } from '@/api/memo'

export default {
  name: "memorow",
  props: {
    memo: Object
  }

};
</script>

<style></style>
