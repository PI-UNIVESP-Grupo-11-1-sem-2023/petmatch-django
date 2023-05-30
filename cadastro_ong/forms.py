from django import forms
from cadastro_ong.models import participantes


class participantes(forms.ModelForm):
    class Meta:
        model = participantes

    Nome = forms.CharField(
        name = "Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Usuário"
            }
        )
    )

    CPF = forms.CharField(
        name ="CPF",
        required=False,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "CPF"
            }
        )
    )

    Telefone = forms.CharField(
        name = "Telefone",
        required = True,
        max_lenght = 40,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Telefone"
            }
        )
    )

    Email = forms.CharField(
        name = "Email",
        required = True,
        max_lenght = 40,
        widget=forms.EmailField(
            attrs={
                "class": "form-control",
                "placeholder": "Email"
            }
        )
    )

    Cep = forms.CharField(
        name = "Cep",
        required = True,
        max_lenght = 40,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Cep"
            }
        )
    )

    Rua = forms.CharField(
        name = "Rua",
        required = True,
        max_lenght = 100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Rua"
            }
        )
    )

    Cidade = forms.CharField(
        name = "Cidade",
        required = True,
        max_lenght = 40,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Cidade"
            }
        )
    )

    Estado = forms.CharField(
        name = "Estado",
        required = True,
        max_lenght = 40,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Estado"
            }
        )
    )