FROM sreflaschenpost/flaschenpost-sre-challenge:latest

# Set a working directory
WORKDIR /app

# Create non-root user for security best practices
RUN addgroup -g 1000 appgroup && \
    adduser -D -u 1000 -G appgroup appuser && \
    chown -R appuser:appgroup /app

# Add the option for custom files 
# COPY --chown=appuser:appgroup src/ /app/

# Switch to non-root user
USER appuser

# Expose port 80 to server HTTP traffic
EXPOSE 80

# Use the default CMD/ENTRYPOINT provided by the base image
# ENTRYPOINT ["executable"]
# CMD ["python3", "app.py"]