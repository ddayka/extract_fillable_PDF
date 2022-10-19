# extract_fillable_PDF
Extract Textbox, Checkbox and RadioButton from fillable PDF

Requirements: <br>
pdfrw (package for reading pdfs in Python)

**Methods:** <br>
_extract_fill_pdf:_ <br>
input: extracted python pdf <br>
return: Formated list of lists with all extracted keys and values <br>

_get_radiobutton:_ <br>
input: radio button key, extracted list (from extract_fill_pdf method): <br>
return: string value of selecttion <br>

_get_string:_ <br>
input: string key, extracted list (from extract_fill_pdf method): <br>
return: string value (str) <br>

_get_checkbox:_ <br>
input: checkbox key, extracted list (from extract_fill_pdf method): <br>
return: True (checked) False Unchecked) <br>
<br>

Usage:
I would reccomend running the extract_fill_pdf method on your pdf 
with the print section uncommented at the bottom, this way, you can 
more than likely, figure out what all the keywords are, which are
needed in the following methods.
