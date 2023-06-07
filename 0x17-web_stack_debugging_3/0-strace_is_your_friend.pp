# script to find out why Apache is returning a 500 error, fix and automate it
file { '/var/www/html/wp-settings.php':
  ensure => present,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php")
                            .gsub(/\.phpp/, ".php") %>'),
    }
