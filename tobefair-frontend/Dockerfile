FROM registry.access.redhat.com/ubi8/nodejs-20-minimal

# Create app directory
WORKDIR /usr/src/app

# Copy server files
COPY server/package.json .
COPY server/server.js .
COPY dist/frontend/browser ../dist/frontend/browser

USER root

# If you are building your code for production
RUN npm install --only=production

EXPOSE 42000

RUN curl -sf https://gobinaries.com/tj/node-prune | sh
RUN node-prune

USER 1001

CMD [ "node", "server.js" ]
