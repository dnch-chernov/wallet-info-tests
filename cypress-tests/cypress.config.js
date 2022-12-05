const { defineConfig } = require("cypress");

module.exports = defineConfig({
  video: false,
  e2e: {
    reporter: 'mochawesome',
    reporterOptions: {
      inlineAssets: true
    },
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
