from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    topics = models.ManyToManyField(Topic, through='TodoTopic')

    def __str__(self):
        return self.title

class TodoTopic(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.todo.title} - {self.topic.name}"