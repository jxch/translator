docker buildx build --platform=linux/arm64,linux/amd64 -t jxch/translator:$(Get-Date -Format 'yyyyMMddHH') -t jxch/translator:latest . --push
