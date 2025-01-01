import PyPDF2

def remove_pdf_password(input_pdf, output_pdf, password):
    try:
        # Open the encrypted PDF file
        with open(input_pdf, 'rb') as infile:
            reader = PyPDF2.PdfReader(infile)

            # Check if the PDF is encrypted
            if reader.is_encrypted:
                # Try to decrypt the PDF with the provided password
                if reader.decrypt(password):
                    # Create a new PDF writer
                    writer = PyPDF2.PdfWriter()

                    # Add all pages to the writer
                    for page_num in range(len(reader.pages)):
                        writer.add_page(reader.pages[page_num])

                    # Write the decrypted PDF to a new file
                    with open(output_pdf, 'wb') as outfile:
                        writer.write(outfile)

                    print(f"Password removed. Decrypted file saved as '{output_pdf}'")
                else:
                    print("Incorrect password. Unable to decrypt the PDF.")
            else:
                print("The PDF is not encrypted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input parameters
input_pdf = 'C:/Users/91972/Downloads/EAadhaar_0124120100217620180809172649_20112024213540.pdf'  # Path to the encrypted PDF
output_pdf = 'AAdharcard.pdf'  # Path to save the decrypted PDF
password = ''  # Password to decrypt the PDF

# Remove the password from the PDF
remove_pdf_password(input_pdf, output_pdf, password)
