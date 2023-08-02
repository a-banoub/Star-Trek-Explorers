import fitz  # PyMuPDF

def get_form_field_values(pdf_file_path):
    pdf_document = fitz.open(pdf_file_path)
    
    if '/AcroForm' in pdf_document.metadata:
        acro_form = pdf_document.metadata['/AcroForm']
        form_fields = acro_form.get_object()['/Fields']
        
        if form_fields:
            print("Form Fields:")
            for field in form_fields:
                field_object = field.getObject()
                field_name = field_object.get('/T')  # Get the field name
                field_value = field_object.get('/V')  # Get the field value
                print(f"{field_name}: {field_value}")
        
    pdf_document.close()

# Example usage with the sample PDF file
pdf_file_path = 'test.pdf'
get_form_field_values(pdf_file_path)
