from django.db import models
from .QuestionChangelog import QuestionChangelog
from .QuestionTopic import QuestionTopic
from .QuestionType import QuestionType
from django.dispatch import receiver
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import pre_save, post_save, pre_delete
from django.core.validators import MaxValueValidator, MinValueValidator


class Question(models.Model):
    # Foreign Keys
    topic = models.ManyToManyField(QuestionTopic, blank=True)
    forked_from = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    last_editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='last_editor')

    # Regular Fields
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=256)
    instruction = models.CharField(max_length=256)
    difficulty = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)
    version = models.PositiveIntegerField(editable=False)
    student_test = models.BooleanField(default=False)

    @property
    def track_fields(self):
        return ('topic',
                'forked_from',
                'type',
                'author',
                'last_editor',
                'name',
                'description',
                'instruction',
                'difficulty',
                'create_date',
                'last_modified_date',
                'version',
                'student_test',)

    def user_save(self, user, *args, **kwargs):
        #print("test")
        self.last_editor = user
        if not self.id:
            self.version = 1
        else:
            self.version += 1
        super(Question, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        #print("test")
        if not self.id:
            self.version = 1
        else:
            self.version += 1
        super(Question, self).save(*args, **kwargs)
        

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Question)
def question_pre_save(sender, instance, **kwargs):
    #Updating
    #print(instance.last_editor)
    if instance.id:
        prev_question = Question.objects.get(pk=instance.id)
        field_track = {}
        for field in instance.track_fields:
            value = getattr(instance, field)
            orig_value = getattr(prev_question, field)
            if value != orig_value:
                field_track[field] = [orig_value, value]

        if field_track:
            note_str = 'Question Update {\n'
            for k, v in field_track.items():
                note_str += ('{field} : {orig_value} -> {value}\n').format(
                    field=k,
                    orig_value=v[0],
                    value=v[1],
                )
            note_str += '}'
            c = QuestionChangelog(
                question = instance,
                user = instance.last_editor,
                change_set = note_str,
                previous_version = field_track.get('version')[0],
            )
            c.save()
            print(note_str)
        
        
@receiver(post_save, sender=Question)
def question_post_save(sender, instance, created, **kwargs):
    if created:
        note_str = 'Question Created'
        c = QuestionChangelog(
            question = instance,
            user = instance.last_editor,
            change_set = note_str,
            previous_version = 0,
        )
        c.save()
        print(note_str)

@receiver(pre_delete, sender=Question)
def question_pre_delete(sender, instance, **kwargs):
    note_str = getattr(getattr(instance, 'last_editor'), 'username') + ' deleted ' + getattr(instance, 'name')
    c = QuestionChangelog(
        user = instance.last_editor,
        change_set = note_str,
        previous_version =  getattr(instance, 'version'),
    )
    c.save()
    print(note_str)
