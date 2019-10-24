const path = require('path');
// eslint-disable-next-line no-unused-vars
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: './static/js/index',
  output: {
    path: path.resolve('./static/bundles/'),
    filename: '[name]-[hash].js',
  },

  plugins: [
    new BundleTracker({
      filename: './webpack-stats.json',
    }),
  ],
};
