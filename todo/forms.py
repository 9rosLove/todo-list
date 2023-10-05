from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms

from todo.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateField(
        widget=forms.SelectDateWidget(

        )
    )

    class Meta:
        model = Task
        fields = "__all__"


class SearchFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FieldWithButtons(
                f"{self.obj}",
                StrictButton("Search", type="submit"),
                input_size="input-group-sm",
            )
        )


class TagSearchForm(SearchFormMixin, forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )
    obj = "name"


class TaskSearchForm(SearchFormMixin, forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by content"}),
    )
    obj = "content"
