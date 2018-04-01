# GSuiteAuthentication-Django
Example Application for authenticating google users and accessing the google api.

Adapted from the flask example here: https://developers.google.com/api-client-library/python/auth/web-app

### Enable APIs for your project
Any application that calls Google APIs needs to enable those APIs in the API Console. To enable the appropriate APIs for your project:

1. Open the [Library](https://console.developers.google.com/apis/library) page in the API Console.
2. Select the project associated with your application. Create a project if you do not have one already.
3. Use the Library page to find each API that your application will use. Click on the Google Drive API and enable it for your project.

### Create authorization credentials
Any application that uses OAuth 2.0 to access Google APIs must have authorization credentials that identify the application to Google's OAuth 2.0 server. The following steps explain how to create credentials for your project. Your applications can then use the credentials to access APIs that you have enabled for that project.

1. Open the [Credentials](https://console.developers.google.com/apis/credentials) page in the API Console.
2. Click Create credentials > OAuth client ID.
3. Complete the form. Set the application type to Web application. You must specify authorized redirect URIs. The redirect URIs are the endpoints to which the OAuth 2.0 server can send responses. The callback URL for this application needs to be set to `http://127.0.0.1:8000/oauth2callback`
4. Download the credentials, rename the file to `client_secrets.json` and copy it into the project folder. 

### Running the application
1. Run `python manage.py migrate`
2. You may need to set the environment variable OAUTHLIB_INSECURE_TRANSPORT to True, the following code will do that on a linux style machine:
`export OAUTHLIB_INSECURE_TRANSPORT=TRUE`
3. Run the application with `python manage.py runserver`
