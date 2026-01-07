from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import uuid

tasks = {}
VALID_STATUSES = {"pending", "in_progress", "completed"}


def current_timestamp():
    return datetime.utcnow().isoformat()

def validate_task(data, is_update=False):
    errors = []

    title = data.get("title")
    description = data.get("description")
    task_status = data.get("status")

    if not is_update or title is not None:
        if not isinstance(title, str) or not (3 <= len(title) <= 100):
            errors.append("title must be a string between 3 and 100 characters")

    if description is not None:
        if not isinstance(description, str) or len(description) > 500:
            errors.append("description must be at most 500 characters")

    if task_status is not None:
        if task_status not in VALID_STATUSES:
            errors.append("status must be one of pending, in_progress, or completed")

    return errors


@api_view(["GET", "POST"])
def tasks_collection(request):

    if request.method == "POST":
        data = request.data
        errors = validate_task(data)
        if errors:
            return Response({"error": errors}, status=status.HTTP_400_BAD_REQUEST)

        task_id = str(uuid.uuid4())
        now = current_timestamp()

        task = {
            "id": task_id,
            "title": data["title"],
            "description": data.get("description", ""),
            "status": data.get("status", "pending"),
            "created_at": now,
            "updated_at": now,
        }

        tasks[task_id] = task
        return Response(task, status=status.HTTP_201_CREATED)

    status_filter = request.query_params.get("status")

    if status_filter and status_filter not in VALID_STATUSES:
        return Response(
            {"error": "Invalid status filter"},
            status=status.HTTP_400_BAD_REQUEST
        )

    result = list(tasks.values())
    if status_filter:
        result = [t for t in result if t["status"] == status_filter]

    return Response(result, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def task_item(request, task_id):

    task = tasks.get(task_id)
    if not task:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(task, status=status.HTTP_200_OK)

    if request.method == "PUT":
        data = request.data
        errors = validate_task(data, is_update=True)
        if errors:
            return Response({"error": errors}, status=status.HTTP_400_BAD_REQUEST)

        task["title"] = data.get("title", task["title"])
        task["description"] = data.get("description", task["description"])
        task["status"] = data.get("status", task["status"])
        task["updated_at"] = current_timestamp()

        return Response(task, status=status.HTTP_200_OK)

    del tasks[task_id]
    return Response(status=status.HTTP_204_NO_CONTENT)
