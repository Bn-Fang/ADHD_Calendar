import dotenv
import os
import canvasapi
import collections
from datetime import datetime  # Correct import statement
import pytz

def canvasHelper():
    # Load environment variables
    dotenv.load_dotenv(dotenv.find_dotenv())

    # Retrieve the Canvas API token and base URL from environment variables
    TOKEN = os.environ.get('CANVAS_API_TOKEN')
    BASEURL = 'https://umich.instructure.com'

    # Initialize a new Canvas object
    canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

    # Get a list of active courses
    courses = canvas_api.get_courses(enrollment_state='active')

    # A dictionary that maps each course to its pending assignments
    task_list = collections.defaultdict(list)
    # Iterate through each courses
    for course in courses:
        # Print course information, just for reference and debugging purposes
        print(f"Course ID: {course.id}, Name: {course.name}")
        # Get assignments for the course
        assignments = course.get_assignments()
        # Get the Eastern Standard Time (EST) timezone
        est_timezone = pytz.timezone('US/Eastern')
        now = datetime.now(tz = est_timezone)
        # List to store pending assignments
        pending_assignments = []

        # Iterate through the assignments
        for assignment in assignments:
            # Check if an assignment has a due date
            if assignment.due_at:
                # Parse due date
                due_date = datetime.strptime(assignment.due_at, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc).astimezone(est_timezone)
                # If the due date is in the future, the assignment is pending
                if due_date > now:
                    assignment_info = {
                        "name": assignment.name,
                        "due_date": due_date,
                        "url": assignment.html_url
                    }
                    pending_assignments.append(assignment_info)
        # Each Course mapped to a list of assignments in the form of a dictionary containing assignment name, due_date in utc, and url
        task_list[course.name] = pending_assignments

    print(task_list)
    return task_list


