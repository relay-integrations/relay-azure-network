FROM relaysh/core:latest-python
RUN ["/bin/bash", "-c", "apk --no-cache add --virtual=relay-azure-build-deps \\\n    gcc \\\n    musl-dev \\\n    libffi-dev \\\n    make \\\n    openssl-dev    rust \\\n    cargo \u0026\u0026 \\\n  pip install azure-common azure-mgmt-compute azure-mgmt-network azure-mgmt-storage msrestazure azure-identity \u0026\u0026 \\\n  apk del relay-azure-build-deps\n"]
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Delete Azure Load Balancers"
LABEL "org.opencontainers.image.description"="This task deletes a provided list of Azure Load Balancers"
LABEL "com.puppet.nebula.sdk.version"="v1"
