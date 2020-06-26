from django.db import models

# Create your models here.

# program table 
class Program(models.Model):
    programTitle = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.programTitle
    
    @property
    def choices(self):
        return self.choice_set.all()


# course table
class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseName = models.TextField(null=False, blank=False)
    program = models.ForeignKey(Program, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseName

    @property
    def choices(self):
        return self.choice_set.all()

# notes table
class Notes(models.Model):
    noteID = models.AutoField(primary_key=True)
    noteTitle = models.TextField(null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    publisher = models.TextField(default='Unknow')

    def __str__(self):
        return self.noteTitle

    @property
    def choices(self):
        return self.choice_set.all()

#publisher table
class Publisher(models.Model):
    publisherID = models.AutoField(primary_key=True)
    publisherName = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.publisherName

    @property
    def choices(self):
        return self.choice_set.all()
