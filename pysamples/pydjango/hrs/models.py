from django.db import models

# Create your models here.


class Dept(models.Model):
    """
    部门类
    """
    no = models.IntegerField(
        primary_key=True, db_column='dno', verbose_name='部门编号')
    name = models.CharField(
        max_length=20, db_column='dname', verbose_name='部门名称')
    location = models.CharField(
        max_length=10, db_column='dloc', verbose_name='部门所在地')

    def __str__(self):
        return 'hrs '+self.name

    class Meta:
        db_table = 'tb_dept'
        app_label = "hrs"


class Emp(models.Model):
    """
    员工类
    """
    no = models.IntegerField(
        primary_key=True, db_column='eno', verbose_name='员工编号')
    name = models.CharField(
        max_length=20, db_column='ename', verbose_name='员工姓名')
    title = models.CharField(
        max_length=10, db_column='etitle', verbose_name='职位')

    mgr = models.ForeignKey('self', on_delete=models.SET_NULL,
                            null=True, blank=True, verbose_name='上级')
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='薪资')
    subsidy = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='补贴')

    dept = models.ForeignKey(Dept, db_column='dno',
                             on_delete=models.PROTECT, verbose_name='部门')

    def __str__(self):
        return 'hrs '+self.name

    class Meta:
        db_table = 'tb_emp'
        app_label = "hrs"
