# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/debian/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/base:debian-11

# Install Pandoc and TeX Live for PDF generation via LuaLaTeX
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    pandoc \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-luatex \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-lang-all \
    librsvg2-bin \
    make \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*
