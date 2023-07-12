import router from "@/router";
export default function () {
  router.addRoute({
    path: "/extension_template/my_page",
    name: "extension_template_my_page",
    meta: {
      requiresAuth: true,
    },
    component: () => import("./components/MyComponent.vue"),
  });
}
