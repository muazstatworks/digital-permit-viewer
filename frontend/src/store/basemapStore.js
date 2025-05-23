import { streetMap, imageryMap } from "@/utils/basemap";
import { defineStore } from "pinia";

// NOTE: Options to change default basemap
// world-imagery
// hybrid
// osm
// street
// satellite
// topo
// gray
// dark-gray
// oceans

export const useBasemapStore = defineStore("basemap", {
  state: () => ({
    currentBasemapId: "satellite", // Default basemap ID
  }),
  actions: {
    setBasemap(id) {
      this.currentBasemapId = id;
    },
  },
});

