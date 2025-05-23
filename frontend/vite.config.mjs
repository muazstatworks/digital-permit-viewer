import { fileURLToPath, URL } from "node:url";

import { PrimeVueResolver } from "@primevue/auto-import-resolver";
import vue from "@vitejs/plugin-vue";
import Components from "unplugin-vue-components/vite";
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
    base: '/digital-permit/',
    optimizeDeps: {
        noDiscovery: true,
    },
    plugins: [
        vue(),
        Components({
            resolvers: [PrimeVueResolver()],
        }),
    ],
    resolve: {
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
    },
    server: {
        proxy: {
            "/digital-permits": {
                target: "https://vertex.gamuda.com.my",
                changeOrigin: true,
                secure: false, // Disable if the API uses self-signed certificates
                headers: {
                    Accept: "application/json",
                }
            },
        },
    },
});
