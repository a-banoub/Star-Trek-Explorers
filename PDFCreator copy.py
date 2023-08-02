import PyPDF2

def get_form_field_values(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        

        # Check if the PDF has form fields
        if '/AcroForm' in pdf_reader.trailer:
            form = pdf_reader['/AcroForm']
            fields = form.get_object()['/Fields']
            if fields:
                print("Form Fields:")
                for field in fields:
                    field_object = field.getObject()
                    field_name = field_object.get('/T')  # Get the field name
                    field_value = field_object.get('/V')  # Get the field value
                    print(f"{field_name}: {field_value}")

# Example usage
pdf_file_path = 'test.pdf'

get_form_field_values(pdf_file_path)