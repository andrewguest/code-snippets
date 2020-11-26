### What this Dockerfile does:

1. Compiles your Vue app inside the Docker container.
2. Copies the contents of the new `build` directory into the `/usr/share/nginx/html` directory.
3. Copies in the customized `nginx.conf` file into the `/etc/nginx/conf.d` directory.
4. Exposes port 80 of the container.
5. Starts the nginx process.

### Expected project structure:

```
some_project/
  |- frontend/
    |- nginx/
        |- nginx.conf
    |- src/
    |- public/
    |- Dockerfile
    |- package.json
```
