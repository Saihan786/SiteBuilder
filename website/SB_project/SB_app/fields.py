from django.forms.models import ModelMultipleChoiceField

class BlockModelChoiceField(ModelMultipleChoiceField):
    """
    This class is a wrapper for label_from_instance, which is overwritten so the block names are shown in the form that uses this field.
    """

    def label_from_instance(self, obj):
        return "%s" % (obj.name)