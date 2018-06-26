from django import forms


class SearchTransactionForm(forms.Form):
    search = forms.CharField(max_length=30, required=False)

    def is_valid(self, *args, **kwargs):
        return super(SearchTransactionForm, self).is_valid()

    def save(self, *args, **kwargs):
        super(SearchTransactionForm, self).is_valid()
