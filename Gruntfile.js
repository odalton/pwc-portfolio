// REFs: https://github.com/sindresorhus/grunt-sass

const sass = require('node-sass');

module.exports = function(grunt) {
  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    connect: {
      uses_defaults: {}
    },
    sass: {
      dev: {
        options: { 
          implementation: sass, 
          sourceMap: true
        },
        files: { 'src/static/css/main.css' : 'src/static/sass/main.scss' }
      },
      prod: {
        options: {
          implementation: sass, 
          sourceMap: false,
          outputStyle: 'compressed'
        },
        files: { 'src/static/css/main.css' : 'src/static/sass/main.scss' }
      }
    },
    watch: {
      css: {
        files: 'src/static/sass/*.scss',
        tasks: [ 'sass:dev' ],
        options: { livereload: false}
      }
    },
    uglify: {
      my_targets: {
        files: { 'src/static/js/main.min.js' : ['src/static/js/*.js'] }
      }
    }
  });
  // Load Grunt plugins
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  // Default task(s).
  grunt.registerTask('default', [
    // 'connect',
    'watch'
  ]);
  grunt.registerTask('lets-ship-it', [
    'sass:prod',
    'uglify'
  ]);
};