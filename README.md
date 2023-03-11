# How to Run

`docker-compose build`<br>
`docker-compose up`

# How to Use

App runs on localhost:8000.<br>
`Filter`, `Pagination` and `Search` fields are shown in Django Form returned by server.<br>
`Model` fields for creating and updating models are shown in the Form as well.<br>
`Date-Time` field for querying historical data **IS NOT** provided in the Form and needs to be entered by hand. See `tasks/` endpoint.

# Endpoints

`/users/`
  - GET: Returns a list of all users.

`/users/register`
  - POST: Registers a new user.<br>

`/users/login`
  - POST: Logs in a user and returns authentication keys. Cookies are also set for the authentication middleware.
 
`/users/logout`
  - GET: Logs out the user, redirects to `/users/`, invalidates the token, clears authentication cookies.

`/users/<id>`
  - GET: Retrieves the details of a user.
  - PUT: Updates the details of a user.
  - DELETE: Deletes a user.<br>

`/tasks/`
  - GET: Retrieves a list of tasks. Use url queryparam `as_of=YYYY-MM-DD-HH:MM:SS` for historical data.

`/tasks/<id>`
  - GET: Retrieves task detail. Use url queryparam `as_of=YYYY-MM-DD-HH:MM:SS` for historical data.
  - PUT: Updates task detail.
  - DELETE: Deletes a task.<br>

`/tasks/changes`
  - GET: Retrieves a list of changes of all tasks.<br>
 
`/tasks/<id>/changes`
  - GET: Retrieves a list of changes of a single task.
