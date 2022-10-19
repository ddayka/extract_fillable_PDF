import pdfrw


def extract_fill_pdf(pdf):
    stringList = []
    checkboxList = []
    for page in pdf.pages:
        annotations = page['/Annots']
        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                if annotation['/T']:
                    key = annotation['/T'][1:-1]
                    if annotation['/AS']:
                        value = str(annotation['/V'])[1:]
                        checkboxList.append([key, value])
                    else:
                        value = str(annotation['/V'])
                        stringList.append([key, value])

    radioButtonKeyList = []
    radioButtonValueList = []

    for page in pdf.pages:
        annotations = page['/Annots']
        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                if annotation['/AS'] is not None and annotation['/T'] is None:
                    radioID = annotation['/Parent']['/T']
                    listIndex = 0
                    if radioID not in radioButtonKeyList:
                        radioButtonKeyList.append(radioID)
                        radioButtonValueList.append([])
                    for index in radioButtonKeyList:
                        if index == radioID:
                            break
                        listIndex += 1
                    for key in annotation['/AP']['/D'].keys():
                        if "Off" not in str(key):
                            radioKey = key
                    radioValue = annotation['/AS']
                    radioButtonValueList[listIndex].append(
                        {
                            "key": str(radioKey),
                            "value": str(radioValue)
                        }
                    )
    '''  # Uncomment to to print list - This is so you can find the 'key' keywords needed for get_X methods
    print("List of String Inputs: ")
    print(stringList)
    print("")
    print("List of Checkbox Inputs: ")
    print(checkboxList)
    print("")
    print("List of Radio Buttons: ")
    print(radioButtonKeyList)
    print(radioButtonValueList)
    print("")
    '''
    return [stringList, checkboxList, [radioButtonKeyList, radioButtonValueList]]


# Returns radio button value as a string. Returns 'NoKey' if no radio button is found
def get_radiobutton(key, extract_list):
    listIndex = 0
    for index in extract_list[2][0]:  # radio button key list
        if index == key:
            break
        listIndex += 1
    for button in extract_list[2][1][listIndex]:  # Radio button value list @ key idx
        if button['value'] != '/Off':
            return str(button['value'])[1:]
    return 'NoKey'


# Return string of fallible text field in pfd due to field keyword.
# Return 'Empty' if no text, Return 'NoKey' if not key present
def get_string(key, extract_list):
    for item in extract_list[0]:  # string list
        if key == item[0]:
            if item[1] != 'None' and item[1] != '()':
                return str(item[1])[1:-1]
            else:
                return 'Empty'
    return 'NoKey'


# Return True if checkbox is checked, False if not. If key not present str 'NoKey' returned
def get_checkbox(key, extract_list):
    for item in extract_list[1]:  # checkbox list
        if key == item[0]:
            if item[1] == 'Yes':
                return True
            else:
                return False
    return 'NoKey'


input_pdf = r"PDF_FILEPATH"
extracted_pdf = pdfrw.PdfReader(input_pdf)
extracted_fill_list =  extract_fill_pdf(extracted_pdf)
