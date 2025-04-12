# Step 1: Use a lightweight Node.js image to build the project
FROM node:18-alpine AS buildstage

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Vue.js project
RUN npm run build

# Production stage with Nginx
FROM nginx:alpine
COPY --from=buildstage /app/dist /usr/share/nginx/html
# Add custom nginx config if needed
# COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80