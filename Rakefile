#!/usr/bin/env ruby
require 'rubygems'

VERSION_STRING = ENV['VERSION'] || File.read('VERSION').chomp

namespace :version do
  desc "Bump the version number in the VERSION and dydra/__init__.py files"
  task :bump do
    new_version_string = VERSION_STRING.split('.').map(&:to_i)
    old_version_tiny   = new_version_string[-1]
    new_version_tiny   = old_version_tiny + 1
    new_version_string[-1] = new_version_tiny
    new_version_string = new_version_string.map(&:to_s).join('.')
    sh "echo '#{new_version_string}' > VERSION"
    sh "sed -i '' 's/#{VERSION_STRING}/#{new_version_string}/' dydra/__init__.py"
    sh "git commit -m 'Bumped the version to #{new_version_string}.' VERSION dydra/__init__.py"
  end

  desc "Tag the current revision as release #{VERSION_STRING}"
  task :tag do
    sh "git tag -s #{VERSION_STRING} -m 'Released version #{VERSION_STRING}.'"
  end
end

desc "Build the dist/dydra-#{VERSION_STRING}.* packages"
task :build => :package

desc "Build the dist/dydra-#{VERSION_STRING}.tar.gz, dist/dydra-#{VERSION_STRING}.tar.bz2, and dist/dydra-#{VERSION_STRING}.zip packages"
task :package => 'VERSION' do
  sh "python setup.py sdist --formats=gztar,bztar,zip"
end

desc "Regenerate the MANIFEST file"
task :manifest => 'MANIFEST.in' do
  sh "python setup.py sdist --manifest-only"
end

desc "Push the dist/dydra-#{VERSION_STRING}.* packages to PyPI"
task :push do
  sh "python setup.py sdist --formats=gztar,bztar,zip upload"
end
