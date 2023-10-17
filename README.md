# mailman-container
A simple container for deploying Mailman3

This is a barebones container that includes Postfix as an inbound
delivery agent and the Mailman 3 components.  I'm providing this as an
example for others so they don't have to start from scratch.

Some notes:

* The example systemd unit file will listen on port 25 for incoming
  mail and 443 for HTTPS access to the UI.

* The files dummy.crt/dummy.key must be provided; these can be a valid
  TLS certificate for the deployed hostname, or a self-signed cert for
  deploying behind an inbound proxy.

* An external MariaDB instance is expected; it is not included in this
  container.

* 'myhost' and 'myorigin' must be updated in main.cf to match your
  install.

* 'mailman-crontab' should be copied to the host /etc/cron.d directory.

* This expects a container name of 'mailman' and directories
  /srv/mailman/config, /srv/mailman/logs and /srv/mailman/mailman

* Example config files are provided.

  