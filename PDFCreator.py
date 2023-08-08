#!/usr/bin/env python3

import PyPDF2

input_file = "fillable_char_sheet.pdf"


def mkpdf (pc):

	pc = pc

	statblock = {}
	statblock = pc.stats
	reader = PyPDF2.PdfReader(input_file)
	page = reader.pages[0]

	def get_fields():
		formfields = reader.get_form_text_fields()
		print(formfields)
		return formfields

	formfields = get_fields()

	print (formfields.items())
	print (formfields.keys())

	def populate():
		def get_exp(expertise):
			exp = ""
			print (expertise.items())
			for key, value in expertise.items():
				print (key,value)
				exp.join (f'{key} : {value}')
				
			return exp
		
		exp = get_exp(pc.expertise)
		
		fieldvalues = {
			'character_name' : pc.name,
			'stat_res': pc.stats ["Resourcefulness"],
			'stat_emp': pc.stats['Empathy'],
			'stat_log': pc.stats['Logic'],
			'stat_tac': pc.stats['Tactics'],
			'species' : pc.species,
			'archetype' : pc.archetype,
			'expertise' : exp
			}

		return (fieldvalues)

	fieldvalues = populate()

	print ("\nformfields.items():", formfields.items())
	print ("\nformfields.keys():", formfields.keys())
	print ("\nfield values items:", fieldvalues.items())

	output_file = f'{pc.name}{pc.id}.pdf'

	def write_fields (reader, fieldvalues:dict):
		
		writer = PyPDF2.PdfWriter()
		page = writer.add_page(reader.pages[0])
		
		for field,value in fieldvalues.items():
			print (field,value)
			if field in formfields:
				formfields[field] = value
				print (field)
	
			else:
				print(f"\nField '{field}' not found in the PDF form.")
				continue
		
		flags = None	
		
		writer.update_page_form_field_values(page, fields=formfields, flags=flags)

		return writer

	writer = write_fields(reader, fieldvalues)

	with open(output_file, "wb") as f:
		writer.write(f)
		