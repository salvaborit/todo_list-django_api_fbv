# To-do list in Django

## Usage

api/tasks/3 for data in http client <br>
api/tags.json for data in json format

## Endpoints

### GET

api/status/ for API status (running or not)
api/tasks/ for all tasks <br>
api/tasks/3 for task with id 3 <br>
api/tags/ for all tags <br>
api/tags/7 for tag with id 7 <br>
api/tags/3/tasks/ to get all tasks with tag id 3

### POST

api/tasks/ with body in json format <br>
api/tags/ with body in json format

### PUT

api/tasks/3 to modify task with json data <br>
api/tags/3 to modify tag with json data

### DELETE

api/tasks/3 to delete task instance <br>
api/tags/3 to delete task instance

# Misc

- Used function based views
