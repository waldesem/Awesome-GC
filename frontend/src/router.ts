import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  routes: [
    {
      path: '/',
      component: () => import('./App.vue')
    },
    {
      path: '/auth',
      name: 'auth',
      component: () => import('./components/AuthPage.vue')
    },
    {
      path: '/gigachat',
      name: 'gigachat',
      component: () => import('./components/GigaPage.vue')
    },
    {
      path: '/:pathMatch(.*)*',  
      name: '404', 
      component: () => import('./components/NotPage.vue')
    }
  ],
  history: createWebHistory()
});

export default router;