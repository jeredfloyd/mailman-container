FROM ubi8/nginx-120
USER 0
RUN yum module -y disable php; yum module -y enable python39
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm; yum --enablerepo=codeready-builder-for-rhel-8-x86_64-rpms install -y postfix sassc python39-pip lynx python39-wheel python39-PyMySQL sudo; yum clean all; mkdir /etc/mailman3

# Fixup nginx SSL config
COPY ssl.conf /opt/app-root/etc/nginx.d/ssl.conf
COPY dummy.crt /etc/pki/tls/certs/dummy.crt
COPY dummy.key /etc/pki/tls/private/dummy.key

# Configure postfix
COPY main.cf master.cf /etc/postfix
COPY sudoers /etc/sudoers.d/default

# Install mailman
USER 1001
ENV PATH="$HOME/.local/bin:$PATH"
COPY bashrc $HOME/.bashrc
COPY mailman-run mailman-upgrade $HOME
RUN pip3 install mailman==3.3.9 mailman-web==0.0.8 mailman-hyperkitty==1.2.1 hyperkitty==1.3.8 postorius==1.3.10 django-mailman==1.3.11

# Patch list defaults
COPY base.py $HOME/.local/lib/python3.9/site-packages/mailman/styles
