# importing required modules
import PyPDF2
  
# creating a pdf file object
pdfFileObj = open('Space Marines Index.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
  
# printing number of pages in pdf file
pages = pdfReader.pages
NumPages = len(pages)
print("Number of pages in PDF: {}".format(NumPages))

#temp list of units to pull out - replace with user input
tempStrArr = ["Bladeguard Veteran Squad", "Captain", "Librarian in terminator armour"]
for n, unit in enumerate(tempStrArr):
    tempStrArr[n] = tempStrArr[n].upper()
print(tempStrArr)

#create empty list for sheets
parsedSheetsList = []

#go through all pages in PDF
for i, page in enumerate(pages):
    #i is page index
    pageObj = page
    #get the whole page text
    pageText = pageObj.extract_text()
    #find where KEYWORDS is after a line return
    keywordIndex = pageText.find("\nKEYWORDS:")
    #Get the string prior to the keywordIndex
    previousStr = pageText[:keywordIndex]
    #If the string before keywords matches a unit searched
    if previousStr in tempStrArr:
        print(previousStr,format(i))
        #create new writer obj
        pdfWriter = PyPDF2.PdfWriter()
        #create new file name
        outputPdfName = "temp" + str(i) + ".pdf"
        #get the current page and next page (format of GW datasheets is pairs)
        page1 = page
        page2 = pages[i+1]
        #add the pages to the pdfWriter
        pdfWriter.add_page(page1)
        pdfWriter.add_page(page2)
        #create the new file
        with open(outputPdfName, "wb") as output_pdf:
            pdfWriter.write(output_pdf)
        #add the file names to a list of parsed sheets
        parsedSheetsList.append(outputPdfName)
        print(parsedSheetsList)
        pdfWriter.close

#replace with an input for output file name
finalFileName = "OutputFile.pdf"
#create pdfwriter object ref
merger = PyPDF2.PdfWriter()

#go through each parsed sheet and add the unit PDFs together
for units in parsedSheetsList:
    merger.append(units)

#create new file then close merger ref
merger.write(finalFileName)
merger.close


# closing the pdf file object]
pdfFileObj.close()