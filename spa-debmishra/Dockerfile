# Step 1: Use a lightweight Node.js image to build the project
FROM node:18-alpine AS buildweb

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

# Expose the port for the application
EXPOSE 8080