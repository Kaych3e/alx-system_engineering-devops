# Script to increase the number of login attempts by a user
# change number of hard limit
exec { 'change_hard_value_to_55':
  command => "/bin/sed -i 's/5/55/g' /etc/security/limits.conf",
}

# change number of soft limit
exec { 'change_soft_value_to_44':
  command => "/bin/sed -i 's/4/44/g' /etc/security/limits.conf",
}
