<!-- A custom Vue3 component. See https://vuejs.org/ -->

<template>
  {{ t("This is a custom component from the extension") }} 'extension_template'
</template>

<script setup lang="ts">
import { useMenuStore } from "@/stores/menu";
import { useI18n } from "vue-i18n";

const menuStore = useMenuStore();
menuStore.setTitle("My Component");

const { t } = useI18n();
</script>
