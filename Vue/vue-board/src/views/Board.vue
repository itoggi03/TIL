<template>
  <div>
    <navi />
    <router-view></router-view>
  </div>
</template>

<script>
import Navi from "@/components/common/Navi";

export default {
  name: "board",
  components: {
    Navi
  }
};
</script>
