import dotenv
import os
import canvasapi

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
BASEURL = 'https://umich.instructure.com'

# Canvas Object
canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

courses = canvas_api.get_courses(enrollment_state='active')

# Iterate through the courses and print their IDs and names
for course in courses:
    print(f"Course ID: {course.id}, Name: {course.name}")


