# File: installing flask from pip3

Package { 'flask':
  ensure   => 'V2.1.0',
  provider => 'pip3',
}
Package { 'Werkzeug':
  ensure   => 'V2.1.1',
  provider => 'pip3',
}
