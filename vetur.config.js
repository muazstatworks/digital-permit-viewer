module.exports = {
  settings: {
    "vetur.useWorkspaceDependencies": true,
    "vetur.experimental.templateInterpolationService": true,
  },
  projects: [
    {
      root: "./frontend",
      package: "./package.json",
      jsconfig: "./jsconfig.json",
    },
  ],
};