FROM python:3.12-alpine

LABEL org.opencontainers.image.title="Free Compute Proof"
LABEL org.opencontainers.image.description="Tiny proof image built on free GitHub Actions compute."
LABEL org.opencontainers.image.source="https://github.com/codewithx55/free-compute-actions-claim"

WORKDIR /app
COPY proof.py /app/proof.py

CMD ["python", "/app/proof.py"]
