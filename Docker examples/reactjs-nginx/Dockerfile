###############
# React image #
###############
FROM node:current-alpine as build

WORKDIR /app

# add app
COPY . /app

# install app dependencies
RUN yarn add package.json

# compile the React app
RUN yarn run build

###############
# Nginx image #
###############
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

# start nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
