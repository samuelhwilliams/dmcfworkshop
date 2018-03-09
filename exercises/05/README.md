## Exercise 5 (5 minutes)
1) Using `cf push` flags (i.e. no manifest file), deploy the contents of the `app` directory as a static application with the following configuration:
    * Static buildpack
    * 2 instances
    * RAM: 64MB
    * Disk: 64MB
    * Name: `<INITIALS>-app`
    * Route: `<INITIALS>-app.cloudapps.digital`
    * No healthcheck
2) Once you're able to connect to your app in a browser, you're done.

## Available commands
* `cf login`
* `cf logout`
* `cf orgs`
* `cf org-users`
* `cf spaces`
* `cf target`
* `cf apps`
* `cf app`
* `cf env`
* `cf set-env`
* `cf start`
* `cf stop`
* `cf restart`
* `cf restage`
* `cf delete`
* `cf marketplace`
* `cf services`
* `cf create-service`
* `cf bind-service`
* `cf unbind-service`
* `cf delete-service`
* `cf domains`
* `cf routes`
* `cf map-route`
* `cf unmap-route`
* `cf push`
