from django.db import models


class Manual(models.Model):
    """
    Model with main info about manual
    """
    title = models.CharField(max_length=50, verbose_name='title')
    short_title = models.CharField(max_length=10, verbose_name='short title')
    description = models.TextField(blank=True, null=True, verbose_name='description')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'manual'
        verbose_name_plural = 'manuals'


class ManualVersion(models.Model):
    """
    Main model for manuals
    """
    manual_info = models.ForeignKey('Manual', on_delete=models.CASCADE, related_name='versions')
    version = models.CharField(max_length=10, verbose_name='version')
    from_date = models.DateField(verbose_name='valid from')

    class Meta:
        unique_together = ['manual_info', 'version']
        verbose_name = 'manual version'
        verbose_name_plural = 'manuals versions'

    def __str__(self) -> str:
        return "".join([self.manual_info.short_title, ' v', self.version])


class ManualElem(models.Model):
    """
    Model for manual elements
    """
    manual = models.ForeignKey('ManualVersion', on_delete=models.CASCADE, related_name='elements')
    code = models.CharField(max_length=30, verbose_name='code')
    value = models.CharField(max_length=100, verbose_name='value')

    def __str__(self) -> str:
        return ": ".join([self.code, self.value])

    class Meta:
        verbose_name = 'element of manual'
        verbose_name_plural = 'elements of manuals'
