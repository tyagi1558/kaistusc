# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ManagerConfig(AppConfig):
    name = 'manager'
    verbose_name = _("사이트 관리도구")
