#!/usr/bin/env python3

import PyPDF2

input_file = "fillable_char_sheet.pdf"


def mkpdf (pc):
	
	pc = pc
	
	statblock = {}
	statblock = pc.stats
	reader = PyPDF2.PdfReader(input_file)
	page = reader._get_page(0)
	
	def get_fields(): #Defines function to get the fields
		formfields = reader.get_form_text_fields() #calls the function from reader and defines "formfields" witnin scope of function
		return formfields #returns the "formfields" value
		
	formfields = get_fields() #calls the newly defined get_fields function and returns the formfields variable in scope
	
	print (formfields.items())
	print (formfields.keys())
	
	def populate():
		
		fieldvalues = {
			'character_name' : pc.name,
			'stat_res': pc.stats ["Resourcefulness"],
			'stat_emp': pc.stats['Empathy'],
			'stat_log': pc.stats['Logic'],
			'stat_tac': pc.stats['Tactics']
		}
		
		return (fieldvalues)
	
	fieldvalues = populate()
	
	print ("formfields.items():", formfields.items())
	print ("formfields.keys():", formfields.keys())
	print ("field values items:", fieldvalues.items())
	
	output_file = f'{pc.name}{pc.id}.pdf'
	
	def write_fields (reader, fieldvalues):
		writer = PyPDF2.PdfWriter()
		writer.add_page(reader.pages[0])
		
		for field,value in fieldvalues.items():
			print (field,value)			
			
			if field in formfields:
				formfields[field] = value 	
				print (field)
			else:
				print(f"Field '{field}' not found in the PDF form.")
				continue
		
#		fields = {formfields[key]: value for key, value in fieldvalues.items()}
		flags = None
		
		writer.update_page_form_field_values(writer.pages[0], fields=formfields, flags=flags)
			
		return writer
	
	writer = write_fields (reader, fieldvalues)
	
	with open(output_file, "wb") as f:
		writer.write(f)
		