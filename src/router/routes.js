const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/IndexPage.vue") },
      { path: "/s", component: () => import("pages/ConsultaPage.vue") },
      { path: "/c", component: () => import("pages/CumplimientoPage.vue") },
      { path: "/t", component: () => import("pages/TungyaPage.vue") },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
