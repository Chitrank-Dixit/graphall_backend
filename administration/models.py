from django.db import models
from miscellaneous.models import TimeStampMixin
#import versioning

class Plan(TimeStampMixin):
    """
        Usage plan to use
    """

    name = models.CharField(max_length=50, unique=True)      # name of the plan should always be unique
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

#     class Meta:
#         permissions = (
#             ("administration.browse_revision_plan", "Can browse revisions"),
#             ("administration.reapply_revision_plan", "Can repply revision"),
#         )
#
# versioning.register(
#     Plan,
#     ['name','created_on','updated_on']
# )