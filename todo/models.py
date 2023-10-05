from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = [ "is_done", "-deadline", "-created_at"]

    @property
    def get_short_tags(self):
        tags = self.tags.all()
        short_list = ", ".join(
            f"{tags}"
            for tags in tags[:2]
        )
        if len(tags) > 2:
            short_list += "..."
        return short_list

    def __str__(self):
        return (
            self.content[:30] + "..."
            if len(self.content) > 30
            else self.content
        )
