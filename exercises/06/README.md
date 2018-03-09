## Exercise 6 (5 minutes)
1) Using a manifest file for all configuration (so you should only type `cf push`), deploy the docker container referenced on screen to PaaS with the following configuration:
    * 1 instance
    * 128MB of RAM
    * 256MB of disk space
    * A name of the format `<INITIALS>-app`
    * A route of the format `<INITIALS>-app.cloudapps.digital`
    * A HTTP healthcheck on the `/_status` endpoint
    * A startup command of `FLASK_APP=run.py flask run --host 0.0.0.0 --port $PORT`
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
