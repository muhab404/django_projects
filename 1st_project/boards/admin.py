from django.contrib import admin
from .models import Board, Topic
from django.contrib.auth.models import Group


# for import and export topic as file in admin
# from import_export.admin import ImportExportModelAdmin

# # Register your models here.
# admin.site.register(Board)

# @admin.register(Topic)
# class TopicAdmin(ImportExportModelAdmin):
#     pass


admin.site.site_header='Boards Admin Panel'
admin.site.site_title='Boards Admin Panel'


class InlineTopic(admin.StackedInline):
    model = Topic
    extra = 1

class BoardAdmin(admin.ModelAdmin):
    inlines=[InlineTopic]

class TopicAdmin(admin.ModelAdmin):
    fields = ('subject','board','created_by','views')
    list_display=('subject','board','created_by','combine_subject_and_board')
    list_display_links=('board','created_by')
    list_editable=('subject',)
    list_filter=('created_by','board',)
    search_fields =('board','created_by')

    def combine_subject_and_board(self,obj):
        return "{} - {}".format(obj.subject,obj.board)

admin.site.register(Board,BoardAdmin)
admin.site.register(Topic,TopicAdmin)