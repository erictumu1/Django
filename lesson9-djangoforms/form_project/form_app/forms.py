from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea) #widget = forms.Textarea allows users to type long messages.
    
    def send_email(self): #This in real life would handle the sending logic for the message.
        print(f"sending email from {self.cleaned_data ['email']} with message: {self.cleaned_data ['message']}")