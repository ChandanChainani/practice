Issue:
```
Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    current directory: $HOME/.rvm/gems/ruby-2.7.2@6.1.6.1/gems/idn-ruby-0.1.0/ext
$HOME/.rvm/rubies/ruby-2.7.2/bin/ruby -I $HOME/.rvm/rubies/ruby-2.7.2/lib/ruby/2.7.0 -r
./siteconf20230207-1208520-14jywwp.rb extconf.rb
checking for -lidn... no
ERROR: could not find idn library!

  Please install the GNU IDN library or alternatively specify at least one
  of the following options if the library can only be found in a non-standard
  location:
    --with-idn-dir=/path/to/non/standard/location
        or
    --with-idn-lib=/path/to/non/standard/location/lib
    --with-idn-include=/path/to/non/standard/location/include

*** extconf.rb failed ***
Could not create Makefile due to some reason, probably lack of necessary
libraries and/or headers.  Check the mkmf.log file for more details.  You may
need configuration options.

Provided configuration options:
	--with-opt-dir
	--without-opt-dir
	--with-opt-include
	--without-opt-include=${opt-dir}/include
	--with-opt-lib
	--without-opt-lib=${opt-dir}/lib
	--with-make-prog
	--without-make-prog
	--srcdir=.
	--curdir
	--ruby=$HOME/.rvm/rubies/ruby-2.7.2/bin/$(RUBY_BASE_NAME)
	--with-idn-dir
	--without-idn-dir
	--with-idn-include
	--without-idn-include=${idn-dir}/include
	--with-idn-lib
	--without-idn-lib=${idn-dir}/lib
	--with-idnlib
	--without-idnlib

To see why this extension failed to compile, please check the mkmf.log which can be found here:

  $HOME/.rvm/gems/ruby-2.7.2@6.1.6.1/extensions/x86_64-linux/2.7.0/idn-ruby-0.1.0/mkmf.log

extconf failed, exit code 1

Gem files will remain installed in $HOME/.rvm/gems/ruby-2.7.2@6.1.6.1/gems/idn-ruby-0.1.0 for
inspection.
Results logged to
$HOME/.rvm/gems/ruby-2.7.2@6.1.6.1/extensions/x86_64-linux/2.7.0/idn-ruby-0.1.0/gem_make.out

An error occurred while installing idn-ruby (0.1.0), and Bundler cannot continue.
Make sure that `gem install idn-ruby -v '0.1.0' --source 'https://rubygems.org/'` succeeds before bundling.

In Gemfile:
  twitter-text was resolved to 3.1.0, which depends on
    idn-ruby
```

Solution:
https://stackoverflow.com/questions/50055812/error-while-bundle-install-for-idn-ruby
```
sudo apt-get install libidn11-dev libldap2-dev
```
