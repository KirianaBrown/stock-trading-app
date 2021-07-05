from flask_assets import Bundle

bundles = {
  'all_css': Bundle(
    'css/style.css',
    'scss/main.scss',
    filters='libsass',
		# depends='scss/*.scss, css/*.css',
    depends='**/*.scss',
    output="gen/all.css",
    extra={'rel': 'stylesheet/css'}
  )
}