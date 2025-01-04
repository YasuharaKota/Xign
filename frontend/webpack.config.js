const path = require("path");
const webpack = require("webpack");

module.exports = {
   entry: "./src/index.js",
   output: {
       path: path.resolve(__dirname, "./static/frontend"),
       filename: "[name].js",
   },
   module: {
       rules: [
           {
               test: /\.js$/,
               exclude: /node_modules/,
               use: {
                   loader: "babel-loader",
               },
           },
           {
               // CSSファイルを処理するルールを追加
               test: /\.css$/i, // .cssファイルを対象
               use: ["style-loader", "css-loader"], // 適用されるローダー: 順に適用
           },
       ],
   },
   optimization: {
       minimize: true,
   },
   plugins: [
       new webpack.DefinePlugin({
           'process.env.NODE_ENV' : JSON.stringify('development')
       })
   ]
}