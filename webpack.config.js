const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: './static/js/index',
  output: {
    path: path.resolve('./static/webpack_bundles/'),
    filename: '[name]-[hash].js',
  },

  plugins: [
    new BundleTracker({
      filename: './webpack-stats.json',
    }),
  ],
};
