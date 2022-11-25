/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  image:{
    domains:['lh3.googleusercontent.com']
  }
}

module.exports = nextConfig
