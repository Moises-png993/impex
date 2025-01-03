const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/IndexPage.vue") },
      { path: "/s", component: () => import("pages/ConsultaPage.vue") },
      { path: "/c", component: () => import("pages/CumplimientoPage.vue") },
      { path: "/t", component: () => import("pages/TungyaPage.vue") },
      { path: "/cont", component: () => import("pages/ContenedorPage.vue") },
      { path: "/u", component: () => import("pages/UploadPage.vue") },
      { path: "/menu", component: () => import("pages/MenuPage.vue") },
      {
        path: "/exportaciones",
        component: () => import("pages/ExportacionesPage.vue"),
      },
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
