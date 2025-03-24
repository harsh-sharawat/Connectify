from django.forms.models import ModelForm
from django import forms
from .models import Room

class Create_room(ModelForm):
    TYPE_CHOICES = [(1, 'Public'), (2, 'Private')]
    typeofform = forms.ChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Room
        fields = ["room_name", "description", "tags", "typeofform"]
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter room description...",
                    "rows": 4,
                    "cols": 50,
                    "maxlength": 500,
                    "required": True,
                }
            ),
            "tags": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tags",
                    "rows": 2,
                    "cols": 50,
                    "maxlength": 500,
                    "required": True,
                }
            ),
        }
        help_texts = {
            "description": "<span class='form-text text-muted'><small>Provide a short description of the room (max 500 characters).</small></span>",
            "tags": "<span class='form-text text-muted'><small>Provide ',' separated tags. These help other users to search the room.</small></span>",
        }

    def __init__(self, *args, **kwargs):
        super(Create_room, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs["class"] = "form-control"
            self.fields[field_name].label = ""  # Removing label

        self.fields["room_name"].widget.attrs["placeholder"] = "Room Name"
        self.fields["room_name"].help_text = (
            '<span class="form-text text-muted"><small>'
            "Required. 100 characters or fewer. Letters, digits, and @/./+/-/_ only."
            "</small></span>"
        )

        # Explicitly setting help text for typeofform
        self.fields["typeofform"].help_text = (
            '<span class="form-text text-muted"><small>'
            "Public - anyone can join. <br> Private - needs permission to join."
            "</small></span>"
        )
