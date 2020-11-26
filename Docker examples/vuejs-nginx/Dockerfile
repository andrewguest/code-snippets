#############
# Vue image #
#############
FROM node:lts-alpine as build

WORKDIR /app/

COPY package*.json /app/

RUN npm install npm@latest -g
RUN npm install

# copy the rest of the files
COPY . /app/

# compile the Vue app
RUN npm run build

###############
# Nginx image #
###############
FROM nginx:stable-alpine

# copy the files from the Vue image above
COPY --from=build /app/dist /usr/share/nginx/html

# remove the default Nginx config file
RUN rm /etc/nginx/conf.d/default.conf

# copy in our custom Nginx config file
COPY nginx/nginx.conf /etc/nginx/conf.d

# start nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
