shipdock
========

A docker-based build framework and continuous-integration system which
runs builds in isolated containers.

In simple cases, shipbuilder acts as a drop-in replacement for Travis CI.
It will read either its own `.ship.yml` config file or `.travis.yml`.
Ease of migration from Travis is a goal but 100% compatibility is currently
not.

