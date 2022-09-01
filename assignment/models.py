from django.db import models


class Scoring(models.Model):
    title = models.CharField(max_length=255)
    is_excluded = models.BooleanField(blank=True, null=True)
    is_patient_not_going_elsewhere = models.BooleanField(blank=True, null=True)
    fitness = models.TextField(blank=True, null=True)
    penalty = models.IntegerField()
    is_sex_ignored = models.BooleanField(blank=True, null=True)
    is_nursing_care_ignored = models.BooleanField(blank=True, null=True)
    is_department_ignored = models.BooleanField(blank=True, null=True)
    anti_keywords = models.JSONField(blank=True, null=True)
    internal_wards = models.JSONField(blank=True, null=True)
    surgery_wards = models.JSONField(blank=True, null=True)
    keywords = models.JSONField(blank=True, null=True)
    departments = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Scoring'


class Scoringallocations(models.Model):
    wards = models.JSONField(blank=True, null=True)
    rooms = models.JSONField(blank=True, null=True)
    is_open_to_other_patients = models.BooleanField(blank=True, null=True)
    scoring = models.ForeignKey(Scoring, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ScoringAllocations'


class Ward(models.Model):
    name = models.CharField(max_length=100)
    ward_cnt = models.IntegerField()
    group_id = models.IntegerField()
    is_nursing_care = models.BooleanField(blank=True, null=True)
    is_excluded_ward = models.BooleanField(blank=True, null=True)
    department_type = models.CharField(max_length=100, blank=True, null=True)
    excluded_rooms = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ward'


class Wardpriority(models.Model):
    department = models.CharField(max_length=255)
    priority = models.IntegerField()
    ward = models.ForeignKey('Ward', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'WardPriority'


class Departments(models.Model):
    config_json = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'departments'
