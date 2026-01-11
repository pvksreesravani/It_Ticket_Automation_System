from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    """
    Form for creating new IT support tickets.
    Auto-fills category and priority via automation service.
    Users only provide title and description.
    """
    
    class Meta:
        model = Ticket
        fields = ['title', 'description']
        
        # Custom labels for form fields
        labels = {
            'title': 'Issue Summary',
            'description': 'Detailed Description',
        }
        
        # Custom widgets for better UX
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Brief summary of your issue',
                'maxlength': '200',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Please provide detailed information about your issue',
                'rows': 6,
            }),
        }
        
        # Help text for fields
        help_texts = {
            'title': 'Provide a short, clear summary of the problem',
            'description': 'Include any error messages, steps to reproduce, or relevant details',
        }
    
    def clean_title(self):
        """
        Validate and clean the title field.
        Ensures title is not empty or too short.
        """
        title = self.cleaned_data.get('title', '').strip()
        
        if not title:
            raise forms.ValidationError('Title cannot be empty.')
        
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        
        return title
    
    def clean_description(self):
        """
        Validate and clean the description field.
        Ensures description has sufficient detail.
        """
        description = self.cleaned_data.get('description', '').strip()
        
        if not description:
            raise forms.ValidationError('Description cannot be empty.')
        
        if len(description) < 10:
            raise forms.ValidationError('Please provide more details (at least 10 characters).')
        
        return description