const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const VueLoader = require('vue-loader/lib/plugin');



module.exports = {
    //mode: 'development',
    mode: 'production',
    devtool: 'inline-source-map',
    entry: {
        main: './src/main.js',
    },
    output: {
        filename: '[name]-bundle.js',
        path: path.resolve(__dirname, 'static')
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.vue$/,
                use: ['vue-loader']
            },
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test: /(\.ttf$|\.woff$)/,
                use: ['file-loader']
            }
        ]
    },
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            title: 'html-webpack-plugin-test'
        }),
        new VueLoader()
    ],
    optimization: {
        splitChunks: {
            chunks: 'all',
        },
    },
}