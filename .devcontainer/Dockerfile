FROM ubuntu:20.04

# 必要なパッケージをインストール
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y \
    binutils \
    build-essential \
    wget \
    strace \
    git \
    tzdata \
    sysstat \
    python3-matplotlib \
    python3-pil \
    fonts-takao \
    fio \
    qemu-kvm \
    virt-manager \
    libvirt-clients \
    virtinst \
    jq \
    docker.io \
    containerd \
    psmisc \
    libvirt-daemon-system && \
    ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    apt clean && rm -rf /var/lib/apt/lists/*

# USER test
# Go の公式バイナリをインストール
RUN wget https://go.dev/dl/go1.21.1.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.21.1.linux-amd64.tar.gz && \
    rm go1.21.1.linux-amd64.tar.gz

# Go のパスを設定
ENV PATH="/usr/local/go/bin:${PATH}"

RUN apt update && apt install -y locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 && \
    export LANG=en_US.UTF-8

RUN adduser `id -un` libvirt && \
    adduser `id -un` libvirt-qemu && \
    adduser `id -un` kvm