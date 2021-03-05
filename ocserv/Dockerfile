FROM alpine:3.10

MAINTAINER Tommy Lau <tommy@gen-new.com>

ENV OC_VERSION=0.12.1
RUN echo http://mirrors.aliyun.com/alpine/v3.10/main/ > /etc/apk/repositories && \
    echo http://mirrors.aliyun.com/alpine/v3.10/community/ >> /etc/apk/repositories
#ADD server-cert.pem /etc/ocserv/certs/server-cert.pem
#ADD server-key.pem /etc/ocserv/certs/server-key.pem

RUN buildDeps=" \
		curl \
		g++ \
		gnutls-dev\
		gpgme \
		libev-dev \
		libnl3-dev \
		libseccomp-dev \
		linux-headers \
		linux-pam-dev \
		lz4-dev \
		libseccomp \
		lz4-libs \
		libev \
		make \
		readline-dev \
		tar \
		xz \
		gnutls-utils iptables libnl3 readline \
	"; \
	set -x \
	&& apk update &&  apk add --update  $buildDeps

# configuration lz4
#RUN mkdir -p /temp && cd /temp \
#    && wget http://10.1.34.13:8081/tools/lz4-1.9.3.tar.gz \
#    && tar xvf lz4-1.9.3.tar.gz \
#    && cd lz4-1.9.3 \
#    && make install \
#    && ln -sf /usr/local/lib/liblz4.* /usr/lib/ \
#    && cd / && rm -rf /temp



RUN	 curl -SL  "http://10.1.34.13:8081/tools/ocserv-1.0.0.tar.xz" -o ocserv.tar.xz \
	&& mkdir -p /usr/src/ocserv \
	&& tar -xf ocserv.tar.xz -C /usr/src/ocserv --strip-components=1 \
	&& rm ocserv.tar.xz* \
	&& cd /usr/src/ocserv \
	&& ./configure \
	&& make \
	&& make install \
	&& mkdir -p /etc/ocserv \
	&& mkdir -p /etc/ocserv/config-per-group\
	&& cd / \
	&& rm -fr /usr/src/ocserv \
	&& runDeps="$( \
		scanelf --needed --nobanner /usr/local/sbin/ocserv \
			| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
			| xargs -r apk info --installed \
			| sort -u \
		)" \
	&& rm -rf /var/cache/apk/*

# Setup config
#COPY groupinfo.txt /tmp/
#RUN set -x \
#	&& sed -i 's/\.\/sample\.passwd/\/etc\/ocserv\/ocpasswd/' /etc/ocserv/ocserv.conf \
#	&& sed -i 's/\(max-same-clients = \)2/\110/' /etc/ocserv/ocserv.conf \
#	&& sed -i 's/\.\.\/tests/\/etc\/ocserv/' /etc/ocserv/ocserv.conf \
#	&& sed -i 's/#\(compression.*\)/\1/' /etc/ocserv/ocserv.conf \
#	&& sed -i '/^ipv4-network = /{s/192.168.1.0/192.168.99.0/}' /etc/ocserv/ocserv.conf \
#	&& sed -i 's/192.168.1.2/8.8.8.8/' /etc/ocserv/ocserv.conf \
#	&& sed -i 's/^route/#route/' /etc/ocserv/ocserv.conf \
#	&& sed -i 's/^no-route/#no-route/' /etc/ocserv/ocserv.conf \
#	&& sed -i '/\[vhost:www.example.com\]/,$d' /etc/ocserv/ocserv.conf \
#	&& mkdir -p /etc/ocserv/config-per-group \
#	&& cat /tmp/groupinfo.txt >> /etc/ocserv/ocserv.conf \
#	&& rm -fr /tmp/groupinfo.txt

ADD ocserv.conf /etc/ocserv/ocserv.conf

WORKDIR /etc/ocserv

COPY Route /etc/ocserv/config-per-group/Route

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 443
CMD ["ocserv", "-d 1", "-c", "/etc/ocserv/ocserv.conf", "-f"]
